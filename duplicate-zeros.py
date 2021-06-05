"""
Problem statements

Given a fixed length array arr of integers, duplicate each occurrence of zero, shifting the remaining elements to the right.
Note that elements beyond the length of the original array are not written.
Do the above modifications to the input array in place, do not return anything from your function.
"""

class DuplicateZeros(object):
    def duplicateZeros(self, arr):
        """
        :type arr: List[int]
        :rtype: None Do not return anything, modify arr in-place instead.
        """
        tempArr = []
        arrLength = len(arr)
        print("input array: {}".format(arr))
        
        for i, item in enumerate(arr): # [1,0,2,3,0,4,5,0]
            if len(tempArr) < arrLength:
                if item != 0:
                    tempArr.append(item)
                else:
                    tempArr.append(item)
                    tempArr.append(0)
            else:
                arr = tempArr
                print("modified array: {}".format(arr))
                break
