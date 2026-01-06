import unittest
from flu_utils import int_to_iupac, convert_to_prop, mine_single_HA, mine_single_NA

class TestFluUtils(unittest.TestCase):

    def test_int_to_iupac(self):
        self.assertEqual(int_to_iupac(1), 'PB2')
        self.assertEqual(int_to_iupac('4'), 'HA')
        self.assertEqual(int_to_iupac(8), 'NS')
        # Test invalid input handling if applicable, though function prints to stdout currently
        
    def test_convert_to_prop(self):
        counts = {'A': 50, 'B': 50}
        props = convert_to_prop(counts)
        self.assertEqual(props['A'], 0.5)
        self.assertEqual(props['B'], 0.5)
        
        counts_uneven = {'A': 1, 'B': 3}
        props_uneven = convert_to_prop(counts_uneven)
        self.assertEqual(props_uneven['A'], 0.25)
        self.assertEqual(props_uneven['B'], 0.75)

    def test_mine_single_HA(self):
        self.assertEqual(mine_single_HA('H1N1'), 'UD')
        self.assertEqual(mine_single_HA('H5'), 'H5')
        self.assertEqual(mine_single_HA('N1'), 'UD')
        self.assertEqual(mine_single_HA('Mixed'), 'UD')

    def test_mine_single_NA(self):
        self.assertEqual(mine_single_NA('H1N1'), 'UD')
        self.assertEqual(mine_single_NA('N2'), 'N2')
        self.assertEqual(mine_single_NA('H3'), 'UD')

if __name__ == '__main__':
    unittest.main()