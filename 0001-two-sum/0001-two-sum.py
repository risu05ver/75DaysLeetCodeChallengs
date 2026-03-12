class Solution:
    def twoSum(self,arr,target):
        for i in range(len(arr)):
            for j in range(len(arr)):
                if i!=j:
                    if target==(arr[i]+arr[j]):
                         return[i,j]



