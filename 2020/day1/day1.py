#!/usr/bin/env python3

# Given a list of numbers, find 2 that add up to the target number
def part1(nums, targetNumber):
    for a in range(len(nums)):
        first = nums[a]
        for b in range(1, len(nums)):
            second = nums[b]
            if first + second == targetNumber:
                return (first, second)


# An alternate method for completing part 1
def alternatePart1(nums, targetNumber):
    # Iterate through list of numbers
    for first in nums:
        # Second loop to multiply each first number by every other number in the list
        # This could be made more efficient by avoiding duplicate comparisons
        for second in nums:
            if first + second == targetNumber:
                print("First: {} Second: {}".format(first, second))
                print("{} + {} = {}".format(first, second, (first + second)))
                print("{} x {} = {}".format(first, second, (first * second)))
                return


# Given a list of numbers, find 3 that add up to the target number
def part2(nums, targetNumber):
    for a in range(len(nums)):
        first = nums[a]
        for b in range(1, len(nums)):
            second = nums[b]
            for c in range(2, len(nums)):
                third = nums[c]
                if first + second + third == targetNumber:
                    return (first, second, third)


# Create a list to hold all of the numbers from the file
nums = []
with open("input", "r") as fh:
    for line in fh:
        # Cast each line to an integer
        nums.append(int(line))

targetNumber = 2020
print("Part 1")
(a, b) = part1(nums, targetNumber)
print("{} + {} = {}".format(a, b, (a + b)))
# Compute product of the two returned numbers to solve part 1
print("{} x {} = {}".format(a, b, (a * b)))
# Add a blank line in between part 1 and part 2 output
print()

print("Part 2")
(a, b, c) = part2(nums, targetNumber)
print("{} + {} + {} = {}".format(a, b, c, (a + b + c)))
# Compute product of the three returned numbers to solve part 2
print("{} x {} x {} = {}".format(a, b, c, (a * b * c)))
