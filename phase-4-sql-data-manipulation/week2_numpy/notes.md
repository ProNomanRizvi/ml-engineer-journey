# Phase 4 - Week 2: NumPy Notes

## Topic 1: Arrays

A NumPy array is like a Python list, but much faster for number-crunching
because it's built in C under the hood. Regular lists can hold mixed
data types, but NumPy arrays hold only one type of number.

Ways to create arrays:
- `np.array([1,2,3])` - from a list
- `np.zeros(5)` / `np.ones(5)` - filled with 0s or 1s
- `np.arange(0,10,2)` - a range with a step
- `np.linspace(0,1,5)` - evenly spaced numbers

Useful attributes to check an array:
- `.shape` - dimensions (rows, columns)
- `.ndim` - how many dimensions (1D, 2D...)
- `.dtype` - what type of numbers it holds
- `.size` - total number of elements

A 2D array is basically a matrix (rows and columns) — this is how tables,
images, and most ML data gets represented.

---

## Topic 2: Vectorization

Vectorization means applying an operation to an entire array at once,
instead of writing a loop to go element by element.

```python
prices * 0.9   # applies to every element instantly
```

I tested this with 1 million elements — a normal Python loop took about
0.21 seconds, while the vectorized NumPy version took only 0.015 seconds.
That's roughly 13-14x faster. This is why NumPy is so important for ML —
loops become too slow once data gets big.

---

## Topic 3: Broadcasting

Broadcasting lets NumPy do math between arrays of different shapes, by
automatically "stretching" the smaller one to match.

- Adding a single number to a whole array stretches that number across
  every element.
- Adding a 1D row to a 2D matrix repeats that row for every row in the
  matrix.
- Two arrays with different shapes, like a column (3,1) and a row (1,3),
  can even stretch in both directions at once and produce a bigger
  matrix.

If shapes don't fit the broadcasting rules, NumPy throws an error instead
of guessing.

---

## Topic 4: Indexing and Slicing

Indexing means grabbing specific elements, slicing means grabbing a
range.

- `arr[0]` / `arr[-1]` - first / last element
- `arr[1:4]` - a range of elements
- `arr[::2]` - every second element

For 2D arrays, indexing uses `[row, column]`:
- `matrix[1, :]` - whole row
- `matrix[:, 2]` - whole column
- `matrix[0:2, 0:2]` - a smaller block from the matrix

Boolean indexing filters based on a condition:
```python
arr[arr > 50]   # only elements greater than 50
```

Fancy indexing picks specific positions at once:
```python
arr[[0, 3, 7]]   # elements at index 0, 3, and 7
```

---

## Topic 5: Math Operations and Dot Product

NumPy has built-in math functions that work on the whole array:
`np.sqrt()`, `np.exp()`, `np.log()`, `np.sum()`, `np.mean()`, `np.max()`,
`np.min()`, `np.std()`.

**Dot product** multiplies matching elements of two arrays and adds them
up into a single number:

```
[1,2,3] · [4,5,6] = (14)+(25)+(3*6) = 32
```

For 2D arrays (matrices), the dot product becomes matrix multiplication.
The rule: the number of columns in the first matrix must match the
number of rows in the second matrix. If they don't match, NumPy throws
an error.

Dot product matters a lot in ML because it's the core operation inside
every layer of a neural network.

---

## Overall Week 2 Summary

- Arrays = fast containers for numbers
- Vectorization = doing math on a whole array at once, much faster than loops
- Broadcasting = doing math between different-shaped arrays automatically
- Indexing/Slicing = grabbing exact pieces of data
- Dot product = the multiply-and-add operation that powers ML math