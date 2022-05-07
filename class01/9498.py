score = int(input())
print('A') if score >= 90 else print('B') if score >= 80 and score < 90 else print(
    'C') if score >= 70 and score < 80 else print('D') if score >= 60 and score < 70 else print('F')
