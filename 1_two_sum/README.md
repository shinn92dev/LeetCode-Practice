# [Two Sum](https://leetcode.com/problems/two-sum/description/)
`Easy` `Array` `Hash Table`


Given an array of integers `nums` and an integer `target`, return indices of the two numbers such that 
they add up to `target`.

You may assume that each input would have **exactly one solution**, 
and you may not use the same element twice.

You can return the answer in any order.

**Example 1:**

> Input: nums = [2,7,11,15], target = 9 
> 
> Output: [0,1]
> 
> Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].

**Example 2:**

> Input: nums = [3,2,4], target = 6
> 
> Output: [1,2]

**Example 3:**

> Input: nums = [3,3], target = 6
> 
> Output: [0,1]

## Solution 1 (`solution_using_nested_loop.py`)
- This solution passed all the tests in LeetCode
- However, it showed very slow running time compared to others
- Need to think about another solution with a better performance

[![001-two-sum-solution1-result.png](https://i.postimg.cc/PJzkxg2p/001-two-sum-solution1-result.png)](https://postimg.cc/XBJP1zM4)

## Solution 2 (`solution_using_in_operator.py`
- Using `in` operator, I solved the problem with just one for loop which led significant improvement compared to the solution 1
- I think using `dictionary` may boost the runtime, and will try that!

[![001-two-sum-solution-2.png](https://i.postimg.cc/5ywDbj2r/001-two-sum-solution-2.png)](https://postimg.cc/fSR8vzX7)