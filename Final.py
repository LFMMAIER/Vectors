import math
import python

#Solver funtions

class Vector(x,y,z):

    def __init__(self,x,y,z):
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
        return line(dirVec, point)

#3 Planes

def threePlanes(plane1,plane2,plane3):
