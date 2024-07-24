names = ["Milo", "Sarah", "Bruno", "Anastasia", "Rosa"]
namesWith = [item for item in names if (len(item)>4)]
namesWith_O = [item for item in names if "o"in item]
print(namesWith_O)