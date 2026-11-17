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

def locationSorter(sheetLines):
    westRegion = ['WA', 'OR', 'ID', 'WY', 'MT', 'NV', 'UT', 'CO', 'CA', 'AZ', 'NM', 'AK', 'HI']
    midwestRegion = ['ND', 'SD', 'MN', 'IA', 'MO', 'NE', 'KS', 'WI', 'IL', 'IN', 'OH', 'MI']
    northRegion = ['PA', 'NY', 'NJ', 'CT', 'ME', 'MA', 'RI', 'VT', 'NH']
    southRegion = ['DE', 'MD', 'VA', 'WV', 'NC', 'SC', 'GA', 'FL', 'AL', 'TN', 'KY', 'MS', 'LA', 'AR', 'OK', 'TX']
    collegeLst = []
    while True:
        regionGet = input('Please region that you wish to attend college in: ')
        validRegions = ['west', 'midwest', 'northeast', 'south', 'no preference']
        if regionGet.lower() in validRegions:
            break
        else:
            print('Please enter a valid region (West, Midwest, Northeast, South, or No preference:')
    if regionGet.lower() == 'west':
        for college in sheetLines[1:]:
            collegeSplitter = college.split(',')
            if collegeSplitter[1] in westRegion:
                collegeLst.append(collegeSplitter[0])
    elif regionGet.lower() == 'midwest':
         for college in sheetLines[1:]:
            collegeSplitter = college.split(',')
            if collegeSplitter[1] in midwestRegion:
                collegeLst.append(collegeSplitter[0])
    elif regionGet.lower() == 'northeast':
         for college in sheetLines[1:]:
            collegeSplitter = college.split(',')
            if collegeSplitter[1] in northRegion:
                collegeLst.append(collegeSplitter[0])
    elif regionGet.lower() == 'south':
         for college in sheetLines[1:]:
            collegeSplitter = college.split(',')
            if collegeSplitter[1] in southRegion:
                collegeLst.append(collegeSplitter[0])
    else:
        for college in sheetLines[1:]:
            collegeSplitter = college.split(',')
            collegeLst.append(collegeSplitter[0])
    return collegeLst


def calculation(userInfo,data,collegeLst):
    SAT_percentile = 0
    ACT_percentile = 0
    userSAT = userInfo["SAT"]
    userACT = userInfo["ACT"]
    result = []
    score = 0
    for row in data[1:]:
        elements = row.strip().split(",")
        name = elements[0]
        if name not in collegeLst:
            continue
        selectivity = float(elements[2])
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
                    elif userACT >= act_average:
                        ACT_percentile = 50
                    elif userACT >= act_25:
                        ACT_percentile = 25
                    else:
                        ACT_percentile = 1
        if SAT_percentile != 0 and ACT_percentile != 0:
            score = (SAT_percentile+ACT_percentile)/2
        elif SAT_percentile != 0:
            score = SAT_percentile
        else: 
            score = ACT_percentile
        recommendation_score = round(score*0.7 + selectivity*0.3,2)
        result.append([name, recommendation_score])
    return result


def rank(result):
    result.sort(key=lambda info:info[1], reverse=True)
    for school in result:
        chance = float(school[1])
        if chance > 75:
            status = "Safety"
        elif chance > 25:
            status = "Target"
        else:
            status = "Reach"
        school.append(status)
    return result[0:10]

file_name = "D:\\CS 100 Roadmap Project\\data.txt"
inF = open(file_name)
data = inF.readlines()
inF.close()
userInfo = getUserInput()
collegeLst = locationSorter(data)
result = calculation(userInfo, data, collegeLst)
topColleges = rank(result)
print("----- Your top 10 recommend colleges -----")
for i in range(len(topColleges)):
    school = topColleges[i]
    print(f"{i+1}. {school[0]}")
    print(f"   Recommendation Score: {school[1]}")
    print(f"   Category: {school[2]}")
    
        
    


