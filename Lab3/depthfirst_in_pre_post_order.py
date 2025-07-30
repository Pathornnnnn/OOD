class Node:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data

    def insert(self, data):
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


    def PrintTree(self):
            if self.left:
                self.left.PrintTree()
            print( self.data),
            if self.right:
                self.right.PrintTree()

    def inorderTraversal(self, root):
        res = []
        if root:
            res = self.inorderTraversal(root.left)
            res.append(root.data)
            res = res + self.inorderTraversal(root.right)
        return res

    def preorderTraversal(self, root):
      res = []
      if root:
          res.append(root.data)
          res += self.preorderTraversal(root.left)
          res += self.preorderTraversal(root.right)
      return res


    def postorderTraversal(self,root):
      res = []
      if root:
          res = self.postorderTraversal(root.left)
          res = res + self.postorderTraversal(root.right)
          res.append(root.data)
      return res

lst = [3,16,9,23,11,7,5,34,19,2]
root = Node(15)
for i in lst:
  root.insert(i)
print(root.inorderTraversal(root))
print(root.preorderTraversal(root))
print(root.postorderTraversal(root))