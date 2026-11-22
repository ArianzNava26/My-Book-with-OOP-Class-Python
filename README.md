# OOP Python Practice

A small collection of Python scripts for learning Object-Oriented Programming (OOP).

## Contents

| File | Description |
| --- | --- |
| `2D.py` | Book stock manager built with a simple class |

## `2D.py`

`2D.py` demonstrates the basics of classes and objects in Python.

It defines a `DaftarBukuku` (my book list) class that stores a book title and its
stock, creates three book objects, prints their details, and then runs an
interactive loop that lets the user add to or subtract from the stock of a
chosen book.

### What it covers

- Defining a class with `__init__`
- Creating instances (objects)
- Accessing instance attributes
- Using `f`-strings for output
- A `while` loop with `if` / `elif` branching
- Reading user input with `input()`

### Requirements

- Python 3.6 or newer

### Running

```bash
python3 2D.py
```

### Example interaction

```text
Mau Nambah apa kurang? nambah
Buku yang mana? 1
Berapa? 5
Maka Stok buku 1 menjadi 25
Lanjut gak? y
oke
```

## Notes

- `venv/` and `__pycache__/` are ignored via `.gitignore`.
- The prompts and messages inside the script are written in Indonesian.
