# Reverse Word Pairs

## Description

Given a list of distinct strings, `words`, find all pairs of words where one word is the exact reverse of the other. Return each valid pair as a list containing both words. 

Each pair should appear only once in the result — meaning if `(word, drow)` is included, `(drow, word)` should not be duplicated elsewhere in the output.

The order of words in the pair should reflect their order in the input list: if `word` comes before `drow` in the list, the pair should be `(word, drow)`.

## Example

```
Input:
    words = ["stressed", "desserts", "hello", "world"]

Output:
    [["stressed", "desserts"]]
```