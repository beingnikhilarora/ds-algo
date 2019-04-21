class TreeNode(object):
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def height(root):
    # Code here
    h = [-1]
    height_util(root, 1, h)
    return h[0]


def height_util(root, level, h):
    if not root:
        return
    if h[0] < level:
        h[0] = level
    height_util(root.left, level + 1, h)
    height_util(root.right, level + 1, h)


if __name__ == '__main__':
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.right = TreeNode(4)
    root.right.left = TreeNode(5)
    root.right.left.left = TreeNode(6)

    print(height(root))