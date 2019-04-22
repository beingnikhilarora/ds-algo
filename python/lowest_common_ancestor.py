class TreeNode(object):
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def lca(root, node1, node2):
    if not root:
        return None

    if root == node1 or root == node2:
        return root

    left = lca(root.left, node1, node2)
    right = lca(root.right, node1, node2)

    if left and right:
        return root

    return left if left is not None else right


if __name__ == '__main__':
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.right = TreeNode(4)
    root.right.left = TreeNode(5)
    root.right.left.left = TreeNode(6)

    ancestor = lca(root, root.right.left.left, root.right)
    print(ancestor.data)