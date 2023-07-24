def count(n):
    flag = 0
    count = 0
    if n == 1 or n == 0:
        print(0)
    else:
        for i in range(2, n+1):
            flag = 0
            for j in range(1, i+1):
                if i % j == 0:
                    flag += 1
            if flag == 2:
                count += 1
        print(count)

n = int(input())
count(n)
