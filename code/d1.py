from common_utils import RunTimeSolution


class Solution1(object):

    # initialize Solution1
    def __init__(self, infile):
        print ('\nSolution1...')
        self.infile = infile
        with open(self.infile, 'r') as f:
            self.nums = [int(line) for line in f]

    # solution to problem 1.a
    def a(self):

        d = {}
        for pos, val in enumerate(self.nums):
            need = 2020 - val
            if need not in d:
                d[val] = pos
            else:
                return val * need

    # solution to problem 1.b
    def b(self):

        sorted_nums = sorted(self.nums)
        for i in range(len(sorted_nums) - 2):
            if i > 0 and sorted_nums[i] == sorted_nums[i - 1]:
                continue
            left = i + 1
            right = len(sorted_nums) - 1
            while left < right:
                s = sorted_nums[i] + sorted_nums[left] + sorted_nums[right]
                if s < 2020:
                    left += 1
                elif s > 2020:
                    right -= 1
                else:
                    return sorted_nums[i] * sorted_nums[left] * sorted_nums[right]


# input data file
input_file = '/Users/dillshau/PycharmProjects/git_projects/AOC_2020/input_data/d1.txt'

# initialize Solution1
sol1 = Solution1(input_file)

# problem a
RunTimeSolution.run(sol1, sol1.a)

# problem b
RunTimeSolution.run(sol1, sol1.b)
