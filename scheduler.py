from setup import *
from datetime import datetime, timedelta
import pandas as pd 
import numpy as np 
import random, copy

# TO DO
# write pandas method that will return the availability in a list based on student name 

def give_availability(name, ID, chart):
    """
    returns availability and instrument of single student based on name
    """
    temp = chart[chart['Name'] == name and chart['ID'] == ID]
    temp = temp[['Name', 'Instrument', 'Avail']]
    return temp.values.flatten().tolist()



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



