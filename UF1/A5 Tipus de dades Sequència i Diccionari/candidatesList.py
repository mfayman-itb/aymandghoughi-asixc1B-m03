num = int(input())
lst = [input() for cand in range(num)]
pos = 0

while pos != -2:
    print(lst[pos])
    pos = int(input()) - 1