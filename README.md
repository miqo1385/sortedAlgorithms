# sortedAlgorithms

Analysis:

1- Analyze the time complexity of your implementation by explaining how the nested loops contribute to the O(n^2) complexity.

The outer loop runs n times (where n is the number of elements in the array).
The inner loop runs, on average, n/2 times for each iteration of the outer loop (since it starts from i + 1 and goes up to n).
Therefore, the overall time complexity is O(n * n/2), which simplifies to O(n^2) in big O notation. The selection sort algorithm has a quadratic time complexity, 
making it inefficient for large datasets.

2- Discuss the space complexity of your algorithm and explain why it is considered an in-place sorting algorithm.

An in-place sorting algorithm is one that doesn't require additional memory proportional to the size of the input. Instead, it performs the sorting using a constant amount of extra space.
In the case of selection sort, the only additional space used is for a few variables (min_index, temp, etc.), and the space required for these variables is constant and doesn't depend on the size of the input array.


3- Reflect on the stability of Selection Sort and provide an example or reasoning why it may or may not reorder equal elements.

Selection Sort is not a stable sorting algorithm. Stability in sorting algorithms refers to the property that equal 
elements in the input array will maintain their relative order in the sorted output. In other words, 
if two elements are equal in the input, and one comes before the other, a stable sorting algorithm ensures that the one 
that comes first will still appear first in the sorted result.

Report:
the code implementation wasn't hard thanks to the big amount of documentation about this 
algorithm. the book shelf example in the lecture was very helpful. it helped me to visualized 
this algorithm very well, the lighter books on the top and the heavy ones on the bottom.

all the test ran very fast because this algorithm is perfect for small data. obviously the 
one that have the biggest number in the beginning an the smallest one in the end took the longest
because it had to swap basically all the elements in the array

this algorithm has a nested loop so the time complexity 0(n^2) will be the one.