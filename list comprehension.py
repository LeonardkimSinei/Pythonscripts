'''list comprehension'''

names =['John Gitao', 'Faith Chep', 'Irene Cheb', 'Tom B']
titles = ['GM','PA','HR','PA']

'''my_dict ={}
for name, title in  zip(names,titles):
   my_dict[name] = title
print (my_dict)'''

my_dict = {name:title for name, title in zip (names, titles) if name != 'Tom B'}
print(my_dict)

nums = [1,2,3,4,5]

square_nums = [n*n for n in nums]
print (square_nums)

'''loop through a dictionary'''
my_dict['Tom B'] = 'PAA'
for key, value in my_dict.items():
   print (key,value)
print (len(my_dict))

''' '''

