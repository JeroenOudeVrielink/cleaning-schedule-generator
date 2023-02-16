import pandas as pd
import datetime

group_1 = ['Torge', 'Thijs', 'Joshua']
group_2 = ['Malte', 'Bente', 'Jeroen']

tasks = ['Kitchen & Hallway downstairs', 'Bathroom & Hallway upstairs', 'Toilet, Trash, Glass & Paper']

# Year/Month/Day
starting_date = datetime.date(2023, 2, 13)
repeating_weeks = 12

week = datetime.timedelta(weeks=1)

data = {
    'Week': [],
    tasks[0]: [],
    tasks[1]: [],
    tasks[2]: []
}

for i in range(repeating_weeks):
    data['Week'].append('Week of ' + starting_date.strftime('%d %B'))
    data[tasks[0]].append(group_1[i % 3] + ' & ' + group_2[(i+2) % 3])
    data[tasks[1]].append(group_1[(i+1) % 3] + ' & ' + group_2[(i+1) % 3])
    data[tasks[2]].append(group_1[(i+2) % 3] + ' & ' + group_2[(i % 3)])
    starting_date += week

df = pd.DataFrame(data)
df.to_csv('cleaning_schedule.csv')
