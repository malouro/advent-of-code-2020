<h1 style="text-align: center;">🎄</h1>

<p style="text-align: center;">
Puzzle solving @ <a href="https://adventofcode.com/2020">Advent of Code</a>
</p>

## Running

Installing dependencies (needed for pre-commit checks and running tests)

```bash
pip install -r requirements-dev.txt
```

## Testing

Test files exist alongside their corresponding puzzle solution, with the naming convention of `test_{day}.py` (ie: `test_01.py`, etc.)

Run full test suite with:

```bash
pytest
```

Run a particular puzzle's tests with:

```bash
pytest calendar/{day}
# Eg: `pytest calendar/01`
```
