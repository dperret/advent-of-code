#!/usr/bin/env python3


class Person:
    def __init__(self):
        self.questions = []

    def __str__(self):
        return "Questions: {}".format(self.questions)

    def setQuestions(self, line):
        print("setQuestions {}".format(line))
        for char in line:
            if char in self.questions:
                pass
            else:
                self.questions.append(char)


class Group:
    def __init__(self):
        self.people = []

    def __str__(self):
        return "People: {}".format(self.people)

    def getQuestionCount(self):
        questions = []
        for person in self.people:
            for q in person.questions:
                if q in questions:
                    pass
                else:
                    questions.append(q)
        return len(questions)

    def getAllYesQuestions(self):
        allYesQuestions = []
        for person in self.people:
            for question in person.questions:
                if question not in allYesQuestions:
                    allYesQuestions.append(question)
        print("AllQuestions: {}".format(allYesQuestions))
        removeQuestions = []
        for person in self.people:
            for q in allYesQuestions:
                if q not in person.questions:
                    # allYesQuestions.remove(q)
                    if q not in removeQuestions:
                        removeQuestions.append(q)
        for z in removeQuestions:
            allYesQuestions.remove(z)
        print("AllYesQuesions: {}".format(allYesQuestions))
        return allYesQuestions

    def getNumAllYes(self):
        print("numAllYes: {}".format(len(self.getAllYesQuestions())))
        return len(self.getAllYesQuestions())


def part1(lines):
    currGroup = Group()
    groups = []
    for line in lines:
        if line != "":
            currPerson = Person()
            # print(line)
            currPerson.setQuestions(line)
            currGroup.people.append(currPerson)
        else:
            groups.append(currGroup)
            currGroup = Group()

    totalQuestions = 0
    for group in groups:
        totalQuestions += group.getQuestionCount()
    return totalQuestions


def part2(lines):
    currGroup = Group()
    groups = []
    for line in lines:
        if line != "":
            currPerson = Person()
            # print(line)
            currPerson.setQuestions(line)
            currGroup.people.append(currPerson)
        else:
            groups.append(currGroup)
            currGroup = Group()

    print("Groups: {}".format(len(groups)))
    totalQuestions = 0
    for group in groups:
        for person in group.people:
            print(person)
        print("Group: {}".format(group.getNumAllYes()))
        totalQuestions += group.getNumAllYes()
    return totalQuestions


with open("input", "r") as fh:
    lines = fh.read().split("\n")
    print("Part 1: {}".format(part1(lines)))
    print("Part 2: {}".format(part2(lines)))
