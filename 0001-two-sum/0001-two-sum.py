class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        visto = {}
        for i in range(len(nums)):
            diff = target - nums[i]
            if diff in visto:
                return [visto[diff], i]
            else:
                visto[nums[i]] = i