from common_utils import RunTimeSolution


class Solution2(object):

    # initialize Solution2
    def __init__(self, infile):
        print ('\nSolution2...')
        self.infile = infile
        with open(self.infile, 'r') as f:
            self.policies = [line for line in f]

    # verify password meets criteria (a)
    def check_password_a(self, inp):
        rules_text = inp.split(sep=':')
        chars = rules_text[1][1:len(rules_text[1])]
        minmax, char = rules_text[0].split(' ')
        min_max_list = minmax.split(sep='-')
        min_obs = int(min_max_list[0])
        max_obs = int(min_max_list[1])
        num_obs = chars.count(char)
        if min_obs <= num_obs <= max_obs:
            return 1
        else:
            return 0

    # verify password meets criteria (b)
    def check_password_b(self, inp):
        rules_text = inp.split(sep=':')
        chars = rules_text[1][1:len(rules_text[1])]
        positions, char = rules_text[0].split(' ')
        positions_list = positions.split(sep='-')
        pos1 = int(positions_list[0]) - 1
        pos2 = int(positions_list[1]) - 1
        if pos1 < 0 or pos2 < 0:
            return 0

        m1 = chars[pos1] == char
        m2 = chars[pos2] == char
        tot = m1 + m2
        if tot == 1:
            return 1
        else:
            return 0

    # solution to problem 2.a
    def a(self):
        res = 0
        for line in self.policies:
            if self.check_password_a(line):
                res += 1
        return res

    # solution to problem 2.b
    def b(self):
        res = 0
        for line in self.policies:
            if self.check_password_b(line):
                res += 1
        return res


# input data file
input_file = '../input_data/d2.txt'


# initialize Solution2
sol2 = Solution2(input_file)

# problem a
RunTimeSolution.run(sol2, sol2.a)

# problem b
RunTimeSolution.run(sol2, sol2.b)
