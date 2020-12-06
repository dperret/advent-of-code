#!/usr/bin/env python3

# Given a character, F/L or B/R, and a range, return the upper or lower half of that range based on the character.
def frontback(char, lower, upper):
    midpoint = round((lower + upper) / 2)
    if(char == 'F' or char == "L"):
        #Return lower half
        return (lower, (midpoint - 1))
    elif (char == 'B' or char == "R"):
        #return upper half
        return (midpoint, upper)
    else:
        print("INVALID CHAR: {}".format(char))
        return -1

# Compute seat id for a given line
def seatid(line):
    # Check line length first
    if(len(line) != 10):
        #print("Problem with line: {}".format(line))
        return 0
    # Split lines into characters that specify rows and columns
    rowdirs = line[:7]
    columndirs = line[-3:]
    # Set min and max values for rows and columns
    row = 0
    column = 0
    rowhigh = 127
    rowlow = 0
    columnlow = 0
    columnhigh = 7
    # Iterate through row characters to determine row
    for char in rowdirs[:6]:
        (rowlow, rowhigh) = frontback(char, rowlow, rowhigh)
    # On last character, set row to either the lower or upper bound.
    # Lower and upper bound should differ by 1 at this point.
    if(rowdirs[6] == "F"):
        row = rowlow
    else:
        row = rowhigh

    # Iterate through column characters to determine column
    for char in columndirs:
        (columnlow, columnhigh) = frontback(char, columnlow, columnhigh)
    if(columndirs[2] == "L"):
        column = columnlow
    else:
        column = columnhigh

    # After row and column have been determined, calculate seat id, and return
    seatid = (row * 8) + column
    return seatid


def part1(lines):
    seatidmax = 0
    for line in lines:
        # Make sure lines are the correct length before attempting to compute seat id
        if(len(line) != 10):
            #print("Problem with line: {}".format(line))
            continue
        rowdirs = line[:7]
        columndirs = line[-3:]
        row = 0
        column = 0
        rowhigh = 127
        rowlow = 0
        columnlow = 0
        columnhigh = 7
        for char in rowdirs[:6]:
            (rowlow, rowhigh) = frontback(char, rowlow, rowhigh)
        if(rowdirs[6] == "F"):
            row = rowlow
        else:
            row = rowhigh
        for char in columndirs:
            (columnlow, columnhigh) = frontback(char, columnlow, columnhigh)
        if(columndirs[2] == "L"):
            column = columnlow
        else:
            column = columnhigh
        seatid = (row * 8) + column
        if(seatid > seatidmax):
            seatidmax = seatid
    return seatidmax

# This method for part 2 calculates all possible seat id values, and removes seatids that are found in the provided list
# The problem with this approach is that invalid seat id values are still included at the end of the method
# Printing all remaining seat id values, and manually adjusting the row range provided enough information to submit the correct answer for part 2.
def part2(lines):
    seatids = []
    for row in range(1,119):
        for column in range(0,8):
            seat = (row * 8) + column
            seatids.append(seat)
    for line in lines:
        if line == "":
            continue
        seat = seatid(line)
        if(seat in seatids):
            seatids.remove(seat)
        else:
            print("Missing SeatID: {}".format(seat))
    print(seatids)

# This is a better way to do part 2, and actually returns the correct seat without manual adjustment of the range
def alternatePart2(lines):
    # Compute seat id values for all seats in input file
    seatids = []
    for line in lines:
        if(len(line) != 10):
            #print("Problem with line: {}".format(line))
            continue
        else:
            seatids.append(seatid(line))
    # Sort list of seat ids
    seatids.sort()
    # Use min and max seat id values as bounds to avoid invalid seat ids at beginning and end
    start = min(seatids)
    end = max(seatids)
    for seat in seatids:
        if(seat > start and seat < end):
            index = seatids.index(seat)
            # Check to see if adjacent seat ids are in list
            if(seatids[index - 1] == (seat - 1) and seatids[index + 1] == seat + 1):
                continue
            else:
                # If seat id is missing, this is our ticket
                #print("seat: {}".format(seat + 1))
                return (seat + 1)

with open("input", "r") as fh:
    lines = fh.read().split("\n")
    print("SeatID Max: {}".format(part1(lines)))
    #part2(lines)
    print("Part 2: {}".format(alternatePart2(lines)))
