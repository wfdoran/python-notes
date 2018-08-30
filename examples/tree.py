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
        if node == None:
            return None
        h_left = 0 if node.left == None else node.left.height
        h_right = 0 if node.right == None else node.right.height
        
        if h_left >= h_right + 2:
            #              A                 
            #             / \                
            #            B                  
            #           / \                    
            #          D   C                 
            A = node
            B = A.left
            C = B.right
            D = B.left
            
            h_d = 0 if D == None else D.height
            h_c = 0 if C == None else C.height
            
            if h_c > h_d:
                #              A                     C
                #             /                   /     \
                #            B                   B       A
                #           / \                 / \     /
                #          D   C               D   E   F
                #             / \
                #            E   F                
            
                E = C.left
                F = C.right
                
                B.right = E
                B.update()
                
                A.left = F
                A.update()
                
                C.left = B
                C.right = A
                return C
                
            else:
                #                                   B
                #                                  / \
                #                                 D   A
                #                                    /
                #                                   C
                A.left = C
                A.update()
                
                B.right = A
                return B
            
        if h_right >= h_left + 2:
            #                      A
            #                       \
            #                        B
            #                       / \
            #                      C   D
            A = node
            B = A.right
            C = B.left
            D = B.right
            
            h_c = 0 if C == None else C.height
            h_d = 0 if D == None else D.height
            
            if h_c > h_d:
                #              A                      C
                #               \                  /     \
                #                B                A       B
                #               / \                \     / \
                #              C   D                F   E   D
                #             / \
                #            F   E                
                
                E = C.right
                F = C.left
                
                B.left = E
                B.update()
                
                A.right = F
                A.update()
                
                C.left = A
                C.right = B
                return C
                
            else:
                #                  B
                #                 / \
                #                A   D
                #                 \
                #                  C
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
        if node != None:
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
        
    def height(self):
        if self.root == None:
            return 0
        else:
            return self.root.height
        
    def print(self):
        if self.root != None:
            self.root.print()
            
    def max_gap(self):
        if self.root != None:
            a = self.root.max_gap
            b = self.root.gap_start
            print(a, b, a+b)
        
import random
        
T = BinaryTree()
X = []
for i in range(1000):
    val = random.randint(1,1000000000)
    T.insert(val)
    if random.randint(1,2) == 1:
        X.append(val)
for val in X:
    T.delete(val)
    
print(T.height())