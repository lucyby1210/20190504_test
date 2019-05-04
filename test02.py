
if __name__ == '__main__':
    while(True):
        n = input('input: ')
        a = []
        cnt = 0
        for i in range(int(n)):
            a.append(True)
        for i in range(int(n)):
            if (i+1)%3 == 0:
                a[i] = ~a[i]
                # print(a)
            if (i+1)%5 == 0:
                a[i] = ~a[i]
                # print(a)
        for i in range(int(n)):
            if int(a[i]) == 1:
                # print(i, end=' ')
                cnt += 1
        print('output: %d' % cnt)

