from collections import defaultdict
import sys
input = sys.stdin.readline

def combination(arr:dict):
    group_count = defaultdict(int)
    
    for value in arr.values():
        group_count[value] += 1

    result = list(group_count.values())
    case = 1
    
    for item in result:
        case *= item + 1
        
    return case - 1
        

T = int(input().rstrip())
for _ in range(T):
    cloth = dict()
    n = int(input().rstrip())
    for _ in range(n):
        name, group = input().rstrip().split()
        cloth[name] = group
    print(combination(cloth))