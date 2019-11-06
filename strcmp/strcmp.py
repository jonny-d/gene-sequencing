"""Functions for comparing pairs of strings"""

def compare_eq_len(a, b):
    """
    Find the shortest common superstring from two equal length strings. If there
    is no overlap then return the concatenation a + b. 
    input:
        a: String.
        b: String.
    ouptut:
        superstring: String. which is the shortest common superstring of a and b
    """
    n = len(a)
    m = len(b)

    # slide b across a from left to right till from just overlapping till full overlap
    overlap = 0 # stores length of the overlap
    lconcat = "" # this stores the shortest common superstring
    for j in range(m):
        starta = 0
        enda = j+1
        startb = m - (j+1)
        endb = m
        if a[starta:enda] == b[startb:endb]:
            # if an overlap is found, check if it is larger than the previously detected one
            print("overlap found")
            if len(a[starta:enda]) > overlap: 
                overlap = len(a[starta:enda]) 
                lconcat = b + a[enda:] # this is the current shortest common superstring
        print(starta, enda, startb, endb, a[starta:enda], b[startb:endb])

    # slide b across a so that b starts from one element past a after full overlap
    rconcat = ""
    for j in range(m-1):
        starta = j+1
        enda = m
        startb = 0
        endb = m - (j+1)
        if a[starta:enda] == b[startb:endb]:
            if len(a[starta:enda]) > overlap: # if there is a bigger overlap then save it 
                print("overlap found")
                overlap = len(a[starta:enda]) 
                rconcat = a + b[endb:]
        print(starta, enda, startb, endb, a[starta:enda], b[startb:endb])

    # after checking for overlaps there may be 1 or no shortest common
    # superstrings stored in both lconcat and rconcat. Choose the shortest one if it exists
    # or the concatenation of a and b if there are no overlaps. We may have to make some
    # arbitrary choices here.

    if not lconcat and not rconcat: # both lconcat and rconcat are empty, no overlaps
        superstring = a + b # append b to a (could prepend here too, this is an arbitrary choice)
    elif lconcat and not rconcat: # lconcat contains overlap and rconcat is empty
        superstring = lconcat 
    elif rconcat and not lconcat: # rconcat contains overlap and lconcat is empty
        superstring = rconcat
    elif rconcat and lconcat and (len(lconcat) <= len(rconcat)): # use lconcat if it is shorter or equal len to rconat
        superstring = lconcat
    elif rconcat and lconcat and (len(rconcat) < len(lconcat)): # use rconcat only if it is shorter than lconat
        superstring = rconcat
    return superstring

def compare_uneq_len(a, b):
    """
    Find the shortest common superstring from two unequal length strings. If there
    is no overlap then return the concatenation a + b. 
    input:
        a: String
        b: String
    ouptut:
        superstring: String which is the shortest common superstring of a and b
    """
    # compare two strings where the text a is longer than the pattern b
    n = len(a)
    m = len(b)

    # check the args are the right way round
    if m > n:
        raise ValueError("string b is longer than string a")

    # slide b across a from left to right till from just overlapping till full overlap
    overlap = 0 # stores length of the overlap
    lconcat = "" # stores the curretn shortest common superstring
    for j in range(n): 
        starta = 0 if (j+1) <= m else ((j+1) - m)  
        enda = j+1 
        startb = (m - (j+1)) if (j+1) < m else 0  
        endb = m 
        if a[starta:enda] == b[startb:endb]:
            print("overlap found")
            if len(a[starta:enda]) > overlap: # if there is a bigger overlap then save it 
                overlap = len(a[starta:enda]) 
                lconcat = b + a[enda:]
        print(starta, enda, startb, endb, a[starta:enda], b[startb:endb])

    print("-")
    rconcat = ""
    for j in range(m - 1):
        starta = (n - m) + (j + 1) 
        enda = n 
        startb = 0 
        endb = m - (j+1) 
        if a[starta:enda] == b[startb:endb]:
            print("overlap found")
            if len(a[starta:enda]) > overlap: # if there is a bigger overlap then save it 
                overlap = len(a[starta:enda]) 
                rconcat = a + b[endb:]
        print(starta, enda, startb, endb, a[starta:enda], b[startb:endb])

    # after checking for overlaps there may be 1 or no shortest common
    # superstrings stored in both lconcat and rconcat. Choose the shortest one if it exists
    # or the concatenation of a and b if there are no overlaps. We may have to make some
    # arbitrary choices here.

    if not lconcat and not rconcat: # both lconcat and rconcat are empty, no overlaps
        superstring = a + b # append b to a (could prepend here too)
    elif lconcat and not rconcat: # lconcat contains overlap and rconcat is empty
        superstring = lconcat
    elif rconcat and not lconcat: # rconcat contains overlap and lconcat is empty
        superstring = rconcat
    elif rconcat and lconcat and (len(lconcat) <= len(rconcat)): # use lconcat if it is shorter or equal len to rconat
        superstring = lconcat
    elif rconcat and lconcat and (len(rconcat) < len(lconcat)): # use rconcat only if it is shorter than lconat
        superstring = rconcat
    return superstring

if __name__ == "__main__":

    a = "GCAGGT"
    b = "TTAGA"
    scs = compare_uneq_len(b, a)
    print("scs", scs)








