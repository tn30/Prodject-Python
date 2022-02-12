new_list = [15, None, "John", 'False', True, 8.1]
print(type(new_list))

new_tuple = (15, None, "John", 'False', True, 8.1)
print(type(new_tuple))

my_int = 10
my_float = 5.8
my_str = "Hello!"
my_list = ['a', '0']
my_tuple = ('d', '9')
my_dict = {'city': 'Novosibirsk', 'country': 'Russia'}

big_list = [my_int, my_float, my_str, my_list, my_tuple, my_dict]
for i in big_list:
    print(f'{i} is {type(i)}')