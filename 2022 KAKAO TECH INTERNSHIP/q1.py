def solution(survey, choices):
    score = {i : 0 for i in ["R","C","J","A"]}
    ans =""
    for i,string in enumerate(survey):
        if string[1] == "T":
            score["R"] -= (choices[i]-4)
        elif string[1] == "F":
            score["C"] -= (choices[i]-4)
        elif string[1] == "M":
            score["J"] -= (choices[i]-4)
        elif string[1] == "N":
            score["A"] -= (choices[i]-4)
        else:
            score[string[1]] += (choices[i]-4)
    for i in ["R","C","J","A"]:
        if score[i]>=0:
            ans += i
        elif i=="R":
            ans += "T"
        elif i=="C":
            ans += "F"
        elif i=="J":
            ans += "M"
        else: ans+= "N"

    return ans

print(solution(["AN", "CF", "MJ", "RT", "NA"],[5, 3, 2, 7, 5]))