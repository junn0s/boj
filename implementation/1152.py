def count_words(s):
    words = s.split()
    return len(words)

input_string = input().strip()
print(count_words(input_string))
