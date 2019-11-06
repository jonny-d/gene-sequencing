"""Shortest common superstring"""

import argparse
import math
import random
import string
import time
import itertools

from strcmp.strcmp import compare_eq_len, compare_uneq_len

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
def assemble_sequence_greedy(frags):
    """
    Naive greedy algorithm for finding the shortest common superstring from a list of fragments of strings.
    The algorithm compares pairs of strings, updating the result of each comparison with the string 
    containing both strings with the longest overlap. The result from each pairwise comparison 
    is then compared to the next fragment in the list. This process is repeated perm(m) times 
    (m is the number of fragments) for each possible ordering of the string fragments.
    The shortest of the resulting strings is the results. Which should hopefully be 
    an accurate reproduction of the original string.
        input:
            frags: a list of equal length string fragments of a source string
        output:
            shortest_common_superstring: Reproduced string
            total_time: The time taken in seconds to run the function
    """
    start_time = time.time()
    scs_list = []
    num_frags = len(frags) # assuming all fragments are equal length
    # get all permutations of
    for perm in itertools.permutations(frags):
        a = perm[0]
        for b in perm[1:]:
            a = scs_of_pair(a, b) # return the shortest common superstring of a and b
        scs_list.append(a)
    shortest_common_superstring = sorted(scs_list, key=lambda x:len(x))[0]
    total_time = time.time() - start_time
    return shortest_common_superstring, total_time

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
        
    parser = argparse.ArgumentParser()

    parser.add_argument("--n", type=int, help="length of random string", default=20)
    parser.add_argument("--m", type=int, help="number of string fragments", default=20)
    parser.add_argument("--l", type=int, help="lenth of string fragments", default=6)
    
    args = parser.parse_args()

    s = generate_random_string(args.n)

    f, ids = get_sequence_fragments(s, args.m, args.l) # works fine
    scs, tt = assemble_sequence_greedy(f)

    print("{} - original string".format(s))
    print("{} - reconstructed string".format(scs))
    print("{} - time taken".format(tt))
    print("{} - expected gaps".format(lander_waterman_metric(args.n, args.l, args.m, 1)))

