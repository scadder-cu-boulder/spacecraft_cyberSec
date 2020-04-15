import Queue
import dump
import threading
import time
import os
import datetime

queue = Queue.Queue()
y = 0


def read_tcpdump_data():
    """read tcpdump data from dump.py and write it to queue"""
    while True:
        global queue
        tcpdump_data = dump.TcpDump().get_dump()
        queue.put(tcpdump_data)


def write_queue_data():
    global queue
    while True:
        while not queue.empty():
            memory_values = read_memory_values()
            write_data_permission = check_semaphore(memory_values[0])
            if not write_data_permission:
                continue
            """lock shared memory space by setting semaphore as 0x10101010"""
            os.system('')  # os.system('devmem 0x40000000 w 0x10101010')  # change semaphore to 0x01010101 if running another instance
            if memory_values[3] == "0x11111111" and int(memory_values[1], 16) >= int(memory_values[2], 16):
                continue
            next_writable_address = get_next_write_address(memory_values[1])
            if next_writable_address == memory_values[2]:
                continue
            print next_writable_address
            x = queue.get()
            command = "devmem " + next_writable_address + " w " + str(x)
            '''write data to shared memory'''
            print command  # os.system(command)
            command = "devmem 0x40000004 w" + next_writable_address
            print command
            '''update last written memory address'''
            os.system('')  # os.system(command)
            '''release shared memory space by setting semaphore bit to 0x00000000'''
            os.system('')  # os.system('devmem 0x40000000 w 0x00000000')


def get_next_write_address(last_written):
    if last_written == "0x40001ffc":
        os.system('')  # os.system('devmem 0x4000000c w 0x11111111')
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
    while True:
        try:
            if int(str(datetime.datetime.now().microsecond)[1])%2 == 1:
            temp_memory_values = ["0x00000000", "0x40000010", "0x40000010", "0x00000000"]  # semaphore, last_written, last_read, next_cycle
            # temp_memory_values = [os.system('devmem 0x40000000 w'), os.system('devmem 0x40000004 w'), os.system('devmem 0x4000008 w'), os.system('devmem 0x4000000c w')]
            break
        except IndexError:
            continue
    return temp_memory_values


t1 = threading.Thread(target=read_tcpdump_data, args=())
t1.start()
t2 = threading.Thread(target=write_queue_data(), args=())
t2.start()
