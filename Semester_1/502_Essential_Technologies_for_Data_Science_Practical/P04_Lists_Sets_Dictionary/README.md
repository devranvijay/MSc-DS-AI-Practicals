# Practical 04 — Lists, Sets, and Dictionaries

**Subject:** 502 – Essential Technologies for Data Science
**File:** `lists_sets_dictionary.py`

## Aim
To demonstrate creation and manipulation of Python's core built-in
data structures — `list`, `set`, and `dict` — including comprehensions.

## Theory
- **List**: An ordered, mutable, index-based collection that allows
  duplicate values. Supports slicing, sorting, and comprehensions.
- **Set**: An unordered collection of unique elements; supports
  mathematical set operations (union, intersection, difference,
  symmetric difference).
- **Dictionary**: A mutable mapping of unique keys to values, offering
  average O(1) lookup — Python's implementation of a hash map.

## How to Run
```bash
python lists_sets_dictionary.py
```

## Sample Output
```
Union (either course)  : {'Aditi', 'Rohan', 'Meera', 'Karan', 'Divya', 'Priya'}
Intersection (both)    : {'Rohan', 'Karan'}
Topper: Meera with 95 marks
```

## Viva Questions & Answers
1. **Q: What is the main difference between a list and a set?**
   A: A list preserves order and allows duplicates; a set stores only
   unique elements and has no guaranteed order (in practice, insertion
   order is not preserved).
2. **Q: What is the time complexity of a dictionary lookup?**
   A: On average O(1), because dictionaries are implemented as hash
   tables in CPython.
3. **Q: How do you remove duplicates from a list using a set?**
   A: `unique_items = list(set(my_list))` — though this loses the
   original order unless combined with `dict.fromkeys(my_list)`.
4. **Q: What is a dictionary comprehension? Give its syntax.**
   A: A concise way to build a dictionary: `{key_expr: value_expr for
   item in iterable}`.
5. **Q: Why are sets useful for "belongs to" style checks?**
   A: Membership testing (`x in my_set`) is on average O(1) for sets
   versus O(n) for lists.

## Real-World Relevance
These structures underpin every `pandas` DataFrame (built from dicts
of lists), feature-engineering deduplication tasks (sets), and ordered
record processing (lists) in real data pipelines.
