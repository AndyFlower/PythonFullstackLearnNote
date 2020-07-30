# abs()
print(abs(-23))
# divmod
print(divmod(7,2)) #(3, 1)
#print(divmod(1+2j,1+0.5j)) #TypeError: can't take floor or mod of complex number.
#input
#input('please input') #please input2
# all
ll = ['a','b','c','d']
print(all(ll)) #True
l1 = ('1','a')
print(all(l1)) #True
print(all([]))#True
print(all(())) #
print(all(['1','','a'])) #False

# enumerate()
seasons = ['Spring', 'Summer', 'Fall', 'Winter']
print(enumerate(seasons)) #<enumerate object at 0x00000226CA6F7678>
print(list(enumerate(seasons))) #[(0, 'Spring'), (1, 'Summer'), (2, 'Fall'), (3, 'Winter')]
print(list(enumerate(seasons,start=1))) #[(1, 'Spring'), (2, 'Summer'), (3, 'Fall'), (4, 'Winter')]