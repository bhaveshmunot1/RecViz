# RecViz
A small library to ease the visualization of recursion

---

### Requirements :
1. `inspect` module

### How to use :
1. Just import 'RecViz' and create an object in recursive function - `x= RecViz.EnableLogging(inspect.currentframe())`
2. If you want to log the return values as well, instead of returning a value direct use - `return x.LogAndReturn(value)`
(See visualizer.py for example)

### Output :
This generates an output file named "RecViz.log" which has the information in XML format.

### TODO :
Add GUI to RecViz.log for visualization.
