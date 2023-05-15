
# libraries
from flask import Flask, render_template, request

import pickle
import numpy as numpy

# Model 
file = 'psl-model.pkl'
mlr = pickle.load(open(file, 'rb'))

webApp = Flask(__name__)

@webApp.route('/')
def home():
	return render_template('home.html')

@webApp.route('/predict', methods=['POST'])
def predict():
    temp_array1 = []
    temp_array2 = []

#Choosing Teams for batting and bwoling    
    if request.method == 'POST':
        
        team1 = request.form['team1']
        if team1 == 'Islamabad United':
            temp_array1 = temp_array1 + [1,0,0,0,0,0]
        elif team1 == 'Karachi Kings':
            temp_array1 = temp_array1 + [0,1,0,0,0,0]
        elif team1 == 'Lahore Qalandars':
            temp_array1 = temp_array1 + [0,0,1,0,0,0]
        elif team1 == 'Multan Sultans':
            temp_array1 = temp_array1 + [0,0,0,1,0,0]
        elif team1 == 'Peshawar Zalmi':
            temp_array1 = temp_array1 + [0,0,0,0,1,0]
        elif team1 == 'Quetta Gladiators':
            temp_array1 = temp_array1 + [0,0,0,0,0,1]

            
            
        team2 = request.form['team2']
        if team2 == 'Islamabad United':
            temp_array2 = temp_array2 + [1,0,0,0,0,0]
        elif team2 == 'Karachi Kings':
            temp_array2 = temp_array2 + [0,1,0,0,0,0]
        elif team2 == 'Lahore Qalandars':
            temp_array2 = temp_array2 + [0,0,1,0,0,0]
        elif team2 == 'Multan Sultans':
            temp_array2 = temp_array2 + [0,0,0,1,0,0]
        elif team2 == 'Peshawar Zalmi':
            temp_array2 = temp_array2 + [0,0,0,0,1,0]
        elif team2 == 'Quetta Gladiators':
            temp_array2 = temp_array2 + [0,0,0,0,0,1]
            
# If user selects inning 1 then that means team no is batting and if user select inning 2 then it means team no 2 is batting

# Input Features
        inning = int(request.form['inning'])
        over = int(request.form['overs'])
        balls = int(request.form['balls'])
        wicket = int(request.form['wickets'])
        
#sending all features to multiple linear regression
        arr = []
        arr = temp_array1 +temp_array2 + [inning,over, balls, wicket]
        
        
        inputs = numpy.array([arr])
        predict = int(mlr.predict(inputs)[0])
# Regressor prediction              
        return render_template('prediction.html', lower_limit = predict-10, upper_limit = predict+5)

if __name__ == '__main__':
	webApp.run(debug=True)
