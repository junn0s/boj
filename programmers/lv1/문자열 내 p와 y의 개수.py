def solution(s:str):
    p = 0
    y = 0
    s = s.lower()
    
    for char in s:
        if char == 'p':
            p += 1
        elif char == 'y':
            y += 1
    
    if p == y:
        return True
    else:
        return False