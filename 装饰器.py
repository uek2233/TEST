import time


def display_time(func):
    def wrapper(*args):
        t1 = time.time()
        res = func(*args)
        t2 = time.time()
        print(f'运行时间是{t2 - t1}秒')
        return res
    return wrapper


def is_prime(num):
    if num < 2:
        return False
    else:
        for i in range(2, num):
            if num % i == 0:
                return False
            else:
                return True


@display_time
def prime_nums(num):
    count = 0
    for i in range(2, num):
        if is_prime(i):
            count += 1
            print(i)
    return count


all_num = prime_nums(100)
print(f'素数的个数是{all_num}')
