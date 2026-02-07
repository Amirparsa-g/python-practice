def build_max_array(a,b):
    for i in range (len(a)):
        if b[i] > a[i]:
            a[i] = b[i]
    for i in range (len(a)-1 , 0 , -1):
        if a[i]>a[i-1]:
            a[i-1] = a[i]
    return a

t = int(input())

for _ in range(t):
    a = []
    b = []
    
    n , q = map(int,input().split())
    a.extend(map(int,input().split()))
    b.extend(map(int,input().split()))
    max_array= build_max_array(a,b)
    pref = [0]*(n+1)
    for i in range(n) :
        pref[i+1] = pref[i] + max_array[i]

    for i in range(q):
        l,r = map(int,input().split())
        ans = pref[r] - pref[l-1]
        print (ans , end=" ")

