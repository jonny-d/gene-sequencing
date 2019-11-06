""""Test the functions in strcmp.py work as expected """ 

import unittest
import random

from strcmp import compare_eq_len, scs_of_pair

random.seed(1234)

class StrcmpTest(unittest.TestCase):
    def setUp(self):
        # test data
        self.test_string = 'GCAGGTTAGA'
        self.test_frags = ['GCAGG', 'GCAGG', 'AGGTT', 'TTAGA', 'GTTAG', 'GGTTA']
        self.test_frag_idxs = [0, 0, 2, 5, 4, 3]
        self.n = 10 # length of test string
        self.m = 6 # number of fragments
        self.l = 5 # length of fragments

    def test_compare_eq_len(self):
        # test when a and b are equal
        a = self.test_frags[0]
        b = self.test_frags[0]
        scs = compare_eq_len(a, b)
        self.assertEqual(a, scs, "Shortest common superstring of identical strings should be that string")
        
        # test an expected overlap
        a = self.test_frags[0]
        b = self.test_frags[2]
        scs = compare_eq_len(a, b)
        self.assertEqual(scs, "GCAGGTT", "Shortest common superstring is not the expected value")

        # test no overlap
        a = "AAA"
        b = "BBB"
        scs = compare_eq_len(a, b)
        self.assertEqual(scs, "AAABBB", "Shortest common superstring is not the expected value")

    def test_scs_of_pair(self):
        # should also work with equal length strings
        # test when a and b are equal
        a = self.test_frags[0]
        b = self.test_frags[0]
        scs = scs_of_pair(a, b)
        self.assertEqual(a, scs, "Shortest common superstring of identical strings should be that string")
        
        # test an expected overlap
        a = self.test_frags[0]
        b = self.test_frags[2]
        scs = scs_of_pair(a, b)
        self.assertEqual(scs, "GCAGGTT", "Shortest common superstring is not the expected value")

        # test no overlap
        a = "AAA"
        b = "BBB"
        scs = scs_of_pair(a, b)
        self.assertEqual(scs, "AAABBB", "Shortest common superstring is not the expected value")

        # check unequal length strings with overlap
        a = "GCAGGTT"
        b = "TTAGA"
        scs = scs_of_pair(a, b)
        self.assertEqual(scs, "GCAGGTTAGA", "Shortest common superstring is not the expected value")

        # check unequal length strings no overlap
        a = "AAAA"
        b = "BBB"
        scs = scs_of_pair(a, b)
        self.assertEqual(scs, "AAAABBB", "Shortest common superstring is not the expected value")

