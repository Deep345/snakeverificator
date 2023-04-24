global stor
snake = input("input snake in turn notation:").lower()
direction = 0
coords = [[0,0]]

validity = True

for letter in snake:
    if letter == "r":
        direction +=1
    elif letter == "l":
        direction -=1
    elif letter !="r" and letter != "l" and letter != "s":
        print("MISINPUT")
        validity = False
        break
    
    stor = coords[-1][:]

    if direction % 4 == 0:
        stor[0]+=1
    elif direction % 4 == 2:
        stor[0]-=1
    elif direction % 4 == 1:
        stor [1] += 1
    elif direction % 4 == 3:
        stor [1] -= 1
    
    if stor in coords:
        validity = False
        break
    else:
        coords.append(stor)

if validity == True:
    print("Valid Snake!")
else:
    print("Invalid Snake!")