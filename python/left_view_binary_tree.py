class TreeNode(object):
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def left_view(root):
    if root is None:
        return []

    queue = [root, None]
    flag = False
    ans = [root.data]

    while queue:
        node = queue.pop(0)

        if node is None:
            if queue:
                queue.append(None)
                flag = True
            continue

        if flag:
            ans.append(node.data)
            flag = False

        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)

    return ans


if __name__ == '__main__':
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.right = TreeNode(4)
    root.right.left = TreeNode(5)
    root.right.left.left = TreeNode(6)

    print(left_view(root))