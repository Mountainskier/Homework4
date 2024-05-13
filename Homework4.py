immutable_var = (1, 3.5, 'Guitar', False)
print(immutable_var)
# immutable_var[2] = 'Piano'  кортеж не поддерживает обращение по элементам.

mutable_list = [1, 3.5, 'Guitar', True]
print(mutable_list)
mutable_list[2] = 'Piano'
mutable_list[1] = 10.8
print(mutable_list)
