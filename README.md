Przykładowy projekt Arkanos
===========================

Run
---

Create venv/virtualenv. Then (in case of venv):
`venv\Scripts\activate` (Windows) or `. venv/bin/activate` (Linux). When finished working with Arkanos, type: `deactivate`.

`python -u arkanos/main.py`

Test
----
Prepare:
`pip install mypy pytest coverage`

Run:
- `mypy arkanos --check-untyped-defs`
- `pytest`
- `python -m doctest -v arkanos\logic\pieces.py`, or better: `pytest --doctest-modules`
- `python -m unittest ` to run only unittest-based tests
- In PyCharm add new configuration, select "pytest", set project path or specific test, eg.: `...PycharmProjects/arkanos/tests/test_pieces.py::test_fight`
  You may add `--doctest-modules` as "Additional Arguments" 
- `coverage run -m pytest` or `coverage run --branch -m pytest`
  - then `coverage report`
  - or `coverage html`

With tox:
```commandline
pip install tox
tox
```

Links
-----

Gitignore taken from
https://github.com/github/gitignore/raw/main/Python.gitignore

Unicode shapes to be used: http://xahlee.info/comp/unicode_drawing_shapes.html 