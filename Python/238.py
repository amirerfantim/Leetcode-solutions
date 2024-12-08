from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        all_products = 1
        products = []
        for num in nums:
            all_products *= num

        for i in range(len(nums)):
            if nums[i] == 0:
                product = 1
                for j in range(len(nums)):
                    if j != i:
                        product *= nums[j]
                products.append(product)
            else:
                products.append(all_products // nums[i])
        return products
