#Geometry Calculator

import math

def Cube(x):
	TotalSurface = x**6
	LateralSurface = x**2
	Volume = x**3
	Diagonal = math.sqrt(3*x)
	Perimeter = 12*x
	print("")
	print("Total Surface = "+str(TotalSurface)+ " cm")
	print("Lateral Surface = "+str(LateralSurface)+ " cm")
	print("Volume = "+str(Volume)+ " cm")
	print("Diagonal = "+str(Diagonal)+ " cm")
	print("Perimeter = "+str(Perimeter)+ " cm")
	
def Cuboid(l,w,h):
	TotalSurface = 2*((l*w)+(l*h)+(w*h))
	LateralSurface = 2*h*(l*w)
	Volume = l*w*h
	Diagonal = math.sqrt((l**2)+(w**2)+(h**2))
	Perimeter = 4*(l+w+h)
	print("")
	print("Total Surface = "+str(TotalSurface)+ " cm")
	print("Lateral Surface = "+str(LateralSurface)+ " cm")
	print("Volume = "+str(Volume)+ " cm")
	print("Diagonal = "+str(Diagonal)+ " cm")
	print("Perimeter = "+str(Perimeter)+ " cm")
	
def Ball(r):
	Volume = 4/3*math.pi*(r**3)
	TotalSurface = 4*math.pi*(r**2)
	print("")
	print("Total Surface = "+str(TotalSurface)+ " cm")
	print("Volume = "+str(Volume)+ " cm")
	
def Pyramid(l,w,h):
	TotalSurface = l*w+(l*(math.sqrt(((w/2)**2)+h**2)))+(w*(math.sqrt(((l/2)**2)+h**2)))
	LateralSurface = (l*(math.sqrt(((w/2)**2)+h**2)))+(w*(math.sqrt(((l/2)**2)+h**2)))
	Volume = l*w*h/3
	BaseArea = l*w
	print("")
	print("Total Surface = "+str(TotalSurface)+ " cm")
	print("Lateral Surface = "+str(LateralSurface)+ " cm")
	print("Volume = "+str(Volume)+ " cm")
	print("BaseArea = "+str(BaseArea)+ " cm")

print("1. Cube")
print("2. Cuboid")
print("3. Ball")
print("4. Pyramid")
print("")
geometry = int(input("Select Geometry Figure (Enter the number): "))

if(geometry==1):
	x=int(input("Enter the length(cm) : "))
	Cube(x)
if(geometry==2):
	l=int(input("Enter the length(cm) : "))
	w=int(input("Enter the width(cm) : "))
	h=int(input("Enter the height(cm) : "))
	Cuboid(l,w,h)
if(geometry==3):
	r=int(input("Enter the radius(cm) : "))
	Ball(r)
else:
	l=int(input("Enter the length(cm) : "))
	w=int(input("Enter the width(cm) : "))
	h=int(input("Enter the height(cm) : "))
	Pyramid(l,w,h)
	

