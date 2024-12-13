a = """
for i in range(1, 20): 
    print( i ) 
    print('  #  ')
    if True:
        print('  \',   \'  ' )
print('\t' )
print('\\' )
"""
b = """
for i in range(1, 20):
    print( i )
    print('  #  ')
    if True:
        print('  \',   \'  ' )
print('\t' )
print('\\' )
"""

for i in range(len(a)-1):
    if a[i] != b[i]:
        print(i)