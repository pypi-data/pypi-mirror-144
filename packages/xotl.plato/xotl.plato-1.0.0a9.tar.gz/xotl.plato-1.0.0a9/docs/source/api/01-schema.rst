==============================================================================
 :mod:`xotl.plato.schema` -- Automatic cast to the type system using schemata
==============================================================================

.. module:: xotl.plato.schema

This module a bridge between `dataclasses`:class: and the `our type system
<xotl.plato.types>`:mod:.   We provide a `SchemaBase`:class: applicable to
dataclasses, that then can be easily parsed/dumped with the types.

.. testsetup::

   import enum
   import dataclasses
   from datetime import datetime, date, timedelta
   from xotl.plato.types import *
   from xotl.plato.schema import *

.. autoclass:: SchemaBase
   :members: get_static_type, reset_static_type_cache

Hooks and hacks
===============

Schemata's type system includes some extensions to the type system which are
useful to bridge some Python's type that don't have an obvious type object in
`xotl.plato.types`:mod:.

.. class:: SchemaType

   This is the type object returned by `SchemaBase.get_static_type`:meth:.
   It's similar to `~xotl.plato.types.ObjectType`:class: but it must keep a
   reference to the dataclass to be able to create instances with
   `SchemaBase.from_full_repr`:meth:

.. autoclass:: EnumType

.. autoclass:: IntEnumType

.. autofunction:: register_simple_type_map

.. autofunction:: reset_simple_type_map

.. autofunction:: temp_simple_type_map
