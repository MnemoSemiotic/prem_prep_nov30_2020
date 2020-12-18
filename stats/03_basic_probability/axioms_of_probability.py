
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

print(setA.union(setB) == setB.union(setA))