class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dct = {}

        for i, num in enumerate(nums):
            complementary = target - num

            if complementary in dct:
                return [dct[complementary], i]
            dct[num] = i