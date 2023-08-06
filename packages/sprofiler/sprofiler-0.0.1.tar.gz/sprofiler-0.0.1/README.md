# sProfiler
Python script profiler/timer supporting code checkpoints and reporting.

## Installation
```
pip install sprofiler
```

## Usage
Use the `Timer` to create named checkpoints throughout your code. Checkpoints need a 'start' and a 'stop', and 
multiple iterations are combined to summarize how long it takes to complete each leg. The `report()` function
prints the results from all checkpoints.
```
import sprofiler as sp
from time import sleep

pr = sp.Profiler()

pr.start('program')
print('Code outside loop')
sleep(1)
    
for _ in range(10):
    pr.start('loop')
    print('Code in loop')
    sleep(1)
    pr.stop('loop')
pr.stop('program')
    
pr.report()
```

The printed report appears as:
```
program | 11.0 s ± 0.0 s per iteration, n = 1
loop | 1.0 s ± 0.0 s per iteration, n = 10
```

## Future Directions

* Automatic logging, so that `report()` isn't strictly needed
* Function decorators
* Potential support for more complex profiling
