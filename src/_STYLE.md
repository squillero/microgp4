CODING CONVENTION & STYLE 
=========================

Welcome onboard! And thank you for trying to help the project with your code.

> Some lines of code or comments may be considered inappropriate by some. Reader discretion is advised. 

## Coding style

* Names (TL;DR): `module_name`, `package_name`, `ClassName`, `method_name`, `ExceptionName`, `function_name`, `GLOBAL_CONSTANT_NAME`, `global_var_name`, `instance_var_name`, `function_parameter_name`, `local_var_name`.

* Start names internal to a module or protected or private within a class with a single underscore (`_`); don't dunder (`__`), unless you have a very good reason and you explain it in the code.

* Use nouns for variables and properties names (`y = foo.baz`). Use full sentences for functions and methods names (`x = foo.get_first_bar()`); functions returning a boolean value (a.k.a., predicates) should start with the `is_` prefix (`if foo.is_gargled()`)

* Do not implement getters and setters, use properties instead.

* Do not override `__repr__`.

* Use `assert` to check the internal consistency and verify the correct usage of methods, not to check for the occurrence of unexpected events. Asserts are only executed in debug mode, not in production.

* Explain the purpose of all classes and functions in docstrings; be verbose when needed, otherwise use single-line descriptions (note: each verbose description also includes a concise one as its first line). Be terse describing methods, but verbose in the class docstring, possibly including usage examples. Comment public attributes and properties in the `Attributes` section of the class docstring (even though PyCharm is not supporting it, yet); don't explain basic customizations (e.g., `__str__`). Comment `__init__` 
only when its parameters are not obvious. Use the formats suggested in the [Google's style guide](https://google.github.io/styleguide/pyguide.html&#35;383-functions-and-methods).

* Annotate all functions (refer to [PEP-483](https://www.python.org/dev/peps/pep-0483/) and [PEP-484](https://www.python.org/dev/peps/pep-0484/) for details).

* Use English for names, in docstrings and in comments (favor formal language over slang, wit over humor, and American English over British).

* Format source code using [Yapf](https://github.com/google/yapf)'s style `"{based_on_style: google, column_limit=120, blank_line_before_module_docstring=true}"`

* Follow [PEP-440](https://www.python.org/dev/peps/pep-0440/) for version identification.

* Follow the [Google's style guide](https://google.github.io/styleguide/pyguide.html) whenever in doubt. 

## Conventions

### Checks

The functions named `run_paranoia_checks` perform sanity checks. They always return `True`, but stop the execution throwing an exception as soon as an inconsistency is detected. The functions are not supposed to be called in production environments (i.e., when `-O` is used). Hint: it is safe to use `assert some_object.run_paranoia_checks()`. `Paranoid` classes implement the `run_paranoia_checks`.

The functions named `is_valid` checks an object against a specification (e.g., a value against a parameter definition, a node against a section definition). They return either `True` or `False`. `Pedantic`classes implement the `is_valid`. Hint: sometimes it could be useful to 
```python
def run_paranoia_checks(self):
    assert self.is_valid()
```
As an alternative, `Pedantic` classes implements the `valid` attribute.
