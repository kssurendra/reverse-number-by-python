# Number Tools

A tiny Python app that reverses an integer and checks whether it is a palindrome.
It includes a Tkinter interface.

Run the app:

```powershell
python number_tools.py
```

Run the tests:

```powershell
python -m unittest discover -s tests
```

Negative integers keep their sign when reversed and are not considered
palindromes. Reversing drops leading zeroes in the result (for example, `1200`
becomes `21`).
