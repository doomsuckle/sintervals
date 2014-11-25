import unittest
from clopper_pearson import clopper_pearson

class test_clopper_pearson(unittest.TestCase):
    
    def test_known_intervals(self):
        '''Test expected results within tolerance.'''
        ret = clopper_pearson(8, 10, 1-0.99)
        expected = (0.35180, 0.98915)
        self.assertAlmostEqual(ret[0], expected[0] , 4)
        self.assertAlmostEqual(ret[1], expected[1] , 4)

    def test_alpha_value_exceptions(self):
        '''Test expected exceptions.'''
        self.assertRaises(ValueError, clopper_pearson, 8, 10, 'a')
        self.assertRaises(ValueError, clopper_pearson, 8, 10, 1.1)
        self.assertRaises(ValueError, clopper_pearson, 8, 10, -1.)
        self.assertRaises(ValueError, clopper_pearson, 8, 10, (-1, 0.5))
        self.assertRaises(ValueError, clopper_pearson, 8, 10, (0.1, 'a'))
        self.assertRaises(ValueError, clopper_pearson, 8, 10, (0.6, 0.9))

    def test_known_asymm_intervals(self):
        '''Test some known intervals for asymmetric coverage and integer ranges.'''

        ret = clopper_pearson(8, 10, (0,0.1))
        expected = (0.0, 0.9455)
        self.assertAlmostEqual(ret[0], expected[0] , 3)
        self.assertAlmostEqual(ret[1], expected[1] , 3)

        ret = clopper_pearson(8, 10, [0,0.1])
        expected = (0.0, 0.9455)
        self.assertAlmostEqual(ret[0], expected[0] , 3)
        self.assertAlmostEqual(ret[1], expected[1] , 3)
        
        ret = clopper_pearson(8, 10, (0.1,0))
        expected = (0.5504, 1.)
        self.assertAlmostEqual(ret[0], expected[0] , 3)
        self.assertAlmostEqual(ret[1], expected[1] , 3)


if __name__ == '__main__':
    unittest.main()
