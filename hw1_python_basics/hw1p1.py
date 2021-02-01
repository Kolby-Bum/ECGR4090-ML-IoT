
# Kolby Bumgarner
# HW1


import numpy as np
import matplotlib.pyplot as plt


# (A) Original given
list_of_names = ['Roger', 'Mary', 'Luisa', 'Elvis']
list_of_ages  = [23, 24, 19, 86]
list_of_heights_cm = [175, 162, 178, 182]

for name in list_of_names:
  print("The name {:} is {:} letters long".format(name, len(name)))

# (B) 
new_list = []
for x in list_of_names:
    new_list.append(len(x))
print("(B)",new_list)

# (C)     
from person import person

new_person = person(name = 'Joe',age = 34, height = 184)
print("(C)","{:} is {:} years old.".format(new_person.name, new_person.age))

# (D)
print("(D)",new_person)

# (E)
people = {}
for i in range(len(list_of_names)):
    people[list_of_names[i]] = list_of_ages[i]
    
print("(E)",people)

# (F)
print("(F)",np.array(list_of_ages))
print("(F)",np.array(list_of_heights_cm))

# (G)
mean_age = np.mean(list_of_ages)
print("(G)",f"The average age is {mean_age} years old.")

# (H)
fig, ax = plt.subplots() 
plt.scatter(list_of_ages, list_of_heights_cm) 
plt.grid(color='k', linestyle='-', linewidth=0.5)
ax.set_xlabel('Age (years)')
ax.set_ylabel('Height (cm)')
ax.set_title("A Person's Age and Height")
