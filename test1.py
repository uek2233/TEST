import math


class Serial_Num(object):
    def __init__(self, n):
        self.n = n
        self.res = 0
    
    def serial_num(self, n):
        tmp = int(math.log10(n))
        w1 = int((n / (10 ** tmp)))
        if n > 10:
            self.res += w1 - tmp + 1
        else:
            self.res += n
        if tmp > 0:
            n = 10 ** tmp - 1
            self.serial_num(n)

    def delay_num(self):
        n = self.n
        tmp = int(math.log10(n))
        w1 = int((n / (10 ** tmp)))
        if n > 10:
            n2 = w1 * (10 ** tmp) + (w1 - 1) * (10 ** (tmp - 1))
            if n < n2:
                self.res -= 1


sn = Serial_Num(20)
sn.serial_num(sn.n)
sn.delay_num()
print(sn.res)
