import random

def getQuestions():
    arr = []
    file = open('Media/questions.txt', encoding='utf-8')

    for row in file:
        arr.append(row.replace('\n', ''))

    return arr

def userIsExist(userName):
    file = open('Media/users.txt', encoding='utf-8')

    for row in file:
        tmp = row.split("=")
        if userName == tmp[0]:
            return True

    return False


def writeUserResult(userName, result):
    arr = []
    userNames = []
    file = open('Media/users.txt', encoding='utf-8')
    for row in file:
        tmp = row.split("=")
        if userName == tmp[0]:
            data = userName + '=' + str(result)
            arr.append(data)
        else:
            arr.append(row)
        userNames.append(tmp[0])

    if userName not in userNames:
        arr.append(userName + "=" + str(result))

    file2 = open('Media/users.txt', 'w', encoding='utf-8')

    for i in range(len(arr)):
        arr[i] = arr[i].replace('\n', '')
        if i == len(arr) - 1:
            file2.write(arr[i])
            continue
        file2.write(arr[i] + '\n')


def userAllowedOneMisstake():
    playerName = ""
    while True:
        user = input("Write your user name... ")
        if userIsExist(user) is True:
            print("User already exist")
            fromZero = input("Do you want to reset your result and start from 0? ")

            if fromZero.lower() == "yes":
                playerName = user
                writeUserResult(user, 0)
                break
            else:
                continue
        else:
            playerName = user
            writeUserResult(user, 0)
            break

    questions = getQuestions()
    game_questions = []

    while len(game_questions) < 10:
        num = random.randint(0, len(questions) - 1)
        if questions[num] not in game_questions:
            game_questions.append(questions[num])

    gquestions = {}
    for el in game_questions:
        q, a = el.split("?")
        gquestions[q] = a.split(",")

    cnt = 0

    variant = ["A", "B", "C", "D"]
    cvariant = ""
    for q, a in gquestions.items():
        correct = a[0]
        random.shuffle(a)
        for i in range(len(variant)):
            print(variant[i], a[i])
            if a[i] == correct:
                cvariant = variant[i]
        answer = input("Your variant: ")
        if answer.upper() == cvariant:
            cnt += 1
            print("Correct.")
        else:
            print("Not. Correct answer was: ", correct)

    writeUserResult(playerName, cnt)
    print("You got %d/10" % cnt)
