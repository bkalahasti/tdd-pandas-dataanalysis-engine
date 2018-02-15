############################################################################### 
# Licensed under the Apache License, Version 2.0 (the "License"); 
# you may not use this file except in compliance with the License. 
# You may obtain a copy of the License at 
# 
#     http://www.apache.org/licenses/LICENSE-2.0 
# 
# Unless required by applicable law or agreed to in writing, software 
# distributed under the License is distributed on an "AS IS" BASIS, 
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. 
# See the License for the specific language governing permissions and 
# limitations under the License. 
############################################################################### 
# Filename: Dataframe-SummaryStatistics-Sample.py
# This Python code creates code for the following purposes:
# - Computes the 50th percentile of Batting Averages from a Batting CSV file. 
############################################################################### 
# This sample code reads from the Boston Marathon CSV file and 
# computes these statistical parameters:
# 1. The USA state with the most runners;
# 2. The fastest USA runner;
# 3. The fastest USA female runner. 
############################################################################### 
 
# List of modules that are imported.
import pandas as pd


# Task 1. The USA state with the most runners.
# Reading dataframe from CSV file.
data = pd.read_csv('C:/Kal/Stat-Work/Stat-Python/student_files/resources/boston_marathon_2017.csv', sep=r',',
                   error_bad_lines=False, usecols=(0, 4, 6, 7),
                   names=['row', 'gender', 'state', 'country'])

# Use groupby to group by country and get_group to group on 'USA'.
grouped_cntr = data.groupby('country').get_group('USA')

# Sort the grouped_sorted1 groupby object and get the top 4 states with the
# most runners. Use size() groupby method. 
# size() method returns a Series(). 
grouped_sorted1 = grouped_cntr.groupby('state').size().sort_values(ascending=False)
print('Top states: {0}'.format(grouped_sorted1[0:3]))
print()

# Sort the grouped_sorted2 groupby object and get the top 4 states with the 
# most runners. Use count() groupby method.
# count() method broadcasts the count to all columns and returns a Dataframe.
grouped_sorted2 = grouped_cntr.groupby('state').count().sort_values(by='row', ascending=False)
print('Top states: {0}'.format(grouped_sorted2['row'][0:3]))
print()


# Tasks 2 and 3. Fastest Runner and Fastest Female Runner Calculations. 
# Read CSV file into Dataframe.
data2 = pd.read_csv('C:/Kal/Stat-Work/Stat-Python/student_files/resources/boston_marathon_2017.csv', sep=r',',
                   error_bad_lines=False, usecols=(0, 2, 4, 7, 21),
                   names=['row', 'name', 'gender', 'country', 'Official Time'])

# Use groupby to group by country and get_group to group on 'USA'.
grouped_ctry = data2.groupby('country').get_group('USA')

# Sort using sort_values on 'Official Time' column.
grouped_sorted3 = grouped_ctry.sort_values(by='Official Time')

# Sort the grouped_sorted3 groupby object and get the Fastest Runner 
# using the min() method.
# min() method returns a single row. 
print("Fastest Runner: ", grouped_sorted3.min())
print()

# Use sort_values on 'Official Time' column after 'Gender' groupby
grouped_gender = grouped_ctry.groupby('gender').get_group('F')

# Sort the grouped_sorted4 groupby object and get the Fastest Female Runner 
# using the min() method.
# min() method returns a single row. 
grouped_sorted4 = grouped_gender.sort_values(by='Official Time')
print("Fastest Female Runner: ", grouped_sorted4.min())
print()







