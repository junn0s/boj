a = input()
b = input()
c = input()

arr = []
arr.append(a[0])
arr.append(b[0])
arr.append(c[0])
Global = ['l', 'k', 'p']
arr = set(arr)
Global = set(Global)

if arr == Global:
    print("GLOBAL")
else:
    print("PONIX")

