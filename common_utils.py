import time


class RunTimeSolution(object):

    def __init__(self, **kwargs):
        self.f = kwargs['f']

    # wrapper function to:
    # (i)  call function arg f
    # (ii) print runtime
    def run(self, f):
        start_time = time.time()
        res = f()
        end_time = time.time()
        runtime_millis = int((end_time - start_time) * 1000000.0)
        print('result = {} \t|  \t runtime(ms) = {}'.format(res, runtime_millis))