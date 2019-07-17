import unittest
import compose_maxproduct
import numpy

class compose_maxproductTestCase(unittest.TestCase):
    # Test input type - Input argument 1 should be a dictionary.
    def test_compose_maxproduct_1(self):
        S = numpy.matrix([[0.7, 0.2, 0.3], [0.1, 0.4, 0.9], [0.8, 0.5, 0.3]]) # matrix is not a dictionary
        R = {(1,1): 0.2, (1,2): 0.7, (1,3): 0.3, (2,1): 0.1, (2,2): 1, (2,3): 0.1, (3,1): 0, (3,2): 0.5, (3,3): 0}
        self.assertRaises(TypeError, lambda: compose_maxproduct.compose_maxproduct(S, R))

    # Test input type - Input argument 2 should be a dictionary.
    def test_compose_maxproduct_2(self):
        S = {(1,1): 0.2, (1,2): 0.7, (1,3): 0.3, (2,1): 0.1, (2,2): 1, (2,3): 0.1, (3,2): 0.5}
        R = numpy.matrix([[0.7, 0.2, 0.3], [0.1, 0.4, 0.9], [0.8, 0.5, 0.3]])  # matrix is not a dictionary
        self.assertRaises(TypeError, lambda: compose_maxproduct.compose_maxproduct(S, R))

    # Test input type - Input arguments should be dictionaries.
    def test_compose_maxproduct_3(self):
        S = [[1], [2], [3]]
        R = {1:2, 12:13, 15:16}
        self.assertRaises(TypeError, lambda: compose_maxproduct.compose_maxproduct(S, R))

    # Test input type - Input argument should be a dictionary.
    def test_compose_maxproduct_4(self):
        S, R = 0.1, 0.1
        self.assertRaises(TypeError, lambda: compose_maxproduct.compose_maxproduct(S, R))

    # Test input size - Dictionaries should have at least one set.
    def test_compose_maxproduct_5(self):
        S, R = {}, {}
        self.assertRaises(ValueError, lambda: compose_maxproduct.compose_maxproduct(S, R))

    # Test key type - Keys of dictionaries should be tuples
    def test_compose_maxproduct_6(self):
        S = {1.0: 0.1, 2.0: 0.2, 3.0: 0.3}
        R = {1.0: 0.1, 2.0: 0.2, 3.0: 0.3}
        self.assertRaises(TypeError, lambda: compose_maxproduct.compose_maxproduct(S, R))

    # Test value type - Values of dictionaries should be floats or ints.
    def test_compose_maxproduct_7(self):
        S = {(1, 1): '0.2', (1, 2): '0.7', (1, 3): '0.3', (2, 1): '0.1', (2, 2): '1', (2, 3): '0.1', (3, 2): '0.5'}
        R = {(1, 1): '0.2', (1, 2): '0.7', (1, 3): '0.3', (2, 1): '0.1', (2, 2): '1', (2, 3): '0.1', (3, 2): '0.5'}
        self.assertRaises(TypeError, lambda: compose_maxproduct.compose_maxproduct(S, R))

    # Test value type - Values of dictionaries should be floats or ints.
    def test_compose_maxproduct_8(self):
        S = {(1, 1): [0.2], (1, 2): [0.7], (1, 3): [0.3], (2, 1): [0.1], (2, 2): [1], (2, 3): [0.1], (3, 2): [0.5]}
        R = {(1, 1): [0.2], (1, 2): [0.7], (1, 3): [0.3], (2, 1): [0.1], (2, 2): [1], (2, 3): [0.1], (3, 2): [0.5]}
        self.assertRaises(TypeError, lambda: compose_maxproduct.compose_maxproduct(S, R))

    # Test value range - Values should be between 0 and 1.
    def test_compose_maxproduct_9(self):
        S = {(1, 1): 0.2, (1, 2): 1.7, (1, 3): 0.3, (2, 1): 0.1, (2, 2): 1, (2, 3): 0.1, (3, 1): 0, (3, 2): 0.5,
             (3, 3): 0}
        R = {(1, 1): 0.2, (1, 2): 1.7, (1, 3): 0.3, (2, 1): 0.1, (2, 2): 1, (2, 3): 0.1, (3, 1): 0, (3, 2): 0.5,
             (3, 3): 0}
        self.assertRaises(ValueError, lambda: compose_maxproduct.compose_maxproduct(S, R))

    # Test - return compose_maxmin value
    def test_compose_maxproduct_10(self):
        S = {(1,1): 0.7, (1,2): 0.2, (1,3): 0.3, (2,1): 0.1, (2,2): 0.4, (2,3): 0.9, (3,1): 0.8, (3,2): 0.5, (3,3): 0.3}
        R = {(1,1): 0.2, (1,2): 0.7, (1,3): 0.3, (2,1): 0.1, (2,2): 1, (2,3): 0.1, (3,1): 0, (3,2): 0.5, (3,3): 0}
        result = {(1,1): 0.14, (1,2): 0.49, (1,3): 0.21, (2,1): 0.04, (2,2): 0.45, (2,3): 0.04, (3,1): 0.16, (3,2): 0.56, (3,3): 0.24}
        self.assertEqual(compose_maxproduct.compose_maxproduct(S, R), result)


# Run all unittests
if __name__ == '__main__':
    unittest.main()
