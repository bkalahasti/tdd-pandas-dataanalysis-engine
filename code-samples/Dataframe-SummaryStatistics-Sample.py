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
# This code sample computes the 50th percentile of Batting Averages from
# the Batting CSV file. 
# Step 1. Create the Pandas DataFrame from the numpy array data.  Provide column
#         names for your dataframe.
# Step 2. Use describe() to retrieve a summary DataFrame.  From this, determine
#         the 50% (percentile) for batting in the MLB.
# Step 3. Show Pandas Scatter plot. 
# Step 4. Optionally create a legend and annotate the maximum value as was done
#         before.
#         Show the plot.
############################################################################### 

# Import the modules necessary for the program. 
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# Read the CSV file into a Dataframe. 
df = pd.read_csv('C:/Kal/Stat-Work/Stat-Python/student_files/resources/baseball/Batting.csv', usecols=(6,8))
df.columns = ['atbats', 'hits']

# Create a new Column called avgs. 
df['avgs'] = df['hits'] / df['atbats']
df2 = df.loc[(df['atbats'] >= 502)]

# Compute the 50th percentile from describe() method. 
fifty = df2.describe()['avgs']['50%']
print('50%: {0:.3f}'.format(fifty))

# Show a Scatter plot.
df2.plot(kind='scatter', x='avgs', y='atbats')
plt.show()

