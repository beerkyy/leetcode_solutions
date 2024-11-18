"""

leetcode - 912 
sort an array
medium


"""


class Solution(object):
    def sortArray(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        #simple merge sort problem 
        def mergeSort(arr):
            #base cond
            if len(arr) <= 1:
                return arr
            
            mid= len(arr)//2
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
        
        sorted_list = mergeSort(nums)
        nums[:] = sorted_list
        return nums


        