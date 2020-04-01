""""""""""""
Installation
""""""""""""

MicroGP4 is available as a `PyPi package <https://en.wikipedia.org/wiki/Python_Package_Index>`_ from https://pypi.org/project/microgp/ and installing it is as simple as

::

    pip install microgp

and then

.. code-block:: python

    >>> import microgp as ugp4
    >>> ugp4.show_banner()

Optional dependencies
=====================

The packages `coloredlogs <https://pypi.org/project/coloredlogs/>`_, `matplotlib <https://pypi.org/project/matplotlib/>`_ and `psutil <https://pypi.org/project/psutil/>`_ are optional, they will not be installed by default, but are exploited if present.

::

    pip install coloredlogs matplotlib psutil

- Under Ubuntu/Debian, you may need ``Python.h``. For example:

::

    sudo apt install python3-dev
    pip3 install coloredlogs matplotlib psutil

- Under Windows, and if you are using `conda <https://docs.conda.io/projects/conda/>`_, you should probably:

::

    conda install coloredlogs matplotlib
    conda install --channel conda-forge psutil

Source Code
===========

The source code is hosted on `GitHub <https://en.wikipedia.org/wiki/GitHub>`_ at https://github.com/squillero/microgp4. The default branch is the more stable, experimental branches (``exp/*``) are only meaningful for developers.

It could be enough to:

::

    pip install -U -r requirements.txt
    python ./setup.py install

have fun...
