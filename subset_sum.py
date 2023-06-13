def find_zero_sum_subsets(nums):
    nums.sort()  # Sort the numbers in ascending order
    subsets = []
    backtrack([], nums, 0, subsets)
    return subsets


def backtrack(subset, nums, start, subsets):
    if len(subset) == 5:  # Base case: subset size is 5
        if sum(subset) == 0:
            subsets.append(subset[:])  # Add the subset to the result
        return

    for i in range(start, len(nums)):
        if i > start and nums[i] == nums[i - 1]:
            continue  # Skip duplicates to avoid duplicates in subsets
        subset.append(nums[i])
        backtrack(subset, nums, i + 1, subsets)  # Recurse with the remaining set
        subset.pop()  # Backtrack: remove the current number


# Example usage
nums = [-12, -3, -6, 7, 2, -2, 6, 3, 9, -7, -5, -8, 1, 11, -9, -4]
zero_sum_subsets = find_zero_sum_subsets(nums)
for subset in zero_sum_subsets:
    print(subset)
