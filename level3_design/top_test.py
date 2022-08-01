# See LICENSE.vyoma for details

# SPDX-License-Identifier: CC0-1.0
import os
import random
from pathlib import Path

import cocotb
from cocotb.binary import BinaryValue
from cocotb.triggers import Timer
from cocotb.clock import Clock
from cocotb.triggers import RisingEdge, FallingEdge

@cocotb.test()
async def test_top1(dut):
    """test for bug detection"""
    
    clock = Clock(dut.clk, 10, units="us")  # Create a 10us period clock on port clk
    cocotb.start_soon(clock.start())        # Start the clock

    dut.rst.value = 1
    await FallingEdge(dut.clk)  
    dut.rst.value = 0
    await FallingEdge(dut.clk)
    
    deg=280
    A=0
    dut.degrees.value=deg
    dut.actv.value=A
    instr=hex(dut.data1.value)[2:]
    out=int(instr,16) #convert Hex  to int
    out=bin(out)[2:] #convert int to binary
    out=out.zfill(64)
    await RisingEdge(dut.clk)
    dut._log.info(f'output={out} expected={1011111111101111100000111000101110001100100000010001110000010111}')
    assert out==1011111111101111100000111000101110001100100000010001110000010111,"something went wrong  Model_out={out} Expected_out={1011111111101111100000111000101110001100100000010001110000010111}".format(
      Model_out=out, Expected_out=1011111111101111100000111000101110001100100000010001110000010111)
   
    
