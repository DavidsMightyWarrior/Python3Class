#!/usr/bin/python3

#print(*objects, sep=' ', end='\n', file=sys.stdout, flush=False)

num = 32
text = "Get a life"
print(text, num)
print(text, num, sep=' ', end='\n')

print("What do you want?")
needs = input()
print("I need: ", needs)
