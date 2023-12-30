'''
1. Two Sum
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.
정수 배열 nums 과 정수가 주어지면 두 숫자의 합이 가 되는 인덱스를target 반환합니다 .target

각 입력에는 정확히 하나의 솔루션이 있다고 가정할 수 있으며 동일한 요소를 두 번 사용할 수 없습니다 .

어떤 순서로든 답변을 반환할 수 있습니다.

Example 1:

Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
Example 2:

Input: nums = [3,2,4], target = 6
Output: [1,2]
Example 3:

Input: nums = [3,3], target = 6
Output: [0,1]

접근방안
-인덱스 0부터 시작, 해당 인덱스 값이 target보다 크면 패스
-해당 인덱스 값이 target보다 작으면 해당 값의 인덱스를 ouput 에 저장
- target-해당인덱스 값을 추출해서 나머지 리스트에서 동일한 값이 있는지 검색
>> 구현 실패

-다중 루프로 무식하게..합산하면서 찾는 전략
- 마이너스가 입력값의 범위이므로, 절대값으로 계산하는 방안을 생각못햇다.

'''


class Solution:
    def twoSum(self,nums, target):
        result = []

        for i in range(len(nums)) : 
            #if abs(nums[i]) <= abs(target) :
            #    print(nums[i], abs(nums[i]))
            for j in range(i+1, len(nums)): 
                print(nums[i], nums[j])
                if abs(nums[i] + nums[j]) == abs(target) :
                    result = [i,j]
                    return result  
           

        return result
    
    #인상적 답안 중 하나
    def twoSum2(self, nums, target):
        for i in reversed(range(len(nums))):
            for j in range(i):
                print(i, j)

    # 찾앗다. 맨 처음 생각햇던 논리 구조
    # enumerate 를 몰랏다.
    # enumerate 함수는 넘겨진 파리미터를(리슽, 튜플 등) 인덱스와 값을 포함해서 리턴한다.
    def twoSum3(self, nums, target):
        for i, num in enumerate(nums):
            x = target - num
            nums[i] = None
            try:
                index = nums.index(x)
                return [i, index]

            except:
                continue
    


a = Solution()
#nums = [2,7,11,15]
#target = 9
#nums = [0,4,3,0]
#target = 0 
#nums = [-1,-2,-3,-4,-5]
#target = -8

#nums = [-3,4,3,90]
#target = 0 
nums = [0,3,-3,4,-1]
target = -1

#print(a.twoSum(nums, target))
#a.twoSum2(nums, target) 
print(a.twoSum3(nums, target) )