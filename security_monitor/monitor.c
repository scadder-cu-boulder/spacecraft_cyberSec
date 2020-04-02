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
 * helloworld.c: simple test application
 *
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
#define MEM_TO_READ (*(volatile u32 *)(0x40000004))
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
	int command_word_flag = (1048576 & value_at_address) >> 20;
	int sync = (917504 & value_at_address) >> 17;
	if (command_word_flag)
	{
		total_count = ((62 & value_at_address) >> 1) + 1;
		receive_count = 0;
	} else
	{
		if (sync == 4)
		{
			positive_sync_count = positive_sync_count + 1;
			if (positive_sync_count > 1)
			{
				print("Possible spoofing attack");
			}
		} else
		{
			positive_sync_count = 0;
			receive_count = receive_count + 1;
			if ((receive_count > total_count) && (receive_count > 1000))
			{
				print("Possible DoS attack");
			} else if (receive_count > total_count)
			{
				print("Possible replay attack");
			}
		}
	}


}

int main()
{
    init_platform();
    MEM_TO_READ = 0x4000000C;
    int value_at_address;
    print("[Security Monitor] Initialized\n\r");

    while(1)
    {

//    	BRAM ++;
//    	microblaze_flush_dcache();
//    	Xil_DCacheInvalidate();
//    	xil_printf("[MB] PS_DDR = %i\n\r", PS_DDR);
//    	xil_printf("[MB] BRAM = %i\n\r", BRAM);


    	// if dump program has cycled around to start writing to the first mem i.e. 0x4000000C
    	if (NEXT_CYCLE == 1)
    	{
    		if ((MEM_TO_READ) < 0x40001fff)
    		{
    			value_at_address = (*(volatile u32 *)(MEM_TO_READ));
    			monitor(value_at_address);
    			MEM_TO_READ = MEM_TO_READ + 4;
    		} else
    		{
    			MEM_TO_READ = 0x4000000C;
    			NEXT_CYCLE = 0;
    		}
    	} else
    	{
    		if (LAST_MEM_WRITTEN >= MEM_TO_READ)
    		{
    			value_at_address = (*(volatile u32 *)(MEM_TO_READ));
    			monitor(value_at_address);
    			MEM_TO_READ = MEM_TO_READ + 4;
    		} else
    		{
    			sleep(2);
    		}
    	}
    	usleep(1000);
    }

    cleanup_platform();
    return 0;
}
