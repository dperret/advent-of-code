#!/usr/bin/env python3


class Bag:
    def __init__(self):
        self.contents = []
        self.outercolor = None

    def __str__(self):
        return "{} bag contents: {}".format(self.outercolor, self.contents)


class Part2Bag:
    def __init__(self):
        self.contents = []
        self.outercolor = None

    def __str__(self):
        return "{} bag contents: {}".format(self.outercolor, self.contents)


def findPossibleOuterBags(allBags, targetBag):
    possibleBags = []
    for bag in allBags:
        if targetBag in bag.contents:
            # print(bag)
            # print(bag.outercolor)
            if bag.outercolor not in possibleBags:
                possibleBags.append(bag.outercolor)
            nextlevel = findPossibleOuterBags(allBags, bag.outercolor)
            for item in nextlevel:
                if item not in possibleBags:
                    possibleBags.append(item)
    return possibleBags


def findTotalBags(allBags, targetBag):
    # Include targetBag as 1 bag
    total = 1
    objectBag = None
    for bag in allBags:
        if bag.outercolor == targetBag:
            objectBag = bag
            break
    if objectBag != None:
        for innerbag in objectBag.contents:
            total += findTotalBags(allBags, innerbag)
    return total


def part1(lines):
    possibleBags = []
    for line in lines:
        if len(line) < 1:
            continue
        index = line.find(" bags contain ")
        outerbag = line[:index]
        # print("Outer bag: {}".format(outerbag))
        newBag = Bag()
        newBag.outercolor = outerbag
        secondhalf = line[index + 14 :]
        if secondhalf == "no other bags.":
            continue
        else:
            parts = secondhalf.split(",")
            # print(parts)
            for part in parts:
                item = part.strip()
                quantity = item[0]
                bagindex = item.find(" bag")
                innerbag = item[2:bagindex]
                # print("{}: {}".format(quantity, innerbag))
                # for i in range(0,int(quantity)):
                #    newBag.contents.append(innerbag)
                newBag.contents.append(innerbag)
                # print(newBag)
        possibleBags.append(newBag)
    outerbags = findPossibleOuterBags(possibleBags, "shiny gold")
    return len(outerbags)


def part2(lines):
    possibleBags = []
    for line in lines:
        if len(line) < 1:
            continue
        index = line.find(" bags contain ")
        outerbag = line[:index]
        # print("Outer bag: {}".format(outerbag))
        newBag = Bag()
        newBag.outercolor = outerbag
        secondhalf = line[index + 14 :]
        if secondhalf == "no other bags.":
            continue
        else:
            parts = secondhalf.split(",")
            # print(parts)
            for part in parts:
                item = part.strip()
                quantity = item[0]
                bagindex = item.find(" bag")
                innerbag = item[2:bagindex]
                # print("{}: {}".format(quantity, innerbag))
                for i in range(0, int(quantity)):
                    newBag.contents.append(innerbag)
                # newBag.contents.append(innerbag)
                # print(newBag)
        possibleBags.append(newBag)
    # TODO: Figure out why findTotalBags is off by 1
    totalbags = findTotalBags(possibleBags, "shiny gold") - 1
    return totalbags


with open("input", "r") as fh:
    lines = fh.read().split("\n")
    print("Part 1: {}".format(part1(lines)))
    print("Part 2: {}".format(part2(lines)))
