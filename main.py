weight = input('weight: ')
unit = input("(K)g or (L)bs: ")
if unit.upper() == "K":
    converted = float(weight) / float(0.45)
    print ("Weight in Lbs: " + str(converted))
else:
    converted = float(weight) * float(0.45)
    print ("Weight in Kgs: " + str(converted))