# Rankine_Cycle_Diff
Simple script to find the difference between having only one turbine in a rankine cycle and multiple turbines.

You need the CoolProp, multiprocessing, time and numpy libraries in python.
You probably only need CoolProp tho, so just do a -pip install CoolProp and it should be fine.

This was just a whim of mine, i was curious why  there's only one turbine in the Rankine Cycle, so i tried to transform the mathematical equations, stumped on how to find all intermediate real enthalpies, decided to try to use a script to forcefully find the solution. If you're curious, there is an actual increase in work produced, it's just super small and the more turbines there are the less the increase.

**Small Edit. I wanted to mess with the expansion efficiencies of turbines, so i graphed the difference between 1 and n turbines based on the expansion efficiencies ranging from 0 to 1. It resulted in a nice clean graph that is leaning toward left. From what i saw, the more turbines, the more the graph leans left, with its movement decreasing with the increasing number of turbines. I think the limit may go towards a number (maybe around 0.35?) but i'm too dumb to know the math.
