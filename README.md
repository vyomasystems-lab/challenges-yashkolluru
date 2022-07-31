# challenges-yashkolluru
challenges-yashkolluru created by GitHub Classroom

## Verification Environment

The verification environment is setup using [Vyoma's UpTickPro](https://vyomasystems.com) provided for the hackathon. The [CoCoTb](https://www.cocotb.org/) based Python test is developed as explained.

## Level1_design

Here the verification is done to MUX circuit to identify bugs. 
The test drives inputs to the Design under test (mux module here) which takes 30 2-bit inputs *inp0 to inp30, 5-bit select lines *sel* and 2-bit otput *out*.

The values are assigned to the input port using 
```
