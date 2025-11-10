for letter in "eggplant":
    if letter == "p":
        break
    print(letter)


message = input("say hi: ")
while True:
    if message == "hi":
        break
    message = input("Say hi: ")


for letter in "fatcat":
    if letter == "a":
        continue
    print(letter)


for letter in "superstitious":
    if letter in "ueio":
        continue
    print(letter)