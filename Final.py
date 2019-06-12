import math
import pygame

#Vector class with built in reduction of values
class Vector():

    def __init__(self,x,y,z):
        self.x = x
        self.y = y
        self.z = z
        self.vec = Vector.reduce(self)

    def __str__(self):
        return str(self.vec)

    def reduce(self):
        num = 2
        top = max(abs(self.x),abs(self.y),abs(self.z))
        while num <= top:
            if self.x%num == 0 and self.y%num == 0 and self.z%num == 0:
                self.x = self.x//num
                self.y = self.y//num
                self.z = self.z//num
                return (self.x,self.y,self.z)
            num += 1
        return (self.x,self.y,self.z)

#Simple point class for management
class Point():

    def __init__(self,x,y,z):
        self.point = (x,y,z)
        self.x = x
        self.y = y
        self.z = z

    def __str__(self):
        return str(self.point)

# Cross product

def cross(vec1,vec2):
    if type(vec1) != Vector or type(vec2) != Vector:
        raise Exception('You tried to cross a non vector')
    return Vector(vec1.y*vec2.z - vec1.z*vec2.y, vec1.z*vec2.x - vec1.x*vec2.z, vec1.x*vec2.y - vec1.y*vec2.x)

# Dot product

def dot(vec1,vec2):
    if type(vec1) != Vector or type(vec2) != Vector:
        raise Exception('You tried to dot a non vector')
    return vec1.x*vec2.x + vec1.y*vec2.y + vec1.z*vec2.z    
    
#2 Planes

def twoPlanes(plane1,plane2):
    if plane1.normal == plane2.normal:
        if plane1.equation() == plane2.equation():
            return plane1
        else:
            return None
    else:
##        if plane1.x != 0 and plane2.x != 0:
##            plane3 = Plane(plane1.x*plane2.x - plane2.x*plane1.x, plane1.y*plane2.x - plane2.y*plane1.x, plane1.z*plane2.x - plane2.z*plane1.x, plane1.D*plane2.x - plane2.D*plane1.x)
##            dirz = 1
##            pz = 0
##            diry = -plane3.z/plane3.y
##            py = plane3.D/plane3.y
##            dirx = (-dirz*plane1.z -diry*plane1.y)/plane1.x
##            px = (plane1.D - pz*plane1.z - py*plane1.y)/plane1.x            
##        return Line((px,py,pz),(dirx*plane3.y*plane1.x,diry*plane3.y*plane1.x,dirz*plane3.y*plane1.x),'3d')

    #Solution cross the two normal vectors. Then all I need to figure out is a point.

        dirVec = cross(plane1.normal,plane2.normal)
        
##        if plane1.y != 0 and plane2.y != 0:
##            px = 0
##            pz = (plane2.D - plane2.y*(plane1.D/plane1.y))/(plane2.y*(-plane1.z/plane1.y) + plane2.z)
##            py = (plane1.D - pz)/plane1.y
##        if plane1.z != 0 and plane2.z != 0:
##            px = 0
##            print(plane2.D - plane2.z*(plane1.D/plane1.z))
##            pz = (plane2.D - plane2.z*(plane1.D/plane1.z))/(plane2.z*(-plane1.y/plane1.z) + plane2.y)
##            py = (plane1.D - pz)/plane1.z
##        if plane1.x != 0 and plane2.x != 0:
##            pz = 0
##            py = (plane2.D - plane2.x*(plane1.D/plane1.x))/(plane2.x*(-plane1.y/plane1.x) + plane2.x)
##            px = (plane1.D - py)/plane1.x
##        else:
##            raise Exception('Hey, so something in the finding the line of intersection of two planes messed up')

        if plane1.x != 0 and plane2.x != 0:
            plane3 = Plane(plane1.x*plane2.x - plane2.x*plane1.x, plane1.y*plane2.x - plane2.y*plane1.x, plane1.z*plane2.x - plane2.z*plane1.x, plane1.D*plane2.x - plane2.D*plane1.x)
            pz = 0
            py = plane3.D/plane3.y
            px1 = ((plane1.D - plane1.y*py)/plane1.x)
            px2 = ((plane2.D - plane2.y*py)/plane2.x)
            if px1 == px2:
                print('hi')
                #return Line((px1,py,pz), (dirVec.x,dirVec.y,dirVec.z), '3d')
            else:
                raise Exception('Something in the intersection of two planes broke...')
            
        if plane1.y != 0 and plane2.y != 0:
            plane3 = Plane(plane1.x*plane2.y - plane2.x*plane1.y, plane1.y*plane2.y - plane2.y*plane1.y, plane1.z*plane2.y - plane2.z*plane1.y, plane1.D*plane2.y - plane2.D*plane1.y)
            pz = 0
            px = plane3.D/plane3.x
            py1 = ((plane1.D - plane1.x*px)/plane1.y)
            py2 = ((plane2.D - plane2.x*px)/plane2.y)
            print(py1,py2)
            if py1 == py2:
                print('hi')
                return Line((px,py1,pz), (dirVec.x,dirVec.y,dirVec.z), '3d')
            else:
                raise Exception('Something in the intersection of two planes broke...')

        if plane1.z != 0 and plane2.z != 0:
            plane3 = Plane(plane1.x*plane2.z - plane2.x*plane1.z, plane1.y*plane2.z - plane2.y*plane1.z, plane1.z*plane2.z - plane2.z*plane1.z, plane1.D*plane2.z - plane2.D*plane1.z)
            py = 0
            px = plane3.D/plane3.x
            pz1 = ((plane1.D - plane1.x*px)/plane1.z)
            pz2 = ((plane2.D - plane2.x*px)/plane2.z)
            if pz1 == pz2:
                print('hi')
                return Line((px,py,pz1), (dirVec.x,dirVec.y,dirVec.z), '3d')
            else:
                raise Exception('Something in the intersection of two planes broke...')

#3 Planes

#def threePlanes(plane1,plane2,plane3):

# Plane and a line

def linePlane(line1,plane1):
    if dot(line1.dirVector, plane1.normal) == 0:
        if isPointPlane(line1.point,plane1):
            return line1
        else:
            return None
    else:
        ls = plane1.normal.x* line1.point.x + plane1.normal.y* line1.point.y + plane1.normal.z* line1.point.z
        rs = plane1.normal.x* line1.dirVector.x + plane1.normal.y* line1.dirVector.y + plane1.normal.z* line1.dirVector.z + plane1.D
        s = rs/-ls
        return Point(line1.point.x + s*line1.dirVector.x,line1.point.y + s*line1.dirVector.y,line1.point.z + s*line1.dirVector.z)


# If a point is on a plane
def isPointPlane(point1,plane1):
    if plane1.normal.x * point1.x + plane1.normal.y * point1.y + plane1.normal.z * point1.z == plane1.D: 
        return True
    else:
        return False

    
#Equation

class Line():

    #point cords in space (x,y,z) or (x,y)
    #dirVector a given dirction from a point (x,y,z) or (x,y)
    #space either '2d' or '3d'
    def __init__(self,point,dirVector,space):

        if space == '2d':
            self.point = Point(point[0],point[1],0)
            self.dirVector = Vector(dirVector[0],dirVector[1],0)
        else:
            self.point = Point(point[0],point[1],point[2])
            self.dirVector = Vector(dirVector[0],dirVector[1],dirVector[2])
        self.space = space
        self.normal = Line.norm(dirVector,space)

    def __str__(self):
        return self.equation('Vector')

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
                return '(x,y) = '+str(self.point.point)+' + t'+str(self.dirVector)
            elif typee == 'Parametic':
                return str(self.point.x)+' + '+str(self.dirVector.x)+'t',str(self.point.y)+' + '+str(self.dirVector.y)+'t'
            elif typee == 'Sclar':
                #print (self.normal)
                c = (self.point.x*self.normal.x + self.point.y*self.normal.y)
                return str(self.normal.x)+'x'+' + '+str(self.normal.y)+'y = '+str(c)
        if self.space == '3d':
            if typee == 'Vector':
                return '(x,y,z) = '+str(self.point.point)+' + t'+str(self.dirVector.vec)
            elif typee == 'Parametic':
                return str(self.point.x)+' + '+str(self.dirVector.x)+'t',str(self.point.y)+' + '+str(self.dirVector.y)+'t',str(self.point.z)+' + '+str(self.dirVector.z)+'t'
            elif typee == 'Sclar':
                return 'does not Exist'

class Plane():
    
    #Define a plane using its cartisian equation
    def __init__(self,x,y,z,D):

        self.x = x
        self.y = y
        self.z = z
        self.D = D
        self.normal = Vector(x,y,z)

    def __str__(self):
        return self.equation()

        
##        self.point = Point(point[0],point[1],point[2])
##        self.dirVector1 = Vector(dirVector1[0],dirVector1[1],dirVector1[2])
##        self.dirVector2 = Vector(dirVector2[0],dirVector2[1],dirVector2[2])
##        self.c = (point[0]*self.normal.x + point[1]*self.normal.y + point[2]*self.normal.z)

    def equation(self):
        return str(self.x)+'x'+' + '+str(self.y)+'y + '+str(self.z)+'z = '+str(self.D)


p = Point(1,2,3)
pi = Plane(4,2,-1,8)
l = Line((3,1,2),(1,-4,-8),'3d')

#print(pi.equation())
#print(isPointPlane(p,pi))
#print(linePlane(l,pi))


pi1 = Plane(1,2,1,4)
pi2 = Plane(2,1,-1,5)

print(twoPlanes(pi1,pi2))
