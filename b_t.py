class Node:
   def __init__(self, data):
      self.left = None
      self.right = None
      self.data = data

   def insert(self, data):
# Compare the new value with the parent node
      if self.data:
         if data < self.data:
            if self.left is None:
               self.left = Node(data)
            else:
               self.left.insert(data)
         elif data > self.data:
             if self.right is None:
                 self.right = Node(data)
             else:
                  self.right.insert(data)
      else:
         self.data = data

# Print the tree
   def PrintTree(self):
      if self.left:
         self.left.PrintTree()
      print( self.data),
      if self.right:
         self.right.PrintTree()

# Use the insert method to add nodes
root = Node(12)
FROM openjdk:22

WORKDIR /app

COPY demo.java src/devops/demo.java

RUN javac -d classes src/devops/demo.java

CMD ["java","-cp","classes", "devops.demo"]



FROM python:3.13

WORKDIR /app

COPY demo.py src/devops1/demo.py

CMD ["python","src/devops1/demo.py"]
root.insert(6)
root.insert(14)
root.insert(3)
root.PrintTree()
