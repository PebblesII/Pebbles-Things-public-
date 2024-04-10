Escolhas = 1

Option = int(input())

while Escolhas <= 20:
    if Option == 1:
        print("{}.Sempre".format(Escolhas, ))
        Escolhas += 1
        Option = int(input())

    if Option == 2:
        print("{}.Frequentemente".format(Escolhas, ))
        Escolhas += 1
        Option = int(input())

    if Option == 3:
        print("{}.De vez em quando".format(Escolhas, ))
        Escolhas += 1
        Option = int(input())

    if Option == 4:
        print("{}.Raramente".format(Escolhas, ))
        Escolhas += 1
        Option = int(input())

    if Option == 5:
        print("{}.Nunca".format(Escolhas))
        Escolhas += 1
        Option = int(input())
