word = input()

croa = ['c=','c-','dz=','d-','lj','nj','s=','z=']

for i in croa:
    word = word.replace(i, 'a')

print(len(word))
