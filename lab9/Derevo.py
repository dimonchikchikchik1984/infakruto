class BinTree:
    def __init__(self, value):
        self.left = None
        self.right = None
        self.value = value

    def add(self, value):
        if self.value:
            if value < self.value:
                if self.left is None:
                    self.left = BinTree(value)
                else:
                    self.left.add(value)
            elif value > self.value:
                if self.right is None:
                    self.right = BinTree(value)
                else:
                    self.right.add(value)
        else:
            self.value = value

    def DFS(self, root):
        res = []
        if root:
            res = self.DFS(root.left)
            res.append(root.value)
            res = res + self.DFS(root.right)

        return res

    def PrintTree(self):
        if self.left:
            self.left.PrintTree()
        print(self.value),
        if self.right:
            self.right.PrintTree()


if __name__ == "__main__":
    tree = BinTree(5)
    tree.add(3)
    tree.add(4)
    tree.add(0)
    tree.add(8)
    tree.add(2)
    tree.PrintTree()
