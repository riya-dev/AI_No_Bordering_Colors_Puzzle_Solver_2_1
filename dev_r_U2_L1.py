# Name: Riya Dev
# Period: 7
# Date: 11/8/2020

from tkinter import *
from graphics import *
import random
# final

def check_complete(assignment, vars, adjs):
   # check if assignment is complete or not. Goal_Test 
   ''' your code goes here '''
   #print('check complete vars' , vars)
   #print('assignment', assignment)
   return len(assignment) == len(vars)

def select_unassigned_var(assignment, vars, adjs):
   # Select an unassigned variable - forward checking, MRV, or LCV
   # returns a variable
   ''' your code goes here '''
   # 1. forward checking
   return random.choice([x for x in vars.keys() if x not in assignment]) #forward checking
   # 2. MRV
   # return min([(len(n), x) for x, n in vars.items() if x not in assignment])[1]
   # 3. LCV
   # return min([(sum([1 for a in adjs[x] if a not in assignment]), x) for x in vars if x not in assignment)
   
def isValid(value, var, assignment, variables, adjs):
   # value is consistent with assignment
   # check adjacents to check 'var' is working or not.
   ''' your code goes here '''
   '''print('\nI S   V A L I D')
   print('value', value)
   print('var', var)
   print('variables', variables)
   print('assignment', assignment)
   print('adjs', adjs)'''
   for x in adjs[var]:
      if x in assignment:
         print(x, "\t", assignment, '\t', assignment[x], '\t', value)
         #print(x, assignment[x], value, adjs[var])
         if assignment[x] == value: return False
   return True
      
def backtracking_search(variables, adjs, shapes, frame): 
   return recursive_backtracking({}, variables, adjs, shapes, frame)

def recursive_backtracking(assignment, variables, adjs, shapes, frame):
   # Refer the pseudo code given in class.
   ''' your code goes here '''
   if check_complete(assignment, variables, adjs): return assignment
   var = select_unassigned_var(assignment, variables, adjs)
   for value in variables[var]: #color
      if isValid(value, var, assignment, variables, adjs):
         assignment[var] = value
         draw_shape(shapes[var], frame, value)
         #print('assignment', assignment, '\n variables', variables, '\nadjs', adjs)
         assignmentcopy = assignment
         variablescopy = variables
         result = recursive_backtracking(assignmentcopy, variablescopy, adjs, shapes, frame)
         #print("result", result)
         if result != None: return result
         del assignment[var]
   return None

# return shapes as {region:[points], ...} form
def read_shape(filename):
   infile = open(filename)
   region, points, shapes = "", [], {}
   for line in infile.readlines():
      line = line.strip()
      if line.isalpha():
         if region != "": shapes[region] = points
         region, points = line, []
      else:
         x, y = line.split(" ")
         points.append(Point(int(x), 300-int(y)))
   shapes[region] = points
   return shapes

# fill the shape
def draw_shape(points, frame, color):
   shape = Polygon(points)
   shape.setFill(color)
   shape.setOutline("black")
   shape.draw(frame)
   space = [x for x in range(9999999)] # give some pause
   
def main():
   regions, variables, adjacents  = [], {}, {}
   # Read mcNodes.txt and store all regions in regions list
   ''' your code goes here '''
   nodes = open("mcNodes.txt")
   for n in nodes.readlines():
      regions.append(n.strip())
      adjacents[n.strip()] = []
   #print('regions', regions)
   
   # Fill variables by using regions list -- no additional code for this part
   for r in regions: variables[r] = {'red', 'green', 'blue'}
   #print('variables', variables)

   # Read mcEdges.txt and fill the adjacents. Edges are bi-directional.
   ''' your code goes here '''
   edges = open("mcEdges.txt")
   for e in edges.readlines():
      p1, p2 = e.split()
      adjacents[p1].append(p2)
      adjacents[p2].append(p1)
      
   #print('adjacents', adjacents)

   # Set graphics -- no additional code for this part
   frame = GraphWin('Map', 300, 300)
   frame.setCoords(0, 0, 299, 299)
   shapes = read_shape("mcPoints.txt")
   for s, points in shapes.items():
      draw_shape(points, frame, 'white')
  
   # solve the map coloring problem by using backtracking_search -- no additional code for this part  
   solution = backtracking_search(variables, adjacents, shapes, frame)
   print (solution)
   
   mainloop()

if __name__ == '__main__':
   main()
   
''' Sample output:
{'WA': 'red', 'NT': 'green', 'SA': 'blue', 'Q': 'red', 'NSW': 'green', 'V': 'red', 'T': 'red'}
By using graphics functions, visualize the map.
'''