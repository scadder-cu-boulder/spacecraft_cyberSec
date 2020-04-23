// MB

/******************************************************************************
*
* Copyright (C) 2009 - 2014 Xilinx, Inc.  All rights reserved.
*
* Permission is hereby granted, free of charge, to any person obtaining a copy
* of this software and associated documentation files (the "Software"), to deal
* in the Software without restriction, including without limitation the rights
* to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
* copies of the Software, and to permit persons to whom the Software is
* furnished to do so, subject to the following conditions:
*
* The above copyright notice and this permission notice shall be included in
* all copies or substantial portions of the Software.
*
* Use of the Software is limited solely to applications:
* (a) running on a Xilinx device, or
* (b) that interact with a Xilinx device through a bus or interconnect.
*
* THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
* IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
* FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL
* XILINX  BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY,
* WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF
* OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
* SOFTWARE.
*
* Except as contained in this notice, the name of the Xilinx shall not be used
* in advertising or otherwise to promote the sale, use or other dealings in
* this Software without prior written authorization from Xilinx.
*
******************************************************************************/

/*
 * This application configures UART 16550 to baud rate 9600.
 * PS7 UART (Zynq) is not initialized by this application, since
 * bootrom/bsp configures it to baud rate 115200
 *
 * ------------------------------------------------
 * | UART TYPE   BAUD RATE                        |
 * ------------------------------------------------
 *   uartns550   9600
 *   uartlite    Configurable only in HW design
 *   ps7_uart    115200 (configured by bootrom/bsp)
 */


// MB
#include <stdio.h>
#include "platform.h"
#include "xil_printf.h"
#include <xil_io.h>
#include <unistd.h>
#include <xil_cache.h>
#include <unistd.h>

//#define PS_DDR (*(volatile u32 *)(0x10000000)) // 0x00100000 ~ 0x3fffffff
#define LAST_MEM_WRITTEN (*(volatile u32 *)(0x40000000)) // 0x40000000 ~ 0x40001fff
#define MEM_READ (*(volatile u32 *)(0x40000004))
#define NEXT_CYCLE (*(volatile u32 *)(0x40000008))
#define SEMAPHORE (*(volatile u32 *)(0x4000000C))

// declare a global variable to count data words

// positive sync - 100
// negative sync - 011

int total_count = 0;
int receive_count = 0;
int positive_sync_count = 0;

void monitor(int value_at_address)
{
	// extract command word flag written by shared memory module
	int command_word_flag = (1048576 & value_at_address) >> 20;
	// extract sync bit
	int sync = (917504 & value_at_address) >> 17;
	// if it is actual command word flag get the count of data words expected
	// command word flag 0 indicates it was received at ingress.


	if (command_word_flag)
	{
		total_count = ((62 & value_at_address) >> 1) + 1;
		print("Command word -> Reset receive_count\n\r");
		receive_count = 0;
		positive_sync_count = 0;
	} else
	{
		// only command word and status words have positive sync.
		// if word is received at ingress, and has positive sync, it must be status word
		// in case of spoofing, command word and status word both will be received at ingress
		if (sync == 4)
		{
			print("Received positive sync\n\r");
			positive_sync_count = positive_sync_count + 1;
			if (positive_sync_count > 1)
			{
				print("Possible spoofing attack\n\r");
			}
			// tracking receive count and total count to check DoS and replay attacks
		}
		if (sync == 1)
		{
			receive_count = receive_count + 1;
			print("Received negative sync\n\r");
			if ((receive_count > total_count) && (receive_count > 1000))
			{
				print("Possible DoS attack\n\r");
			} else if (receive_count > total_count)
			{
				print("Possible replay attack\n\r");
			}
		}
	}


}

int main()
{
    init_platform();
    MEM_READ = 0x40000010;
    LAST_MEM_WRITTEN = 0x40000010;
    NEXT_CYCLE = 0x00000000;
    SEMAPHORE = 0x00000000;
    int value_at_address;
    print("[Security Monitor] Initialized\n\r");

    while(1)
    {
    	// if dump program has cycled around to start writing to the first mem i.e. 0x4000000C
    	if (NEXT_CYCLE == 1)
    	{
    		if ((MEM_READ) <= 0x40001ff8)
    		{
    			value_at_address = (*(volatile u32 *)(MEM_READ + 4));
    			monitor(value_at_address);
    			MEM_READ = MEM_READ + 4;
    		} else
    		{
    			MEM_READ = 0x40000010;
    			NEXT_CYCLE = 0;
    		}
    	} else
    	{
    		if (LAST_MEM_WRITTEN > MEM_READ)
    		{
    			value_at_address = (*(volatile u32 *)(MEM_READ + 4));
    			monitor(value_at_address);
    			MEM_READ = MEM_READ + 4;
    		} else
    		{
    			sleep(1);
    		}
    	}
    	usleep(1000);
    }

    cleanup_platform();
    return 0;
}
