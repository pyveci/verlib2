# Changelog


## Unreleased

## 2025-02-11 v0.3.0
- Added original `distutils/version.py` from Python 3.11.11.
  Because some custom version implementations derive from it,
  it is a good idea to have it around for Python 3.12 and higher.
- Fixed `verlib2.__version__`, now using `importlib.metadata`.

## 2025-02-02 v0.2.1
- Maintenance release including a minor change about a `mypy`
  admonition `left operand of "and" is always true`, ca3fb2d6da8.

## 2023-10-24 v0.2.0
- Add `version` property for backward-compatibility with `distutils.version`

## 2023-10-14 v0.1.0
- First release
