""""Test the functions in q3.py work as expected """ 

import unittest
import random

from q3 import generate_random_string, get_sequence_fragments

random.seed(1234)

class Q3Test(unittest.TestCase):
    def setUp(self):
        self.test_string = 'GCAGGTTAGA'
        self.test_frags = ['GCAGG', 'GCAGG', 'AGGTT', 'TTAGA', 'GTTAG', 'GGTTA']
        self.test_frag_idxs = [0, 0, 2, 5, 4, 3]
        self.n = 10 # length of test string
        self.m = 6 # number of fragments
        self.l = 5 # length of fragments

    def test_generate_random_string(self):
        seq = generate_random_string(self.n)
        self.assertEqual(seq, self.test_string)

    def test_get_sequence_fragments(self):
        frags, frag_idxs = get_sequence_fragments(self.test_string, self.m, self.l) 
        self.assertEqual(frags, self.test_frags)
        self.assertEqual(frag_idxs, self.test_frag_idxs)

        # check the frag indices line up with the original string
        frags = []
        for idx in frag_idxs:
            frags.append(self.test_string[idx:idx+self.l])
        self.assertEqual(frags, self.test_frags)

