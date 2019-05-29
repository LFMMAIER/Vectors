import math
import pygame

class Vector:

    def __init__(self,x,y,z):
        self.vec = (x,y,z)
        self.x = x
        self.y = y
        self.z = z

class Point:

    def __init__(self,x,y,z):
        self.point = (x,y,z)
        self.x = x
        self.y = y
        self.z = z

# Cross product function

def cross(vec1,vec2):
    return Vector(vec1.y*vec2.z - vec1.z*vec2.y, vec1.z*vec2.x - vec1.x*vec2.z, vec1.x*vec2.y - vec1.y*vec2.x)

# Dot product

def dot(vec1,vec2):
    return vec1.x*vec2.x + vec1.y*vec2.y + vec1.z*vec2.z
        
    
#2 Planes

def twoPlanes(plane1,plane2):
    if plane1.normal == plane2.normal:
        if plane1.eqn == plane2.eqn:
            return plane1
        else:
            return None
    else:
        #Need calculations here to determine the point and the direction vector
        return line(Vector(dirVec), point)

#3 Planes

#def threePlanes(plane1,plane2,plane3):

# Plane and a line

#def planeLine(line1,plane1):
#    if dot(line1.dirvec, plane1.normal) == 0:
#        if


# If a point is on a plane
def isPointPlane(point1,plane1):
    if plane1.normal.x * point1.x + plane1.normal.y * point1.y + plane1.normal.z * point1.z == plane1.c: 
        return True
    else:
        return False

    
#Equation

class Line():

    #point cords in space (x,y,z) or (x,y)
    #dirVector a given dirction from a point (x,y,z) or (x,y)
    #space either '2d' or '3d'
    def __init__(self,point,dirVector,space):

        self.point = point
        if space == '2d':
            self.dirVector = Vector(dirVector[0],dirVector[1],0)
        else:
            self.dirVector = Vector(dirVector[0],dirVector[1],dirVector[2])
        self.space = space
        self.normal = Line.norm(dirVector,space)

    #retuns the normal vector of the line
    @staticmethod
    def norm(dirVector,space):
        if space == '2d':
            normal = Vector(dirVector[1],dirVector[0],0)
            return normal
        else:
            return 'undefined'
    
    #returns the equation that is wanted
    #
    #type:
    #Vector(shows dirction vector and a point on a line)
    #Parametic(shows direct coralation to the points on the line)
    #Sclar(standard form ONLY IN 2d Space)
    #
    def equation(self,typee):
        if self.space == '2d':
            if typee == 'Vector':
                return '(x,y) = '+str(self.point)+' + t'+str(self.dirVector)
            elif typee == 'Parametic':
                return str(self.point[0])+' + '+str(self.dirVector.x)+'t',str(self.point[1])+' + '+str(self.dirVector.y)+'t'
            elif typee == 'Sclar':
                #print (self.normal)
                c = -1*(self.point[0]*self.normal.x + self.point[1]*self.normal.y)
                return str(self.normal.x)+'x'+' + '+str(self.normal.y)+'y + '+str(c)
        if self.space == '3d':
            if typee == 'Vector':
                return '(x,y,y) = '+str(self.point)+' + t'+str(self.dirVector.vec)
            elif typee == 'Parametic':
                return str(self.point[0])+' + '+str(self.dirVector.x)+'t',str(self.point[1])+' + '+str(self.dirVector.y)+'t',str(self.point[2])+' + '+str(self.dirVector.z)+'t'
            elif typee == 'Sclar':
                return 'does not Exist'

class Plane():
    
    #point cords in space (x,y,z)
    #Two dirVector a given dirction from a point (x,y,z)
    def __init__(self,point,dirVector1,dirVector2):

        self.point = point
        self.dirVector1 = Vector(dirVector1[0],dirVector1[1],dirVector1[2])
        self.dirVector2 = Vector(dirVector2[0],dirVector2[1],dirVector2[2])
        self.normal = cross(self.dirVector1,self.dirVector2)
        self.c = -1*(point[0]*self.normal.x + point[1]*self.normal.y + point[2]*self.normal.z)

    def equation(self,typee):
        if typee == 'Vector':
                return '(x,y) = '+str(self.point)+' + t'+str(self.dirVector1.vec)+' + s'+str(self.dirVector2.vec)
        elif typee == 'Parametic':
                return str(self.point[0])+' + '+str(self.dirVector1.x)+'t'+' + '+str(self.dirVector2.x)+'s',str(self.point[1])+' + '+str(self.dirVector1.y)+'t'+' + '+str(self.dirVector2.y)+'s',str(self.point[2])+' + '+str(self.dirVector1.z)+'t'+' + '+str(self.dirVector2.z)+'s'
        elif typee == 'Catisian':
                #print (self.normal)
                return str(self.normal.x)+'x'+' + '+str(self.normal.y)+'y + '+str(self.normal.z)+'z + '+str(self.c)
       
boi = Plane((2,4,5),(7,-8,1),(2,9,-5))

print (boi.equation('Catisian'))


point = Point(1,2,3)
pi = Plane((3,2,1),(3,2,1),(1,1,1))

print(pi.equation('Catisian'))
print(isPointPlane(point,pi))
