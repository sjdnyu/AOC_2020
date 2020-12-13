from common_utils import RunTimeSolution


class Solution5(object):

    # initialize Solution5
    def __init__(self, infile):
        print('\nSolution5...')
        self.infile = infile

    # get list of ids from each file line
    def rows_cols(self):
        rcs = list()
        with open (self.infile) as f:
            for line in f:
                row = [x for x in range (0, 128)]
                col = [x for x in range (0, 8)]
                for i, char in enumerate (line):
                    if char == "F":
                        row = row[:(len (row) // 2)]
                    elif char == "B":
                        row = row[(len (row) // 2):]
                    elif char == "L":
                        col = col[:(len (col) // 2)]
                    elif char == "R":
                        col = col[(len (col) // 2):]
                rcs.append([row, col])
        return rcs

    # solution to problem 5.a
    def a(self):
        rcs = self.rows_cols()
        ids = [r[0] * 8 + c[0] for r, c in rcs]
        r = max(ids)
        return r

    # solution to problem 5.b
    def b(self):
        rcs = self.rows_cols()
        ids = [r[0] * 8 + c[0] for r, c in rcs]
        for r, pass_id in zip (range(min (ids), max(ids)), sorted(ids)):
            if r != pass_id:
                return r


# input data file
input_file = '/Users/dillshau/PycharmProjects/git_projects/AOC_2020/input_data/d5.txt'

# initialize Solution1
sol5 = Solution5(input_file)

# problem a
RunTimeSolution.run(sol5, sol5.a)

# problem b
RunTimeSolution.run(sol5, sol5.b)

