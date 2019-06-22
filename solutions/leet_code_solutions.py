from typing import List


def two_sum(nums: List[int], target: int) -> List[int]:
    """
    Given an array of integers, return indices of the two numbers such that they add up to a specific target.
    :param nums: list of numbers
    :param target: pre-specified number
    >>> two_sum(nums = [2,7,11,15], target = 9)
    [0, 1]
    """
    dictionary = dict()
    pos = 0
    while pos < len(nums):
        if (target - nums[pos]) not in dictionary:
            dictionary[nums[pos]] = pos
            pos += 1
        else:
            return [dictionary[target - nums[pos]], pos]


def find_disappeared_numbers(nums: List[int]) -> object:
    """
    Given an array of integers where 1 ≤ a[i] ≤ n (n = size of array), some elements appear twice and others appear once.
    Find all the elements of [1, n] inclusive that do not appear in this array.
    Do it without extra space and in O(n) runtime. You may assume the returned list does not count as extra space.
    :param nums: list of integers
    :return: inclusive numbers that not appeared in list
    >>> find_disappeared_numbers(nums = [4,3,2,7,8,2,3,1])
    [6, 5]
    """
    result = []
    if nums:
        my_max = len(nums)
        my_dict = dict.fromkeys(nums)
        for i in range(0, my_max):
            x = my_max - i
            if x not in my_dict:
                result.append(x)
    return result


def num_jewels_in_stones(j: str, s: str) -> int:
    """
    You're given strings J representing the types of stones that are jewels, and S representing the stones you have.
    Each character in S is a type of stone you have.
    You want to know how many of the stones you have are also jewels.The letters in J are guaranteed distinct,
    and all characters in J and S are letters. Letters are case sensitive,
    so "a" is considered a different type of stone from "A".
    :param j: stones that marked as jewels
    :param s: input stones
    :return: amount of jewel stones
    >>> num_jewels_in_stones(j = "aA", s = "aAAbbbb")
    3
    """
    my_dict = dict.fromkeys(j, 0)
    for i in s:
        if i in my_dict:
            my_dict[i] += 1
    return sum(my_dict.values())


def sorted_squares(a: List[int]) -> List[int]:
    """
    Given an array of integers A sorted in non-decreasing order, return an array of
    the squares of each number, also in sorted non-decreasing order.
    :param a: list of numbers
    :return: sorted list of squares
    >>> sorted_squares(a = [-5, -1, 0, 2, 3])
    [0, 1, 4, 9, 25]
    """

    return sorted(map(lambda x: x ** 2, a))


def to_lower_case(string: str) -> str:
    """
    Implement function ToLowerCase() that has a string parameter str, and returns the same string in lowercase.
    P.S. combination of map and reduce functions is fast
    :param string: Input string
    :return: same string in lowercase

    >>> to_lower_case(string = "AaBbCc")
    'aabbcc'
    """
    from functools import reduce
    return reduce(lambda x, y: x + y, map(lambda x: x.lower(), string))


def last_stone_weight(stones: List[int]) -> int:
    """
    We have a collection of rocks, each rock has a positive integer weight.

    Each turn, we choose the two heaviest rocks and smash them together.  Suppose the stones have weights x and y
    with x <= y.  The result of this smash is:
    If x == y, both stones are totally destroyed;
    If x != y, the stone of weight x is totally destroyed, and the stone of weight y has new weight y-x.
    At the end, there is at most 1 stone left.  Return the weight of this stone (or 0 if there are no stones left.)
    :param stones: numbers representing different weight of the stones
    :return: weight of last stone left
    >>> last_stone_weight(stones =[2,7,4,1,8,1])
    1
    """
    x = stones.pop(stones.index(max(stones)))
    while len(stones) > 0:
        y = stones.pop(stones.index(max(stones)))
        stones.append(abs(x - y))
        x = stones.pop(stones.index(max(stones)))
    return x


if __name__ == '__main__':
    import doctest

    doctest.testmod()
