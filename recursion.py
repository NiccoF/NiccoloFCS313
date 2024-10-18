"""
Student information for this assignment:

Replace <FULL NAME> with your name.
On my honor, Niccolo Faelnar, this
programming assignment is my own work and I have not provided this code to
any other student.

I have read and understand the course syllabus's guidelines regarding Academic
Integrity. I understand that if I violate the Academic Integrity policy (e.g.
copy code from someone else, have the code generated by an LLM, or give my
code to someone else), the case shall be submitted to the Office of the Dean of
Students. Academic penalties up to and including an F in the course are likely.

UT EID 1: nvf89
"""


def group_sum(start, nums, target):
    """
    Given a list of ints, determine if there exists a group of some ints that sum to the
    given target.

    pre: start >= 0, len(nums) >= 0, target >= 0, nums will only contain ints
    post: return True if nums has a group of ints that sum to target, False otherwise
    """
    if start >= len(nums):
        return target == 0
    if group_sum(start + 1, nums, target - nums[start]):
        return True
    return group_sum(start + 1, nums, target)


def group_sum_6(start, nums, target):
    """
    Given a list of ints, determine if there exists a group of some ints that sum to the
    given target. Additionally, if there is are 6's present in the array, they must all
    be chosen.

    pre: start >= 0, len(nums) >= 0, target >= 0, nums will only contain ints
    post: return True if nums has a group of ints that sum to target, False otherwise
    """
    if start >= len(nums):
        return target == 0
    if nums[start] == 6:
        return group_sum_6(start + 1, nums, target - nums[start])
    if group_sum_6(start + 1, nums, target - nums[start]):
        return True
    return group_sum_6(start + 1, nums, target)


def group_no_adj(start, nums, target):
    """
    Given a list of ints, determine if there exists a group of some ints that sum to
    the given target. Additionally, if a value is chosen, the value immediately after
    (the value adjacent) cannot be chosen.

    pre: start >= 0, len(nums) >= 0, target >= 0, nums will only contain ints
    post: return True if nums has a group of ints that sum to target, False otherwise
    """
    if start >= len(nums):
        return target == 0
    if group_no_adj(start + 2, nums, target - nums[start]):
        return True
    return group_no_adj(start + 1, nums, target)


def group_sum_5(start, nums, target):
    """
    Given a list of ints, determine if there exists a group of some ints that sum to
    the given target. Additionally, if a multiple of 5 is in the array, it must be included
    If the value immediately following a multiple of 5 if 1, it must not be chosen

    pre: start >= 0, len(nums) >= 0, target >= 0, nums will only contain ints
    post: return True if nums has a group of ints that sum to target, False otherwise
    """
    if start >= len(nums):
        return target == 0
    if nums[start] % 5 == 0:
        if nums[start + 1] == 1:
            return group_sum_5(start + 2, nums, target - nums[start])
        else:
            return group_sum_5(start + 1, nums, target - nums[start])
    if group_sum_5(start + 1, nums, target - nums[start]):
        return True
    return group_sum_5(start + 1, nums, target)


def group_sum_clump(start, nums, target):
    """
    Given a list of ints, determine if there exists a group of some ints that sum to
    the given target. Additionally, if there is a group of identical numbers in succession,
    they must all be chosen, or none of them must be chosen.
    EX: [1, 2, 2, 2, 5, 2], all three of the middle 2's must be chosen, or none of them must be
    chosen to be included in the sum. One loop is allowed to check for identical numbers.

    pre: start >= 0, len(nums) >= 0, target >= 0, nums will only contain ints
    post: return True if nums has a group of ints that sum to target, False otherwise
    """
    if start >= len(nums):
        return target == 0
    num_repeats = 0
    for i in range(start, len(nums)):
        if nums[i] == nums[start]:
            num_repeats += 1
    if num_repeats > 1:
        if group_sum_clump(start + num_repeats, nums, target - nums[start] * num_repeats):
            return True
        return group_sum_clump(start + num_repeats, nums, target)
    if group_sum_clump(start + 1, nums, target - nums[start]):
        return True
    return group_sum_clump(start + 1, nums, target)


def split_array(nums):
    """
    Given a list of ints, determine if the numbers can be split evenly into two groups
    The sum of these two groups must be equal
    Write a recursive helper to call from this function
    Are these not already helper functions with the kickoff being the test cases?

    pre: len(nums) >= 0, nums will only contain ints
    post: return True if nums can be split, False otherwise
    """
    left_list = []
    right_list = []
    index = 0
    return split_array_helper(nums, index, left_list, right_list)

def split_array_helper(nums, index, left_list, right_list):
    """
    Recursive Helper for split_array
    """
    if index >= len(nums):
        return sum(left_list) == sum(right_list)
    left_list.append(nums[index])
    if split_array_helper(nums, index + 1, left_list, right_list):
        return True
    left_list.pop()
    right_list.append(nums[index])
    if split_array_helper(nums, index + 1, left_list, right_list):
        return True
    right_list.pop()
    return False


def split_odd_10(nums):
    """
    Given a list of ints, determine if the numbers can be split evenly into two groups
    The sum of one group must be odd, while the other group must be a multiple of 10
    Write a recursive helper to call from this function

    pre: len(nums) >= 0, nums will only contain ints
    post: return True if nums can be split, False otherwise
    """
    left_list = []
    right_list = []
    index = 0
    return split_odd10_helper(nums, index, left_list, right_list)

def split_odd10_helper(nums, index, left_list, right_list):
    """
    Recursive Helper for split_odd10
    """
    if index >= len(nums):
        if(sum(left_list) % 10 == 0 or sum(right_list) % 10 == 0):
            if(sum(left_list) % 2 != 0 or sum(left_list) % 2 != 0):
                return True
        return False
    left_list.append(nums[index])
    if split_odd10_helper(nums, index + 1, left_list, right_list):
        return True
    left_list.pop()
    right_list.append(nums[index])
    if split_odd10_helper(nums, index + 1, left_list, right_list):
        return True
    right_list.pop()
    return False


def split_53(nums):
    """
    Given a list of ints, determine if the numbers can be split evenly into two groups
    The sum of these two groups must be equal
    Additionally, all multiples of 5 must be in one group, and all multiples of 3 (and not 5)
    must be in the other group
    Write a recursive helper to call from this function

    pre: len(nums) >= 0, nums will only contain ints
    post: return True if nums can be split, False otherwise
    """
    three_list = []
    five_list = []
    index = 0
    return split_53_helper(nums, index, three_list, five_list)

def split_53_helper(nums, index, three_list, five_list):
    """
    Recursive Helper for split_53
    """
    if len(nums) == 0:
        return False
    if index >= len(nums):
        return sum(three_list) == sum(five_list)
    if nums[index] % 5 != 0:
        three_list.append(nums[index])
        if split_53_helper(nums, index + 1, three_list, five_list):
            return True
        three_list.pop()
    if nums[index] % 3 != 0:
        five_list.append(nums[index])
        if split_53_helper(nums, index + 1, three_list, five_list):
            return True
        five_list.pop()
    return False