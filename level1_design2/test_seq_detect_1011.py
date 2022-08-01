# See LICENSE.vyoma for details

# SPDX-License-Identifier: CC0-1.0

import os
import random
from pathlib import Path

import cocotb
from cocotb.clock import Clock
from cocotb.triggers import RisingEdge, FallingEdge
from cocotb.triggers import Timer

"""for sequence 1011011""" 
@cocotb.test()
async def test_seq_bug1(dut):
    """Test for seq detection """

    clock = Clock(dut.clk, 10, units="us")  # Create a 10us period clock on port clk
    cocotb.start_soon(clock.start())        # Start the clock

    # reset
    dut.reset.value = 1
    await FallingEdge(dut.clk)  
    dut.reset.value = 0
    await FallingEdge(dut.clk)
    
    dut.inp_bit.value=1
    await FallingEdge(dut.clk)
    dut._log.info(f'State={int(dut.current_state):02} Expected_state={1} Out={int(dut.seq_seen.value):02}')
    dut.inp_bit.value=0
    await FallingEdge(dut.clk)
    dut._log.info(f'State={int(dut.current_state):02} Expected_state={2} Out={int(dut.seq_seen.value):02}')
    dut.inp_bit.value=1
    await FallingEdge(dut.clk)
    dut._log.info(f'State={int(dut.current_state):02} Expected_state={3} Out={int(dut.seq_seen.value):02}')
    dut.inp_bit.value=1
    await FallingEdge(dut.clk)
    dut._log.info(f'State={int(dut.current_state):02} Expected_state={4} Out={int(dut.seq_seen.value):02}')
    assert dut.seq_seen==1,"Sequence detected by logic by not by DUT: Model_out={out} model_state={S} Expected_out={out1} Expected_state={S1}".format(
            out=int(dut.seq_seen.value), S=int(dut.current_state), out1=1, S1=4)
    dut.inp_bit.value=0
    await FallingEdge(dut.clk)
    dut._log.info(f'Current_state={int(dut.current_state):02} Expected_state={2} Out={int(dut.seq_seen.value):02}')
    dut.inp_bit.value=1
    await FallingEdge(dut.clk)
    dut._log.info(f'State={int(dut.current_state):02} Expected_state={3} Out={int(dut.seq_seen.value):02}')
    dut.inp_bit.value=1
    await FallingEdge(dut.clk)
    dut._log.info(f'State={int(dut.current_state):02} Expected_state={4} Out={int(dut.seq_seen.value):02}')
    assert dut.seq_seen==1,"Sequence detected by logic by not by DUT: Model_out={out} model_state={S} Expected_out={out1} Expected_state={S1}".format(
            out=int(dut.seq_seen.value), S=int(dut.current_state), out1=1, S1=4)

"""for sequence 11011""" 
@cocotb.test()
async def test_seq_bug2(dut):
    """Test for seq detection """

    clock = Clock(dut.clk, 10, units="us")  # Create a 10us period clock on port clk
    cocotb.start_soon(clock.start())        # Start the clock
    
    # reset
    dut.reset.value = 1
    await FallingEdge(dut.clk)  
    dut.reset.value = 0
    await FallingEdge(dut.clk)
    await FallingEdge(dut.clk)
    
    dut.inp_bit.value=1
    await FallingEdge(dut.clk)
    dut._log.info(f'State={int(dut.current_state):02} Expected_state={1} Out={int(dut.seq_seen.value):02}')
    dut.inp_bit.value=1
    await FallingEdge(dut.clk)
    dut._log.info(f'State={int(dut.current_state):02} Expected_state={1} Out={int(dut.seq_seen.value):02}')
    dut.inp_bit.value=0
    await FallingEdge(dut.clk)
    dut._log.info(f'State={int(dut.current_state):02} Expected_state={2} Out={int(dut.seq_seen.value):02}')
    dut.inp_bit.value=1
    await FallingEdge(dut.clk)
    dut._log.info(f'State={int(dut.current_state):02} Expected_state={3} Out={int(dut.seq_seen.value):02}')
    dut.inp_bit.value=1
    await FallingEdge(dut.clk)    
    dut._log.info(f'State={int(dut.current_state):02} Expected_state={4} Out={int(dut.seq_seen.value):02}')
    assert dut.seq_seen==1,"Sequence detected by logic by not by DUT: Model_out={out} model_state={S} Expected_out={out1} Expected_state={S1}".format(
            out=int(dut.seq_seen.value), S=int(dut.current_state), out1=1, S1=4)

"""for sequence 101011""" 
@cocotb.test()
async def test_seq_bug3(dut):
    """Test for seq detection """

    clock = Clock(dut.clk, 10, units="us")  # Create a 10us period clock on port clk
    cocotb.start_soon(clock.start())        # Start the clock
    
    # reset
    dut.reset.value = 1
    await FallingEdge(dut.clk)  
    dut.reset.value = 0
    await FallingEdge(dut.clk)
    await FallingEdge(dut.clk)
    
    dut.inp_bit.value=1
    await FallingEdge(dut.clk)
    dut._log.info(f'State={int(dut.current_state):02} Expected_state={1} Out={int(dut.seq_seen.value):02}')
    dut.inp_bit.value=0
    await FallingEdge(dut.clk)
    dut._log.info(f'State={int(dut.current_state):02} Expected_state={2} Out={int(dut.seq_seen.value):02}')
    dut.inp_bit.value=1
    await FallingEdge(dut.clk)
    dut._log.info(f'State={int(dut.current_state):02} Expected_state={3} Out={int(dut.seq_seen.value):02}')
    dut.inp_bit.value=0
    await FallingEdge(dut.clk)
    dut._log.info(f'State={int(dut.current_state):02} Expected_state={2} Out={int(dut.seq_seen.value):02}')
    dut.inp_bit.value=1
    await FallingEdge(dut.clk)    
    dut._log.info(f'State={int(dut.current_state):02} Expected_state={3} Out={int(dut.seq_seen.value):02}')
    dut.inp_bit.value=1
    await FallingEdge(dut.clk)    
    dut._log.info(f'State={int(dut.current_state):02} Expected_state={4} Out={int(dut.seq_seen.value):02}')
    assert dut.seq_seen==1,"Sequence detected by logic by not by DUT: Model_out={out} model_state={S} Expected_out={out1} Expected_state={S1}".format(
            out=int(dut.seq_seen.value), S=int(dut.current_state), out1=1, S1=4)
    
