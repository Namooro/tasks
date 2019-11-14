from typing import List


def two_sum(nums: List[int], target: int) -> List[int]:
    """
    Given an array of integers, return indices of the two numbers such that they add up to a specific target.
    :param nums: list of numbers
    :param target: pre-specified number
    >>> two_sum(nums = [2, 7, 11, 15], target = 9)
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


def ballot(names: List[str]):
    """
    There is a list of all votes for specific candidates in election.
    Our task is to find who is the winner based on maximum votes.
    In the case when the more than one person has a max amount of votes, a person,
    whose name is later in alphabet becomes the president.
    :param names: list of votes for specific challenger
    :return: name of the elected candidate
    >>> ballot(names = ["Ash", "Zoe", "Ash"])
    'Ash'
    >>> ballot(names = ["Aaron", "Bob", "Bob", "Aaron", "Zoe"])
    'Bob'
    """
    from collections import Counter
    if names:
        ballot_dict = Counter(names)
        winners = sorted([key for key in ballot_dict.keys() if ballot_dict[key] == max(ballot_dict.values())],
                         reverse=True)
        return winners[0]
    else:
        return ""


def find_disappeared_numbers(nums: List[int]) -> List[int]:
    """
    Given an array of integers where 1 ≤ a[i] ≤ n (n = size of array), some elements appear twice and others appear once.
    Find all the elements of [1, n] inclusive that do not appear in this array.
    Do it without extra space and in O(n) runtime. You may assume the returned list does not count as extra space.
    :param nums: list of integers
    :return: inclusive numbers that not appeared in list
    >>> find_disappeared_numbers(nums = [4, 3, 2, 7, 8, 2, 3, 1])
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
    from collections import Counter
    my_dict = Counter(s)
    return sum([my_dict.get(i) for i in my_dict.keys() if i in j])


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


def single_number(nums: List[int]) -> List[int]:
    """
    Given an array of numbers nums, in which exactly two elements appear only once
     and all the other elements appear exactly twice. Find the two elements that appear only once.
    :param nums: list of numbers
    :return: list of elements that appeared only once
    >>> sorted(single_number([1, 2, 1, 3, 2, 5]))
    [3, 5]
     """
    hash_table = {}
    for i in nums:
        try:
            hash_table.pop(i)
        except KeyError:
            hash_table[i] = 1
    return list(hash_table.keys())


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
    >>> last_stone_weight(stones = [2, 7, 4, 1, 8, 1])
    1
    """
    x = stones.pop(stones.index(max(stones)))
    while len(stones) > 0:
        y = stones.pop(stones.index(max(stones)))
        stones.append(abs(x - y))
        x = stones.pop(stones.index(max(stones)))
    return x


def min_steps(n: int) -> int:
    """
    Initially on a notepad only one character 'A' is present.
    You can perform two operations on this notepad for each step:
    Copy All: You can copy all the characters present on the notepad (partial copy is not allowed).
    Paste: You can paste the characters which are copied last time.
    Given a number n. You have to get exactly n 'A' on the notepad by performing the minimum number of steps permitted.
    Output the minimum number of steps to get n 'A'.
    :param n: length of line that contains 'A'
    :return: minimum number of steps that we need to achieve desirable length
    Solution: we just should find biggest divisor of N
    >>> min_steps(14)
    9
    >>> min_steps(3)
    3
    """
    if n == 1:
        return 0
    solution = n // 2
    for x in range(solution, 2, -1):
        if n % x == 0:
            return int(n // x) + min_steps(x)
    return n


def climb_stairs(n: int) -> int:
    """
    You are climbing a stair case. It takes n steps to reach to the top.
    Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?
    :param n: number of steps in stair case
    It's just the finding the fibonacci number
    >>> climb_stairs(2)
    2
    >>> climb_stairs(5)
    8
    """
    if n == 1:
        return 1
    first = 1
    second = 2
    for i in range(2, n):
        first, second = second, first + second
    return second


def first_missing_positive(nums: List[int]) -> int:
    """Given an unsorted integer array, find the smallest missing positive integer.
            algorithm should run in O(n) time and uses constant extra space.
    >>> first_missing_positive([])
    1
    >>> first_missing_positive([1, 1000])
    2
    >>> first_missing_positive([3, 4, -1, 1])
    2
    >>> first_missing_positive([7, 8, 9, 11, 12])
    1
    """

    if len(nums) > 0:
        nums = set([x for x in nums if x > 0])
        for i in range(1, max(nums) + 1):
            if i not in nums:
                return i
    else:
        return 1


if __name__ == '__main__':
    import doctest

    doctest.testmod()
