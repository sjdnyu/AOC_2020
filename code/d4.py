from common_utils import RunTimeSolution
import re


class Solution4(object):

    # initialize Solution4
    def __init__(self, infile):
        print('\nSolution4...')
        self.infile = infile
        self.passports = self.parsefile()

    # list of dictionaries from file
    def parsefile(self):
        passports = list()
        file = open(self.infile, mode='r')
        for line in file.read().split("\n\n"):
            line = line.replace("\n", " ")
            line_list = line.split(" ")
            line_dict = dict()
            for part in line_list:
                k, v = part.split(":")
                part_dict = {k : v}
                line_dict.update(part_dict)
            passports.append(line_dict)
        return passports

    # check validity of one passport - rules a
    def check_passport_a(self, pp, required_keys):
        pp_list = list(pp.keys())
        for rk in required_keys:
            n = pp_list.count(rk)
            if n < 1:
                return False
        return True

    # check validity of one passport - rules b
    def check_passport_b(self, pp, required_keys):
        pp_list = list(pp.keys())

        for rk in required_keys:
            n = pp_list.count(rk)
            if n < 1:
                return False

            if rk == "byr":
                byr_int = int(pp[rk])
                if byr_int >= 1920 and byr_int <= 2002: continue
                else: return False

            if rk == "iyr":
                iyr_int = int(pp[rk])
                if iyr_int >= 2010 and iyr_int <= 2020: continue
                else: return False

            if rk == "eyr":
                eyr_int = int(pp[rk])
                if eyr_int >= 2020 and eyr_int <= 2030: continue
                else: return False

            if rk == "hgt":
                hgt_res = re.match("^(1([5-8][0-9]|9[0-3])cm|(59|[6][0-9]|[7][0-6])in)$", pp[rk])
                if hgt_res: continue
                else: return False

            if rk == "hcl":
                hcl_res = re.match("#[0-9a-f]{6}", pp[rk])
                if hcl_res: continue
                else: return False

            if rk == "ecl":
                ecl_res = re.match("^(amb|blu|brn|gry|grn|hzl|oth)$", pp[rk])
                if ecl_res: continue
                else: return False

            if rk == "pid":
                pid_res = re.match("^\\d{9}$", pp[rk])
                if pid_res: return True
                else: return False
        return True

    # solution to problem 4.a
    def a(self):
        required_keys = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]
        res = sum([self.check_passport_a(p, required_keys) for p in self.passports])
        return res

    # solution to problem 4.b
    def b(self):
        required_keys = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]
        res = sum([self.check_passport_b(p, required_keys) for p in self.passports])
        return res


# input data file
input_file = '/Users/dillshau/PycharmProjects/git_projects/AOC_2020/input_data/d4.txt'

# initialize Solution1
sol4 = Solution4(input_file)

# problem a
RunTimeSolution.run(sol4, sol4.a)

# problem b
RunTimeSolution.run(sol4, sol4.b)

