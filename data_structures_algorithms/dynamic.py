"""Dynamic programming is a method for solving complex problems by breaking them down into simpler subproblems.
Solutions to subproblems are stored in memory and used to quickly find the solution to the full problem.
"""


def fib_recursive(n):
    """Complexity O(2^N)"""
    print(f"fib_recursive({n})")
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib_recursive(n - 1) + fib_recursive(n - 2)


# fib_recursive(3)


def fib_dynamic(n):
    """Complexity O(N)"""
    if n == 0:
        return 0
    previous = 0
    current = 1
    i = 1
    while i < n:
        print(f"fib_dynamic({i})")
        print(f"previous: {previous}, current: {current}")
        next_item = previous + current
        previous = current
        current = next_item
        i += 1
    return current


# fib_dynamic(10)


def longest_common_substring_optimized(str1, str2):
    """Time Complexity O(N * M) space complexity O(N)"""
    # Create one row of the matrix.
    matrix_row = [0] * len(str2)

    # Variables to remember the largest value, and the row it
    # occurred at.
    max_value = 0
    max_value_row = 0
    for row in range(len(str1)):
        # Variable to hold the upper-left value from the
        # current matrix position.
        up_left = 0
        for col in range(len(str2)):
            # Save the current cell's value; this will be up_left
            # for the next iteration.
            saved_current = matrix_row[col]

            # Check if the characters match
            if str1[row] == str2[col]:
                matrix_row[col] = 1 + up_left

                # Update the saved maximum value and row,
                # if appropriate.
                if matrix_row[col] > max_value:
                    max_value = matrix_row[col]
                    max_value_row = row
            else:
                matrix_row[col] = 0

            # Update the up_left variable
            up_left = saved_current

    # The longest common substring is the substring
    # in str1 from index max_value_row - max_value + 1,
    # up to and including max_value_row.
    start_index = max_value_row - max_value + 1
    return str1[start_index : max_value_row + 1]


# print(longest_common_substring_optimized("dd apple pie available", "apple pies"))


def longest_substring_finder(string1, string2):
    """Complexity O(N^2)"""
    answer = ""
    len1, len2 = len(string1), len(string2)
    for i in range(len1):
        for j in range(len2):
            lcs_temp = 0
            match = ""
            while (i + lcs_temp < len1) and (j + lcs_temp < len2) and string1[i + lcs_temp] == string2[j + lcs_temp]:
                match += string2[j + lcs_temp]
                lcs_temp += 1
            if len(match) > len(answer):
                answer = match
    return answer


# print(longest_substring_finder("dd apple pie available", "apple pies"))
# print(
#     longest_substring_finder(
#         "cov_basic_as_cov_x_gt_y_rna_genes_w1000000", "cov_rna15pcs_as_cov_x_gt_y_rna_genes_w1000000"
#     )
# )
# print(longest_substring_finder("apples", "apples"))


class LCSMatrix:
    def __init__(self, str1, str2):
        self.row_count = len(str1)
        self.column_count = len(str2)
        self.row_string = str1
        self.column_string = str2
        self.matrix = self._create_matrix()

    # Returns the number of columns in the matrix, which also equals the length
    # of the second string passed to the constructor.
    def get_column_count(self):
        return self.column_count

    def _create_matrix(self):
        matrix = [[[0, {}]] * self.column_count for _ in range(self.row_count)]
        for row in range(self.row_count):
            for col in range(self.column_count):
                if self.row_string[row] == self.column_string[col]:
                    up_left = matrix[row - 1][col - 1][0] if row > 0 and col > 0 else 0
                    # Extend LCS from top-left diagonal
                    lcs_set = set()
                    if row > 0 and col > 0 and matrix[row - 1][col - 1][1]:
                        for element in matrix[row - 1][col - 1][1]:
                            lcs_set.add(element + self.row_string[row])
                    else:
                        lcs_set.add(self.row_string[row])
                    matrix[row][col] = [1 + up_left, lcs_set]

                else:
                    # Take the longer LCS from left or up
                    left_length, left_set = matrix[row][col - 1] if col > 0 else (0, set())
                    up_length, up_set = matrix[row - 1][col] if row > 0 else (0, set())

                    if left_length > up_length:
                        matrix[row][col] = [left_length, left_set]
                    elif up_length > left_length:
                        matrix[row][col] = [up_length, up_set]
                    else:
                        matrix[row][col] = [left_length, left_set | up_set]
        return matrix

    # Returns the matrix entry at the specified row and column indices, or 0 if
    # either index is out of bounds.
    def get_entry(self, row_index, column_index):
        if 0 <= row_index <= self.row_count and 0 <= column_index <= self.column_count:
            try:
                return self.matrix[row_index][column_index][0]
            except Exception:
                pass
        return 0

    # Returns the number of rows in the matrix, which also equals the length
    # of the first string passed to the constructor.
    def get_row_count(self):
        return self.row_count

    # Returns the set of distinct, longest common subsequences between the two
    # strings that were passed to the constructor.
    def get_longest_common_subsequences(self):
        max_length = 0
        longest_subsequences = set()
        for row in range(self.row_count):
            for col in range(self.column_count):
                cell_length = self.matrix[row][col][0]
                if cell_length > max_length:
                    max_length = cell_length
                    longest_subsequences = self.matrix[row][col][1]
                elif cell_length == max_length:
                    longest_subsequences |= self.matrix[row][col][1]

        return longest_subsequences


matrix_instance = LCSMatrix("DATA STRUCTURES", "ALGORITHMS")
print(matrix_instance.get_longest_common_subsequences())
