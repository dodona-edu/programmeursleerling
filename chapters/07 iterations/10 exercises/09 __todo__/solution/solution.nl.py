# numerieke score inlezen
numerieke_score = int(input())

# letterscore bepalen
if numerieke_score >= 90:
    letterscore = 'A'
elif numerieke_score >= 80:
    letterscore = 'B'
elif numerieke_score >= 70:
    letterscore = 'C'
elif numerieke_score >= 60:
    letterscore = 'D'
else:
    letterscore = 'F'

# letterscore uitschrijven
print(letterscore)
