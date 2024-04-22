### Use this space to try out ideas and free code ### 
class Solution(object):
    '''
    Finding two numbers in array that sum of them match with the target.
    Solution with time and space complexity O(n)
    '''
    def twoSum(self, numberArray, target):
        scanNumberMap = {}
        for i, number in enumerate(numberArray):
            findingValue = target - number
            if findingValue in scanNumberMap:
                return [scanNumberMap[findingValue], i]
            scanNumberMap[number] = i
            return []
