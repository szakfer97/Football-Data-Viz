import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from soccerplots.radar_chart import Radar

def get_player_data(player_name):
    player_data = df[df['Player'] == player_name].reset_index(drop=True)
    if not player_data.empty:
        return player_data.iloc[0].tolist(), player_data['Squad'].values[0]
    else:
        return None, None

df = pd.read_csv('prem_data.csv')
df['Player'] = df['Player'].str.split('\\', expand=True)[0]

player_1 = input("Enter the name of the first player: ")
player_2 = input("Enter the name of the second player: ")

a_values, club_1 = get_player_data(player_1)
b_values, club_2 = get_player_data(player_2)

if a_values is None or b_values is None:
    print("One or both players were not found in the dataset.")
    exit()
df = df.drop(['Rk', 'Nation', 'Pos', 'Age', 'Born', '90s'], axis=1)

params = list(df.columns)
params = params[2:]

ranges = []
for param in params:
    numeric_values = pd.to_numeric(df[param], errors='coerce')
    numeric_values = numeric_values.dropna()

    if not numeric_values.empty:
        a = numeric_values.min()
        a = a - (a * 0.25)

        b = numeric_values.max()
        b = b + (b * 0.25)

        ranges.append((a, b))
    else:
        ranges.append((0, 1))

print("Ranges:", ranges)

a_values = a_values[2:] if a_values else []
b_values = b_values[2:] if b_values else []

a_values = [pd.to_numeric(val, errors='coerce') for val in a_values]
b_values = [pd.to_numeric(val, errors='coerce') for val in b_values]

a_values = [0 if np.isnan(val) else val for val in a_values]
b_values = [0 if np.isnan(val) else val for val in b_values]

print(f"{player_1} values:", a_values)
print(f"{player_2} values:", b_values)

values = [a_values, b_values]

title = dict(
    title_name=player_1,
    title_color='red',
    subtitle_name=club_1,
    subtitle_color='red',
    title_name_2=player_2,
    title_color_2='blue',
    subtitle_name_2=club_2,
    subtitle_color_2='blue',
    title_fontsize=18,
    subtitle_fontsize=15
)

endnote = 'Compiled by Szakacsi Ferenc-Adam'
radar = Radar()

fig, ax = radar.plot_radar(ranges=ranges, params=params, values=values,
                           radar_color=['red', 'blue'],
                           alphas=[.75, .6], title=title, endnote=endnote,
                           compare=True)

plt.show()