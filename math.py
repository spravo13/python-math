#!usr/bin/env python

from cmath import pi, sqrt
from time import sleep

def programs():
	print ("\n area of circle			('area of circle','circle area', 'aoc', 'ac', 'ca')\
		\n area of trapezoid		('area of trapezoid', 'trapezoid area', 'aot', 'at', 'ta')\
		\n area of parallelogram		('area of parallelogram', 'paralellogram area', 'aop', 'ap', 'pa')\
		\n area of triangle		('area of triangle', 'triangle area', 'atr', 'aotr', 'tar')\
		\n SA of cylinder			('sa of cylinder', 'cylinder sa', 'sac', 'saoc', 'csa')\
		\n volume of cylinder		('volume of cylinder', 'cylinder volume', 'vc', 'voc', 'cv')\
		\n SA of sphere			('sa of sphere', 'sphere sa', 'sas', 'saos', 'ssa')\
		\n circumference			('circumference', 'c')\
		\n length of arc			('length of arc', 'arc length', 'la', 'loa', 'al')\
		\n area of sector			('area of sector', 'sector area', 'as', 'aos', 'sa')\
		\n volume of sphere		('volume of sphere', 'sphere volume', 'vs', 'vos', 'sv')\
		\n discriminant			('discriminant', 'd')\
		\n quadratic formula		('quadratic formula', 'qf')\
		\n degrees to radians		('degrees to radians', 'd2r')\
		\n radians to degrees		('radians to degrees', 'r2d')\
		\n")

def degree2radian():						#degree to radian conversion
	d = float(input("Enter degrees: "))
	r = d*(pi/180)
	rpi = d/180
	print(r , " or ",rpi,"π radians")

def radian2degree():						#radian to degree
	r = float(input("Enter radians: "))
	d = r*(180/pi)
	print(d , "degrees")

def areaCircle():							#Area of Circle
	r = float(input("Enter radius: "))
	a = r*r*pi
	print("Area is: " , a)

def areaTrapezoid():						#Area of trapezoid    
	h = float(input("Height of trapezoid: "))
	b1 = float(input('Base one value: '))
	b2 = float(input('Base two value: '))
	a = ((b1 + b2) / 2) * h
	print("Area is:" , a)
	
def areaParallelogram():					#Area of Parallelogram	
	b = float(input('Length of base: '))
	h = float(input('Measurement of height: '))
	a = b * h
	print("Area is: " , a)
	
def areaTriangle():							#Area of Triangle
	b = float(input('Base of triangle: '))
	h = float(input('Height of triangle: '))
	a = 0.5 * b * h
	print("Area is: " , a)

def sacylinder():							#Surface Area of Cylinder
	r = float(input('Raduis of cylinders faces: '))
	h = float(input('Height of circle: '))
	sa = ((2*pi*r) * h) + ((pi*r**2)*2)
	print("Surface Area is: " , sa)

def volumeCylinder():						#Volume of cylinder
	h = float(input('Height of cylinder: '))
	r = float(input('Raduis of cylinder: '))
	v = pi * r * r * h
	print ("Volume is: ", v)

def SAsphere():								#Surface area of sphere
	r = float(input('Raduis of sphere: '))
	sa = 4 * pi * r **2
	print ("Surface Area is: ", sa)

def sphereVolume():							#Sphere Volume 
	r = float(input('Raduis of sphere: '))
	v = (4/3) * (pi * r ** 3)
	print ("Volume is: ", v)

def circumference():						#Circumference 
	d = float(input('Diameter of circle: '))
	c = pi * d
	print ("Circumference is: ", c)

def arclength():							#Arc Length
	d = float(input('Diameter of circle: '))
	a = float(input('angle measure: '))
	if a >= 361:
		print("Angle is not possible")
	return
	l = (pi*d) * (a/360)
	print ("Arc Length is: ", l)

def sectorarea():							#Area of Sector
	r = float(input('Radius of Circle: '))
	a = float(input('angle measure: '))
	if a >= 361:
		print ("Angle is not possible")
	return
	sa = (pi*r**2) * (a/360)
	print ("Sector Area: ", sa)
    
def discriminant():							#Discriminant
	a = float(input('The A value: '))
	b = float(input('The B value: '))
	c = float(input('The C value: '))
	d = (b**2) - (4*a*c)
	if d > 0: 
		print ('Two Solutions. Discriminant value is:', d)
	elif d == 0: 
		print ('One Solution. Discriminant value is:', d)
	elif d < 0:
		print ('No Real Solutions. Discriminant value is:', d)

def quadraticFormula():						#Quadratic Formula
	a = float(input('The A value: '))
	b = float(input('The B value: '))
	c = float(input('The C value: '))
	d  = (b**2) - (4*a*c)
	d = sqrt(d)
	qf1 = (-b + d) / 2 * a
	qf2 = (-b - d) / 2 * a
	print ('Solution 1: (%r,0)' % qf1)
	print ('Solution 2: (%r,0)' % qf2)

degree2radianls =      ['degrees to radians', 'd2r']
radian2degreels =      ['radians to degrees', 'r2d']
areaCirclels =         ['area of circle', 'circle area', 'aoc', 'ac', 'ca']
areaTrapezoidls =      ['area of trapezoid', 'trapezoid area', 'aot', 'at', 'ta']
areaParallelogramls =  ['area of parallelogram', 'paralellogram area', 'aop', 'ap', 'pa']
areaTrianglels =       ['area of triangle', 'triangle area', 'atr', 'aotr', 'tar']
saCylinderls =         ['sa of cylinder', 'cylinder sa', 'sac', 'saoc', 'csa']
volumeCylinderls =     ['volume of cylinder', 'cylinder volume', 'vc', 'voc', 'cv']
discriminantls =       ['discriminant', 'd']
saSpherels =           ['sa of sphere', 'sphere sa', 'sas', 'saos', 'ssa']
volumeSpherels =       ['volume of sphere', 'sphere volume', 'vs', 'vos', 'sv']
quadraticFormulals =   ['quadratic formula', 'qf']
circumferencels =      ['circumference', 'c']
lengthArcls =          ['length of arc', 'arc length', 'la', 'loa', 'al']
sectorAreals =         ['area of sector', 'sector area', 'as', 'aos', 'sa']
plist =                ['p', 'programs', 'program list', 'list', 'ls']

programsls = False
runAgain = 'y'
while runAgain in ('y', 'Y'):

	select = input('Select a program: ')

	if    select in areaCirclels:			areaCircle()
	elif  select in degree2radianls:		degree2radian()
	elif  select in radian2degreels:		radian2degree()
	elif  select in areaTrapezoidls:		areaTrapezoid()
	elif  select in areaParallelogramls:	areaParallelogram()
	elif  select in areaTrianglels:			areaTriangle()
	elif  select in saCylinderls:			sacylinder()
	elif  select in volumeCylinderls:		volumeCylinder()
	elif  select in discriminantls:			discriminant()
	elif  select in saSpherels:				SAsphere()
	elif  select in volumeSpherels:			sphereVolume()
	elif  select in quadraticFormulals:		quadraticFormula()
	elif  select in circumferencels:		circumference()
	elif  select in lengthArcls:			arclength()
	elif  select in sectorAreals:			sectorarea()
	elif  select in plist:					programs(); programsls = True
	else: print('That is not a program		For Program List Type "p"')
	programsls = True

	sleep(.4)
	if programsls == False:
		print('Do you want to do another calculation?(y/n)')
		runAgain = input()

