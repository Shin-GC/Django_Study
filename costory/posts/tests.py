from django.test import TestCase

# Create your tests here.

data = [i for i in range(1, 101)]
stick = 0
while len(data)!=1:
    loser = (stick + 1) % len(data)
    del data[loser]
    stick = loser

print(data)
