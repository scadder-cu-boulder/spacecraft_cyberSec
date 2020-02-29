connect -url tcp:127.0.0.1:3121
source /home/scadder/project/team2/team2_v007_memory_reading/team2_v007_memory_reading.sdk/design_1_wrapper_hw_platform_0/ps7_init.tcl
targets -set -filter {jtag_cable_name =~ "Digilent JTAG-SMT2 210251A5476F" && level==0} -index 1
fpga -file /home/scadder/project/team2/team2_v007_memory_reading/team2_v007_memory_reading.sdk/design_1_wrapper_hw_platform_0/design_1_wrapper.bit
targets -set -nocase -filter {name =~"APU*" && jtag_cable_name =~ "Digilent JTAG-SMT2 210251A5476F"} -index 0
loadhw -hw /home/scadder/project/team2/team2_v007_memory_reading/team2_v007_memory_reading.sdk/design_1_wrapper_hw_platform_0/system.hdf -mem-ranges [list {0x40000000 0xbfffffff}]
configparams force-mem-access 1
targets -set -nocase -filter {name =~"APU*" && jtag_cable_name =~ "Digilent JTAG-SMT2 210251A5476F"} -index 0
stop
ps7_init
ps7_post_config
configparams mdm-detect-bscan-mask 2
targets -set -nocase -filter {name =~ "microblaze*#0" && bscan=="USER2"  && jtag_cable_name =~ "Digilent JTAG-SMT2 210251A5476F"} -index 1
rst -processor
targets -set -nocase -filter {name =~ "ARM*#0" && jtag_cable_name =~ "Digilent JTAG-SMT2 210251A5476F"} -index 0
rst -processor
targets -set -nocase -filter {name =~ "ARM*#1" && jtag_cable_name =~ "Digilent JTAG-SMT2 210251A5476F"} -index 0
rst -processor
targets -set -nocase -filter {name =~ "microblaze*#0" && bscan=="USER2"  && jtag_cable_name =~ "Digilent JTAG-SMT2 210251A5476F"} -index 1
dow /home/scadder/project/team2/team2_v007_memory_reading/team2_v007_memory_reading.sdk/MB/Debug/MB.elf
targets -set -nocase -filter {name =~ "ARM*#0" && jtag_cable_name =~ "Digilent JTAG-SMT2 210251A5476F"} -index 0
dow /home/scadder/project/team2/team2_v007_memory_reading/team2_v007_memory_reading.sdk/PS_0/Debug/PS_0.elf
targets -set -nocase -filter {name =~ "ARM*#1" && jtag_cable_name =~ "Digilent JTAG-SMT2 210251A5476F"} -index 0
dow /home/scadder/project/team2/team2_v007_memory_reading/team2_v007_memory_reading.sdk/ps_ethernet/Debug/ps_ethernet.elf
configparams force-mem-access 0
targets -set -nocase -filter {name =~ "microblaze*#0" && bscan=="USER2"  && jtag_cable_name =~ "Digilent JTAG-SMT2 210251A5476F"} -index 1
con
targets -set -nocase -filter {name =~ "ARM*#0" && jtag_cable_name =~ "Digilent JTAG-SMT2 210251A5476F"} -index 0
con
targets -set -nocase -filter {name =~ "ARM*#1" && jtag_cable_name =~ "Digilent JTAG-SMT2 210251A5476F"} -index 0
con
