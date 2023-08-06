# spx17979-driver
Python driver for the [SparkFun SPX-17979 Qwiic Sound Trigger](https://www.sparkfun.com/products/17979).

![PyPI](https://img.shields.io/pypi/v/spx17979-driver)
![PyPI - License](https://img.shields.io/pypi/l/spx17979-driver)
![PyPI - Downloads](https://img.shields.io/pypi/dm/spx17979-driver) 


## Installation

The package is available on PyPI. Installation is can be done with your favourite package manager. For example:

```bash
pip install spx17979-driver
```

## Usage

In order to initialise the device we need an open `SMBus` object. 
Depending on the machine that you are running on you may need to provide another bus number or path:
```python
from spx17979 import SPX17979
from smbus2 import SMBus


with SMBus(1) as bus:
    device = SPX17979(bus=bus)
```

When the device has been triggered by a sound, the `trigger` property will be `True`. 
It can be reset by calling the `reset()` method. That is it!

A simple usage example:
```python
from time import sleep

from spx17979 import SPX17979
from smbus2 import SMBus


with SMBus(1) as bus:
    device = SPX17979(bus=bus)
    device.reset()
    
    while True:
        if device.trigger:
            print("Triggered!")
            sleep(0.5)  # Prevent triggering twice on the same sound
            device.reset()
        sleep(0.001)
```


