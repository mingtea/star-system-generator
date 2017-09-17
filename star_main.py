import random

print('Enter name of system: ')
star_sys_name = input()
num_of_stars = 1

star_type_int = random.randrange(0, 4)
star_color = None
star_type_dict = {
	0: 'main sequence',
	1: 'giant',
	2: 'supergiant',
	3: 'neutron',
	4: 'black hole'}

if star_type_int < 3:
	star_color_int = random.randrange(0, 2)
	star_color_dict = {
	0: 'blue',
	1: 'red',
	2: 'white',
	3: 'yellow'}
	star_color = star_color_dict[star_color_int]
elif star_type_int == 2:
	star_color = 'red'
elif star_type_int >= 3:
	star_color = 'other'

star_type = star_type_dict[star_type_int]


print('The ' + star_sys_name + ' has ' + str(num_of_stars) + ' star')
print(star_sys_name + ' is a ' + star_type + ' star.')
print(star_sys_name + ' is a ' + star_color + ' star. ')
