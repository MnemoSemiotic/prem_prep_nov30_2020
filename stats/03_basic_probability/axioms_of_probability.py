
setA = set(['bear', 'cat', 'dog', 'dolphin', 'weasel'])
setB = set(['bear', 'dog', 'elephant', 'weasel', 'mink', 'mountain lion'])
setC = set(['bear', 'whale', 'sea cucumber', 'mink', 'eagle', 'dog'])

sample_space = setA.union(setB).union(setC)

# print(sample_space)


'''
Commutative
A ∪ B = B ∪ A
AB = BA
'''

# print(setA.union(setB) == setB.union(setA))
# print(setA.intersection(setB) == setB.intersection(setA))

# booleans
a = True
b = False
c = True

# print((a or b) == (b or a))
# print((a and b) == (b and a))


'''
Associative
(A ∪ B) ∪ C = A ∪ (B ∪ C) = A ∪ B ∪ C 
⇒ 5 + (6 + 7) = (5 + 6) + 7 = 5 + 6 + 7
(AB)C = A(BC) = ABC
'''

a = True
b = False
c = True

# print((a or b) or c == a or (b or c))



'''
Distributive
A ∪ (BC) = (A ∪ B)(A ∪ C) 
A(B ∪ C) = (AB) ∪ (AC)
5*(2 * 3) = (5 * 2) + (5 * 3)
'''

a = True
b = False
c = True

# print((a or (b and c)) == ((a or b) and (a or c)))


'''
A ∪ A = A
AA = A
'''
a = True
b = False
c = True

# print((a or a) == a)
# print((a and a) == a)


'''
Domination Laws
Aside: 
U = Universal Set
The set of which all other subsets are a subset of
∅  = Empty Set = { }
A ∪ U = U
A ∩ U = A
A ∩ ∅ = ∅
'''
# print(sample_space)
# print(setA.union(sample_space))

# print(setA)
# print(setA.intersection(sample_space))


null_set = set()
print(null_set)