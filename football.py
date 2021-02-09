import pandas as pd
import math
import numpy

csv_url = "https://raw.githubusercontent.com/himquantum/python-data-project/main/football.csv"
df = pd.read_csv(csv_url, error_bad_lines=False)
goal_diff = abs(df['Goals'] - df['Goals Allowed'])
team_diff = pd.concat([df['Team'], goal_diff], axis=1, ignore_index=True, sort=True)
team_diff.columns = ['Team', 'Goal_diff']

print(team_diff['Goal_diff'].idxmin())
print(team_diff['Goal_diff'].idxmax())
print(team_diff[team_diff.Goal_diff == team_diff.Goal_diff.min()])

