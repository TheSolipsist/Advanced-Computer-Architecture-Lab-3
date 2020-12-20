# Advanced-Computer-Architecture-Lab-3

Results collected by McPAT running on VirtualBox VM Ubuntu 19.10.
 
 
### Step 1: McPAT framework basics

#### Question 1:

As explained [here](https://semiengineering.com/knowledge_centers/low-power/low-power-design/power-consumption/):


Total Power = P<sub>switching</sub> + P<sub>short-circuit</sub> + P<sub>leakage</sub>

Dynamic power is the sum of two factors: switching power plus short-circuit power. Switching power is dissipated when charging or discharging internal and net capacitances. Short-circuit power is the power dissipated by an instantaneous short-circuit connection between the supply voltage and the ground at the time the gate switches state.

Leakage power is a function of the supply voltage, the switching threshold voltage, and the transistor size.

Of the following leakage components, sub-threshold leakage is dominant.
* I1: Diode reverse bias current
* I2: Sub-threshold current
* I3: Gate-induced drain leakage
* I4: Gate oxide leakage

While dynamic power is dissipated only when switching, leakage power due to leakage current is continuous.

#### Question 2:

The 40 W processor could run a given program in less time than its 4 W counterpart, which would mean that, overall, the system would require less energy (assuming there are other components that consume power). In addition, if the 40 W processor has lower leakage power consumption, that would make it a more efficient choice. McPAT provides us with the total, dynamic, and leakage power, which could show us which processor is better (through the leakage/total ratio).

#### Question 3:

### Step 2: gem5 & McPAT: EDP optimization

#### Question 1:

#### Question 2:
