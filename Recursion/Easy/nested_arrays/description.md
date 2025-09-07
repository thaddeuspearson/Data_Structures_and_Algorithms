# Nested Array

## Description

A **Nested Array** is a list that can hold integers **or** other Nested Arrays (i.e., it can be nested).  
Its total value—often called the **product sum**—is computed by summing all integers, but giving extra weight to numbers inside nested lists. Specifically, items at the top level have weight **1**, items one level deeper have weight **2**, and so on.  
Formally, the value of a Nested Array is the sum of its elements, where the value of any sub-array is multiplied by its **depth** before being added.

## Example

Input:
[5, 2, [7, -1], 3, [6, [-13, 8], 4]]

Output:
12

Explanation:
Depth 1: 5 + 2 + 3 = 10
Depth 2: [7, -1] -> (7 + -1) * 2 = 6 * 2 = 12
Depth 2: [6, [-13, 8], 4]

    6 (at depth 2) contributes 6

    [-13, 8] at depth 3 -> (-13 + 8) * 3 = (-5) * 3 = -15

    4 (at depth 2) contributes 4
    Total for this sub-array at depth 2: (6 + -15 + 4) * 2 = (-5) * 2 = -10

Overall: 10 (depth 1) + 12 (first depth-2 array) + (-10) (second depth-2 array) = 12