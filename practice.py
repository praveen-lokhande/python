s=set({1,2,3})
p=set({4,5,6})
print(p)
'''s.add(1)
s.add(2)
s.add(3)'''
s1=s.union({1,2,3})
print(s,s1)
print(s.isdisjoint(p))
s.union()