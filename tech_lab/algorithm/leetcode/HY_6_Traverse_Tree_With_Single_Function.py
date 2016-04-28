# coding: utf-8
"""
Description: 输入一个TreeNode, 用一个函数遍历它，返回它的一个全节点Path。

"""
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


# 此处我们需要做的是不断的把值装入一个统一的容器里。
# 因为用到了递归，所以我们可能需要把值一层层的收集起来
# 在最底层的时候，我们的node是没有左叶片和右叶片的，它返回自己的值
# 这个值应该被它的上一层节点捕捉到, 上一层节点将它的两个叶片的值和自己的值汇拢后，再传给上一层

def traverse_node(node):
    """
    :paramn node: obj of TreeNode
    :returns:
    """
    cur_path = [node.val]
    if isinstance(node.left, TreeNode):
        cur_path.extend(traverse_node(node.left))
    if isinstance(node.right, TreeNode):
        cur_path.extend(traverse_node(node.right))
    return cur_path


class TreeNode(object):
    """ Made this Class for test """

    def __init__(self, x):
        self.val = x
        self.left = None          # 我猜想此处是数字 # 然后我又觉得此处应该是个实例才对，必须是实例。
        self.right = None


#  测试用节点说明：
#         1
#       /   \
#      2     3
#     / \     \
#    4   5     6
#   / \
#  7   8

n7 = TreeNode(7)
n8 = TreeNode(8)
n5 = TreeNode(5)
n6 = TreeNode(6)

n4 = TreeNode(4)
n4.left = n7
n4.right = n8

n3 = TreeNode(3)
n3.right = n6

n2 = TreeNode(2)
n2.left = n4
n2.right = n5

n1 = TreeNode(1)
n1.left = n2
n1.right = n3

