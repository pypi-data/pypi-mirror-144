# Python client

`dfir_iris_client` offers a Python interface to communicate with IRIS.

It relies exclusively on the API, which means output of the methods are the same as specified in the API reference.

## Versions
The Python client version follows the API versions (until the patch level). Meaning for API v1.0.1, one need to install `dfir_iris_client-1.0.1`.


## Build
To build a wheel from the sources:

1. `pip3 install wheel`
2. `python setup.py bdist_wheel --universal`
3. `pip3 install build/XXX.whl`


## Examples
Some examples are available [https://github.com/dfir-iris/iris-client/templates](here).

## Documentation 
The documentation is available in the [https://dfir-iris.github.io/modules/modules.html](documentation).
