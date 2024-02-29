#Part 1: Create a BSTNode class - Day7 Activity2
class BSTNode:
  def __init__(self, data = None, left = None, right = None):
    self.data = data
    self.left = left
    self.right = right
  def __str__(self):
    return str(self.data)
  def __repr__(self):
    return str(self.data)
    
node1 = BSTNode(3)
print("What is the BSTNode 1:" ,node1) #3

node2 = BSTNode(4, left=node1)
print("What is the BSTNode 2:" ,node2) #4

node3 = BSTNode()
print("What is the BSTNode 3:" ,node3) #None
node3.data = 5
print("What is the BSTNode 3 data:" ,node3) #5

#Part 2: Create a BST class
  #Part 3: Add functionality to your BST class

class BST:
  def __init__(self, root = None):
    self.root = root
    self.contents = []
    
  def __str__(self):
    if self.root == None:
      return "Tree is empty"
    else:
      self.output = ""
      self.print_tree(node = self.root)
      return str(self.root)
  def __repr__(self):
    if self.root == None:
      return "Tree is empty"
    else:
      self.output = ""
      self.print_tree(node = self.root)
      return str(self.root)
  
  def print_tree(self, node, level = 0):
    if node!= None:
      self.output += "\n" + "\t" * level + str(node.data)
      self.print_tree(node.left, level + 1)
      self.print_tree(node.right, level + 1)
    else:
      return None
  
bst = BST()
print("Is the BST empty:" ,bst)

bst.root = node2
print("What is the BST root:" ,bst)

node2.right = node3
print("What is the Node to the right:" ,bst)