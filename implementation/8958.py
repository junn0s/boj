count = int(input())

for _ in range(count):
    quiz = input()
    arr = [0] * (len(quiz) + 1)
    for i in range(len(quiz)):
        if quiz[i] == 'O':
            arr[i+1] += arr[i] + 1
        else:
            continue
    print(sum(arr))