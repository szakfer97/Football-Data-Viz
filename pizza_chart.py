import pandas as pd
import numpy as np
from scipy import stats
import math
from mplsoccer import PyPizza, add_image, FontManager
import matplotlib.pyplot as plt

df = pd.read_csv('prem_data.csv')
df['Player'] = df['Player'].str.split('\\', expand=True)[0]
df = df.loc[(df['Pos'] == 'DF') & (df['90s'] > 5)]
df = df.drop(['Rk', 'Nation', 'Pos', 'Squad',
             'Age', 'Born'], axis=1).reset_index()
params = list(df.columns)
params = params[2:]
name = input('Enter the name: ')
player = df.loc[df['Player'] == name].reset_index()
player = list(player.loc[0])
print(player)
df.Player.values
print(len(player), print(len(params)))
player = player[3:]
print(len(player), print(len(params)))
values = []
for x in range(len(params)):
    values.append(math.floor(
        stats.percentileofscore(df[params[x]], player[x])))
round(stats.percentileofscore(df[params[0]], player[0]))
for n, i in enumerate(values):
    if i == 100:
        values[n] = 99
baker = PyPizza(
    params=params,
    straight_line_color="#000000",
    straight_line_lw=1,
    last_circle_lw=1,
    other_circle_lw=1,
    other_circle_ls="-."
)
fig, ax = baker.make_pizza(
    values,
    figsize=(8, 8),
    param_location=110,
    kwargs_slices=dict(
        facecolor="#dd996c", edgecolor="#000000",
        zorder=2, linewidth=1
    ),
    kwargs_params=dict(
        color="#000000", fontsize=12,
        va="center", alpha=.5
    ),
    kwargs_values=dict(
        color="#000000", fontsize=12,
        zorder=3,
        bbox=dict(
            edgecolor="#000000", facecolor="#dd996c",
            boxstyle="round,pad=0.2", lw=1
        )
    )
)

fig.text(
    0.515, 0.97, name, size=18,
    ha="center", color="#000000"
)

fig.text(
    0.515, 0.942,
    "Per 90 Percentile Rank vs. Premier League defenders | 2020-21",
    size=15,
    ha="center", color="#000000"
)

notes = 'Players only with more than 15 90s'
credits = "Data: statsbomb via fbref"

fig.text(
    0.99, 0.005, f"{notes}\n{credits}", size=9,
    color="#000000",
    ha="right"
)

plt.show()