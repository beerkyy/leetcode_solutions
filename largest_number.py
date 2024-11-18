"""

Given a list of non-negative integers nums, arrange them such that they form the largest number and return it.

Since the result may be very large, so you need to return a string instead of an integer.

"""
class Solution(object):
    def largestNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: str
        """
    #merge sort 
    #combine them into one output string
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
                if compare(left_hand[i], right_hand[j]):
                    result.append(left_hand[i])
                    i += 1
                else:
                    result.append(right_hand[j])
                    j += 1
            result.extend(left_hand[i:])
            result.extend(right_hand[j:])
            return result
        
        #compare if [1] [2]  [1,2] [3,4] 1234 < 4321  
        def compare(a, b):
            return str(a) +  str(b) > str(b) + str(a)
        
        #our list is sorted if we
        sorted_list = mergeSort(nums)
        result = "".join([str(nums) for nums in sorted_list])
        
        return "0" if result[0] == "0" else result
