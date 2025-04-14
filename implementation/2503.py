def check_strike_ball(candidate, guess):
    candidate_str = str(candidate)
    guess_str = str(guess)
    
    strike = 0
    ball = 0
    
    for i in range(3):
        if candidate_str[i] == guess_str[i]:
            strike += 1
    
    for i in range(3):
        if guess_str[i] in candidate_str and candidate_str[i] != guess_str[i]:
            ball += 1
    
    return strike, ball


candidates = []
for i in range(1, 10):
    for j in range(1, 10):
        if i == j:
            continue
        for k in range(1, 10):
            if i == k or j == k:
                continue
            number = i * 100 + j * 10 + k
            candidates.append(number)


n = int(input().strip())

for _ in range(n):
    guess, s, b = map(int, input().split())
    
    new_candidates = []
    for candidate in candidates:
        strike, ball = check_strike_ball(candidate, guess)
        if strike == s and ball == b:
            new_candidates.append(candidate)
    
    candidates = new_candidates

print(len(candidates))