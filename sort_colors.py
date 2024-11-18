#sort colors leetcode - 75
#medium 
#solved by using merge sort
#O(nlogn) time complexity
class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        def mergeSort(arr):

            if len(arr) <= 1:
                return arr
            
            mid = len(arr) // 2

            left_hand = mergeSort(arr[:mid])
            right_hand = mergeSort(arr[mid:])

            return merge(left_hand, right_hand)
        
        def merge(left_hand, right_hand):

            result = []
            i = j = 0

            while i < len(left_hand) and j < len(right_hand):
                if left_hand[i] < right_hand[j]:
                    result.append(left_hand[i])
                    i += 1
                else:
                    result.append(right_hand[j])
                    j += 1
            
            result.extend(left_hand[i:])
            result.extend(right_hand[j:])
            return result
        
        merge_sorted = mergeSort(nums)
        nums[:] = merge_sorted
        return nums

        
