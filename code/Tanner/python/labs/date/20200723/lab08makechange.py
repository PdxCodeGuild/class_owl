v = float(input("how much money do you have?: "))

penny = int(v*100)
quarters = penny // 25
penny - (quarters * 25)

print("you have", penny, "pennies")

