maximum = 1000
getallen = set(range(1, maximum + 1))
deelbaar_door_3 = {getal for getal in getallen if not getal % 3}
deelbaar_door_7 = {getal for getal in getallen if not getal % 7}
deelbaar_door_11 = {getal for getal in getallen if not getal % 11}

A = deelbaar_door_3 & deelbaar_door_7 & deelbaar_door_11
B = (deelbaar_door_3 & deelbaar_door_7) - deelbaar_door_11
C = getallen - deelbaar_door_3 - deelbaar_door_7 - deelbaar_door_11
