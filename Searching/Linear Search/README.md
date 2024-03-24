Linear Search, also known as Sequential Search, is one of the simplest and most straightforward searching algorithms. It works by sequentially examining each element in a collection of data(array or list) until a match is found or the entire collection has been traversed.

**How Does Linear Search Algorithm Work**:

    • Every element is considered as a potential match for the key and checked for the same.
    • If any element is found equal to the key, the search is successful and the index of that element is returned.
    • If no element is found equal to the key, the search return -1.

|                  | Best                                  | Average | Worst                                |
| ---------------- | ------------------------------------- | ------- | ------------------------------------ |
| Time Complexity  | O(1) - key present at the first index | O(N)    | O(N) - key present at the last index |
| Space Complexity | O(1)                                  | O(1)    | O(1)                                 |