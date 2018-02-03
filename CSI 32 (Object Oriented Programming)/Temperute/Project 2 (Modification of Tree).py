# Tree4.py
# Sabina Akter
# 4/30/2017

from cs1graphics import *
from math import sin, cos, pi
from random import *

# Tree is a recursive class.

class Tree(Drawable):
    def __init__(self, root, length, width, angle,n):
        Drawable.__init__(self)
        if n == 0:  # base case
            self.trunk = None
        else:
            # root and branch are the starting point and ending point of
            # the trunk (the tree before it branches).
            branch = root + length * Point(cos(angle),sin(angle))
            self.trunk = Path(root, branch)
            self.trunk.setBorderWidth(width)

            #recursive calls:
            # at branch, tree splits into 2 smaller trees
            # at angle of pi/6 from the current "trunk"
            # and with shorter length 

            self.left = Tree(branch, length * 0.15 * randint(4,6), width*(cos(pi/6)) , angle - pi/6,n-1)        
            self.right = Tree(branch, length * 0.15 * randint(5,6),width*(cos(pi/6)), angle + pi/6,n-1)
            
            
            

    def _draw(self):
         Drawable._draw(self)
         if self.trunk == None:  # base case
             return
         else:  
             self.trunk._draw()

             #recursive calls
             self.left._draw()
             self.right._draw()
         

if __name__ == "__main__":
    paper = Canvas(600,600,'Light Blue')
    grass = Rectangle(1400,300, Point(450,550))
    grass.setFillColor('Light green')
    paper.add(grass)
    s = Tree(Point(300,500),100,1.3**9, -pi/2, 8)
    paper.add(s)
    


