class TreeNode(object):
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def diameter(root):
    # Code here
    ans = [-1]
    diameter_util(root, ans)
    return ans[0]


def diameter_util(root, ans):
    if not root:
        return 0

    left = diameter_util(root.left, ans)
    right = diameter_util(root.right, ans)

    depth = left if left > right else right

    if ans[0] < left + right + 1:
        ans[0] = left + right + 1

    return depth + 1


if __name__ == '__main__':
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.right = TreeNode(4)
    root.right.left = TreeNode(5)
    root.right.left.left = TreeNode(6)

    print(diameter(root))