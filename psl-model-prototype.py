
import pandas as pandas
import numpy as numpy
import pickle


dataframe = pandas.read_csv('psl_formated.csv')

# Data Cleaning
# Removing unwanted columns
unuseable_columns = ['match_number','runs', 'is_four', 'is_six', 'is_wicket','wicket', 'wicket_text','result']
dataframe.drop(labels=unuseable_columns, axis=1, inplace=True)

# teams
teams = ['Islamabad United', 'Quetta Gladiators', 'Lahore Qalandars','Karachi Kings', 'Peshawar Zalmi', 'Multan Sultans']
dataframe = dataframe[(dataframe['team_1'].isin(teams)) & (dataframe['team_2'].isin(teams))]


# Data Preprocessing 
new_dataframe = pandas.get_dummies(data=dataframe, columns=['team_1', 'team_2'])

# Rearranging the columns
new_dataframe = new_dataframe[['psl_year','team_1_Islamabad United', 'team_1_Quetta Gladiators', 'team_1_Lahore Qalandars','team_1_Karachi Kings', 'team_1_Peshawar Zalmi', 'team_1_Multan Sultans'
,'team_2_Islamabad United', 'team_2_Quetta Gladiators', 'team_2_Lahore Qalandars','team_2_Karachi Kings', 'team_2_Peshawar Zalmi', 'team_2_Multan Sultans',
'inning','over', 'ball', 'total_runs', 'wickets']]

# Train and Test Data
xAxisTrain = new_dataframe.drop(labels='total_runs', axis=1)[new_dataframe['psl_year'] <= 2019]
xAxisTest = new_dataframe.drop(labels='total_runs', axis=1)[new_dataframe['psl_year'] >= 2020]
yAxisTrain = new_dataframe[new_dataframe['psl_year'] <= 2019]['total_runs']
yAxisTest = new_dataframe[new_dataframe['psl_year'] >= 2020]['total_runs']
xAxisTrain.drop(labels='psl_year', axis=True, inplace=True)
xAxisTest.drop(labels='psl_year', axis=True, inplace=True)


#Model
from sklearn.linear_model import LinearRegression
mlr = LinearRegression()
mlr.fit(xAxisTrain,yAxisTrain)



# pickle File
file = 'psl-model.pkl'
pickle.dump(mlr, open(file, 'wb'))