import time


# verify password meets criteria (a)
def check_password_a(inp):
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
def check_password_b(inp):
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


# solution to problem 1.a
def solution_2a(infile):
    res = 0
    with open(infile, 'r') as f:
        for line in f:
            if check_password_a(line):
                res += 1
    return res


# solution to problem 1.b
def solution_2b(infile):
    res = 0
    with open(infile, 'r') as f:
        for line in f:
            if check_password_b(line):
                res += 1
    return res


# wrapper function to call and print runtime oof each solution
def time_func(f, *args):
    stime = time.time()
    res = f(args[0])
    etime = time.time()
    runtime_millis = int((etime - stime) * 1000000.0)
    print('result = {} \t|  \t runtime(ms) = {}'.format(res, runtime_millis))


# input data file
input_file = '/Users/dillshau/PycharmProjects/AOC/2020/input_data/d2.txt'

# problem 2.a
time_func(solution_2a, input_file)

# problem 2.b
time_func(solution_2b, input_file)
