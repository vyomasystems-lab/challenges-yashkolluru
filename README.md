# challenges-yashkolluru
challenges-yashkolluru created by GitHub Classroom

![](https://github.com/vyomasystems-lab/challenges-yashkolluru/blob/master/Screenshot%20(86).png)
## Verification Environment

The verification environment is setup using [Vyoma's UpTickPro](https://vyomasystems.com) provided for the hackathon. The [CoCoTb](https://www.cocotb.org/) based Python test is developed as explained.

# Level1_design1 (Multiplexer Verification)

Here the verification is done to MUX circuit to identify bugs. 
The test drives inputs to the Design under test (mux module here) which takes 30 2-bit inputs *inp0 to inp30, 5-bit select lines *sel* and 2-bit otput *out*.

The values are assigned to the input port using 
```
In=[0,1,2,3,0,1,2,3,0,1,2,3,0,1,2,3,0,1,2,3,0,1,2,3,0,1,2,3,0,1,2]
    for i in range(16):
        S=random.randint(0,30)
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
```
The assert statement is used for comparing the MUX's outut to the expected value

The following errors is seen:
i) when S=30 was assigned by random function in **test_mux1(dut)** in **test_mux.py** file
```
 assert dut.out.value == In[S], "Mux result is incorrect:model_out={Out}, expected output={EXP} at sel={SEL}".format(
 AssertionError: Mux result is incorrect:model_out=0, expected output=2 at sel=30
```
ii) when S=13 was assigned by random function in **test_mux(dut)** in **test_mux.py** file
```
 assert dut.out.value == In[S], "Mux result is incorrect:model_out={Out}, expected output={EXP} at sel={SEL}".format(
  AssertionError: Mux result is incorrect:model_out=0, expected output=1 at sel=13
```

## Test Scenario
i) when S=13 was assigned by random function in **test_mux(dut)** in **test_mux.py** file
- Test Inputs: inp0=0.... inp12=0 inp13=1 .....inp30=2
- Expected Output: out=1
- Observed Output in the DUT dut.out=0

ii) when S=30 was assigned by random function in **test_mux1(dut)** in **test_mux.py** file
- Test Inputs: inp0=0.... inp12=0 inp13=1 .....inp30=2
- Expected Output: out=2
- Observed Output in the DUT dut.out=0

Output mismatches for the above inputs proving that there is a design bug

## Design Bug
Based on the above test input and analysing the design, we see the following

i)
```
5'b01011: out = inp11;
5'b01101: out = inp12;  ====> BUG
5'b01101: out = inp13;
```
here the logic should be ``5'b01100: out = inp12;`` insted of ``5'b01101: out = inp12;`` as in design code

ii)
```
 5'b11101: out = inp29;
      default: out = 0;  ===> BUG
    endcase
```
Here we need to insert a logic above line ``default: out = 0;``that is ``5'b11110: out = inp30``.

## Design Fix
Updating the design and re-running the test makes the test. The updated code is commited as **mux_rectified.v** file with no bugs.

![](https://github.com/vyomasystems-lab/challenges-yashkolluru/blob/master/Screenshot%20(88).png)

## Verification Strategy
imported random library and assigned random function to selectlines. Made two tests one is **test_mux(dut)** for inp0 to inp15 and another is **test_mux1(dut)** for inp16 to inp30.

# Level1_design2 (Sequence Detector Verification)
Here the verification is done to sequence detector circuit (which detects 1011 sequence also repetition is allowed) to identify bugs. 
The test drives inputs to the Design under test (seq_detect_1011 module here) which takes **clk, rst, inp_bit** as inputs and gives **seq_seen** as output.

The values are assigned to the input ports *clk* and *rst* using
```
clock = Clock(dut.clk, 10, units="us")  # Create a 10us period clock on port clk
cocotb.start_soon(clock.start())        # Start the clock

# reset
dut.reset.value = 1
await FallingEdge(dut.clk)  
dut.reset.value = 0
await FallingEdge(dut.clk)
```
the values are assigned to *inp_bit* at regular intervals according to sequence which is considered  like for example sequence "10"
```
dut.inp_bit.value=1
await FallingEdge(dut.clk)
dut._log.info(f'State={int(dut.current_state):02} Expected_state={1} Out={int(dut.seq_seen.value):02}')
dut.inp_bit.value=0
await FallingEdge(dut.clk)
````

The assert statement is used for comparing the Sequenence detector's outut and state to the expected value and state respectively
The following errors is seen:

i) for sequence 1011011
```
 assert dut.seq_seen==1,"Sequence detected by logic by not by DUT: Model_out={out} model_state={S} Expected_out={out1} Expected_state={S1}".format(
 AssertionError: Sequence detected by logic but not by DUT: Model_out=0 model_state=0 Expected_out=1 Expected_state=4
```
ii) for sequence 11011
```
assert dut.seq_seen==1,"Sequence detected by logic but not by DUT: Model_out={out} model_state={S} Expected_out={out1} Expected_state={S1}".format(
AssertionError: Sequence detected by logic by not by DUT: Model_out=0 model_state=0 Expected_out=1 Expected_state=4
```
iii) for sequence 101011
```
assert dut.seq_seen==1,"Sequence detected by logic but not by DUT: Model_out={out} model_state={S} Expected_out={out1} Expected_state={S1}".format(
AssertionError: Sequence detected by logic by not by DUT: Model_out=0 model_state=0 Expected_out=1 Expected_state=4
```

## Test Scenario 
- Test inputs: each bit in the sequence 1011011 is given to inp_bit at regular intervals
- Expected Output: seq_seen=1
- Observed Output in the DUT dut.seq_seen=0
- Expected state: current_state=4
- Observed State in the DUT dut.current_state=0
## Test Scenario
- Test inputs: each bit in the sequence 11011 is given to inp_bit at regular intervals
- Expected Output: seq_seen=1
- Observed Output in the DUT dut.seq_seen=0
- Expected state: current_state=4
- Observed State in the DUT dut.current_state=0
## Test Scenario
- Test inputs: each bit in the sequence 101011 is given to inp_bit at regular intervals
- Expected Output: seq_seen=1
- Observed Output in the DUT dut.seq_seen=0
- Expected state: current_state=4
- Observed State in the DUT dut.current_state=0

## Design Bug
Based on the above test input and analysing the design, we see the following
i) 
```
SEQ_1011:
      begin
        next_state = IDLE;   ====> BUG
      end
```
ii) 
```
SEQ_1:
      begin
        if(inp_bit == 1)
          next_state = IDLE;   ====> BUG
        else
          next_state = SEQ_10;
```
iii) 
```
SEQ_101:
      begin
        if(inp_bit == 1)
          next_state = SEQ_1011;
        else
          next_state = IDLE;   ====> BUG
```

## Design Fix
Updating the design and re-running the test makes the test. The updated code is commited as **seq_detect_modified.v** file with no bugs.

![](https://github.com/vyomasystems-lab/challenges-yashkolluru/blob/master/Screenshot%20(89).png)

## Verification Strategy
Imported Path library from **pathlib**, Clock library from **cocotb.clock** and RisingEdge, FallingEdge libraries from **cocotb.triggers**. After this a clock signal was generated of period 10us. Then according the desired sequence inuts are assigend to inp_bit in regular intervals and performed all other required tests. 

# Level2_design (Bitmanipulation Co-Processor Verification)
Here the verification is done to Bitmanipulation Co-Processor circuit to identify bugs in it. The test drives inputs to the Design under test (mkbitmanip module here) which takes **mav_putvalue_instr, mav_putvalue_src1, mav_putvalue_src2, mav_putvalue_src3** as 32-bit inputs and gives **mav_putvalue** as 33-bit output where LSB is for validation.

The values are assigned to the input ports *mav_putvalue_src1, mav_putvalue_src2, mav_putvalue_src* using
```
 mav_putvalue_src1 = 0x50000000
 mav_putvalue_src2 = 0x50000000
 mav_putvalue_src3 = 0x00000000
 ```
The values are assigned to *mav_putvalue_instr* are using the 32-bit instruction values, used in if else statements of **model_mkbitmanip.py** file

The assert statement is used for comparing the Bitmanipulator Co-Processor's outut to the expected value which is got through **model_mkbitmanip.py** file
The following errors is seen:

for instruction input (mav_putvalue_instr) 400070B3 where opcode=0110011, Func3=111, Func7=0100000 and the name of instruction is ANDN
```
assert dut_output == expected_mav_putvalue, error_message
                    AssertionError: Value mismatch DUT = 0xa0000001 does not match MODEL = 0x1
```

## Test Scenario
- Test inputs: mav_putvalue_src1 = 0x50000000, mav_putvalue_src2 = 0x5000000, mav_putvalue_src3 = 0x00000000, mav_putvalue_instr = 0x400070B3
- Expected Output: 0x1
- Observed Output in the DUT dut_output=0xa0000001

## Verification Strategy
Imported coroutine library from **cocotb.decorators**, Timer and RisingEdge libraries from **cocotb.triggers**, TestFailure from **cocotb.result** and imported Clock from **cocotb.clock** and then by changing the values in *mav_putvalue_instr* tested the given circuit.


# Level3_design (Trigonometric Function Implementer Circuit)
Here verification is done to Trigonometric Function Implementer Circuit to identify bugs in it. The test drives inputs to the Design under test (top_buggy module here) which takes inputs of 32-bit **degrees**, **clk**,**rst** and a 3-bit **actv** and gives a 64-bit **data1** as output which is in **IEEE 754** standard.

The values are assigned to the input ports *clk* and *rst* using
```
clock = Clock(dut.clk, 10, units="us")  # Create a 10us period clock on port clk
cocotb.start_soon(clock.start())        # Start the clock

# reset
dut.reset.value = 1
await FallingEdge(dut.clk)  
dut.reset.value = 0
await FallingEdge(dut.clk)
```
The value assigned to remaining input ports are
 ```
 dut.degrees.value=deg
 dut.actv.value=A
```

The assert statement is used for comparing the Trigonometric Function Implementer Circuit's output to expected output. So, by executing the **top_test.py**
The following errors is seen:
```
assert out==1011111111101111100000111000101110001100100000010001110000010111,"something went wrong  Model_out={out} Expected_out={EXP}".format(
      AssertionError: something went wrong: Model_out=0011111111101111100000111000101110001100100000010001110000010111,   Expected_out=1011111111101111100000111000101110001100100000010001110000010111
 ```
 
## Test scenario
- Test inputs: deg=280, A=0
- Expected output:1011111111101111100000111000101110001100100000010001110000010111
- Observed output in dut: 0011111111101111100000111000101110001100100000010001110000010111

## Design Bug
Based on the above test input and analysing the design, we see the following
```
///////////// If input value is between 181 and 360//////////
 
   if (degrees > `INPUT_WIDTH'd180 && (degrees < `INPUT_WIDTH'd360 || degrees == `INPUT_WIDTH'd360))
	begin
	degrees_tmp1 <= degrees - `INPUT_WIDTH'd180;
 
	begin
	  if(degrees_tmp1 >`INPUT_WIDTH'd90)
	    begin
	      quad <= 2'b00;    ==========================================>>BUG
	      degrees_tmp2 <= `INPUT_WIDTH'd180 - degrees_tmp1;
	      end
```
## Design Fix
Updating the design and re-running the test makes the test. The updated code is commited as **seq_detect_modified.v** file with no bugs.
