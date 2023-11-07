#!/usr/bin/python3
# 1-my_list.py
"""an inherited list class MyList."""


class MyList(list):
    def print_sorted(self):
        """Print a list in ascending order."""
        print(sorted(self))
