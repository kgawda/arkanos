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
`pip install mypy pytest`

Run:
- `mypy arkanos --check-untyped-defs`
- `pytest`
- `python -m doctest -v arkanos\logic\pieces.py`, or better: `pytest --doctest-modules`
- `python -m unittest ` to run only unittest-based tests

Links
-----

Gitignore taken from
https://github.com/github/gitignore/raw/main/Python.gitignore

Unicode shapes to be used: http://xahlee.info/comp/unicode_drawing_shapes.html 