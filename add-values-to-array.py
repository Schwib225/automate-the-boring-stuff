#! python3

listValues = []
while True:
    print('Enter the value you want to add to the array ' + str(len(listValues) + 1) + ' (or enter nothing to stop)')
    v = input()
    if v == '':
        break
    listValues = listValues + [v]
print('The list of values is: ')
for v in listValues:
    print('    ' + v)