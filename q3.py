"""Shortest common superstring"""

import math
import random
import string
import time
import logging

from strcmp.strcmp import compare_eq_len, compare_uneq_len

# import pdb

random.seed(1234) # fixed random seed to make the results reproducible

def generate_random_string(n, alphabet="ACTG"):
    """Generate a random string of length n using the given alphabet"""
    seq = ''.join(random.choices(alphabet, k=n))# create the sequence 
    return seq

def get_sequence_fragments(string, m, l):
    """
    Create m random fragments each of length l from string.
    input:
        string: String of to fragment
        m: Int. Number of fragments to return
        l: Int. Length of the fragments (all same length)
    output:
        frags: List of strings 
        frag_idxs: List of ints. Starting index of each fragment in original string 
    """
    n = len(string)
    frags = [] # list to store the fragments
    frag_idxs = []
    # create m fragments
    for _ in range(m):
        max_range = n - l + 1 
        start = random.choice(range(max_range)) # pick start idx from 0 to n-l 
        frag_idxs.append(start)
        frags.append(string[start:start + l]) 
    return frags, frag_idxs

# # find the shortest common supersequence from the fragments, this is the shortest sequence which has all the sequences as subsequences
# def assemble_sequence_greedy(frags):
#     """
#     Naive algorithm for finding the shortest common superstring from a list of fragments. The algorithm
#     compares pairs of strings, updating the result of each comparison with the string containing both strings with the 
#     longest overlap. The result from each pairwise comparison this is then compared to the next fragment in the
#     list. This process is repeated m times (m is the number of fragments), starting with the ith frag in the list
#     each time. The shorted of the m resulting strings is the results. This algorithn does not compare every possible
#     permutation of strings.
#         input:
#             frags: a list of equal length string fragments
#         output:
#             shortest: The shortest common superstring produced by the algorithm
#             shortest_len: The length of the returned string
#             total_time: The time taken in seconds to run the function
#     """
#     start_time = time.time()
#     num_frags = len(frags)
#     m = len(frags[0])
#     shorts = []
#     for i in range(num_frags):
#         a = f[i] # current fragment
#         rest = [x for idx, x in enumerate(f) if idx != i] # all other fragments
#         for b in rest:
#             # first just compare one fragment to all the others
#             if len(a) > len(b): # compare strings then update a with longest overlap
#                 a = compare_uneq_len(a, b)
#             else:
#                 a = compare_eq_len(a, b)
#         shorts.append(a)
#     shortest = sorted(shorts, key=lambda x:len(x))[0]
#     shortest_len = len(shortest)
#     total_time = time.time() - start_time
#     return shortest, shortest_len, total_time


def lander_waterman_metric(n, l, m, t):
    """
    Equation which can be used to compute the number of expected gaps in a sequence when trying to find the 
    shortest common superstring from a number of fragments, given the following parameters:
    input:
        n: length of the target string 
        l: length of the fragments (assuming equal length fragments)
        m: number of fragments
        t: recognize overlaps of this length        
    ouptut:
        g: the number of expected gaps
    """
    g = n * math.exp((-n*(l-t))/t)
    return g

if __name__ == '__main__':
        
    # logging.basicConfig(level=logging.INFO)
    # # logger = logging.getLogger(__name__)

    n = 10 # length of the random sequence seq
    fragm = 6 
    fragl = 5 
    s = generate_random_string(10)
    f, ids = get_sequence_fragments(s, fragm, fragl) # works fine


