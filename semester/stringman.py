from shlex import join


def  common(s1,s2):
    set1 = set(s1)
    set2 = set(s2)
    d = set1 & set2  # Intersection of two sets
    print(d)  # Print the common characters
    c =sorted(set1 & set2)
    print("c=",c)
    j= join(c)
    print("j=",j)  # Print the joined string of common characters

common("hello", "world")