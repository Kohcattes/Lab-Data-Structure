class BSTNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class BST:
    def __init__(self):
        self.root = None

    def is_empty(self):
        return self.root == None

    def insert(self, data):
        pNew = BSTNode(data)
        if self.is_empty():
            self.root = pNew
        else:
            jam = self.root
            while True:
                if data<jam.data:
                    if jam.left == None:
                        break
                    jam = jam.left
                else:
                    if jam.right == None:
                        break
                    jam = jam.right
            if jam.data > data:
                jam.left = pNew
            else:
                jam.right = pNew
    
    def search(self, jam, data):
        while jam != None:
            if data < jam.data:
                jam = jam.left
            elif data > jam.data:
                jam = jam.right
            elif data == jam.data:
                break
        return jam

    def delete(self, data):
        jam = self.search(self.root, data)
        if jam == None:
            return None
        

    def findMin(self):
        jam = self.root
        if self.is_empty():
            return None
        while jam.left != None:
            jam = jam.left
        return jam.data

    def findMax(self):
        jam = self.root
        if self.is_empty():
            return None
        while jam.right != None:
            jam = jam.right
        return jam.data

    def preorder(self, root):
        if root != None:
            print("->", root.data, end=" ")
            self.preorder(root.left)
            self.preorder(root.right)

    def inorder(self, root):
        if root != None:
            self.inorder(root.left)
            print("->", root.data, end=" ")
            self.inorder(root.right)

    def postorder(self, root):
        if root != None:
            self.postorder(root.left)
            self.postorder(root.right)
            print("->", root.data, end=" ")

    def traverse(self):
        print("Preorder")
        self.preorder(self.root)
        print()
        print("Inorder")
        self.inorder(self.root)
        print()
        print("Postorder")
        self.postorder(self.root)
        print()

def main():
    myBST = BST()
    #myBST.insert(14)
    #myBST.insert(23)
    #myBST.insert(7)
    #myBST.insert(10)
    #myBST.insert(33)
    #myBST.traverse()
    print(myBST.findMax())
    print(myBST.findMin())
    print(myBST.delete(50))

main()