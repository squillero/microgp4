Contributing to MicroGP
=======================

First off all, thanks! :+1:

## How Can I Contribute?

* [Join the team](#join-the-team)
* Use the tool and [report a success story](#report)
* Fail to use the tool and [submit a bug report](#report)
* [Fix a bug](#coding)
* [Add a brand new functionality](#coding)
* [Improve an existing functionality](#coding)
* Extend/update/proofread the documentation
* Draw logo/icons
* [~~Donate money~~](#money-donations)

### Join the team

Welcome on board!  If you have a clear idea about an algorithmic improvement, but you are not able to hack it, just drop us an email.

If you are looking for a master thesis, contact directly Alberto (INRA) or Giovanni (Politecnico di Torino). Even if there are no theses officially advertised, there is always space for further improvements. Whether you are interested in a shorter activity, such a bachelor thesis, or a much longer one, don't hesitate contacting us.

### Reports

Use [GitHub's issues](https://github.com/squillero/microgp4/issues) for reporting bugs. 

### Coding

The source code is available on [GitHub](https://github.com/squillero/microgp4), feel free to fork and start implementing your sharp ideas --- we even prepared an oversimplified [stylesheet](#cding-style) to ease contributing to the code.

If you think you need it, ask Alberto or Giovanni to get write access to the main repo.

## Coding Style

> **Notez Bien**: All these rules are meant to be broken, **BUT** you need a very good reason **AND** you must explain it in a comment.

* Names (TL;DR): `module_name`, `package_name`, `ClassName`, `method_name`, `ExceptionName`, `function_name`, `GLOBAL_CONSTANT_NAME`, `global_var_name`, `instance_var_name`, `function_parameter_name`, `local_var_name`.

* Start names internal to a module or protected or private within a class with a single underscore (`_`); don't dunder (`__`).

* Use nouns for variables and properties names (`y = foo.baz`). Use full sentences for functions and methods names (`x = foo.calculate_next_bar(previous_bar)`); functions returning a boolean value (a.k.a., predicates) should start with the `is_` prefix (`if is_gargled(quz)`).

* Do not implement getters and setters, use properties instead. Whether a function does not need parameters consider using a property (`foo.first_bar` instead of `foo.calculate_first_bar()`). However, do not hide complexity: if a task is computationally intensive, use an explicit method (e.g., `big_number.get_prime_factors()`). 

* Do not override `__repr__`.

* Use `assert` to check the internal consistency and verify the correct usage of methods, not to check for the occurrence of unexpected events. That is: The optimized bytecode should not waste time verifying the correct invocation of methods or running sanity checks.

* Explain the purpose of all classes and functions in docstrings; be verbose when needed, otherwise use single-line descriptions (note: each verbose description also includes a concise one as its first line). Be terse describing methods, but verbose in the class docstring, possibly including usage examples. Comment public attributes and properties in the `Attributes` section of the class docstring (even though PyCharm is not supporting it, yet); don't explain basic customizations (e.g., `__str__`). Comment `__init__` only when its parameters are not obvious. Use the formats suggested in the [Google's style guide](https://google.github.io/styleguide/pyguide.html&#35;383-functions-and-methods).

* Annotate all functions (refer to [PEP-483](https://www.python.org/dev/peps/pep-0483/) and [PEP-484](https://www.python.org/dev/peps/pep-0484/) for details).

* Use English for names, in docstrings and in comments (favor formal language over slang, wit over humor, and American English over British).

* Format source code using [Yapf](https://github.com/google/yapf)'s style `"{based_on_style: google, column_limit=120, blank_line_before_module_docstring=true}"`

* Follow [PEP-440](https://www.python.org/dev/peps/pep-0440/) for version identification.

* Follow the [Google's style guide](https://google.github.io/styleguide/pyguide.html) whenever in doubt. 

## Conventions

### Paranoid classes

`Paranoid` classes implement `run_paranoia_checks()`.

The functions named `run_paranoia_checks` perform sanity checks. They always return `True`, but stop the execution throwing an exception as soon as an inconsistency is detected. The functions are not supposed to be called in production environments (i.e., when `-O` is used). Hint: it is safe to use `assert some_object.run_paranoia_checks()`. 

### Pedantic classes

`Pedantic`classes implement `is_valid(obj)`.

The functions named `is_valid` checks an object against a specification (e.g., a value against a parameter definition, a node against a section definition). They return either `True` or `False`. Hint: sometimes it could be useful to do something like
```python
def run_paranoia_checks(self):
    assert self.is_valid(self.value), "Meaningful message"
```

## Money Donations

Thanks for trying, but we do not accept money donations:

* Alberto and Giovanni are working on MicroGP as an integral part of their research activities. Thus, they are already paid by their institutions, namely: *Politecnico di Torino* (Italy) and *French National Institute for Agricultural Research* (France).
* Students worked, are working, and will work on MicroGP for their academic curricula, either master theses or Ph.D. programs.
* A few volunteers did a terrific job on specific topics, but, being volunteers, they did not ask for a wage.

So, why not donating **time** instead of money? Please contact us and join the project. 