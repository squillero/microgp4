### Coding Style

> **Notez Bien**: All these rules are meant to be broken, **BUT** you need a very good reason **AND** you must explain it in a comment.

* Names (TL;DR): `module_name`, `package_name`, `ClassName`, `method_name`, `ExceptionName`, `function_name`, `GLOBAL_CONSTANT_NAME`, `global_var_name`, `instance_var_name`, `function_parameter_name`, `local_var_name`.

* Start names internal to a module or protected or private within a class with a single underscore (`_`); don't dunder (`__`).

* Use nouns for variables and properties names (`y = foo.baz`). Use full sentences for functions and methods names (`x = foo.calculate_next_bar(previous_bar)`); predicates (i.e., functions returning a boolean value) should start with the `is_` prefix (`if is_gargled(quz):`).

* Do not implement getters and setters, use properties instead. Whether a function does not need parameters consider using a property (`foo.first_bar` instead of `foo.calculate_first_bar()`). However, do not hide complexity: if a task is computationally intensive, use an explicit method (`big_number.get_prime_factors()`). 

* Do not override `__repr__`.

* Use `assert` to check the internal consistency and verify the correct usage of methods, not to check for the occurrence of unexpected events. That is: The optimized bytecode should not waste time verifying the correct invocation of methods or running sanity checks.

* Annotate all functions (refer to [PEP-483](https://www.python.org/dev/peps/pep-0483/) and [PEP-484](https://www.python.org/dev/peps/pep-0484/) for details).

* Prefer an f-string (a.k.a. formatted string literal) over an explicit formatting operation or the string interpolation operator (`f"v={foo}"` instead of `"v={}".format(foo)` or `"v=%s" % (foo,)`). Use single quotes for string constants such as function parameters and dictionary keys (`'utf-8'` or `data['foo']`); use double quotes for messages to the user (`logging.warning(f"data: {data['bar']}")`).

* Explicitly derive container classes from `collections.abc`.

* Override `__getstate__` and `__setstate__` if you define `__slots__`; write these functions in the very beginning of the class, before `__init__`. Define `__slots__` only if you are really confident about it.

* Explain the purpose of all classes and functions in docstrings; be verbose when needed, otherwise use single-line descriptions (note: each verbose description also includes a concise one as its first line). Be terse describing methods, but verbose in the class docstring, possibly including usage examples. Comment public attributes and properties in the `Attributes` section of the class docstring (even though PyCharm is not supporting it, yet); don't explain basic customizations (e.g., `__str__`). Comment `__init__` only when its parameters are not obvious. Use the formats suggested in the [Google's style guide](https://google.github.io/styleguide/pyguide.html&#35;383-functions-and-methods).

* Use English for names, in docstrings and in comments. Favor formal language over slang, wit over humor, and American English over British.

* Format source code using [Yapf](https://github.com/google/yapf)'s style `"{based_on_style: google, column_limit=120, blank_line_before_module_docstring=true}"`

* Follow [PEP-440](https://www.python.org/dev/peps/pep-0440/) for version identification.

* Follow the [Google's style guide](https://google.github.io/styleguide/pyguide.html) whenever in doubt. 

### Conventions

#### Paranoid classes

`Paranoid` classes implement `run_paranoia_checks()`.

The functions named `run_paranoia_checks` perform sanity checks. They always return `True`, but stop the execution throwing an exception as soon as an inconsistency is detected. The functions are not supposed to be called in production environments (i.e., when `-O` is used). Hint: it is safe to use `assert some_object.run_paranoia_checks()`. 

#### Pedantic classes

`Pedantic`classes implement `is_valid(obj)`.

The functions named `is_valid` checks an object against a specification (e.g., a value against a parameter definition, a node against a section definition). They return either `True` or `False`. Hint: sometimes it could be useful to do something like
```python
def run_paranoia_checks(self):
    assert self.is_valid(self.value), "Meaningful message"
```

