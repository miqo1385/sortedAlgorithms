import unittest


def selectionSort(array):
    size = len(array)

    for ind in range(size):
        min_index = ind

        for j in range(ind + 1, size):
            # select the minimum element in every iteration
            if array[j] < array[min_index]:
                min_index = j
        # swapping the elements to sort the array
        (array[ind], array[min_index]) = (array[min_index], array[ind])
    return array


class our_function_test(unittest.TestCase):
    """A randomly generated array of integers."""
    def test_01(self):
        arr = [0, -1, 3, 2, 1]
        sort = selectionSort(arr)
        self.assertEqual(sort, [-1, 0, 1, 2, 3])

    """An array already sorted in ascending order."""
    def test_02(self):
        arr = [1, 2, 3, 4]
        sort = selectionSort(arr)
        self.assertEqual(sort, [1, 2, 3, 4])

    """An array sorted in descending order."""
    def test_03(self):
        arr = [4, 3, 2, 1, -1]
        sort = selectionSort(arr)
        self.assertEqual(sort, [-1, 1, 2, 3, 4])

    """An array with all elements being the same."""
    def test_04(self):
        arr = [1,1,1,1,1,1]
        sort = selectionSort(arr)
        self.assertEqual(sort, [1,1,1,1,1,1])
    """An empty array"""
    def test_05(self):
        arr = []
        sort = selectionSort(arr)
        self.assertEqual(sort, [])

    """ an array with one element (edge cases)."""
    def test_06(self):
        arr = [1]
        sort = selectionSort(arr)
        self.assertEqual(sort, [1])


if __name__ == "__main__":
    unittest.main()
