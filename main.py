def getUserInput():
    userInfo = {}
    userInfo["Name"] = input("Please enter your name: ")
    userGPA = float(input("Please enter your high school GPA (0-4): "))
    while userGPA < 0 or userGPA > 4:
        userGPA = float(input("Invalid GPA. Please enter a value from 0 to 4: "))
    userInfo["GPA"] = userGPA 
    scorePref = input("Would you like to enter your SAT score, ACT score, or both?: ")
    if scorePref.upper() == "ACT":
        userInfo["SAT"] = "None"
        userACT = int(input("Please enter your highest ACT score: "))
        while userACT < 1 or userACT > 36:
            userACT = int(input("Invalid score. Please enter a valid ACT score (1-36): "))
        userInfo["ACT"] = userACT
    elif scorePref.upper() == "SAT":
        userInfo["ACT"] = "None"
        userSAT = int(input("Please enter your highest SAT score: "))
        while userSAT > 1600 or userSAT < 0:
            userSAT = int(input("Invalid score. Please enter a valid SAT score (0-1600): "))
        userInfo["SAT"] = userSAT
    elif scorePref.lower() == "both":
        userACT = int(input("Please enter your highest ACT score: "))
        while userACT < 1 or userACT > 36:
            userACT = int(input("Invalid score. Please enter a valid ACT score (1-36): "))
        userInfo["ACT"] = userACT 
        userSAT = int(input("Please enter your highest SAT score: "))
        while userSAT > 1600 or userSAT < 0:
            userSAT = int(input("Invalid score. Please enter a valid SAT score (0-1600): "))
        userInfo["SAT"] = userSAT
    return userInfo

file_name = "D:\\CS 100 Roadmap Project\\data.txt"
inF = open(file_name)
data = inF.readlines()
userInfo = getUserInput()
def calculation(userInfo,data):
    SAT_percentile = 0
    ACT_percentile = 0
    userSAT = userInfo["SAT"]
    userACT = userInfo["ACT"]
    result = []
    score = 0
    for row in data[1:]:
        elements = row.strip().split(",")
        name = elements[0]
        sat_25 = int(elements[3])
        sat_75 = int(elements[4])
        act_25 = int(elements[5])
        act_75 = int(elements[6])
        act_average = int(elements[7])
        sat_average = int(elements[8])
        if userSAT != "None":
            if userSAT >= sat_75:
                SAT_percentile = 75
            elif userSAT >= sat_average:
                SAT_percentile = 50
            elif userSAT >= sat_25:
                SAT_percentile = 25
            else:
                SAT_percentile = 1
        if userACT != "None":
                    if userACT >= act_75:
                        ACT_percentile = 75
                    elif userSAT >= act_average:
                        ACT_percentile = 50
                    elif userSAT >= act_25:
                        ACT_percentile = 25
                    else:
                        ACT_percentile = 1
        if SAT_percentile != 0 and ACT_percentile != 0:
            score = (SAT_percentile+ACT_percentile)/2
        elif SAT_percentile != 0:
            score = SAT_percentile
        else: 
            score = ACT_percentile
        
        result.append([name, score])
    return result
result = calculation(userInfo, data)

def rank(result):
    result.sort(key=lambda info:info[1], reverse=True)
    return result[0:10]

print(rank(result))
    

        
    


