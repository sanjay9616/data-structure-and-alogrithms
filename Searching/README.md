<h2>Searching</h2>

Searching is a technique to find a desired item within a collection of data. This collection of data can take various forms, such as arrays, lists, trees, or other structured representations.

Below are some search algorithms and their time complexity and space complexity:

| Algorithm                                                                                                                                                                 | Best | Average                              | Worst                 | Space Complexity |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---- | ------------------------------------ | --------------------- | ---------------- |
| <a href="https://github.com/sanjay9616/data-structure-and-alogrithms/tree/master/Searching/Linear%20Search">Linear Search</a>                                             | O(1) | O(N)                                 | O(N)                  | O(1)             |
| <a href="https://github.com/sanjay9616/data-structure-and-alogrithms/blob/master/Searching/Sentinel%20Linear%20Search/README.md">Sentinel Linear Search</a>               | O(1) | O(N)                                 | O(N)                  | O(1)             |
| <a href="https://github.com/sanjay9616/data-structure-and-alogrithms/tree/master/Searching/Binary%20Search">Binary Search</a>                                             | O(1) | O(log<sub>2</sub>(N))                | O(log<sub>2</sub>(N)) | O(1)             |
| <a href="https://github.com/sanjay9616/data-structure-and-alogrithms/blob/master/Searching/The%20Ubiquitous%20Binary%20Search/README.md">The Ubiquitous Binary Search</a> | O(1) | O(N)                                 | O(N)                  | O(1)             |
| <a href="https://github.com/sanjay9616/data-structure-and-alogrithms/blob/master/Searching/Ternary%20Search/README.md">Ternary Search</a>                                 | O(1) | O(log<sub>3</sub>(N))                | O(log<sub>3</sub>(N)) | O(1)             |
| <a href="https://github.com/sanjay9616/data-structure-and-alogrithms/blob/master/Searching/Jump%20Search/README.md">Jump Search</a>                                       | O(1) | O(√N)                                | O(√N)                 | O(1)             |
| <a href="https://github.com/sanjay9616/data-structure-and-alogrithms/blob/master/Searching/Interpolation%20Search/README.md">Interpolation Search</a>                     | O(1) | O(log<sub>2</sub>(log<sub>2</sub>N)) | O(N)                  | O(1)             |
| <a href="https://github.com/sanjay9616/data-structure-and-alogrithms/blob/master/Searching/Fibonacci%20Search/README.md">Fibonacci Search</a>                             | O(1) | O(log(N))                            | O(log(N))             | O(1)             |
| <a href="https://github.com/sanjay9616/data-structure-and-alogrithms/blob/master/Searching/Exponential%20Search/README.md">Exponential Search</a>                         | O(1) | O(N)                                 | O(N)                  | O(1)             |
| <a href="https://github.com/sanjay9616/data-structure-and-alogrithms/tree/master/Searching/Linear%20Search">Meta Binary Search</a>                                        | O(1) | O(N)                                 | O(N)                  | O(1)             |

<h2><a href="https://github.com/sanjay9616/data-structure-and-alogrithms/tree/master/Searching/Linear%20Search">Linear Search</a></h2>

Linear Search, also known as Sequential Search, is one of the simplest and most straightforward searching algorithms. It works by sequentially examining each element in a collection of data(array or list) until a match is found or the entire collection has been traversed.

<h2><a href="https://github.com/sanjay9616/data-structure-and-alogrithms/blob/master/Searching/Sentinel%20Linear%20Search/README.md">Sentinel Linear Search</a></h2>

Sentinel Linear Search as the name suggests is a type of Linear Search where the number of comparisons is reduced as compared to a traditional linear search. In a traditional linear search, only N comparisons are made, and in a Sentinel Linear Search, the sentinel value is used to avoid any out-of-bounds comparisons, but there is no additional comparison made specifically for the index of the element being searched.

<h2><a href="https://github.com/sanjay9616/data-structure-and-alogrithms/tree/master/Searching/Binary%20Search">Binary Search</a></h2>

Binary Search is defined as a searching algorithm based on divide and conquer technique used in a sorted array by repeatedly dividing the search interval in half. The idea of binary search is to use the information that the array is sorted and reduce the time complexity to O(log N)

<h2><a href="https://github.com/sanjay9616/data-structure-and-alogrithms/blob/master/Searching/The%20Ubiquitous%20Binary%20Search/README.md">The Ubiquitous Binary Search</a></h2>

<h2><a href="https://github.com/sanjay9616/data-structure-and-alogrithms/blob/master/Searching/Ternary%20Search/README.md">Ternary Search</a></h2>

Ternary Search is defined as a searching algorithm based on divide and conquer technique like Binary Search used in a sorted array that divides the search space into three parts instead of two.

<h2><a href="https://github.com/sanjay9616/data-structure-and-alogrithms/blob/master/Searching/Jump%20Search/README.md">Jump Search</a></h2>

Jump Search is defined as a searching algorithm used in a **sorted array** and the basic idea is to check fewer elements (than linear search) by jumping ahead by fixed steps or skipping some elements in place of searching all elements

<h2><a href="https://github.com/sanjay9616/data-structure-and-alogrithms/blob/master/Searching/Interpolation%20Search/README.md">Interpolation Search</a></h2>

Interpolation Search is defined as is an efficient searching algorithm for **sorted** collections of data, such as arrays or lists. It is an improvement over Binary Search, particularly when the data is uniformly distributed.

Binary Search always goes to the middle element to check. On the other hand, interpolation search may go to different locations according to the value of the key being searched. For example, if the value of the key is closer to the last element, interpolation search is likely to start search toward the end side.

<h2><a href="https://github.com/sanjay9616/data-structure-and-alogrithms/blob/master/Searching/Fibonacci%20Search/README.md">Fibonacci Search</a></h2>

Fibonacci Search is a comparison-based (Divide and Conquer Algorithm) technique that uses Fibonacci numbers to search an element in a **sorted array**.

<h2><a href="https://github.com/sanjay9616/data-structure-and-alogrithms/blob/master/Searching/Exponential%20Search/README.md">Exponential Search</a></h2>

Exponential search allows for searching through a **sorted**, **unbounded** list for a specified input value (the search "key"). The algorithm consists of two stages. The first stage determines a range in which the search key would reside if it were in the list. In the second stage, a binary search is performed on this range.