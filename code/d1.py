import time


class Solution1(object):

    # solution to problem 1.a
    def solution_a(self, infile):
        with open(infile, 'r') as f:
            report = [int(line) for line in f]

        d = {}
        for pos, val in enumerate(report):
            need = 2020 - val
            if need not in d:
                d[val] = pos
            else:
                return val * need


    # solution to problem 1.b
    def solution_1b(infile):
        with open(infile, 'r') as f:
            nums = [int(line) for line in f]

        nums.sort()
        for i in range(len(nums) - 2):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            l = i + 1
            r = len(nums) - 1
            while l < r:
                s = nums[i] + nums[l] + nums[r]
                if s < 2020:
                    l += 1
                elif s > 2020:
                    r -= 1
                else:
                    return nums[i] * nums[l] * nums[r]


    # wrapper function to call and print runtime of each solution
    def time_func(f, *args):
        stime = time.time()
        res = f(args[0])
        etime = time.time()
        runtime_millis = int((etime - stime) * 1000000.0)
        print('result = {} \t|  \t runtime(ms) = {}'.format(res, runtime_millis))


# input data file
input_file = '/Users/dillshau/PycharmProjects/AOC/2020/input_data/d1.txt'

# problem 1
time_func(solution_1a, input_file)

# problem 2
time_func(solution_1b, input_file)