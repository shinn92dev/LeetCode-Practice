"""
Add Docstring
"""
from timer import timer


@timer
def two_sum_using_in(nums: list[int], target: int) -> list[int]:
    for idx, num in enumerate(nums):
        target_element = target - num
        if target_element in nums[idx+1:]:
            return [idx, nums[idx+1:].index(target_element) + idx + 1]


def main():
    test_case1 = ([2, 7, 11, 15], 9)
    test_case2 = ([3, 2, 4], 6)
    test_case3 = ([3, 3], 6)
    print(two_sum_using_in(test_case1[0], test_case1[1]))
    print(two_sum_using_in(test_case2[0], test_case2[1]))
    print(two_sum_using_in(test_case3[0], test_case3[1]))


if __name__ == "__main__":
    main()