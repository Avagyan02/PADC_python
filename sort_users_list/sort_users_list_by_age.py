import os

class Human:
    def __init__(self, name, surname, age):
        self.name = name
        self.age = age
        self.surname = surname

    def ConcatUserInfo(self):
        return self.name + " " + str(self.age) + " ";

def writeIntoSortedFile(arr):
    sortedUsersList = open("Media/sortedUsersList.txt", "w")

    for i in range(len(arr)):
        userData = " ".join(arr[i].values())
        sortedUsersList.writelines(userData)


def sortUsers(arr):
    sortField = ""
    while True:
        tmpSortField = input("Write the field which will be used for sort users list ").lower()
        if (tmpSortField not in list(arr[0].keys())):
            continue

        sortField = tmpSortField
        break

    sortedUsers = sorted(arr, key=lambda d: d[sortField])
    writeIntoSortedFile(sortedUsers)

def getUsers():
    if not os.path.exists("Media/users.txt"):
        f = open("Media/users.txt", "w")

        for i in range(15):


        # f.writelines("John Doe 30 DevOps\n")
        # f.writelines("Ann Smith 22 HR\n")
        # f.writelines("Susan Kent 26 Designer\n")
        # f.writelines("Adam Smith 20 developer\n")
        # f.close()

    users = open('Media/users.txt', encoding='utf-8')
    sortArr = []
    for row in users:
        tmp = row.split(" ")

        sortArr.append({
            "name": tmp[0],
            "surname": tmp[1],
            "age": tmp[2],
            "profession": tmp[3]
        })

    users.close()
    sortUsers(sortArr)


getUsers()