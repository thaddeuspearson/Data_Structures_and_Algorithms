# Monotonic Array

## Description

Write a function that takes in an array of numbers and returns a boolean indicating whether the array is monotonic. An array is said to be monotonic if its elements, from left to right, are entirely non-increasing or non-decreasing.

In other words, an array is monotonic if for every pair of indices `i` and `j` such that `i < j`, the elements at those positions either always satisfy `array[i] <= array[j]` or always satisfy `array[i] >= array[j]`.

An empty array or an array with one element is considered monotonic by definition.

## Example

```
Input:
    array = [1, 2, 2, 3]

Output:
    True
--------------------------

Input:
    array = [5, 4, 4, 2]

Output:
    True
--------------------------

Input:
    array = [1, 3, 2]

Output:
    False
```