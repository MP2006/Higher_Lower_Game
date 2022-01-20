from art import logo, vs

from game_data import data

import random


def startGame():
    startList = []
    first = random.choice(data)
    startList.append(first)
    second = random.choice(data)
    while second == first:
        second = random.choice(data)
    startList.append(second)
    return startList


def compare(dataList):
    resultList = []
    first = dataList[0]
    second = dataList[1]
    firstValue = first["follower_count"]
    secondValue = second["follower_count"]
    if firstValue > secondValue:
        firstValue = True
        secondValue = False
    elif secondValue > firstValue:
        firstValue = False
        secondValue = True
    resultList.append(firstValue)
    resultList.append(secondValue)
    return resultList


def panel(dataList):
    first = dataList[0]
    second = dataList[1]
    name1 = first["name"]
    name2 = second["name"]
    description1 = first["description"]
    description2 = second["description"]
    country1 = first["country"]
    country2 = second["country"]
    print(f"Compare A: {name1}, a {description1}, from {country1}.")
    print(vs)
    print(f"Against B: {name2}, a {description2}, from {country2}.")


def randomList(dataList):
    randomItem = random.choice(data)
    while randomItem == dataList[0]:
        randomItem = random.choice(data)
    dataList.append(randomItem)
    return dataList


def nextLevel(dataList):
    panel(dataList)
    selectionList = ["A", "B"]
    boolList = compare(dataList)
    selection = input("Who had more followers? Type 'A' or 'B': ").upper()
    while selection not in selectionList:
        print("Invalid input, please try again.")
        selection = input("Who has more followers? Type 'A' or 'B': ").upper()
    if selection == "A":
        selection = boolList[0]
    elif selection == "B":
        selection = boolList[1]
    return selection


def showCount(dataList):
    first = dataList[0]
    second = dataList[1]
    firstValue = first["follower_count"]
    secondValue = second["follower_count"]
    name1 = first["name"]
    name2 = second["name"]
    print(f"\n{name1} has {firstValue} millions followers | {name2} has {secondValue} millions followers\n")


def main():
    choice = "y"
    highScore = 0
    while choice == "y":
        print(logo)
        print("Instagram followers (2020 version)\n")
        streak = 0
        dataList = startGame()
        boolList = compare(dataList)
        selection = nextLevel(dataList)
        if not selection:
            print(f"\nSorry, that's wrong. Final score: {streak}")
            showCount(dataList)
        if selection:
            streak += 1
            print(f"\nYou're right! Current score: {streak}")
            showCount(dataList)
            for i in range(len(boolList)):
                if selection == boolList[i]:
                    temp = dataList[i]
                    dataList = [temp]
        while selection:
            dataList = randomList(dataList)
            selection = nextLevel(dataList)
            if not selection:
                print(f"\nSorry, that's wrong. Final score: {streak}")
                showCount(dataList)
            if selection:
                streak += 1
                print(f"\nYou're right! Current score: {streak}")
                showCount(dataList)
                dataList = [dataList[1]]
        if streak > highScore:
            highScore = streak
        print(f"Your high score is: {highScore}")
        choice = input("\nWould you like to play again? (y or n): ")
    print("Thank you for playing!")


main()
