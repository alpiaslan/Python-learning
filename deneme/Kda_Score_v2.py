#İt's about KDA score for games
ar = float(input("Enter your Kill Score:"))
ax = float(input("Enter your Death Score:"))
az = float(input("Enter your Asist score:"))
bx = ar+az
if bx == 0:
    print("You would be better for Team")
else:
    if ax == 0:
        print("Kda:",bx)
    else:
        ac = (float(ar)+float(az))/float(ax)
        if 0<ac<=2.5:
            print("Kda:",ac,"This score is not good")
        if 2.5<ac<4:
            print("Kda:",ac,"This score is normal")
        if 4<=ac:
            print("Kda:",ac,"This Score is awesome")
        if ac==0:
            print("Kda:",ac,"You have to do for win this game")
