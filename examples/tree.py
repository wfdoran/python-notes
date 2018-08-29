class Node:
    def __init__(self, val):
        self.left = None
        self.right = None
        self.val = val
        self.min = val
        self.max = val
        self.count = 1
        self.height = 1
        self.max_gap = -1
        self.gap_start = -1
        
    def update(self):
        self.count = 1
        self.height = 1
        
        if self.left == None:
            self.min = self.val
        else:
            self.min = self.left.min
            self.count += self.left.count
            self.height = max(self.height, self.left.height + 1)
            
        if self.right == None:
            self.max = self.val
        else:
            self.max = self.right.max
            self.count += self.right.count
            self.height = max(self.height, self.right.height + 1)
            
        self.max_gap = 0
        if self.left != None:
            if self.left.max_gap >= self.max_gap:
                self.max_gap = self.left.max_gap
                self.gap_start = self.left.gap_start
            if self.val - self.left.max >= self.max_gap:
                self.max_gap = self.val - self.left.max
                self.gap_start = self.left.max
        if self.right != None:
            if self.right.min - self.val >= self.max_gap:
                self.max_gap = self.right.min - self.val
                self.gap_start = self.val
            if self.right.max_gap >= self.max_gap:
                self.max_gap = self.right.max_gap
                self.gap_start = self.right.gap_start
                
    def balance(node):
        h_left = 0 if node.left == None else node.left.height
        h_right = 0 if node.right == None else node.right.height
        
        if h_left >= h_right + 2:
            #              A                   B
            #             / \                 / \
            #            B                       A
            #           / \                     /
            #              C                   C
            A = node
            B = node.left
            C = node.left.right
            A.left = C
            A.update()
            B.right = A
            return B
            
        if h_right >= h_left + 2:
            A = node
            B = node.right
            C = node.right.left
            A.right = C
            A.update()
            B.left = A
            return B
        return node
            
    def insert(node, val):
        if node == None:
            return Node(val)
            
        if val < node.val:
            node.left = Node.insert(node.left, val)
        elif val > node.val:
            node.right = Node.insert(node.right, val)
            
        node = Node.balance(node)    
        node.update()
        return node
        
    def delete(node, val):
        if node == None:
            return None
        
        if val < node.val:
            node.left = Node.delete(node.left, val)
        elif val > node.val:
            node.right = Node.delete(node.right, val)
        else:
            if node.right == None:
                node = node.left
            elif node.left == None:
                node =  node.right
            else:
                A = node
                B = node.left
                C = node.left.right
                A.left = C
                B.right = A
                node = Node.delete(B, val)
            
        node = Node.balance(node)
        node.update()
        return node
            
        
            
    def print(self):
        if self.left != None:
            self.left.print()
        print(" " * self.height, end = "")
        print(self.val, self.min, self.max, self.count)
        if self.right != None:
            self.right.print()
                
class BinaryTree:
    def __init__(self):
        self.root = None
        
    def __del__(self):
        self.root = None   
        
    def insert(self, val):
        self.root = Node.insert(self.root, val)
        
    def delete(self,val):
        self.root = Node.delete(self.root, val)
        
    def print(self):
        if self.root != None:
            self.root.print()
            
    def max_gap(self):
        if self.root != None:
            a = self.root.max_gap
            b = self.root.gap_start
            print(a, b, a+b)
        
T = BinaryTree()
T.insert(5)
T.insert(1)
T.insert(10)
T.insert(7)
T.print()
T.max_gap()
print()
T.delete(5)
T.print()
T.max_gap()
print()
        
for i in range(11,20):
    T.insert(i)
T.print()
print()

for i in range(10,20,2):
    T.delete(i)
T.print()