"""
-> Merge Two 2D Arrays by Summing Values 

You are given two 2D integer arrays nums1 and nums2.

• nums1[i] = [idi, vali] indicate that the number with the id idi has a value equal to vali.
• nums2[i] = [idi, vali] indicate that the number with the id idi has a value equal to vali.

Each array contains unique ids and is sorted in ascending order by id.

Merge the two arrays into one array that is sorted in ascending order by id, respecting the following conditions:

• Only ids that appear in at least one of the two arrays should be included in the resulting array.
• Each id should be included only once and its value should be the sum of the values of this id in the two arrays.
If the id does not exist in one of the two arrays, then assume its value in that array to be 0.

Return the resulting array. The returned array must be sorted in ascending order by id.

"""

class Solution:
    def mergeArrays(self, nums1: list[list[int]], nums2: list[list[int]]) -> list[list[int]]:
        i, j = 0, 0
        res = []

        while i < len(nums1) and j < len(nums2):
            if nums1[i][0] < nums2[j][0]:
                res.append(nums1[i])
                i += 1
            elif nums1[i][0] > nums2[j][0]:
                res.append(nums2[j])
                j += 1
            else:
                res.append([nums1[i][0], nums1[i][1] + nums2[j][1]])
                i, j, = i+1, j+1
        while i < len(nums1):
            res.append(nums1[i])
            i += 1
        while j < len(nums2):
            res.append(nums2[j])
            j += 1
        return res

obj = Solution()
nums1 = [[1,2],[2,3],[4,5]]
nums2 = [[1,4],[3,2],[4,1]]

print(obj.mergeArrays(nums1, nums2))