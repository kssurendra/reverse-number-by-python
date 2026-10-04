"""Reverse integers and check whether they are palindromes."""

import tkinter as tk
from tkinter import ttk


def reverse_integer(value: int) -> int:
    """Return the digits of an integer in reverse order, preserving its sign."""
    sign = -1 if value < 0 else 1
    return sign * int(str(abs(value))[::-1])


def is_palindrome(value: int) -> bool:
    """Return whether a non-negative integer reads the same both ways."""
    return value >= 0 and value == reverse_integer(value)


def main() -> None:
    root = tk.Tk()
    root.title("Number Tools")
    root.resizable(False, False)

    frame = ttk.Frame(root, padding=16)
    frame.grid()

    ttk.Label(frame, text="Enter an integer:").grid(
        row=0, column=0, sticky="w", pady=(0, 8)
    )
    number_entry = ttk.Entry(frame, width=24)
    number_entry.grid(row=1, column=0, sticky="ew", pady=(0, 8))
    result_label = ttk.Label(frame, text=" ")
    result_label.grid(row=3, column=0, sticky="w", pady=(8, 0))

    def analyze_number() -> None:
        try:
            value = int(number_entry.get())
        except ValueError:
            result_label.config(text="Please enter a valid integer.")
            return

        reversed_value = reverse_integer(value)
        palindrome = "Yes" if is_palindrome(value) else "No"
        result_label.config(
            text=f"Reversed: {reversed_value}\nPalindrome: {palindrome}"
        )

    ttk.Button(frame, text="Analyze", command=analyze_number).grid(
        row=2, column=0, sticky="ew"
    )
    number_entry.bind("<Return>", lambda _event: analyze_number())
    number_entry.focus()

    root.mainloop()


if __name__ == "__main__":
    main()
