"""
-> Pascal's Triangle || 

Given an integer rowIndex, return the rowIndexth (0-indexed) row of the Pascal's triangle.
In Pascal's Triangle, each number is the sum of two numbers directly above it as shown.

                1
               1 1
              1 2 1
             1 3 3 1
            1 4 6 4 1

"""

class Solution:
    def PascalTriangle(self, rowIndex: int) -> list[int]:
        # Initialize the first row of Pascal's triangle 
        res = [1]

        # Generate each row of Pascal's triangle up to the given rowIndex
        for i in range(rowIndex):
            # Create a new row with one more element than the previous row 
            next_row = [0] * (len(res) + 1)

            # calculate the values for the next row based on the previous row
            for j in range(len(res)):
                next_row[j] += res[j]
                next_row[j + 1] += res[j]
            res = next_row  # Update res to the newly calculated row

        return res  # Return the row at the specified index
    
