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


print('For Islamabad United press 1 ')
print('For Quetta Gladiators press 2 ')
print('For  Lahore Qalandars press 3 ')
print('For Karachi Kings Riders press 4 ')
print('For Peshawar Zalmi press 5 ')
print('For Multan Sultans press 6 ')

bowling_team = input('Enter bowling Team no : ')

if bowling_team == '1':
    temp_array2 = temp_array2 + [1, 0, 0, 0, 0, 0]
elif bowling_team == '2':
    temp_array2 = temp_array2 + [0, 1, 0, 0, 0, 0]
elif bowling_team == '3':
    temp_array2 = temp_array2 + [0, 0, 1, 0, 0, 0]
elif bowling_team == '4':
    temp_array2 = temp_array2 + [0, 0, 0, 1, 0, 0]
elif bowling_team == '5':
    temp_array2 = temp_array2 + [0, 0, 0, 0, 1, 0]
elif bowling_team == '6':
    temp_array2 = temp_array2 + [0, 0, 0, 0, 0, 1]

inning = int(input('Enter inning number : '))
over = int(input('Enter Overs : '))
ball = int(input('Enter balls bowled in Over : '))
wickets = int(input('Enter wickets  : '))


temp_array = []
temp_array = temp_array1 +temp_array2 + [inning,over, ball, wickets]

data = np.array([temp_array])
my_prediction = int(regressor.predict(data)[0])
print("Predicted Score is : ",my_prediction)



