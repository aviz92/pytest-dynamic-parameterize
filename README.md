# pytest-dynamic-parameterize
A powerful pytest plugin for Python projects, enabling dynamic test parameterization using functions. <br>
Easily generate test parameters at runtime from any function—supporting advanced, data-driven, or config-based testing workflows.

---

## 🚀 Features
- ✅ **Dynamic Parameterization**: Generate test parameters dynamically by referencing a function.
  - Use the `@pytest.mark.parametrize_func("function_name")` marker on your test.
  - Supports both local and fully-qualified function names (e.g., `my_func` or `my_module.my_func`).
  - Supports **multiple** `@pytest.mark.parametrize_func` markers on a single test for advanced parameterization.
  - Pass keyword arguments to your parameter function via the marker: `@pytest.mark.parametrize_func("my_params", some_param="some_value")`.
  - Enables:
    - Data-driven tests from config files, databases, or APIs
    - Centralized test data logic
    - Cleaner, more maintainable test code

---

## 📦 Installation
```bash
pip install pytest-dynamic-parameterize
```

---

### 🔧 Usage
1. **Define a parameter function** (must accept a `config` argument and return a list of tuples or values):

```python
# parameterize_functions.parametrize_functions.my_params.py
def my_params(config, some_param=None) -> list[tuple]:
    if some_param == "special":
        return [(10, 20, 30)]
    return [
        (1, 2, 3),
        (4, 5, 9),
    ]
```

2. **Mark your test with one or more `@pytest.mark.parametrize_func` decorators**:

```python
import pytest
from tests.parameterize_functions.parametrize_functions.my_params import my_params

@pytest.mark.parametrize_func("my_params")
def test_add(a, b, expected):
  assert a + b == expected
```

- **Pass arguments to your parameter function:**
  ```python
  import pytest
  from tests.parameterize_functions.parametrize_functions.my_params import my_params

  @pytest.mark.parametrize_func("my_params", some_param="special")
  def test_add_special(a, b, expected):
      assert a + b == expected
  ```

- **Use multiple parametrize_func markers for advanced parameterization:**
  ```python
  import pytest
  from tests.parameterize_functions.parametrize_functions.my_params import my_params

  @pytest.mark.parametrize_func("my_params", some_param="special")
  @pytest.mark.parametrize_func("my_params")
  def test_add_multi(a1, b1, expected1, a2, b2, expected2):
    assert a1 + b1 == expected1
    assert a2 + b2 == expected2
  ```

- You can also use a fully-qualified function path:
  ```python
  import pytest

  @pytest.mark.parametrize_func("parameterize_functions.parametrize_functions.my_params")
  def test_add(a, b, expected):
      ...
  ```

- The function can be imported or defined in the same module.
- The function should return a list of argument tuples matching the test signature.

---

## 🤝 Contributing
If you have improvements, ideas, or bugfixes:
- Fork the repo <br>
- Create a new branch <br>
- Submit a pull request <br>
I welcome additions that promote clean, productive, and maintainable development. <br>

---

## 🙏 Thanks
Thanks for exploring this repository! <br>
Happy testing! <br>
