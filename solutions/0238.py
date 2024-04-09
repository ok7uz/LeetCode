List = list


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        zero_count = 0
        product = 1

        for num in nums:
            if num == 0:
                zero_count += 1
            else:
                product *= num

        if zero_count > 1:
            return [0] * len(nums)
        
        for i in range(len(nums)):
            if nums[i] == 0:
                nums[i] = product
            else:
                nums[i] = product // nums[i] * (1 - zero_count)
        
        return nums
    

solution = Solution()
print(solution.productExceptSelf([-1, 1, 0, -3, 3, 7, 0]))    
