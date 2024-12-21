import time
from contextlib import contextmanager
from time import sleep

class cm_timer_1:
    def __enter__(self):
        self.start = time.time()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.end = time.time()
        delta = self.end - self.start
        print(f"time: {delta:.2f} seconds")

@contextmanager
def cm_timer_2():
    start = time.time()
    try:
        yield
    finally:
        end = time.time()
        delta = end - start
        print(f"time: {delta:.2f} seconds")

if __name__ == "__main__":

    print("cm_timer_1:")
    with cm_timer_1():
        sleep(1.5)

    print("cm_timer_2:")
    with cm_timer_2():
        sleep(2)