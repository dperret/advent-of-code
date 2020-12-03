#!/usr/bin/env python3


def part1(lines):
    tree = "#"
    hittrees = 0
    column = 0
    for row in lines:
        # Return if an empty line is read. This assumes an empty line at the end of the file.
        if len(row) == 0:
            return hittrees
        # If column index is larger than the row length, wrap around to beginning of row
        if column >= len(row):
            column -= len(row)
        if row[column] == tree:
            hittrees += 1
        column += 3
    return hittrees


# Same as part 1, but take number of rows and columns to jump as parameters
def part2(lines, rowjump, columnjump):
    tree = "#"
    hittrees = 0
    column = 0
    rowindex = 0
    while rowindex < len(lines):
        row = lines[rowindex]
        if len(row) == 0:
            return hittrees
        if column >= len(row):
            column -= len(row)
        if row[column] == tree:
            hittrees += 1
        column += columnjump
        rowindex += rowjump
    return hittrees


with open("input", "r") as fh:
    lines = fh.read().split("\n")
    print("Part 1 Trees Hit: {}".format(part1(lines)))
    # Part 2 - compute 5 different paths, then multiple number of trees hit
    firstpath = part2(lines, 1, 1)
    secondpath = part2(lines, 1, 3)
    thirdpath = part2(lines, 1, 5)
    fourthpath = part2(lines, 1, 7)
    fifthpath = part2(lines, 2, 1)
    part2final = firstpath * secondpath * thirdpath * fourthpath * fifthpath
    print("Part 2: {}".format(part2final))
