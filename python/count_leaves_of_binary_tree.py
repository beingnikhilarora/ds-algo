class TreeNode(object):
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def count_leaves(root):
    if not root:
        return 0
    if not (root.left or root.right):
        return 1
    else:
        return count_leaves(root.left) + count_leaves(root.right)


if __name__ == '__main__':
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.right = TreeNode(4)
    root.right.left = TreeNode(5)
    root.right.left.left = TreeNode(6)

    print(count_leaves(root))