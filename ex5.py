#!/usr/bin/python3
my_name = 'Joab O. Nyamagiri'
my_age = 73     # not a lie
my_height = 74      # inches
my_weight = 180     # kgs
my_eyes = 'Black'
my_teeth = 'White'
my_hair = 'Black'

print(f"Let's talk about {my_name}.")   # f-string format
print(f"He's {my_height} inches tall.")
print("He's {} pounds heavy.".format(my_weight))    # str.format
print("Actually that's not too heavy.")
print("He's got {} eyes and {} hair.".format(my_eyes, my_hair))
print(f"His teeth are usually {my_teeth} depending on the coffee.")

# this line is tricky, try to get it exactly right
total = my_age + my_height + my_weight
print(f"If I add {my_age}, {my_height}, and {my_weight} I get {total}.")
print("If I add {}, {}, and {} I get {}.".format(my_age, my_height, +
                                                 my_weight, total))
