s = input().upper()
def minion(string):
    vowels = 'AEIOU'
    str_length = len(string)
    kevin_score , stuart_score = 0 , 0

    for i in range(str_length):
        if s[i] in vowels:
            kevin_score += (str_length - i)
        else:
            stuart_score += (str_length - i)

    if kevin_score > stuart_score:
        print("Kevin", kevin_score)
    elif kevin_score < stuart_score:
        print("Stuart", stuart_score)
    else:
        print("Draw")

minion(s)
