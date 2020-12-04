#!/usr/bin/env python3

# fields = {"byr": "Birth Year",
#    "iyr": "Issue Year"
#    "eyr": "Expiration Year",
#    "hgt": "Height",
#    "hcl": "Hair Color",
#    "ecl": "Eye Color",
#    "pid": "Passport ID",
#    "cid": "Country ID"}


class Passport:
    def __init__(self):
        self.byr = None
        self.iyr = None
        self.eyr = None
        self.hgt = None
        self.hcl = None
        self.ecl = None
        self.pid = None
        self.cid = "North Pole"

    def __str__(self):
        return "Birth Year: {}".format(self.byr)

    def setField(self, data):
        fieldData = data.split(":")
        if fieldData[0] == "byr":
            self.byr = fieldData[1]
        elif fieldData[0] == "iyr":
            self.iyr = fieldData[1]
        elif fieldData[0] == "eyr":
            self.eyr = fieldData[1]
        elif fieldData[0] == "hgt":
            self.hgt = fieldData[1]
        elif fieldData[0] == "hcl":
            self.hcl = fieldData[1]
        elif fieldData[0] == "ecl":
            self.ecl = fieldData[1]
        elif fieldData[0] == "pid":
            self.pid = fieldData[1]
        elif fieldData[0] == "cid":
            self.cid = fieldData[1]

    def updateData(self, line):
        items = line.split(" ")
        for item in items:
            self.setField(item)

    def isValid(self):
        if (
            self.byr is None
            or self.iyr is None
            or self.eyr is None
            or self.hgt is None
            or self.hcl is None
            or self.ecl is None
            or self.pid is None
        ):
            return False
        else:
            return True

    def byrValid(self):
        if int(self.byr) >= 1920 and int(self.byr) <= 2002:
            return True
        else:
            return False

    def iyrValid(self):
        if int(self.iyr) >= 2010 and int(self.iyr) <= 2020:
            return True
        else:
            return False

    def eyrValid(self):
        if int(self.eyr) >= 2020 and int(self.eyr) <= 2030:
            return True
        else:
            return False

    def hgtValid(self):
        try:
            units = self.hgt[-2:]
            value = int(self.hgt[:-2])
            if units == "cm":
                if value >= 150 and value <= 193:
                    return True
                else:
                    return False
            elif units == "in":
                if value >= 59 and value <= 76:
                    return True
                else:
                    return False
            else:
                return False
        except:
            return False

    def hclValid(self):
        if len(self.hcl) == 7:
            if self.hcl[0] == "#":
                try:
                    value = int(self.hcl[1:], 16)
                    return True
                except:
                    return False
            else:
                return False
        else:
            return False

    def eclValid(self):
        validEyeColors = ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]
        if self.ecl in validEyeColors:
            return True
        else:
            return False

    def pidValid(self):
        if len(self.pid) == 9:
            try:
                number = int(self.pid)
                return True
            except:
                return False
        else:
            return False

    def extraValid(self):
        if self.isValid() == False:
            return False
        else:
            return (
                self.byrValid()
                and self.iyrValid()
                and self.eyrValid()
                and self.hgtValid()
                and self.hclValid()
                and self.eclValid()
                and self.pidValid()
            )


def part1(lines):
    numPassports = 0
    validPassports = 0
    currentPassport = Passport()
    for line in lines:
        if line != "":
            currentPassport.updateData(line)
        else:
            if currentPassport.isValid():
                validPassports += 1
            numPassports += 1
            currentPassport = Passport()
    print("Total Passports: {}".format(numPassports))
    print("Valid Passports: {}".format(validPassports))
    return validPassports


def part2(lines):
    numPassports = 0
    extraValidPassports = 0
    currentPassport = Passport()
    for line in lines:
        if line != "":
            currentPassport.updateData(line)
        else:
            if currentPassport.extraValid():
                extraValidPassports += 1
            numPassports += 1
            currentPassport = Passport()
    print("Extra Valid Passports: {}".format(extraValidPassports))
    return extraValidPassports


with open("input", "r") as fh:
    lines = fh.read().split("\n")
    print("Part 1 Valid Passports: {}".format(part1(lines)))
    print("Part 2 Extra Valid Passports: {}".format(part2(lines)))
