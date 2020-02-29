-- Copyright 1986-2019 Xilinx, Inc. All Rights Reserved.
-- --------------------------------------------------------------------------------
-- Tool Version: Vivado v.2019.1 (lin64) Build 2552052 Fri May 24 14:47:09 MDT 2019
-- Date        : Fri Oct 18 11:20:24 2019
-- Host        : scadder-Precision-5530 running 64-bit Ubuntu 18.04.3 LTS
-- Command     : write_vhdl -force -mode synth_stub
--               /home/scadder/project/project_1/project_1.srcs/sources_1/bd/design_1/ip/design_1_mdm_1_0/design_1_mdm_1_0_stub.vhdl
-- Design      : design_1_mdm_1_0
-- Purpose     : Stub declaration of top-level module interface
-- Device      : xc7z045ffg900-2
-- --------------------------------------------------------------------------------
library IEEE;
use IEEE.STD_LOGIC_1164.ALL;

entity design_1_mdm_1_0 is
  Port ( 
    Debug_SYS_Rst : out STD_LOGIC;
    Dbg_Clk_0 : out STD_LOGIC;
    Dbg_TDI_0 : out STD_LOGIC;
    Dbg_TDO_0 : in STD_LOGIC;
    Dbg_Reg_En_0 : out STD_LOGIC_VECTOR ( 0 to 7 );
    Dbg_Capture_0 : out STD_LOGIC;
    Dbg_Shift_0 : out STD_LOGIC;
    Dbg_Update_0 : out STD_LOGIC;
    Dbg_Rst_0 : out STD_LOGIC;
    Dbg_Disable_0 : out STD_LOGIC;
    Dbg_Clk_1 : out STD_LOGIC;
    Dbg_TDI_1 : out STD_LOGIC;
    Dbg_TDO_1 : in STD_LOGIC;
    Dbg_Reg_En_1 : out STD_LOGIC_VECTOR ( 0 to 7 );
    Dbg_Capture_1 : out STD_LOGIC;
    Dbg_Shift_1 : out STD_LOGIC;
    Dbg_Update_1 : out STD_LOGIC;
    Dbg_Rst_1 : out STD_LOGIC;
    Dbg_Disable_1 : out STD_LOGIC;
    Dbg_Clk_2 : out STD_LOGIC;
    Dbg_TDI_2 : out STD_LOGIC;
    Dbg_TDO_2 : in STD_LOGIC;
    Dbg_Reg_En_2 : out STD_LOGIC_VECTOR ( 0 to 7 );
    Dbg_Capture_2 : out STD_LOGIC;
    Dbg_Shift_2 : out STD_LOGIC;
    Dbg_Update_2 : out STD_LOGIC;
    Dbg_Rst_2 : out STD_LOGIC;
    Dbg_Disable_2 : out STD_LOGIC
  );

end design_1_mdm_1_0;

architecture stub of design_1_mdm_1_0 is
attribute syn_black_box : boolean;
attribute black_box_pad_pin : string;
attribute syn_black_box of stub : architecture is true;
attribute black_box_pad_pin of stub : architecture is "Debug_SYS_Rst,Dbg_Clk_0,Dbg_TDI_0,Dbg_TDO_0,Dbg_Reg_En_0[0:7],Dbg_Capture_0,Dbg_Shift_0,Dbg_Update_0,Dbg_Rst_0,Dbg_Disable_0,Dbg_Clk_1,Dbg_TDI_1,Dbg_TDO_1,Dbg_Reg_En_1[0:7],Dbg_Capture_1,Dbg_Shift_1,Dbg_Update_1,Dbg_Rst_1,Dbg_Disable_1,Dbg_Clk_2,Dbg_TDI_2,Dbg_TDO_2,Dbg_Reg_En_2[0:7],Dbg_Capture_2,Dbg_Shift_2,Dbg_Update_2,Dbg_Rst_2,Dbg_Disable_2";
attribute x_core_info : string;
attribute x_core_info of stub : architecture is "MDM,Vivado 2019.1";
begin
end;
