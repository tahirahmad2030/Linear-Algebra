import numpy as np
import math
class Vector(object):
    def __init__(self, coordinates):
        try:
            if not coordinates:
                raise ValueError
            self.coordinates = tuple(coordinates)
            self.dimension = len(coordinates)

        except ValueError:
            raise ValueError('The coordinates must be nonempty')

        except TypeError:
            raise TypeError('The coordinates must be an iterable')


    def __str__(self):
        return 'Vector: {}'.format(self.coordinates)


    def __eq__(self, v):
        return self.coordinates == v.coordinates


    def subtract(self,v2):
        return list(np.array(self.coordinates) - np.array(v2))    
    

    def add(self,v2):
        return list(np.array(self.coordinates) + np.array(v2)) 

    def scalerMultiplication(self,v2):
        return list(np.array(self.coordinates)*(np.array(v2))) 

    def magnitude(self):
        total=0
        for coordinate in self.coordinates:
            total=total + coordinate**2
        return math.sqrt(total)
    
    def normalise(self):
        magnitide=self.magnitude()
        t=[]
        for i in self.coordinates:
            t.append((1/magnitide)*i)
        return t
      
    def dotproduct(self,v2):
        import itertools
        dotpro=0
        for x,y in zip(self.coordinates,v2.coordinates):
            dotpro = dotpro + (x*y)
        return dotpro
    
    def rad(self,v2):
        dotpro=self.dotproduct(v2)
        magnitude1 = self.magnitude()
        magnitude2 = v2.magnitude()
        v= dotpro/(magnitude1*magnitude2)
        return math.acos(v)
    
    def degree(self,v2):
        radian = self.rad(v2)
        print radian
        degree = (180/math.pi)*radian
        return degree
    
    def checkparallel(self,v2):
        epsilon = -1.e-15
        q=v2.coordinates[0]/self.coordinates[0]
        print q
        for x,y in zip(self.coordinates,v2.coordinates):
            qq=y/x
            print qq
            if qq != q:
               return "Not Parallel"
        return "Parallel"     
    
    def checkorthogonal(self,v2):
        epsilon = 1.e-10
        print self.dotproduct(v2)
        if abs(self.dotproduct(v2)) < epsilon:
           return "Orthogonal"
        else:  
           return "Not Orthogonal"
        
    def projection(self,b):
        dotpro = self.dotproduct(b)
        magnitude= b.magnitude()
        scalar = dotpro/(magnitude**2)
         
        return b.scalerMultiplication(scalar)
    
    def perpendiculartobase(self,b):
        projection = self.projection(b)
        print projection
        return self.subtract(projection)
v=Vector([-9.88,-3.264,-8.159])
b=Vector([-2.155,-9.353,-9.473])
print v.perpendiculartobase(b)

