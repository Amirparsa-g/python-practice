t= int(input())
for i in range(t):
    array=[]
    total=0
    n , s , x= map(int,input().split()) 
   
    array.extend(map(int,input().split()))
    total = sum(array)
    if total == s or (total < s and (s-total)%x==0):
      print("YES")
    else:
      print("NO")
      