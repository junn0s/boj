import sys
input = sys.stdin.readline

n = int(input())
book_list = []
book_cnt = dict()

for _ in range(n):
    book_list.append(input().rstrip())
    
book_list.sort()

for book in book_list:
    if book in book_cnt.keys():
        book_cnt[book] += 1
    else:
        book_cnt[book] = 1
        
sorted_books = sorted(book_cnt.items(), key=lambda x:x[1], reverse=True)
print(sorted_books[0][0])