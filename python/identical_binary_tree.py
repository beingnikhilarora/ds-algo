class TreeNode(object):
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def isIdentical(root1, root2):
    # Code here
    if not (root1 or root2):
        return True
    elif not (root1 and root2):
        return False
    if root1.data == root2.data and isIdentical(root1.left, root2.left) and isIdentical(root1.right, root2.right):
        return True

    return False

if __name__ == '__main__':
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.right = TreeNode(4)
    root.right.left = TreeNode(5)
    root.right.left.left = TreeNode(6)

    root2 = TreeNode(1)
    root2.left = TreeNode(2)
    print(isIdentical(root, root))
    print(isIdentical(root, root2))