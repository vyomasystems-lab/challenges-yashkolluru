# challenges-yashkolluru
challenges-yashkolluru created by GitHub Classroom

![](https://github.com/vyomasystems-lab/challenges-yashkolluru/blob/master/Screenshot%20(86).png)
## Verification Environment

The verification environment is setup using [Vyoma's UpTickPro](https://vyomasystems.com) provided for the hackathon. The [CoCoTb](https://www.cocotb.org/) based Python test is developed as explained.

## Level1_design

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
i)when S=30 was assigned by random function in **test_mux1(dut)**
```
 assert dut.out.value == In[S], "Mux result is incorrect:model_out={Out}, expected output={EXP} at sel={SEL}".format(
 AssertionError: Mux result is incorrect:model_out=0, expected output=2 at sel=30
```
ii)when S=13 was assigned by random function in **test_mux(dut)**
```
 assert dut.out.value == In[S], "Mux result is incorrect:model_out={Out}, expected output={EXP} at sel={SEL}".format(
  AssertionError: Mux result is incorrect:model_out=0, expected output=1 at sel=13
```

## Test Scenario
i)when S=13 was assigned by random function in **test_mux(dut)**
-Test Inputs: inp0=0.... inp12=0 inp13=1 .....inp30=2
-Expected Output: out=1
-Observed Output in the DUT dut.out=0

ii)when S=30 was assigned by random function in **test_mux1(dut)**
-Test Inputs: inp0=0.... inp12=0 inp13=1 .....inp30=2
-Expected Output: out=2
-Observed Output in the DUT dut.out=0

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

