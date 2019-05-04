
def rev(word):
    tmp = list(word)
    l = len(tmp)
    ans = ''
    for i in range(l):
        ans += tmp[l-i-1]
    return ans

if __name__ == '__main__':
    while(True):
        tmpstr = input('input string: ')
        ansstr = ''
        for w in tmpstr.strip().split(' '):
            ansstr += rev(w)
            ansstr += ' '
        print(ansstr)
