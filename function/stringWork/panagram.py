word="the quick brown fwx jumps ever a lazy dqg"
alph="abcdefghijklmnopqrstuvwxyz"
ispanagram=True
for ch in alph:
    if word.count(ch)==0:
        ispanagram=False
        break
print(ispanagram)