import uuid


def setError(sArt, iVon, iBis):
    return {"uuid": uuid.uuid4(), "art": sArt, "von:": iVon, "bis": iBis}


def splitListFrmTo(olist, frm, to):
    return olist[frm:to]


def splitList(olist, to):
    return splitListFrmTo(olist, 0, to)


def main():
    rollLenght = int(input("Rollenlaenge: "))
    rollErrors = []
    roll = [None] * rollLenght
    while input("Neuer Fehler: ") != "nein":
        art = input("Art: ")
        von = input("Von: ")
        bis = input("Bis: ")
        errorObj = setError(art, int(von), int(bis))
        rollErrors.append(errorObj)
        roll[int(von)] = errorObj
        roll[int(bis)] = errorObj
    anfangsAbfall = input("Anfangsabfall: ")
    roll = splitListFrmTo(roll, int(anfangsAbfall), len(roll))
    print(roll)


if __name__ == '__main__':
    main()
