vlib questa_lib/work
vlib questa_lib/msim

vlib questa_lib/msim/xilinx_vip
vlib questa_lib/msim/xil_defaultlib
vlib questa_lib/msim/xpm
vlib questa_lib/msim/axi_bram_ctrl_v4_1_1
vlib questa_lib/msim/blk_mem_gen_v8_4_3
vlib questa_lib/msim/axi_lite_ipif_v3_0_4
vlib questa_lib/msim/mdm_v3_2_16
vlib questa_lib/msim/microblaze_v11_0_1
vlib questa_lib/msim/lmb_bram_if_cntlr_v4_0_16
vlib questa_lib/msim/lmb_v10_v3_0_9
vlib questa_lib/msim/axi_infrastructure_v1_1_0
vlib questa_lib/msim/axi_vip_v1_1_5
vlib questa_lib/msim/processing_system7_vip_v1_0_7
vlib questa_lib/msim/lib_cdc_v1_0_2
vlib questa_lib/msim/proc_sys_reset_v5_0_13
vlib questa_lib/msim/generic_baseblocks_v2_1_0
vlib questa_lib/msim/axi_register_slice_v2_1_19
vlib questa_lib/msim/fifo_generator_v13_2_4
vlib questa_lib/msim/axi_data_fifo_v2_1_18
vlib questa_lib/msim/axi_crossbar_v2_1_20
vlib questa_lib/msim/axi_protocol_converter_v2_1_19
vlib questa_lib/msim/axi_clock_converter_v2_1_18
vlib questa_lib/msim/axi_dwidth_converter_v2_1_19
vlib questa_lib/msim/axi_mmu_v2_1_17

vmap xilinx_vip questa_lib/msim/xilinx_vip
vmap xil_defaultlib questa_lib/msim/xil_defaultlib
vmap xpm questa_lib/msim/xpm
vmap axi_bram_ctrl_v4_1_1 questa_lib/msim/axi_bram_ctrl_v4_1_1
vmap blk_mem_gen_v8_4_3 questa_lib/msim/blk_mem_gen_v8_4_3
vmap axi_lite_ipif_v3_0_4 questa_lib/msim/axi_lite_ipif_v3_0_4
vmap mdm_v3_2_16 questa_lib/msim/mdm_v3_2_16
vmap microblaze_v11_0_1 questa_lib/msim/microblaze_v11_0_1
vmap lmb_bram_if_cntlr_v4_0_16 questa_lib/msim/lmb_bram_if_cntlr_v4_0_16
vmap lmb_v10_v3_0_9 questa_lib/msim/lmb_v10_v3_0_9
vmap axi_infrastructure_v1_1_0 questa_lib/msim/axi_infrastructure_v1_1_0
vmap axi_vip_v1_1_5 questa_lib/msim/axi_vip_v1_1_5
vmap processing_system7_vip_v1_0_7 questa_lib/msim/processing_system7_vip_v1_0_7
vmap lib_cdc_v1_0_2 questa_lib/msim/lib_cdc_v1_0_2
vmap proc_sys_reset_v5_0_13 questa_lib/msim/proc_sys_reset_v5_0_13
vmap generic_baseblocks_v2_1_0 questa_lib/msim/generic_baseblocks_v2_1_0
vmap axi_register_slice_v2_1_19 questa_lib/msim/axi_register_slice_v2_1_19
vmap fifo_generator_v13_2_4 questa_lib/msim/fifo_generator_v13_2_4
vmap axi_data_fifo_v2_1_18 questa_lib/msim/axi_data_fifo_v2_1_18
vmap axi_crossbar_v2_1_20 questa_lib/msim/axi_crossbar_v2_1_20
vmap axi_protocol_converter_v2_1_19 questa_lib/msim/axi_protocol_converter_v2_1_19
vmap axi_clock_converter_v2_1_18 questa_lib/msim/axi_clock_converter_v2_1_18
vmap axi_dwidth_converter_v2_1_19 questa_lib/msim/axi_dwidth_converter_v2_1_19
vmap axi_mmu_v2_1_17 questa_lib/msim/axi_mmu_v2_1_17

vlog -work xilinx_vip -64 -sv -L axi_vip_v1_1_5 -L processing_system7_vip_v1_0_7 -L xilinx_vip "+incdir+/tools/Xilinx/Vivado/2019.1/data/xilinx_vip/include" \
"/tools/Xilinx/Vivado/2019.1/data/xilinx_vip/hdl/axi4stream_vip_axi4streampc.sv" \
"/tools/Xilinx/Vivado/2019.1/data/xilinx_vip/hdl/axi_vip_axi4pc.sv" \
"/tools/Xilinx/Vivado/2019.1/data/xilinx_vip/hdl/xil_common_vip_pkg.sv" \
"/tools/Xilinx/Vivado/2019.1/data/xilinx_vip/hdl/axi4stream_vip_pkg.sv" \
"/tools/Xilinx/Vivado/2019.1/data/xilinx_vip/hdl/axi_vip_pkg.sv" \
"/tools/Xilinx/Vivado/2019.1/data/xilinx_vip/hdl/axi4stream_vip_if.sv" \
"/tools/Xilinx/Vivado/2019.1/data/xilinx_vip/hdl/axi_vip_if.sv" \
"/tools/Xilinx/Vivado/2019.1/data/xilinx_vip/hdl/clk_vip_if.sv" \
"/tools/Xilinx/Vivado/2019.1/data/xilinx_vip/hdl/rst_vip_if.sv" \

vlog -work xil_defaultlib -64 -sv -L axi_vip_v1_1_5 -L processing_system7_vip_v1_0_7 -L xilinx_vip "+incdir+../../../../team2_v_003_one_MB.srcs/sources_1/bd/design_1/ipshared/ec67/hdl" "+incdir+../../../../team2_v_003_one_MB.srcs/sources_1/bd/design_1/ipshared/8c62/hdl" "+incdir+../../../../team2_v_003_one_MB.srcs/sources_1/bd/design_1/ip/design_1_processing_system7_0_0" "+incdir+/tools/Xilinx/Vivado/2019.1/data/xilinx_vip/include" \
"/tools/Xilinx/Vivado/2019.1/data/ip/xpm/xpm_cdc/hdl/xpm_cdc.sv" \
"/tools/Xilinx/Vivado/2019.1/data/ip/xpm/xpm_memory/hdl/xpm_memory.sv" \

vcom -work xpm -64 -93 \
"/tools/Xilinx/Vivado/2019.1/data/ip/xpm/xpm_VCOMP.vhd" \

vcom -work axi_bram_ctrl_v4_1_1 -64 -93 \
"../../../../team2_v_003_one_MB.srcs/sources_1/bd/design_1/ipshared/70bf/hdl/axi_bram_ctrl_v4_1_rfs.vhd" \

vcom -work xil_defaultlib -64 -93 \
"../../../bd/design_1/ip/design_1_axi_bram_ctrl_0_0/sim/design_1_axi_bram_ctrl_0_0.vhd" \
"../../../bd/design_1/ip/design_1_axi_bram_ctrl_1_0/sim/design_1_axi_bram_ctrl_1_0.vhd" \

vlog -work blk_mem_gen_v8_4_3 -64 "+incdir+../../../../team2_v_003_one_MB.srcs/sources_1/bd/design_1/ipshared/ec67/hdl" "+incdir+../../../../team2_v_003_one_MB.srcs/sources_1/bd/design_1/ipshared/8c62/hdl" "+incdir+../../../../team2_v_003_one_MB.srcs/sources_1/bd/design_1/ip/design_1_processing_system7_0_0" "+incdir+/tools/Xilinx/Vivado/2019.1/data/xilinx_vip/include" \
"../../../../team2_v_003_one_MB.srcs/sources_1/bd/design_1/ipshared/c001/simulation/blk_mem_gen_v8_4.v" \

vlog -work xil_defaultlib -64 "+incdir+../../../../team2_v_003_one_MB.srcs/sources_1/bd/design_1/ipshared/ec67/hdl" "+incdir+../../../../team2_v_003_one_MB.srcs/sources_1/bd/design_1/ipshared/8c62/hdl" "+incdir+../../../../team2_v_003_one_MB.srcs/sources_1/bd/design_1/ip/design_1_processing_system7_0_0" "+incdir+/tools/Xilinx/Vivado/2019.1/data/xilinx_vip/include" \
"../../../bd/design_1/ip/design_1_blk_mem_gen_0_0/sim/design_1_blk_mem_gen_0_0.v" \

vcom -work axi_lite_ipif_v3_0_4 -64 -93 \
"../../../../team2_v_003_one_MB.srcs/sources_1/bd/design_1/ipshared/66ea/hdl/axi_lite_ipif_v3_0_vh_rfs.vhd" \

vcom -work mdm_v3_2_16 -64 -93 \
"../../../../team2_v_003_one_MB.srcs/sources_1/bd/design_1/ipshared/550e/hdl/mdm_v3_2_vh_rfs.vhd" \

vcom -work xil_defaultlib -64 -93 \
"../../../bd/design_1/ip/design_1_mdm_1_0/sim/design_1_mdm_1_0.vhd" \

vcom -work microblaze_v11_0_1 -64 -93 \
"../../../../team2_v_003_one_MB.srcs/sources_1/bd/design_1/ipshared/f8c3/hdl/microblaze_v11_0_vh_rfs.vhd" \

vcom -work xil_defaultlib -64 -93 \
"../../../bd/design_1/ip/design_1_microblaze_0_0/sim/design_1_microblaze_0_0.vhd" \

vcom -work lmb_bram_if_cntlr_v4_0_16 -64 -93 \
"../../../../team2_v_003_one_MB.srcs/sources_1/bd/design_1/ipshared/6335/hdl/lmb_bram_if_cntlr_v4_0_vh_rfs.vhd" \

vcom -work xil_defaultlib -64 -93 \
"../../../bd/design_1/ip/design_1_dlmb_bram_if_cntlr_0/sim/design_1_dlmb_bram_if_cntlr_0.vhd" \

vcom -work lmb_v10_v3_0_9 -64 -93 \
"../../../../team2_v_003_one_MB.srcs/sources_1/bd/design_1/ipshared/78eb/hdl/lmb_v10_v3_0_vh_rfs.vhd" \

vcom -work xil_defaultlib -64 -93 \
"../../../bd/design_1/ip/design_1_dlmb_v10_0/sim/design_1_dlmb_v10_0.vhd" \
"../../../bd/design_1/ip/design_1_ilmb_bram_if_cntlr_0/sim/design_1_ilmb_bram_if_cntlr_0.vhd" \
"../../../bd/design_1/ip/design_1_ilmb_v10_0/sim/design_1_ilmb_v10_0.vhd" \

vlog -work xil_defaultlib -64 "+incdir+../../../../team2_v_003_one_MB.srcs/sources_1/bd/design_1/ipshared/ec67/hdl" "+incdir+../../../../team2_v_003_one_MB.srcs/sources_1/bd/design_1/ipshared/8c62/hdl" "+incdir+../../../../team2_v_003_one_MB.srcs/sources_1/bd/design_1/ip/design_1_processing_system7_0_0" "+incdir+/tools/Xilinx/Vivado/2019.1/data/xilinx_vip/include" \
"../../../bd/design_1/ip/design_1_lmb_bram_0/sim/design_1_lmb_bram_0.v" \

vlog -work axi_infrastructure_v1_1_0 -64 "+incdir+../../../../team2_v_003_one_MB.srcs/sources_1/bd/design_1/ipshared/ec67/hdl" "+incdir+../../../../team2_v_003_one_MB.srcs/sources_1/bd/design_1/ipshared/8c62/hdl" "+incdir+../../../../team2_v_003_one_MB.srcs/sources_1/bd/design_1/ip/design_1_processing_system7_0_0" "+incdir+/tools/Xilinx/Vivado/2019.1/data/xilinx_vip/include" \
"../../../../team2_v_003_one_MB.srcs/sources_1/bd/design_1/ipshared/ec67/hdl/axi_infrastructure_v1_1_vl_rfs.v" \

vlog -work axi_vip_v1_1_5 -64 -sv -L axi_vip_v1_1_5 -L processing_system7_vip_v1_0_7 -L xilinx_vip "+incdir+../../../../team2_v_003_one_MB.srcs/sources_1/bd/design_1/ipshared/ec67/hdl" "+incdir+../../../../team2_v_003_one_MB.srcs/sources_1/bd/design_1/ipshared/8c62/hdl" "+incdir+../../../../team2_v_003_one_MB.srcs/sources_1/bd/design_1/ip/design_1_processing_system7_0_0" "+incdir+/tools/Xilinx/Vivado/2019.1/data/xilinx_vip/include" \
"../../../../team2_v_003_one_MB.srcs/sources_1/bd/design_1/ipshared/d4a8/hdl/axi_vip_v1_1_vl_rfs.sv" \

vlog -work processing_system7_vip_v1_0_7 -64 -sv -L axi_vip_v1_1_5 -L processing_system7_vip_v1_0_7 -L xilinx_vip "+incdir+../../../../team2_v_003_one_MB.srcs/sources_1/bd/design_1/ipshared/ec67/hdl" "+incdir+../../../../team2_v_003_one_MB.srcs/sources_1/bd/design_1/ipshared/8c62/hdl" "+incdir+../../../../team2_v_003_one_MB.srcs/sources_1/bd/design_1/ip/design_1_processing_system7_0_0" "+incdir+/tools/Xilinx/Vivado/2019.1/data/xilinx_vip/include" \
"../../../../team2_v_003_one_MB.srcs/sources_1/bd/design_1/ipshared/8c62/hdl/processing_system7_vip_v1_0_vl_rfs.sv" \

vlog -work xil_defaultlib -64 "+incdir+../../../../team2_v_003_one_MB.srcs/sources_1/bd/design_1/ipshared/ec67/hdl" "+incdir+../../../../team2_v_003_one_MB.srcs/sources_1/bd/design_1/ipshared/8c62/hdl" "+incdir+../../../../team2_v_003_one_MB.srcs/sources_1/bd/design_1/ip/design_1_processing_system7_0_0" "+incdir+/tools/Xilinx/Vivado/2019.1/data/xilinx_vip/include" \
"../../../bd/design_1/ip/design_1_processing_system7_0_0/sim/design_1_processing_system7_0_0.v" \

vcom -work lib_cdc_v1_0_2 -64 -93 \
"../../../../team2_v_003_one_MB.srcs/sources_1/bd/design_1/ipshared/ef1e/hdl/lib_cdc_v1_0_rfs.vhd" \

vcom -work proc_sys_reset_v5_0_13 -64 -93 \
"../../../../team2_v_003_one_MB.srcs/sources_1/bd/design_1/ipshared/8842/hdl/proc_sys_reset_v5_0_vh_rfs.vhd" \

vcom -work xil_defaultlib -64 -93 \
"../../../bd/design_1/ip/design_1_rst_processing_system7_0_50M_0/sim/design_1_rst_processing_system7_0_50M_0.vhd" \

vlog -work generic_baseblocks_v2_1_0 -64 "+incdir+../../../../team2_v_003_one_MB.srcs/sources_1/bd/design_1/ipshared/ec67/hdl" "+incdir+../../../../team2_v_003_one_MB.srcs/sources_1/bd/design_1/ipshared/8c62/hdl" "+incdir+../../../../team2_v_003_one_MB.srcs/sources_1/bd/design_1/ip/design_1_processing_system7_0_0" "+incdir+/tools/Xilinx/Vivado/2019.1/data/xilinx_vip/include" \
"../../../../team2_v_003_one_MB.srcs/sources_1/bd/design_1/ipshared/b752/hdl/generic_baseblocks_v2_1_vl_rfs.v" \

vlog -work axi_register_slice_v2_1_19 -64 "+incdir+../../../../team2_v_003_one_MB.srcs/sources_1/bd/design_1/ipshared/ec67/hdl" "+incdir+../../../../team2_v_003_one_MB.srcs/sources_1/bd/design_1/ipshared/8c62/hdl" "+incdir+../../../../team2_v_003_one_MB.srcs/sources_1/bd/design_1/ip/design_1_processing_system7_0_0" "+incdir+/tools/Xilinx/Vivado/2019.1/data/xilinx_vip/include" \
"../../../../team2_v_003_one_MB.srcs/sources_1/bd/design_1/ipshared/4d88/hdl/axi_register_slice_v2_1_vl_rfs.v" \

vlog -work fifo_generator_v13_2_4 -64 "+incdir+../../../../team2_v_003_one_MB.srcs/sources_1/bd/design_1/ipshared/ec67/hdl" "+incdir+../../../../team2_v_003_one_MB.srcs/sources_1/bd/design_1/ipshared/8c62/hdl" "+incdir+../../../../team2_v_003_one_MB.srcs/sources_1/bd/design_1/ip/design_1_processing_system7_0_0" "+incdir+/tools/Xilinx/Vivado/2019.1/data/xilinx_vip/include" \
"../../../../team2_v_003_one_MB.srcs/sources_1/bd/design_1/ipshared/1f5a/simulation/fifo_generator_vlog_beh.v" \

vcom -work fifo_generator_v13_2_4 -64 -93 \
"../../../../team2_v_003_one_MB.srcs/sources_1/bd/design_1/ipshared/1f5a/hdl/fifo_generator_v13_2_rfs.vhd" \

vlog -work fifo_generator_v13_2_4 -64 "+incdir+../../../../team2_v_003_one_MB.srcs/sources_1/bd/design_1/ipshared/ec67/hdl" "+incdir+../../../../team2_v_003_one_MB.srcs/sources_1/bd/design_1/ipshared/8c62/hdl" "+incdir+../../../../team2_v_003_one_MB.srcs/sources_1/bd/design_1/ip/design_1_processing_system7_0_0" "+incdir+/tools/Xilinx/Vivado/2019.1/data/xilinx_vip/include" \
"../../../../team2_v_003_one_MB.srcs/sources_1/bd/design_1/ipshared/1f5a/hdl/fifo_generator_v13_2_rfs.v" \

vlog -work axi_data_fifo_v2_1_18 -64 "+incdir+../../../../team2_v_003_one_MB.srcs/sources_1/bd/design_1/ipshared/ec67/hdl" "+incdir+../../../../team2_v_003_one_MB.srcs/sources_1/bd/design_1/ipshared/8c62/hdl" "+incdir+../../../../team2_v_003_one_MB.srcs/sources_1/bd/design_1/ip/design_1_processing_system7_0_0" "+incdir+/tools/Xilinx/Vivado/2019.1/data/xilinx_vip/include" \
"../../../../team2_v_003_one_MB.srcs/sources_1/bd/design_1/ipshared/5b9c/hdl/axi_data_fifo_v2_1_vl_rfs.v" \

vlog -work axi_crossbar_v2_1_20 -64 "+incdir+../../../../team2_v_003_one_MB.srcs/sources_1/bd/design_1/ipshared/ec67/hdl" "+incdir+../../../../team2_v_003_one_MB.srcs/sources_1/bd/design_1/ipshared/8c62/hdl" "+incdir+../../../../team2_v_003_one_MB.srcs/sources_1/bd/design_1/ip/design_1_processing_system7_0_0" "+incdir+/tools/Xilinx/Vivado/2019.1/data/xilinx_vip/include" \
"../../../../team2_v_003_one_MB.srcs/sources_1/bd/design_1/ipshared/ace7/hdl/axi_crossbar_v2_1_vl_rfs.v" \

vlog -work xil_defaultlib -64 "+incdir+../../../../team2_v_003_one_MB.srcs/sources_1/bd/design_1/ipshared/ec67/hdl" "+incdir+../../../../team2_v_003_one_MB.srcs/sources_1/bd/design_1/ipshared/8c62/hdl" "+incdir+../../../../team2_v_003_one_MB.srcs/sources_1/bd/design_1/ip/design_1_processing_system7_0_0" "+incdir+/tools/Xilinx/Vivado/2019.1/data/xilinx_vip/include" \
"../../../bd/design_1/ip/design_1_xbar_2/sim/design_1_xbar_2.v" \

vcom -work xil_defaultlib -64 -93 \
"../../../bd/design_1/sim/design_1.vhd" \

vlog -work axi_protocol_converter_v2_1_19 -64 "+incdir+../../../../team2_v_003_one_MB.srcs/sources_1/bd/design_1/ipshared/ec67/hdl" "+incdir+../../../../team2_v_003_one_MB.srcs/sources_1/bd/design_1/ipshared/8c62/hdl" "+incdir+../../../../team2_v_003_one_MB.srcs/sources_1/bd/design_1/ip/design_1_processing_system7_0_0" "+incdir+/tools/Xilinx/Vivado/2019.1/data/xilinx_vip/include" \
"../../../../team2_v_003_one_MB.srcs/sources_1/bd/design_1/ipshared/c83a/hdl/axi_protocol_converter_v2_1_vl_rfs.v" \

vlog -work xil_defaultlib -64 "+incdir+../../../../team2_v_003_one_MB.srcs/sources_1/bd/design_1/ipshared/ec67/hdl" "+incdir+../../../../team2_v_003_one_MB.srcs/sources_1/bd/design_1/ipshared/8c62/hdl" "+incdir+../../../../team2_v_003_one_MB.srcs/sources_1/bd/design_1/ip/design_1_processing_system7_0_0" "+incdir+/tools/Xilinx/Vivado/2019.1/data/xilinx_vip/include" \
"../../../bd/design_1/ip/design_1_auto_pc_5/sim/design_1_auto_pc_5.v" \

vlog -work axi_clock_converter_v2_1_18 -64 "+incdir+../../../../team2_v_003_one_MB.srcs/sources_1/bd/design_1/ipshared/ec67/hdl" "+incdir+../../../../team2_v_003_one_MB.srcs/sources_1/bd/design_1/ipshared/8c62/hdl" "+incdir+../../../../team2_v_003_one_MB.srcs/sources_1/bd/design_1/ip/design_1_processing_system7_0_0" "+incdir+/tools/Xilinx/Vivado/2019.1/data/xilinx_vip/include" \
"../../../../team2_v_003_one_MB.srcs/sources_1/bd/design_1/ipshared/ac9d/hdl/axi_clock_converter_v2_1_vl_rfs.v" \

vlog -work axi_dwidth_converter_v2_1_19 -64 "+incdir+../../../../team2_v_003_one_MB.srcs/sources_1/bd/design_1/ipshared/ec67/hdl" "+incdir+../../../../team2_v_003_one_MB.srcs/sources_1/bd/design_1/ipshared/8c62/hdl" "+incdir+../../../../team2_v_003_one_MB.srcs/sources_1/bd/design_1/ip/design_1_processing_system7_0_0" "+incdir+/tools/Xilinx/Vivado/2019.1/data/xilinx_vip/include" \
"../../../../team2_v_003_one_MB.srcs/sources_1/bd/design_1/ipshared/e578/hdl/axi_dwidth_converter_v2_1_vl_rfs.v" \

vlog -work xil_defaultlib -64 "+incdir+../../../../team2_v_003_one_MB.srcs/sources_1/bd/design_1/ipshared/ec67/hdl" "+incdir+../../../../team2_v_003_one_MB.srcs/sources_1/bd/design_1/ipshared/8c62/hdl" "+incdir+../../../../team2_v_003_one_MB.srcs/sources_1/bd/design_1/ip/design_1_processing_system7_0_0" "+incdir+/tools/Xilinx/Vivado/2019.1/data/xilinx_vip/include" \
"../../../bd/design_1/ip/design_1_auto_us_0/sim/design_1_auto_us_0.v" \
"../../../bd/design_1/ip/design_1_auto_ds_0/sim/design_1_auto_ds_0.v" \
"../../../bd/design_1/ip/design_1_auto_ds_1/sim/design_1_auto_ds_1.v" \
"../../../bd/design_1/ip/design_1_auto_pc_4/sim/design_1_auto_pc_4.v" \

vlog -work axi_mmu_v2_1_17 -64 "+incdir+../../../../team2_v_003_one_MB.srcs/sources_1/bd/design_1/ipshared/ec67/hdl" "+incdir+../../../../team2_v_003_one_MB.srcs/sources_1/bd/design_1/ipshared/8c62/hdl" "+incdir+../../../../team2_v_003_one_MB.srcs/sources_1/bd/design_1/ip/design_1_processing_system7_0_0" "+incdir+/tools/Xilinx/Vivado/2019.1/data/xilinx_vip/include" \
"../../../../team2_v_003_one_MB.srcs/sources_1/bd/design_1/ipshared/b5b8/hdl/axi_mmu_v2_1_vl_rfs.v" \

vlog -work xil_defaultlib -64 "+incdir+../../../../team2_v_003_one_MB.srcs/sources_1/bd/design_1/ipshared/ec67/hdl" "+incdir+../../../../team2_v_003_one_MB.srcs/sources_1/bd/design_1/ipshared/8c62/hdl" "+incdir+../../../../team2_v_003_one_MB.srcs/sources_1/bd/design_1/ip/design_1_processing_system7_0_0" "+incdir+/tools/Xilinx/Vivado/2019.1/data/xilinx_vip/include" \
"../../../bd/design_1/ip/design_1_s00_mmu_0/sim/design_1_s00_mmu_0.v" \
"../../../bd/design_1/ip/design_1_auto_pc_6/sim/design_1_auto_pc_6.v" \

vlog -work xil_defaultlib \
"glbl.v"

