#!/usr/bin/env python3

def frontback(char, lower, upper):
    midpoint = round((lower + upper) / 2)
    #print("midpoint {}".format(midpoint))
    if(char == 'F' or char == "L"):
        #Return lower half
        return (lower, (midpoint - 1))
    elif (char == 'B' or char == "R"):
        #return upper half
        return (midpoint, upper)
    else:
        print("INVALID CHAR: {}".format(char))
        return -1

def seatid(line):
    if(len(line) != 10):
        print("Problem with line: {}".format(line))
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
        #print("{}-{}".format(rowlow, rowhigh))
    if(rowdirs[6] == "F"):
        row = rowlow
        #print("row {}".format(rowlow))
    else:
        row = rowhigh
        #print("row {}".format(rowhigh))
    for char in columndirs:
        (columnlow, columnhigh) = frontback(char, columnlow, columnhigh)
        #print("{}-{}".format(columnlow, columnhigh))
    if(columndirs[2] == "L"):
        column = columnlow
        #print("column {}".format(columnlow))
    else:
        column = columnhigh
        #print("column {}".format(columnhigh))
    seatid = (row * 8) + column
    return seatid


def part1(lines):
    seatidmax = 0
    for line in lines:
        #print(len(line))
        #print(line)
        if(len(line) != 10):
            print("Problem with line: {}".format(line))
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
            #print("{}-{}".format(rowlow, rowhigh))
        if(rowdirs[6] == "F"):
            row = rowlow
            #print("row {}".format(rowlow))
        else:
            row = rowhigh
            #print("row {}".format(rowhigh))
        for char in columndirs:
            (columnlow, columnhigh) = frontback(char, columnlow, columnhigh)
            #print("{}-{}".format(columnlow, columnhigh))
        if(columndirs[2] == "L"):
            column = columnlow
            #print("column {}".format(columnlow))
        else:
            column = columnhigh
            #print("column {}".format(columnhigh))
        seatid = (row * 8) + column
        if(seatid > seatidmax):
            seatidmax = seatid
    return seatidmax

def part2(lines):
    seatids = []
    for row in range(1,119):
        for column in range(0,8):
            #print("row: {} column: {}".format(row, column))
            seat = (row * 8) + column
            seatids.append(seat)
    #seatstaken = {}
    #for seat in seatids:
    #    seatstaken[seat] = False
    #print(seatstaken)
    for line in lines:
        if line == "":
            continue
        seat = seatid(line)
        #print(seat)
        #print(seatstaken[seat])
        if(seat in seatids):
            seatids.remove(seat)
        else:
            print("Missing SeatID: {}".format(seat))
        #if(seat in seatstaken.keys()):
        #    seatstaken[seat] = True
        #else:
        #    print(seat)
    print(seatids)
    #for seat in seatstaken:
    #    print(seat.value)
    #    if(seat.value == False):
    #        print(seat.value)

with open("input", "r") as fh:
    lines = fh.read().split("\n")
    #print(lines)
    #print(len(lines))
    print("SeatID Max: {}".format(part1(lines)))
    part2(lines)
    #print("Part 1: {}".format(part1(lines)))
    #print("Part 2: {}".format(part2(lines)))
