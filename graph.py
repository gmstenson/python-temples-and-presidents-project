import pandas as pd
from matplotlib import pyplot as plt
from matplotlib import style
import numpy as np

plt.style.use('fivethirtyeight')
fig = plt.gcf()
fig.canvas.manager.set_window_title("Temple Statistics per President")
fig.subplots_adjust(bottom=0.25)

temples = pd.read_csv("presidents.csv")
w = 0.25

presidents = temples.President
groundbreakings = temples.Groundbreakings
dedications = temples.Dedications
announcements = temples.Announcements

x_indexes = np.arange(len(presidents))

plt.bar(x_indexes - w, announcements, width = w, color = '#28536B', label='Announcements')
plt.bar(x_indexes, groundbreakings, width = w, color = '#4F3130', label='Groundbreakings')
plt.bar(x_indexes + w, dedications, width = w, color = '#6BA368', label='Dedications')

title_string = "Temple Statistics per President"
subtitle_string = "**Data as of April 2022**"

plt.suptitle(title_string, fontsize=12)
plt.title(subtitle_string, fontsize=8)
plt.xlabel("Church Presidents", fontsize=10)
plt.ylabel("Number of Temples", fontsize=10)
plt.tick_params(axis='x', which='major', labelsize=6)
plt.tick_params(axis='y', which='major', labelsize=8)
plt.xticks(x_indexes, presidents, rotation = 90)

plt.legend(loc=2, prop={'size': 10})

plt.show()