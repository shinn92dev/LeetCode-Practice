"""
Add Docstring
"""
from timer import timer


@timer
def two_sum_using_nested_loop(nums: list[int], target: int) -> list[int]:
    result = []
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] + nums[j] == target:
                result.append(i)
                result.append(j)
    return result


def main():
    test_case1 = ([2, 7, 11, 15], 9)
    test_case2 = ([3, 2, 4], 6)
    test_case3 = ([3, 3], 6)
    print(two_sum_using_nested_loop(test_case1[0], test_case1[1]))
    print(two_sum_using_nested_loop(test_case2[0], test_case2[1]))
    print(two_sum_using_nested_loop(test_case3[0], test_case3[1]))


if __name__ == "__main__":
    main()
