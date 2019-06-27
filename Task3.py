import datetime


class timeit:
    def __enter__(self):
        print('init')
        self.start_time = datetime.datetime.now()

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.finish_time = datetime.datetime.now()
        print('spend time: {}'.format(self.finish_time - self.start_time))


with timeit():
    a = [lambda x: x * x for x in range(10_000_000)]
