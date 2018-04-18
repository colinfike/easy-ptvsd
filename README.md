# EasyPtvsd 
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/ambv/black)

EasyPtvsd is a convenience library that makes it a bit easy to remote debug with ptvsd without having to remember the function calls and all that. It currently provides a decorator that can be used to setup the ptvsd server, wait for attachment, then immediately break into the debugger.

## Installation and Usage

### Installation

EasyPtvsd can be installed by running `pip install easy_ptvsd`.  It currently requires python 3.6+ but  should run on python 2 but not officially supported at this time.

### Usage

To get started import wait_and_break and decorate a function with it:

```
from easy_ptvsd import wait_and_break

@wait_and_break()
def test_function(message):
    print(message)

test_function('easy peezy')
```
This will pause execution until the remote debug session is attached to.

wait_and_break has default secret and address values of ```my_secret``` and ```("0.0.0.0", 3000)``` respectively. You can pass in your desired secret and address to the decorator if you wish to change the defaults.
```@wait_and_break(secret="custom_secret", address=("127.0.0.1", 3333))```

# Black
EasyPtvsd uses Black to format it's code to a consistent, determinitistic form. https://github.com/ambv/black
