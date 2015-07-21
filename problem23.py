import EulerTools

upperBound = 28123 
possible = [False]*upperBound 

abundant = []
for i in range(12,l):
  if EulerTools.sumDivisors(i) > i:
    abundant.append(i)

for i in range(len(abundant)):
  for j in range(i,len(abundant)):
    if abundant[i] + abundant[j] < upperBound:
      possible[abundant[i] + abundant[j]] = True 

print(sum([i for i in range(len(possible)) if not(possible[i])]))