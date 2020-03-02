""""""""""
Parameters
""""""""""

.. toctree::
    :caption: Parameters
    :maxdepth: 2

The parameters are used to make the macros dynamic. For example you can build
a parameter of type :mod:`microgp.parameter.categorical.Categorical` passing
some values (`alternatives`); the macro that contains this kind of parameter
will take the given values and the resulting text of the macro will depend on
the values taken by the parameters assigned. The method
:mod:`microgp.parameter.helpers.make_parameter` allows to build a parameter
providing the parameter class type and the needed attributes.

**Examples:**

>>> registers = ugp.make_parameter(ugp.parameter.Categorical, alternatives=['ax', 'bx', 'cx', 'dx'])
>>> int256 = ugp.make_parameter(ugp.parameter.Integer, min=0, max=256)
>>> add = ugp.Macro("    add {reg}, 0{num:x}h ; ie. {reg} += {num}", {'reg': registers, 'num': int256})


There are several types of parameters:

- `Integer`_ (:mod:`microgp.parameter.integer.Integer`);

- `Bitstring`_ (:mod:`microgp.parameter.bitstring.Bitstring`);

- `Categorical, CategoricalSorted`_ (:mod:`microgp.parameter.categorical`);

- `LocalReference, ExternalReference`_ (:mod:`microgp.parameter.reference`);

- `Information`_ (:mod:`microgp.parameter.special.Information`).

Parameter
=========

Parameters inheritance hierarchies:

.. image:: ../images/parameter_class_uml.jpg
  :width: 800
  :alt: Structure of a node


:mod:`microgp.parameter.Parameter`

.. autoclass:: microgp.parameter.Parameter

:mod:`microgp.parameter.Structural`

.. autoclass:: microgp.parameter.Structural

:mod:`microgp.parameter.Special`

.. autoclass:: microgp.parameter.Special

Integer
*******

:mod:`microgp.parameter.integer`

.. automodule:: microgp.parameter.integer
    :members:

Bitstring
*********

:mod:`microgp.parameter.bitstring`

.. automodule:: microgp.parameter.bitstring
    :members:

Categorical, CategoricalSorted
******************************

:mod:`microgp.parameter.categorical`

.. automodule:: microgp.parameter.categorical
    :members:

LocalReference, ExternalReference
*********************************

:mod:`microgp.parameter.reference`

.. autoclass:: microgp.parameter.reference.Reference

.. autoclass:: microgp.parameter.reference.LocalReference

.. autoclass:: microgp.parameter.reference.ExternalReference

Information
***********

:mod:`microgp.parameter.special.Information`

.. autoclass:: microgp.parameter.special.Information

Helpers
=======

:mod:`microgp.parameter.helpers`

.. automodule:: microgp.parameter.helpers
    :members:
