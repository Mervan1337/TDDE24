def list_it(l):
    for i in l:
        yield i


l = [1,2,3,4,5,6,7,8]
new_l = []
l_gen = list_it(l)
for i in range(len(l)):
    new_l.append(next(l_gen))

print(new_l)