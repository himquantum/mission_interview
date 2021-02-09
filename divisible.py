for i in range(1, 100):
    if i % 4 == 0:
        if i % 6 == 0:
            print("linkedIn " + str(i))
        else:
            print("Linked" + str(i))
    elif i % 6 == 0:
        print("In" + str(i))