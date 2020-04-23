import Queue
from dump import TcpDump
import threading
import time
import datetime
import subprocess as sub

queue = Queue.Queue()
y = 0


def read_tcpdump_data(direction, port):
    """read tcpdump data from dump.py and write it to queue"""
    tcpdump = TcpDump()
    tcpdump.start_tcpdump(direction, port)
    global queue
    tcpdump.get_dump(queue, direction)


def write_queue_data():
    global queue
    while True:
        while not queue.empty():
            memory_values = read_memory_values()
            write_data_permission = check_semaphore(memory_values[0])
            if not write_data_permission:
                continue
            """lock shared memory space by setting semaphore as 0x10101010"""
            # os.system('devmem 0x4000000c w 0x10101010')
            # change semaphore to 0x01010101 if running another instance
            sub.Popen(["devmem", "0x4000000c", "w", "0x10101010"], stdout=sub.PIPE)
            if memory_values[3] == "0x00000001" and int(memory_values[1], 16) >= int(memory_values[2], 16):
                continue
            next_writable_address = get_next_write_address(memory_values[1])
            if next_writable_address == memory_values[2]:
                continue
            # print next_writable_address
            x = queue.get()
            x = str(x)
	    print x
            # command = "devmem " + next_writable_address + " w " + "0x" + str(x)
            '''write data to shared memory'''
            # os.system(command)
            sub.Popen(["devmem", next_writable_address, "w", x], stdout=sub.PIPE)
            # command = "devmem 0x40000000 w " + next_writable_address
            '''update last written memory address'''
            # os.system(command)
            sub.Popen(["devmem", "0x40000000", "w", next_writable_address], stdout=sub.PIPE)
            '''release shared memory space by setting semaphore bit to 0x00000000'''
            # os.system('devmem 0x4000000c w 0x00000000')
            sub.Popen(["devmem", "0x4000000c", "w", "0x00000000"], stdout=sub.PIPE)


def get_next_write_address(last_written):
    if last_written == "0x40001FFC":
        # os.system('devmem 0x40000008 w 0x00000001')
        sub.Popen(["devmem", "0x40000008", "w", "0x00000001"], stdout=sub.PIPE)
        '''set next cycle as 1 and reset memory address'''
        return "0x40000010"
    return '0x{0:0{1}X}'.format((int(last_written, 16) + 4), 8)


def check_semaphore(semaphore):  # change semaphore to 0x01010101 if running another instance
    if semaphore == "0x00000000":
        return True
    elif semaphore == "0x10101010":
        return True
    else:
        return False


def read_memory_values():
    temp_memory_values = ["", "", "", ""]
    # temp_memory_values = ["0x00000000", "0x40000010", "0x40000010", "0x00000000"]
    # semaphore, last_written, last_read, next_cycle
    proc = sub.Popen(["devmem", "0x4000000c", "w"], stdout=sub.PIPE)
    (out, err) = proc.communicate()
    temp_memory_values[0] = out[:-1]
    proc = sub.Popen(["devmem", "0x40000000", "w"], stdout=sub.PIPE)    
    (out, err) = proc.communicate()
    temp_memory_values[1] = out[:-1]
    proc = sub.Popen(["devmem", "0x40000004", "w"], stdout=sub.PIPE)
    (out, err) = proc.communicate()
    temp_memory_values[2] = '0x{0:0{1}X}'.format((int((out[:-1]), 16) - 4), 8)
    proc = sub.Popen(["devmem", "0x40000008", "w"], stdout=sub.PIPE)
    (out, err) = proc.communicate()
    temp_memory_values[3] = out[:-1]
    print temp_memory_values
    return temp_memory_values


t1 = threading.Thread(target=read_tcpdump_data, args=("out","2001"))
t1.start()
t2 = threading.Thread(target=read_tcpdump_data, args=("in", "2000"))
t2.start()
t3 = threading.Thread(target=write_queue_data, args=())
t3.start()
