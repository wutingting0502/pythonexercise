"""*args """
def tupleArgs(arg1, arg2= 'B', *arg3):
    print('arg 1:%s ' % arg1)
    print('arg 2:%s ' % arg2)
    for eachArgNum in range(len(arg3)):
        print('the %d in arg 3 :%s ' % (eachArgNum,arg3[eachArgNum]))

if __name__ == '__main__':
    tupleArgs('A')

def tupleArgs(arg1, arg2= 'B', *arg3):
    print('arg 1:%s ' % arg1)
    print('arg 2:%s ' % arg2)
    for eachArgNum in range(len(arg3)):
        print('the %d in arg 3 :%s ' % (eachArgNum,arg3[eachArgNum]))

if __name__ == '__main__':
    tupleArgs('23', 'C')

def tupleArgs(arg1, arg2= 'B', *arg3):
    print('arg 1:%s ' % arg1)
    print('arg 2:%s ' % arg2)
    for eachArgNum in range(len(arg3)):
        print('the %d in arg 3 :%s ' % (eachArgNum,arg3[eachArgNum]))
if __name__ == '__main__':
    tupleArgs('12', 'A', 'GF', 'L')

    """**kw  """

def dictArgs(kw1, kw2= 'B', **kw3):
    print('kw 1:%s ' % kw1)
    print('kw 2:%s ' % kw2)
    for eachKw in kw3:
        print('the %s ---->:%s ' % (eachKw,kw3[eachKw]))
if __name__ == '__main__':
    dictArgs('A')

def dictArgs(kw1, kw2= 'B', **kw3):
    print('kw 1:%s ' % kw1)
    print('kw 2:%s ' % kw2)
    for eachKw in kw3:
        print('the %s ---->:%s ' % (eachKw,kw3[eachKw]))
if __name__ == '__main__':
    dictArgs('23', 'C')


def dictArgs(kw1, kw2='B', **kw3):
        print('kw 1:%s ' % kw1)
        print('kw 2:%s ' % kw2)
        for eachKw in kw3:
            print('the %s ---->:%s ' % (eachKw, kw3[eachKw]))
    if __name__ == '__main__':
        dictArgs('12', 'A', c='C', d='12121212')

def dictArgs(kw1, kw2= 'B', **kw3):
    print('kw 1:%s ' % kw1)
    print('kw 2:%s ' % kw2)
    for eachKw in kw3:
        print('the %s ---->:%s ' % (eachKw,kw3[eachKw]))
if __name__ == '__main__':
    dictArgs('kw', c='C', d='12121212', kw='KW')