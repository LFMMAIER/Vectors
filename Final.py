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
        top = max(abs(self.x),abs(self.y),abs(self.z))
        while top != 1:
            #print (top)
            #print (self.x%top == 0 and self.y%top == 0 and self.z%top == 0)
            if self.x%top == 0 and self.y%top == 0 and self.z%top == 0:
                self.x = self.x//top
                self.y = self.y//top
                self.z = self.z//top
            top -= 1
        if self.x < 0:
            return (-1*self.x,-1*self.y,-1*self.z)
        else:
            return (self.x,self.y,self.z)

#Simple point class for management
class Point():

    def __init__(self,x,y,z):
        self.x = round(x,2)
        self.y = round(y,2)
        self.z = round(z,2)
        self.point = (self.x,self.y,self.z)

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

#Triple Scalar

def tripleScalar(vec1,vec2,vec3):
    return dot(vec1,cross(vec2,vec3))

#2 Planes

def twoPlanes(plane1,plane2):
    if plane1.normal.vec == plane2.normal.vec:
        if plane1.equation() == plane2.equation():
            return (plane1 , '2PlanesAreCoincident')
        else:
            return ('DNE' , '2PlanesAreParrallel')
    else:
        dirVec = cross(plane1.normal,plane2.normal)

        if plane1.x != 0 and plane2.x != 0:
            plane3 = Plane(plane1.x*plane2.x - plane2.x*plane1.x, plane1.y*plane2.x - plane2.y*plane1.x, plane1.z*plane2.x - plane2.z*plane1.x, plane1.D*plane2.x - plane2.D*plane1.x)
            print (plane3.equation())
            pz = 0
            if plane3.y != 0:
                py = round(plane3.D/plane3.y,2)
                px1 = round(((plane1.D - plane1.y*py)/plane1.x),2)
                px2 = round(((plane2.D - plane2.y*py)/plane2.x),2)
                print (py,px1,px2)
                if px1 == px2:
                    return (Line((px1,py,pz), (dirVec.x,dirVec.y,dirVec.z), '3d'), '2PlanesIntersectAtALine')
                #else:
                    #raise Exception('Something in the intersection of two planes broke...')

        if plane1.y != 0 and plane2.y != 0:
            plane3 = Plane(plane1.x*plane2.y - plane2.x*plane1.y, plane1.y*plane2.y - plane2.y*plane1.y, plane1.z*plane2.y - plane2.z*plane1.y, plane1.D*plane2.y - plane2.D*plane1.y)
            pz = 0
            if plane3.x != 0:
                px = round(plane3.D/plane3.x,2)
                py1 = round(((plane1.D - plane1.x*px)/plane1.y),2)
                py2 = round(((plane2.D - plane2.x*px)/plane2.y),2)
                if py1 == py2:
                    return (Line((px,py1,pz), (dirVec.x,dirVec.y,dirVec.z), '3d'), '2PlanesIntersectAtALine')
                #else:
                    #raise Exception('Something in the intersection of two planes broke...')

        if plane1.z != 0 and plane2.z != 0:
            plane3 = Plane(plane1.x*plane2.z - plane2.x*plane1.z, plane1.y*plane2.z - plane2.y*plane1.z, plane1.z*plane2.z - plane2.z*plane1.z, plane1.D*plane2.z - plane2.D*plane1.z)
            py = 0
            if plane3.x != 0:
                px = round(plane3.D/plane3.x,2)
                pz1 = round(((plane1.D - plane1.x*px)/plane1.z),2)
                pz2 = round(((plane2.D - plane2.x*px)/plane2.z),2)
                if pz1 == pz2:
                    return (Line((px,py,pz1), (dirVec.x,dirVec.y,dirVec.z), '3d'), '2PlanesIntersectAtALine')
                #else:
        raise Exception('Something in the intersection of two planes broke...')


#3 Planes

def threePlanes(plane1,plane2,plane3):
    ans = None

    #If the planes are coincident
    if plane1.equation() == plane2.equation() and plane1.equation() == plane3.equation():
        return (plane1, '3PlanesCoincident')

    #If two planes are coicident and possibly intersect a third
    if type(twoPlanes(plane1,plane2)[0]) == Plane:
        ans = twoPlanes(twoPlanes(plane1,plane2)[0],plane3)[0]
    elif type(twoPlanes(plane3,plane2)[0]) == Plane:
        ans = twoPlanes(twoPlanes(plane3,plane2)[0],plane1)[0]
    elif type(twoPlanes(plane1,plane3)[0]) == Plane:
        ans = twoPlanes(twoPlanes(plane1,plane3)[0],plane2)[0]

    if type(ans) == str:
        return ('DNE', '2PlanesCoincidentAnd1Parallel')
    elif type(ans) == Line:
        return (ans, '2PlanesAreCoincidentAndIntersectAThirdPlane')

    #If the 3 planes are parrallel
    if plane1.normal.vec == plane2.normal.vec and plane1.normal.vec == plane3.normal.vec:
        return ('DNE', '3PlanesParallel')

    #If two Planes intersect at a line
    if type(twoPlanes(plane1,plane2)[0]) == Line:
        ans = linePlane(twoPlanes(plane1,plane2)[0],plane3)[0]
    elif type(twoPlanes(plane2,plane3)[0]) == Line:
        ans = linePlane(twoPlanes(plane2,plane3)[0],plane1)[0]
    elif type(twoPlanes(plane1,plane3)[0]) == Line:
        ans = linePlane(twoPlanes(plane1,plane3)[0],plane2)[0]
    print (ans)
    #If the 3 planes intersect at a line
    if type(ans) == Line:
        return (ans, '3PlanesIntersectAtALine')
    #If the 3 planes intersect at a point
    elif type(ans) == Point:
        return (ans, '3PlanesIntersectAtAPoint')
    #If the 2 planes are parlle and intersect the third
    else:
        #If the 3 planes form a triangular prism
        if tripleScalar(plane1.normal,plane2.normal,plane3.normal) == 0:
            return ('DNE', '3PlanesIntersectandMakeAPrisim')
        #If two planes are parrallel and intersect the third
        else:
            return ('DNE', '2PlanesThatAreParallelAndIntersectAThirdPlane')

# Plane and a line

def linePlane(line1,plane1):
    if dot(line1.dirVector, plane1.normal) == 0:
        if isPointPlane(line1.point,plane1):
            return (line1, 'LineLiesOnThePlane')
        else:
            return ('DNE', 'LineParrallelToPlane')
    else:
        ls = -(plane1.x* line1.point.x + plane1.y* line1.point.y + plane1.z* line1.point.z) + plane1.D
        rs = plane1.x* line1.dirVector.x + plane1.y* line1.dirVector.y + plane1.z* line1.dirVector.z
        s = ls/rs
        return (Point(line1.point.x + s*line1.dirVector.x,line1.point.y + s*line1.dirVector.y,line1.point.z + s*line1.dirVector.z), 'LineIntersectionWithAPlane')


# If a point is on a plane
def isPointPlane(point1,plane1):
    if plane1.normal.x * point1.x + plane1.normal.y * point1.y + plane1.normal.z * point1.z == plane1.D:
        return True
    else:
        return False

# 2d lines intersection

def twoDline(line1,line2):
    s = None

    #If two lines have the same direction vector
    if line1.dirVector.vec == line2.dirVector.vec:
        s = (line1.point.x-line2.point.x)/line1.dirVector.x
        if line2.point.y + s == line1.point.y:
            return (line1, 'LinesAreCoincidentR2')
        else:
            return ('DNE', 'LinesAreParallelR2')

    #Which point they intersect at
    ls = line1.dirVector.y - (line1.dirVector.x/line2.dirVector.x)*line2.dirVector.y
    rs = ((line1.point.x - line2.point.x)/line2.dirVector.x) * line2.dirVector.y + line2.point.y - line1.point.y
    s = rs/ls
    return (Point(line1.point.x + s*line1.dirVector.x, line1.point.y + s*line1.dirVector.y,0),'LinesInterscetAtAPointR2')

# 3d lines intersection

def threeDline(line1,line2):
    s = None
    d = None

    #If two lines have the same direction vector
    if line1.dirVector.vec == line2.dirVector.vec:
        s = (line1.point.x-line2.point.x)/line1.dirVector.x
        if line2.point.y + s == line1.point.y:
            return (line1, 'LinesAreCoincidentR3')
        else:
            return ('DNE', 'LinesAreParallelR3')

    #Which point they intersect at or if they are skew
    ls = line1.dirVector.y - (line1.dirVector.x/line2.dirVector.x)*line2.dirVector.y
    rs = ((line1.point.x - line2.point.x)/line2.dirVector.x) * line2.dirVector.y + line2.point.y - line1.point.y
    s = rs/ls
    d = (line1.dirVector.x*s + line1.point.x - line2.point.x)/line2.dirVector.x
    if math.isclose(line1.point.z + s*line1.dirVector.z, line2.point.z + d*line2.dirVector.z):
        return (Point(line1.point.x + s*line1.dirVector.x, line1.point.y + s*line1.dirVector.y, line1.point.z + s*line1.dirVector.z), 'LiesInterscetAtAPointR3')
    else:
        return ('DNE', 'LinesAreSkewedR3')


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
                c = '='+str(self.point.x*self.normal.x + self.point.y*self.normal.y)
                #if staments to format equaitons
                eqx = str(self.normal.x)+'x'
                eqy = '+'+str(self.normal.y)+'y'
                if self.normal.x == 1 or self.normal.x == -1:
                    if self.normal.y < 0:
                        eqx = '-x'
                    else:
                        eqx = 'x'
                if self.normal.y < 0:
                    eqy = ' - '+str(abs(self.normal.y))+'y'
                if self.normal.y == 1 or self.normal.y == -1:
                    if self.normal.y < 0:
                        eqy = '-y'
                    else:
                        eqy = '+y'
                return eqx+eqy+c
        if self.space == '3d':
            if typee == 'Vector':
                return '(x,y,z) = '+str(self.point.point)+' + t'+str(self.dirVector.vec)
            elif typee == 'Parametic':
                return str(self.point.x)+' + '+str(self.dirVector.x)+'t',str(self.point.y)+' + '+str(self.dirVector.y)+'t',str(self.point.z)+' + '+str(self.dirVector.z)+'t'
            elif typee == 'Sclar':
                return 'does not Exist'

#class for specialty lines
class straightLine():
    #xory is a variable it tell the class if it is a horazantial or vertical line
    # either 'x' or 'y'
    def __init__(self,value,xory):
        self.value = value
        self.xory = xory
        self.space = '2d'

    def equation(self):
        if self.xory == 'x':
            return 'x = '+str(self.value)
        if self.xory == 'y':
            return 'y = '+str(self.value)

class Plane():

    #Define a plane using its cartisian equation
    def __init__(self,x,y,z,D):

        self.x,self.y,self.z,self.D = Plane.Planereduce(x,y,z,D)
        self.normal = Vector(x,y,z)

    def __str__(self):
        return self.equation()
    #Reduces The Plane coeffients
    @staticmethod
    def Planereduce(x,y,z,D):
        top = max(abs(x),abs(y),abs(z),abs(D))
        while top >= 1:
            #print (top)
            #print (self.x%top == 0 and self.y%top == 0 and self.z%top == 0)
            if x%top == 0 and y%top == 0 and z%top == 0 and D%top == 0:
                x = x//top
                y = y//top
                z = z//top
                D = D//top
            top -= 1
        return (x,y,z,D)

##        self.point = Point(point[0],point[1],point[2])
##        self.dirVector1 = Vector(dirVector1[0],dirVector1[1],dirVector1[2])
##        self.dirVector2 = Vector(dirVector2[0],dirVector2[1],dirVector2[2])
##        self.c = (point[0]*self.normal.x + point[1]*self.normal.y + point[2]*self.normal.z)

    def equation(self):
        #algorim to dispaly the equations properly wiht coffients of 1 as x,y,z and replaceing '+' with '-' when a coeffecnt is negitive
        eqD = ' = '+str(self.D)
        eqx = str(self.x)+'x'
        eqy = ' + '+str(self.y)+'y'
        eqz = ' + '+str(self.z)+'z'
        if self.x == 1 or self.x == -1:
            if self.normal.x < 0:
                eqx = '-x'
            else:
                eqx = 'x'
        if self.y < 0:
            eqy = ' - '+str(abs(self.y))+'y'
        if self.y == 1 or self.y == -1:
            if self.y < 0:
                eqy = ' - y'
            else:
                eqy = ' + y'
        if self.z < 0:
            eqz = ' - '+str(abs(self.z))+'z'
        if self.z == 1 or self.z == -1:
            if self.z < 0:
                eqz = ' - z'
            else:
                eqz = ' + z'
        return eqx+eqy+eqz+eqD

#creates a picture box class that displays differnd types of interctions With static Atributes

class vectordiagram():

    def __init__(self,cords):
        self.rect = (cords[0],cords[1],575,450)

    @staticmethod
    def drawrect(surface,rect):
        pygame.draw.rect(surface,(0,0,0),rect, 2)


    #Types of Outcomes
    #lines in R2
    # 'LinesInterscetAtAPointR2'
    # 'LinesAreCoincidentR2'
    # 'LinesAreParallelR2'
    #lines in R3
    # 'LinesInterscetAtAPointR3'
    # 'LinesAreCoincidentR3'
    # 'LinesAreParallelR3'
    # 'LinesAreSkewedR3'
    #Lines And Planes in R3
    # 'LineIntersectionWithAPlane'
    # 'LineLiesOnThePlane'
    # 'LineParrallelToPlane'
    #2 Planes
    # '2PlanesAreCoincident'
    # '2PlanesAreParrallel'
    # '2PlanesIntersectAtALine'
    #3 Planes
    # '2PlanesAreCoincidentAndIntersectAThirdPlane'
    # '2PlanesCoincidentAnd1Parallel'
    # '2PlanesThatAreParallelAndIntersectAThirdPlane'
    # '3PlanesCoincident'
    # '3PlanesIntersectandMakeAPrisim'
    # '3PlanesIntersectAtALine'
    # '3PlanesIntersectAtAPoint'
    # '3PlanesParallel'

    def display(self,surface,type):

        if type == None:
            vectordiagram.drawrect(surface,self.rect)
        else:
            vectordiagram.drawrect(surface,self.rect)
            diagram = pygame.image.load(type +'.png')
            #Centering the image
            offset = ((self.rect[2]-diagram.get_width())/2,(self.rect[3]-diagram.get_height())/2)
            surface.blit(diagram, (self.rect[0]+offset[0], self.rect[1]+offset[1]))



#p = Line((-3,1,4),(-1,1,4),'3d')
#k = Line((1,4,6),(-6,-1,6),'3d')

#print(threeDline(p,k))


#p = Point(1,2,3)
#pi = Plane(4,2,-1,8)
#l = Line((3,1,2),(1,-4,-8),'3d')

#print(pi.equation())
#print(isPointPlane(p,pi))
#print(linePlane(l,pi))


#pi1 = Plane(1,2,3,1)
#pi2 = Plane(1,5,-2,-1)
#pi3 = Plane(0,2,1,-2)

#print(threePlanes(pi1,pi2,pi3))
print(twoPlanes(Plane(6,1,0,6),Plane(1,2,5,7)))
