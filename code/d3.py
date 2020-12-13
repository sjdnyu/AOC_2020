from common_utils import RunTimeSolution
import numpy as np


class Solution3(object):

    # initialize Solution3
    def __init__(self, infile):
        print('\nSolution3...')
        self.infile = infile
        with open(self.infile, 'r') as f:
            self.trajectory = list([str(line.strip ()) for line in f])

    # number of trees for a given slope
    def num_trees(self, s):
        num_cols = len(self.trajectory[0])
        num_rows = np.shape(self.trajectory)[0]
        row_pos = 0
        col_pos = 0
        res = 0

        for row_pos, row in enumerate(self.trajectory):
            if col_pos >= num_cols:
                col_pos = col_pos - num_cols
            if (row_pos % s[1]) != 0:
                continue
            val = row[col_pos]
            if row_pos >= num_rows:
                break
            if val == '#':
                res += 1
            col_pos += s[0]

        return res

    # solution to problem 1.a
    def a(self):
        res = self.num_trees((3, 1))
        return res

    # solution to problem 1.a
    def b(self):
        r1 = self.num_trees((3, 1))
        r2 = self.num_trees((1, 1))
        r3 = self.num_trees((5, 1))
        r4 = self.num_trees((7, 1))
        r5 = self.num_trees((1, 2))
        res = r1 * r2 * r3 * r4 * r5
        return res


# input data file
input_file = '/Users/dillshau/PycharmProjects/git_projects/AOC_2020/input_data/d3.txt'

# initialize Solution1
sol3 = Solution3(input_file)

# problem a
RunTimeSolution.run(sol3, sol3.a)

# problem b
RunTimeSolution.run(sol3, sol3.b)
