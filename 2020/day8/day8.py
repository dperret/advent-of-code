#!/usr/bin/env python3
import statistics


def processInstruction(index, accumulator, line, modifyInstruction):
    if line == "":
        return (index, accumulator)
    parts = line.split(" ")
    instruction = parts[0]
    value = int(parts[1])
    if index == modifyInstruction:
        if instruction == "jmp":
            instruction = "nop"
        elif instruction == "nop":
            instruction = "jmp"
    if instruction == "acc":
        return (index + 1, accumulator + value)
    elif instruction == "jmp":
        return (index + value, accumulator)
    elif instruction == "nop":
        return (index + 1, accumulator)


def part1(lines):
    i = 0
    accumulator = 0
    linesExecuted = []
    while i < len(lines):
        if i in linesExecuted:
            print("Duplicate instruction: {}".format(i))
            return accumulator
        linesExecuted.append(i)
        i, accumulator = processInstruction(i, accumulator, lines[i], -1)
    return accumulator


def part2(lines, modifyInstruction):
    i = 0
    accumulator = 0
    linesExecuted = []
    counter = 0
    duplicateJumpsExecuted = []
    while i < len(lines):
        if counter > 10000:
            return -1
        # if(i in linesExecuted):
        #    # print("Duplicate instruction: {}: {}".format(i, lines[i]))
        #    if(lines[i][:5] == "jmp -"):
        #        duplicateJumpsExecuted.append(i)
        #        if(len(duplicateJumpsExecuted) > 10000):
        #            #for item in duplicateJumpsExecuted:
        #            #    print(item)
        #            #print(duplicateJumpsExecuted)
        #            #print(statistics.mode(duplicateJumpsExecuted))
        #            return accumulator
        linesExecuted.append(i)
        counter += 1
        currentInstruction = i
        i, accumulator = processInstruction(i, accumulator, lines[i], modifyInstruction)
        if i == currentInstruction:
            break
    print("Finished! i: {} accumulator: {}".format(i, accumulator))
    return accumulator


def identifyCandidates(lines):
    candidates = []
    for i in range(1, len(lines) - 1):
        instruction = lines[i][:3]
        previousInstruction = lines[i - 1][:3]
        nextInstruction = lines[i + 1][:3]
        if instruction == "acc":
            continue
        elif instruction == "jmp":
            candidates.append(i)
            # if nextInstruction == "jmp":
            #    continue
            # else:
            #    candidates.append(i)
        elif instruction == "nop":
            candidates.append(i)
            # if int(lines[i][4:]) >= 0:
            #    candidates.append(i)
    # for item in changeInstructions:
    #    candidates.remove(item)
    return candidates


with open("input", "r") as fh:
    lines = fh.read().split("\n")
    changeInstructions = identifyCandidates(lines)
    # changeInstructions = range(0,623)
    # changeInstructions = [298]
    for modifyInstruction in changeInstructions:
        accumulator = part2(lines, modifyInstruction)
        if accumulator != -1:
            print("modifyInstruction: {}".format(modifyInstruction))
            print("Part 2: {}".format(accumulator))
            exit()
