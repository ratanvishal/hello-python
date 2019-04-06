import time
from functools import lru_cache
@lru_cache(maxsize=32)
def some_work(n):
    # some task taking n seconds
    time.sleep(n)
    return n


if __name__=='__main__':
    print("now running some work")
    some_work(3)
    print("done...calling again")
    some_work(3)
    print("called again")
    some_work(3)
    print("called again vishal")
    input()
    some_work(1)
    print("done")


