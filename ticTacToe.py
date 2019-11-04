# printing "X" and "O"
def printxo(list1,list2,list3,count):
    x = int(input("give the number corresponding to the position of your marking"))
    count+=1
    x = x-1
    if x >=0 and x <=2:
        if count%2 ==0:
            list3[x] = "X"
        else:
            list3[x] = "O"
    elif x >=3 and x <=5:
        if count%2 ==0:
            list2[x-3] = "X"
        else:
            list2[x-3] = "O"
    else:
        if count%2 ==0:
            list1[x-6] = "X"
        else:
            list1[x-6] = "O"
    matrix = [list1,list2,list3]
    for n in range(3):
        print('|'.join(matrix[n]))
        print("-"*5)
    checkForWinners(list1,list2,list3,count)
    printxo(list1,list2,list3,count)
def resetGame():
    list1 = [" "," "," "]
    list2 = [" "," "," "]
    list3 = [" "," "," "]
    x = int(input("give the number corresponding to the position of your marking"))
    x = x - 1
    count = 0
    if x >=0 and x <=2:
        if count%2 ==0 :
            list3[x] = "X"
        else:
            list3[x] = "O"
    elif x >=3 and x <=5:
        if count%2 ==0:
            list2[x-3] = "X"
        else:
            list2[x-3] = "O"
    else:
        if count%2 ==0:
            list1[x-6] = "X"
        else:
            list1[x-6] = "O"
    matrix = [list1,list2,list3]
    for n in range(3):
        print("|".join(matrix[n]))
        print("-"*5)
    checkForWinners(list1,list2,list3,count)
    printxo(list1,list2,list3,count)
def checkForWinners(list1,list2,list3,count):
    a = ["X","X","X"]
    matrix = [list1,list2,list3]
    b = ["O","O","O"]
    if a in matrix or b in matrix:
        if count % 2 == 0:
            print("player X has won")
        else:
            print("player O has won")
        exit(0)
    for n in range(3):
        if list1[n] == list2[n] and list2[n] == list3[n]:
            if list1[n] == "X" or list1[n] == "O":
                if count % 2 == 0:
                    print("player X has won")
                else:
                    print("player O has won")
                exit(0)
    if list1[0] == list2[1] and list2[1] == list3[2]:
        if list1[0] == "X" or list1[0] == "O":
            if count % 2 == 0:
                print("player X has won")
            else:
                print("player O has won")
            exit(0)
    if list1[2] == list2[1] and list2[1] == list3[0]:
        if list1[2] == "X" or list1[2] == "O":
            if count % 2 == 0:
                print("player X has won")
            else:
                print("player O has won")
            exit(0)
resetGame()