import numpy as np
import pandas as pd
import math

name=input("input file name:")
df = pd.read_csv(name,header=None)
print("if you want to calculate the angle, input a; if you want to calculate bond, input b; if you want to calculate dihedral angle, input d!")
tiaojian=input()

if tiaojian == "d":
	print("you can measure the dihedral angle that you want to work!")
	i=33
	while i>=1:
		print("please input the number of the atom1:")
		atom1=input()
		print("please input the number of the atom2:")
		atom2=input()
		print("please input the number of the atom3:")
		atom3=input()
		print("please input the number of the atom4:")
		atom4=input()
		atom1=int(atom1)
		atom2=int(atom2)
		atom3=int(atom3)
		atom4=int(atom4)
		atom_1=atom1-1
		atom_2=atom2-1
		atom_3=atom3-1
		atom_4=atom4-1
		x1=df.loc[atom_1,0]
		y1=df.loc[atom_1,1]
		z1=df.loc[atom_1,2]
#print(x1,y1,z1)
		x2=df.loc[atom_2,0]
		y2=df.loc[atom_2,1]
		z2=df.loc[atom_2,2]
#print(x2,y2,z2)
		x3=df.loc[atom_3,0]
		y3=df.loc[atom_3,1]
		z3=df.loc[atom_3,2]
#print(x3,y3,z3)
		x4=df.loc[atom_4,0]
		y4=df.loc[atom_4,1]
		z4=df.loc[atom_4,2]
#bbs.keinsci.com/thread-12861-1-1.html
#stackoverflow.com/questions/20305272/dihedral-torsion-angle-from-four-points-in-cartesian-coordinates-in-python
		A=np.array([x1,y1,z1])
		B=np.array([x2,y2,z2])
		C=np.array([x3,y3,z3])
		D=np.array([x4,y4,z4])
		f=A-B
		g=B-C
		h=D-C
		a=np.cross(f,g)
		b=np.cross(h,g)
		axb=np.cross(a,b)
		cos=np.dot(a,b)
		sin=np.dot(axb,g)/np.linalg.norm(g)
		r=-np.arctan2(sin,cos)
		dihedral=np.degrees(r)

		print(dihedral)


if tiaojian == "a":
	print("you can measure the angle that you want to work!")
	i=33
	while i>=1:
		print("please input the number of the atom1:")
		atom1=input()
		print("please input the number of the center atom2:")
		atom2=input()
		print("please input the number of the atom3:")
		atom3=input()
		atom1=int(atom1)
		atom2=int(atom2)
		atom3=int(atom3)
		atom_1=atom1-1
		atom_2=atom2-1
		atom_3=atom3-1
		x1=df.loc[atom_1,0]
		y1=df.loc[atom_1,1]
		z1=df.loc[atom_1,2]
#print(x1,y1,z1)
		x2=df.loc[atom_2,0]
		y2=df.loc[atom_2,1]
		z2=df.loc[atom_2,2]	
#print(x2,y2,z2)
		x3=df.loc[atom_3,0]
		y3=df.loc[atom_3,1]
		z3=df.loc[atom_3,2]
#print(x3,y3,z3)
		a=np.sqrt((x2-x1)**2+(y2-y1)**2+(z2-z1)**2)
		b=np.sqrt((x3-x2)**2+(y3-y2)**2+(z3-z2)**2)
		cosin=((x1-x2)*(x3-x2)+(y1-y2)*(y3-y2)+(z1-z2)*(z3-z2))/(a*b)
		#print("the angle is Angle system(角度制) :")
		angle=math.acos(cosin)/3.141592653589793*180
		print(angle)
		fp=open('angle',"a")
		fp.write("The angle ")
		atom1=str(atom1)
		atom2=str(atom2)
		atom3=str(atom3)
		fp.write(atom1)
		fp.write(",")
		fp.write(atom2)
		fp.write(",")
		fp.write(atom3)
		fp.write(": ")
		fp.write(str(angle))
		fp.write("\n")
		fp.close()
	#i=i-1

if tiaojian == "b":
	print("you can measure the length of bond that you want to work!")
	i=33
	while i>=1:
		print("please input the number of the atom1:")
		atom1=input()
		print("please input the number of the atom2:")
		atom2=input()
		atom1=int(atom1)
		atom2=int(atom2)
		atom_1=atom1-1
		atom_2=atom2-1
		x1=df.loc[atom_1,0]
		y1=df.loc[atom_1,1]
		z1=df.loc[atom_1,2]
#print(x1,y1,z1)
		x2=df.loc[atom_2,0]
		y2=df.loc[atom_2,1]
		z2=df.loc[atom_2,2] 
#print(x2,y2,z2)
		l2=(x2-x1)**2+(y2-y1)**2+(z2-z1)**2
		l=np.sqrt(l2)
		print(l)

		fp=open('result',"a")
		fp.write("The length of bond")
		atom1=str(atom1)
		atom2=str(atom2)
		fp.write(atom1)
		fp.write(",")
		fp.write(atom2)
		fp.write(":")
		fp.write(str(l))
		fp.write("\n")
		fp.close()
		i=i-1
