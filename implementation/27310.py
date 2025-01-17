emoji = input()
col = 0
und = 0

for i in emoji:
    if i == ':':
        col += 1
    if i == "_":
        und += 1
        
print(len(emoji) + col + (und*5))