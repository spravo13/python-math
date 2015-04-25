"""A python program which solves mainly geometry problems"""

from cmath import pi, sqrt
from time import sleep

def programs():
    """List of programs and their aliases"""

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

def degree2radian():
    """degree to radian"""

    degree = float(input("Enter degrees: "))
    radian = degree*(pi/180)
    radian_pi = degree/180
    print(radian , " or ", radian_pi,"π radians")

def radian2degree():

    """radian to degree"""
    radian = float(input("Enter radians: "))
    degree = radian*(180/pi)
    print(degree , "degrees")

def areacircle():
    """area of circle"""

    radian = float(input("Enter radius: "))
    area = radian*radian*pi
    print("Area is: " , area)

def areatrapezoid():
    """area of trapezoid"""

    height = float(input("Height of trapezoid: "))
    base_1 = float(input('Base one value: '))
    base_2 = float(input('Base two value: '))
    area = ((base_1 + base_2) / 2) * height
    print("Area is:" , area)
	
def areaparallelogram():
    """area of parallelogram"""

    base = float(input('Length of base: '))
    height = float(input('Measurement of height: '))
    area = base * height
    print("Area is: " , area)
	
def areatriangle():
    """area of triangle"""

    base = float(input('Base of triangle: '))
    height = float(input('Height of triangle: '))
    area = 0.5 * base * height
    print("Area is: " , area)

def sacylinder():
    """surface area of cylinder"""

    radian = float(input('Raduis of cylinders faces: '))
    height = float(input('Height of circle: '))
    surface_area = ((2*pi*radian) * height) + ((pi*radian**2)*2)
    print("Surface Area is: " , surface_area)

def volumecylinder():
    """volume of cylinder"""

    height = float(input('Height of cylinder: '))
    radian = float(input('Raduis of cylinder: '))
    volume = pi * radian * radian * height
    print ("Volume is: ", volume)

def sasphere():
    """surface area of sphere"""

    radian = float(input('Raduis of sphere: '))
    surface_area = 4 * pi * radian **2
    print ("Surface Area is: ", surface_area)

def spherevolume():
    """Sphere Volume"""

    radian = float(input('Raduis of sphere: '))
    volume = (4/3) * (pi * radian ** 3)
    print ("Volume is: ", volume)

def circumference():
    """circumference"""

    diameter = float(input('Diameter of circle: '))
    circumference = pi * diameter
    print ("Circumference is: ", circumference)

def arclength():
    """arc length"""

    diameter = float(input('Diameter of circle: '))
    angle = float(input('angle measure: '))
    if angle >= 361:
        print("Angle is not possible")
    return
    arc_length = (pi*diameter) * (angle/360)
    print ("Arc Length is: ", arc_length)

def sectorarea():
    """area of sector"""

    radius = float(input('Radius of Circle: '))
    angle = float(input('angle measure: '))
    if angle >= 361:
        print ("Angle is not possible")
    return
    surface_area = (pi*radius**2) * (area/360)
    print ("Sector Area: ", surface_area)
    
def discriminant():
    """discriminant"""

    a_value = float(input('The A value: '))
    b_value = float(input('The B value: '))
    c_value = float(input('The C value: '))
    discriminant = (b_value**2) - (4*a_value*c_value)
    if discriminant > 0: 
        print ('Two Solutions. Discriminant value is:', discriminant)
    elif discriminant == 0: 
        print ('One Solution. Discriminant value is:', discriminant)
    elif discriminant < 0:
        print ('No Real Solutions. Discriminant value is:', discriminant)

def quadraticformula():
    """quadratic formula"""
    a_value = float(input('The A value: '))
    b_value = float(input('The B value: '))
    c_value = float(input('The C value: '))
    d_value  = (b_value**2) - (4*a_value*c_value)
    d_value = sqrt(d_value)
    qf1 = (-b_value + d_value) / 2 * a_value
    qf2 = (-b_value - d_value) / 2 * a_value
    print ('Solution 1: (%r,0)' % qf1)
    print ('Solution 2: (%r,0)' % qf2)

DEGREE_TO_RADIAN_LS =	['degrees to radians', 'd2r']
RADIAN_TO_DEGREE_LS =	['radians to degrees', 'r2d']
AREA_CIRCLE_LS =	['area of circle', 'circle area', 'aoc', 'ac', 'ca']
AREA_TRAPEZOID_LS =	['area of trapezoid', 'trapezoid area', 'aot', 'at', 'ta']
AREA_PARALLELOGRAM_LS =	['area of parallelogram', 'paralellogram area', 'aop', 'ap', 'pa']
AREA_TRIANGLE_LS =	['area of triangle', 'triangle area', 'atr', 'aotr', 'tar']
SA_CYLINDER_LS =	['sa of cylinder', 'cylinder sa', 'sac', 'saoc', 'csa']
VOLUME_CYLINDER_LS =	['volume of cylinder', 'cylinder volume', 'vc', 'voc', 'cv']
DISCRIMINANT_LS =	['discriminant', 'd']
SA_SPHERE_LS =		['sa of sphere', 'sphere sa', 'sas', 'saos', 'ssa']
VOLUME_SPHERE_LS =	['volume of sphere', 'sphere volume', 'vs', 'vos', 'sv']
QUADRATIC_FORMULA_LS =	['quadratic formula', 'qf']
CIRCUMFERENCE_LS =	['circumference', 'c']
LENGTH_ARC_LS =		['length of arc', 'arc length', 'la', 'loa', 'al']
AREA_SECTOR_LS =	['area of sector', 'sector area', 'as', 'aos', 'sa']
PROGRAM_LS =		['p', 'programs', 'program list', 'list', 'ls']

LIST = False
RUN_AGAIN = 'y'
while RUN_AGAIN in ('y', 'Y'):

    SELECT = input('Select a program: ')

    if    SELECT in AREA_CIRCLE_LS:		areacircle()
    elif  SELECT in DEGREE_TO_RADIAN_LS:	degree2radian()
    elif  SELECT in RADIAN_TO_DEGREE_LS:	radian2degree()
    elif  SELECT in AREA_TRAPEZOID_LS:		areatrapezoid()
    elif  SELECT in AREA_PARALLELOGRAM_LS:	areaparallelogram()
    elif  SELECT in AREA_TRIANGLE_LS:		areatriangle()
    elif  SELECT in SA_CYLINDER_LS:		sacylinder()
    elif  SELECT in VOLUME_CYLINDER_LS:		volumecylinder()
    elif  SELECT in DISCRIMINANT_LS:		discriminant()
    elif  SELECT in SA_SPHERE_LS:		sasphere()
    elif  SELECT in VOLUME_SPHERE_LS:		spherevolume()
    elif  SELECT in QUADRATIC_FORMULA_LS:	quadraticformula()
    elif  SELECT in CIRCUMFERENCE_LS:		circumference()
    elif  SELECT in LENGTH_ARC_LS:		arclength()
    elif  SELECT in AREA_SECTOR_LS:		sectorarea()
    elif  SELECT in PROGRAM_LS:			programs(); LIST = True
    else: print('That is not a program		For Program List Type "p"')
    LIST = True

    sleep(.4)
    if LIST == False:
        print('Do you want to do another calculation?(y/n)')
        RUN_AGAIN = input()

