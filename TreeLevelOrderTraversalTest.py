from TreeLevelOrderTraversal import levelOrderNodesOf
import unittest

class BinaryTreeHeightTest(unittest.TestCase):

    def test_singleNodeTree(self):
        self.assertTrue(levelOrderNodesOf('1', '8') == [8])

    def test_twoLevelsTreeWithOnlyLeft(self):
        self.assertTrue(levelOrderNodesOf('2', '8 5') == [8, 5])

    def test_twoLevelsTreeWithOnlyRight(self):
        self.assertTrue(levelOrderNodesOf('2', '8 10') == [8, 10])

    def test_exerciseExample(self):
        self.assertTrue(levelOrderNodesOf('6', '1 2 5 3 6 4') == [1, 2, 5, 3, 6, 4])

if __name__ == '__main__':
    unittest.main()