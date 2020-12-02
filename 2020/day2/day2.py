#!/usr/bin/env python3


def part1(line):
    # Split line, using spaces as delimiters.
    items = line.split()
    policy = items[0]
    # Split the policy portion into min and max values, using a dash as the delimiter.
    policy_items = policy.split("-")
    policy_min = int(policy_items[0])
    policy_max = int(policy_items[1])
    # Character is the second component of the line, but has a trailing colon.
    character = items[1][0]
    # Password is the remaining component of the line.
    password = items[2]
    # Initialize count variable to count the number of times the character appears in the password
    count = 0
    for a in range(len(password)):
        if password[a] == character:
            count += 1
    # If character appears greater than or equal to the policy minimum,
    # or less than or equal to the policy maximum number of times, the password is valid.
    if count >= policy_min and count <= policy_max:
        return True
    else:
        return False


def part2(line):
    items = line.split()
    policy = items[0]
    policy_items = policy.split("-")
    policy_first_position = int(policy_items[0]) - 1
    policy_second_position = int(policy_items[1]) - 1
    character = items[1][0]
    password = items[2]
    # Character must be in either the first position or the second position, but not both
    # Boolean != Boolean is an xor
    if (password[policy_first_position] == character) != (
        password[policy_second_position] == character
    ):
        return True
    else:
        return False


part1_valid = 0
part2_valid = 0
with open("input", "r") as fh:
    for line in fh:
        if part1(line):
            part1_valid += 1
        if part2(line):
            part2_valid += 1

print("Part 1: {}".format(part1_valid))
print("Part 2: {}".format(part2_valid))
