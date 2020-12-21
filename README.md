# Advanced-Computer-Architecture-Lab-3

Results collected by McPAT running on VirtualBox VM Ubuntu 19.10.
 
 
### Step 1: McPAT framework basics

#### Question 1:

As explained [here](https://semiengineering.com/knowledge_centers/low-power/low-power-design/power-consumption/):


Total Power = P<sub>switching</sub> + P<sub>short-circuit</sub> + P<sub>leakage</sub>

Dynamic power is the sum of two factors: switching power plus short-circuit power. Switching power is dissipated when charging or discharging internal and net capacitances. Short-circuit power is the power dissipated by an instantaneous short-circuit connection between the supply voltage and the ground at the time the gate switches state.

Leakage power is a function of the supply voltage, the switching threshold voltage, and the transistor size. Of the following leakage components, sub-threshold leakage is dominant.
* I1: Diode reverse bias current
* I2: Sub-threshold current
* I3: Gate-induced drain leakage
* I4: Gate oxide leakage

While dynamic power is dissipated only when switching, leakage power due to leakage current is continuous.

#### Question 2:

The 40 W processor could run a given program in less time than its 4 W counterpart, which would mean that, overall, the system would require less energy (assuming there are other components that consume power). In addition, if the 40 W processor has lower leakage power consumption, that would make it a more efficient choice. McPAT provides us with the total, dynamic, and leakage power, which could show us which processor is better (through the leakage/total power ratio).

#### Question 3:

From ```resultsARM_A9.txt``` and ```resultsXEON.txt```:

| Power        | ARM_A9  |  XEON   |
| :----------: | :-----: | :-----: |
| Total (Peak) | 1.74189 | 134.938 |
| Leakage      | 0.108687| 36.8319 |

If the ```ARM_A9``` processor took 40 seconds to run a given program, it would consume energy equal to ```40 * 1.74189 = 69.6756 J```, while the ```XEON``` processor, which would run the same program in 1 second, would consume ```134.938 J```. In addition to that, if we don't shut the system down after running the program, power leakage would continue. The ```ARM_A9``` processor has ```0.108687 W``` leakage power, while the ```XEON``` processor has ```36.8319``` leakage power. So, the ```ARM_A9``` processor is more energy efficient, since it consumes less energy and also has lower leakage power.

### Step 2: gem5 & McPAT: EDP optimization

#### Question 1:

#### Question 2:
