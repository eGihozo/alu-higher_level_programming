# python-almost_a_circle

I am working on a Python project about classes, inheritance, JSON
serialization, file storage and unit tests. It has a `Base` class and
`Rectangle` and `Square` classes built on top of it.

| File | Description |
|------|-------------|
| `models/base.py` | `Base` class: ids, JSON strings, save and load from files |
| `models/rectangle.py` | `Rectangle` class with validation, display and update |
| `models/square.py` | `Square` class that inherits from `Rectangle` |
| `tests/test_base.py` | Unittests for `Base` |
| `tests/test_rectangle.py` | Unittests for `Rectangle` |
| `tests/test_square.py` | Unittests for `Square` |

Run the tests with `python3 -m unittest discover tests`.
