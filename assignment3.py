xy = []

n = int(input("Enter the number of polygon points: "))
points = 0

while points < n:
    new = [float(xx) for xx in (input("Enter x and y value for point %i: " %(points+1))).split()]
    if len(new) == 2:
        xy.append(new)
        points = points+1
    else:
        print("Error, please input only 2 numbers separated by a space")

headers = ["Points", "X", "Y"]
print('\n')
print(*headers, sep='\t')
print("-"*20)

Ax = 0
Sx = 0
Sy = 0
Ix = 0
Iy = 0
Ixy = 0

for ins in range(-1,n-1):
    xi = xy[ins][0]
    xi1 = xy[ins+1][0]
    yi = xy[ins][1]
    yi1 = xy[ins+1][1]

    print (f"{ins+2}\t{xi1:.2f}\t{yi1:.2f}")

    Ax = Ax + ((xi1+xi)*(yi1-yi))/2
    Sx = Sx + ((xi1-xi)*(yi1**2+yi1*yi+yi**2))/(-6)
    Sy = Sy + ((yi1-yi)*(xi1**2+xi*xi1+xi**2))/6
    Ix = Ix + ((xi1-xi)*(yi1**3+yi1**2*yi+yi1*yi**2+yi**3))/(-12)
    Iy = Iy + ((yi1-yi)*(xi1**3+xi1**2*xi+xi1*xi**2+xi**3))/12
    Ixy = Ixy + ((yi1-yi)*(yi1*(3*xi1**2+2*xi1*xi+xi**2)+yi*(3*xi**2+2*xi1*xi+xi1**2)))/(-24)

Xt = Sy/Ax
Yt = Sx/Ax
Ixt = Ix - Yt**2*Ax
Iyt = Iy - Xt**2*Ax
Ixyt = Ixy + Xt*Yt*Ax
print('\n')
print(f"Ax = {Ax:.2f}")
print(f"Sx = {Sx:.2f}")
print(f"Sy = {Sy:.2f}")
print(f"Ix = {Ix:.2f}")
print(f"Iy = {Iy:.2f}")
print(f"Ixy = {Ixy:.2f}")
print(f"Xt = {Xt:.2f}")
print(f"Yt = {Yt:.2f}")
print(f"Ix = {Ixt:.2f}")
print(f"Iy = {Iyt:.2f}")
print(f"Ixyt = {Ixyt:.2f}")