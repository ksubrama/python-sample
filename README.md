## Setup

This code was tested on Python 3.6 using the modules in the requirements.txt file.
I suspect it will work on anything 3.3+.

Please see the Makefile and run `make init` to install all the pip modules needed.

## Running tests and "driver"

This is default make target or `make test` if you prefer.  This will lint and test
the library.

A top-level "app.py" is provided to run the given code with a few samples.
`make run` will launch that.
