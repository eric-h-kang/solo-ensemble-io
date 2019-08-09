from setup import *
from datetime import datetime, timedelta
import pandas as pd 
import numpy as np 
import random, copy

# TO DO
# write pandas method that will return the availability in a list based on student name 
def give_availability(name, ID, df):
    """
    returns availability and instrument of single student based on name
    """
    temp = df.loc[(df['Name'] == name) & (df['ID'] == ID)]
    return temp[['Name','n']].values.flatten().tolist()

d = {
     "Name": [1, 2, 3, 4, 5],
     "ID": [9, 8, 7, 6, 5],
     "n": ["a", "b", "c", "d", "e"]
}
df = pd.DataFrame(d)
print(give_availability(1, 9, df))

students = pd.DataFrame(columns = ['Name', 'Instrument', 'ID', 'Skill', 'Avail', 'Start', 'Piano'])

# build random arrays by required times 
morning_solos = random.shuffle(students[students['Avail'] == 'AM']['Name'].tolist())
afternoon_solos = random.shuffle(students[students['Avail'] == 'PM']['Name'].tolist())
flex_solos = random.shuffle(students[students['Avail'] == 'None']['Name'].tolist())                                                                                                            

# generate timeslots for each performance
timeslots = []
start = datetime.strptime('7:45', '%I:%M')
for i in range(40):
    timeslots.append(start.strftime('%I:%M'))
    start = start + timedelta(minutes = 15)

# build empty schedules for ensemble/solos
ensemble_room = pd.DataFrame(columns = ["Time", 'Student', 'Accompanist'])
solo_room = pd.DataFrame(columns = ["Time", 'Student', 'Accompanist'])
solo_room2 = pd.DataFrame(columns = ["Time", 'Student', 'Accompanist'])

# begin filling rooms 



