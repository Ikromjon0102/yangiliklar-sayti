a,b=map(int,input().split())
start = a-a%3+3 if a%3!=0 else a
stop = b if b%3==0 else b-1 if (b-1)%3==0 else b-2
n = (stop-start)//3

summ = (start + stop) * n//2
# print(start, stop, n)


print(summ)