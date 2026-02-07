t = int(input())
for _ in range(t):
    array=[]
    n = int(input())
    array.extend(map(int,input().split()))
    array_sort=sorted(array)
    rank_map = {}
    for i, val in enumerate(array_sort):
        rank_map[val] = i
    
    ok = True
    for i in range(n-1):
        if (rank_map[array[i]]%2) == rank_map[array[i+1]]%2:
            ok = False
            break
    print("YES" if ok else "NO")

   
