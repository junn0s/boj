import sys
input = sys.stdin.readline


word_list = input().rstrip()
Croatia_list = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']
Croatia_count = 0
count = 0

i = 0
while i < len(word_list):
    temp = word_list[i]
    for j in range(i+1, i+3):
        if j < len(word_list) and word_list[j]:
            temp = temp + word_list[j]
            if temp in Croatia_list:
                Croatia_count += 1
                i = j + 1
                break
    else:
        i += 1
        count += 1
        
        
print(count + Croatia_count)