import csv

# use the command 'wc' to figure out how many lines there are in the file.
# command: wc -l data/usa_housing.csv
# Answer: 10001

# use the command 'head' to figure out the headers of the file is
# command: head -n 1 data/usa_housing.csv

# Answer: Avg. Area Income,Avg. Area House Age,Avg. Area Number of Rooms,Avg.
# Area Number of Bedrooms,Area Population,Price,Address

# use the command 'grep' to figure out how many times the initials
# for the state 'CA' occurs in the document.

# command: cat data/usa_housing.csv | grep -c 'usa'
# Answer: 32

# Use either a pandas dataframe or pure python to parse the 'Address' field
# and add the column 'zipcode' to the dataset. If there is no zipcode given , give in none.

statesAvgIncomeDict = {}
statesWithZip = []
with open('data/usa_housing.csv', encoding="utf-8") as housingFile:
    reader = csv.DictReader(housingFile)
    for row in reader:
        # print(row)
        zip_code = row['Address'].split()[-1]
        state_abbr = row['Address'].split()[-2]
        avg_income = round(float(row['Avg. Area Income']), 2)
        row['Zipcode'] = zip_code
        if state_abbr not in statesAvgIncomeDict:
            statesAvgIncomeDict[state_abbr] = [avg_income, 1]
        else:
            statesAvgIncomeDict[state_abbr][0] += avg_income
            statesAvgIncomeDict[state_abbr][1] += 1
        statesWithZip.append(row)

fieldnames = statesWithZip[0].keys()
with open('data/new_usa_housing.csv', 'w', newline='', encoding="utf-8") as new_usa_housing:
    writer = csv.DictWriter(new_usa_housing, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(statesWithZip)

# Use either a pandas dataframe or pure python to figure out the following
# the largest average area income per state (sum the averages of each state together)

stateAndAverageIncome = []
for k, v in statesAvgIncomeDict.items():
    info_to_pass = []
    info_to_pass.append(k)
    info_to_pass.append(round(v[0]/v[1], 2))
    stateAndAverageIncome.append(info_to_pass)
print(stateAndAverageIncome)

highestAvgAndState = [stateAndAverageIncome[0]]
for i in stateAndAverageIncome:
    if i[1] > highestAvgAndState[0][1]:
        highestAvgAndState.clear()
        highestAvgAndState.append(i)
print(highestAvgAndState)