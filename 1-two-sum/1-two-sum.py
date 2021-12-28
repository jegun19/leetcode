class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for num in nums:
            # if num > target:
                # pass
            # else:
                # loop through the remaining elements
                first_id = nums.index(num)
                for match in nums[first_id+1:]:
                    if num + match == target:
                        second_id = nums[first_id+1:].index(match)
                        ans = list()
                        ans.append(first_id)
                        ans.append(first_id + 1 + second_id)
                        return ans