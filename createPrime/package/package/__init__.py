#coding=utf-8
'''
暴力产生素数，在服务器上运行，输出素数表
'''
import time

def judge(n, prime):
    for i in prime:
        if (i > (n ** 0.5)):
            return 1
        if (n % i == 0):
            return 0
    else:
        return 1
        
def createPrime(n, prime):
    if (n < 10):
        return prime

    for i in range(11, n, 2):
        if judge(i, prime):
            prime.append(i)
        print str(float(i)/float(n) * 100) + '%'
    return prime

def writeFile(output,title = '', heading = ''):
    file = open(title, 'w')
    file.write('date: ' + str(time.localtime()) + '\n' + '----------------------------------------' + '\n')
    file.write(heading + '\n' + '----------------------------------------' + '\n')
    for i in output:
        file.write(str(i)+'\n')
    file.close()

class time_tq():
    def __init__(self):
        self.h = 0
        self.m = 0
        self.s = 0
        self.str = ''
    
    def set_time(self, seconds):
        self.h = int(seconds / 3600)
        seconds -= self.h * 3600
        self.m = int(seconds / 60)
        seconds -= self.m * 60
        self.s = seconds
        self.str = str(self.h) + 'h' + str(self.m) + 'm' + str(self.s) + 's'

def main():
    prime = [2, 3, 5, 7]
    n = input('please input a num: ')
    '''
    if (type(n) != 'int'):
        print 'input error'
    else:
        createPrime(n, prime)
    '''
    start_time = time.time()
    createPrime(n,prime)
    end_time = time.time()
    t = time_tq()
    t.set_time(end_time - start_time)
    writeFile(prime, 'prime.txt', t.str)
    
main()