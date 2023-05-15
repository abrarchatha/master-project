import pickle
import numpy as np


filename = 'psl-model.pkl'
regressor = pickle.load(open(filename, 'rb'))

temp_array1 = []
temp_array2 = []


print('For Islamabad United press 1 ')
print('For Quetta Gladiators press 2 ')
print('For  Lahore Qalandars press 3 ')
print('For Karachi Kings Riders press 4 ')
print('For Peshawar Zalmi press 5 ')
print('For Multan Sultans press 6 ')


bating_team = input('Enter bating Team no : ')


if bating_team == '1':
    temp_array1 = temp_array1 + [1, 0, 0, 0, 0, 0]
elif bating_team == '2':
    temp_array1 = temp_array1 + [0, 1, 0, 0, 0, 0]
elif bating_team == '3':
    temp_array1 = temp_array1 + [0, 0, 1, 0, 0, 0]
elif bating_team == '4':
    temp_array1 = temp_array1 + [0, 0, 0, 1, 0, 0]
elif bating_team == '5':
    temp_array1 = temp_array1 + [0, 0, 0, 0, 1, 0]
elif bating_team == '6':
    temp_array1 = temp_array1 + [0, 0, 0, 0, 0, 1]
