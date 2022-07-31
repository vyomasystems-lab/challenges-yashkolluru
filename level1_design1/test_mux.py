# See LICENSE.vyoma for details

import cocotb
from cocotb.triggers import Timer
import random
@cocotb.test()
async def test_mux(dut):
    """Test for mux2"""
    
    In=[0,1,2,3,0,1,2,3,0,1,2,3,0,1,2,3,0,1,2,3,0,1,2,3,0,1,2,3,0,1,2]
    for i in range(16):
        S=random.randint(14,30)
        #input driving
        dut.inp0.value=In[0]
        dut.inp1.value=In[1]
        dut.inp2.value=In[2]
        dut.inp3.value=In[3]
        dut.inp4.value=In[4]
        dut.inp5.value=In[5]
        dut.inp6.value=In[6]
        dut.inp7.value=In[7]
        dut.inp8.value=In[8]
        dut.inp9.value=In[9]
        dut.inp10.value=In[10]
        dut.inp11.value=In[11]
        dut.inp12.value=In[12]
        dut.inp13.value=In[13]
        dut.inp14.value=In[14]
        dut.inp15.value=In[15]
        dut.inp16.value=In[16]
        dut.inp17.value=In[17]
        dut.inp18.value=In[18]
        dut.inp19.value=In[19]
        dut.inp20.value=In[20]
        dut.inp21.value=In[21]
        dut.inp22.value=In[22]
        dut.inp23.value=In[23]
        dut.inp24.value=In[24]
        dut.inp25.value=In[25]
        dut.inp26.value=In[26]
        dut.inp27.value=In[27]
        dut.inp28.value=In[28]
        dut.inp29.value=In[29]
        dut.inp30.value=In[30]
    
      
        dut.sel.value=S

        await Timer(2, units='ns')
        dut._log.info(f'S={S:05} In[S]={In[S]:02} model={In[S]:02} DUT={int(dut.out.value):02}')
        assert dut.out.value == In[S], f"Mux result is incorrecr:{dut.X.value}!=1"
