#!/usr/bin/python
t=int(raw_input())
for i in range(t):
    [n,k]=raw_input().strip().split()
    n=int(n)
    k=int(k)
    count=n
    l=raw_input().strip().split()
    for i in l:
        if(i<'0'):
            count=count-1
    if(count<k):
        print "YES"
    else:
        print "NO"