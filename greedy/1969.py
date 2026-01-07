# DNA

import sys
input = sys.stdin.readline

n, m = map(int, input().split())
dna = list()
final_dna_result = ''
hamming_distance = 0

for _ in range(n):
    tmp_dna = list(input().rstrip())
    dna.append(tmp_dna)

for i in range(m):
    type = {"A":0, "C":0, "G":0, "T":0}
    for j in range(n):
        type[dna[j][i]] += 1
    max_type = max(type, key=type.get)
    final_dna_result += max_type
    hamming_distance += sum(type.values()) - max(type.values())

print(f"{final_dna_result}\n{hamming_distance}")
    
