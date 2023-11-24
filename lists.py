li = []

for _ in range(int(input())):
    
    query, *params = input().split()
    params = [int(x) for x in params]
    
    if query=='insert':
        li.insert(int(params[0]), int(params[1]))
    
    elif query=='print':
        print(li)
        
    elif query=='remove':
        li.remove(int(params[0]))
        
    elif query=='append':
        li.append(int(params[0]))
        
    elif query=='sort':
        li.sort()
        
    elif query=='pop':
        li.pop()
        
    elif query=='reverse':
        li.reverse()