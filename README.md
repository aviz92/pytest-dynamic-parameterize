# pytest-dynamic-parameterize
A powerful pytest plugin for Python projects, enabling dynamic test parameterization using functions. <br>
Easily generate test parameters at runtime from any function—supporting advanced, data-driven, or config-based testing workflows.

---

## 🚀 Features
- ✅ **Dynamic Parameterization**: Generate test parameters dynamically by referencing a function.
  - Use the `@pytest.mark.parametrize_func("function_name")` marker on your test.
  - Supports both local and fully-qualified function names (e.g., `my_func` or `my_module.my_func`).
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
# parameterize_functions.dynamic_parameters.my_params.py
def my_params(config):
    # Example: generate parameters dynamically
    return [
        (1, 2, 3),
        (4, 5, 9),
    ]
```

2. **Mark your test with `@pytest.mark.parametrize_func`**:

```python
import pytest
from parameterize_functions.dynamic_parameters import my_params

@pytest.mark.parametrize_func("my_params")
def test_add(a, b, expected):
    assert a + b == expected
```

- You can also use a fully-qualified function path:
  ```python
  @pytest.mark.parametrize_func("parameterize_functions.dynamic_parameters.my_params")
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
