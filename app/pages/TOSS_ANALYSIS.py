import numpy as np
import pandas as pd
import warnings
import streamlit as st
warnings.simplefilter(action='ignore', category=FutureWarning)

import streamlit as st
import plotly.express as px

# Sample data
df = px.data.iris()

# Create a Plotly scatter plot
fig = px.scatter(df, x="sepal_width", y="sepal_length", color="species")

# Display the plot in Streamlit
st.plotly_chart(fig)


import streamlit as st
import altair as alt
import pandas as pd

# Sample data
df = pd.DataFrame({
    'x': [1, 2, 3, 4, 5],
    'y': [10, 20, 30, 40, 50],
    'category': ['A', 'A', 'B', 'B', 'C']
})

# Create an interactive Altair plot
chart = alt.Chart(df).mark_circle(size=60).encode(
    x='x',
    y='y',
    color='category',
    tooltip=['x', 'y', 'category']
).interactive()

# Display the Altair chart in Streamlit
st.altair_chart(chart)



import streamlit as st
from bokeh.plotting import figure
from bokeh.models import ColumnDataSource

# Sample data
source = ColumnDataSource(data=dict(x=[1, 2, 3, 4, 5], y=[6, 7, 2, 4, 5]))

# Create a Bokeh figure
p = figure(title="Interactive Bokeh Plot", x_axis_label="X", y_axis_label="Y", tools="pan,wheel_zoom,box_zoom,reset")

# Add circle glyphs
p.circle('x', 'y', size=10, source=source)

# Display the Bokeh plot in Streamlit
st.bokeh_chart(p)


# # Load the data
# data = pd.read_csv("../data/processed/clean_data.csv")
# toss_data = data.iloc[:, [1, 2, 3, 6, 7, 8, 9, 10, 11]]
# toss_data_grouped = toss_data.groupby("season")

# import seaborn as sns
# import matplotlib.pyplot as plt

# # Sample data for plotting
# data_x = [1, 2, 3, 4, 5]
# data_y = [10, 15, 8, 20, 12]

# # 1. Dark Grid Theme
# plt.figure()
# sns.set_theme(style="darkgrid", palette="dark")
# sns.histplot([1, 2, 1.5, 3, 2.5, 4])
# plt.title("Dark Grid Theme")
# st.pyplot(plt)


# # 2. White Grid with Dark Background
# plt.figure()
# sns.set_theme(style="whitegrid", rc={"axes.facecolor": "#2E3440", "figure.facecolor": "#2E3440", "grid.color": "#FFFFFF"})
# sns.lineplot(x=data_x, y=data_y)
# plt.title("White Grid with Dark Background")
# st.pyplot(plt)


# # 3. Minimalist Dark Theme
# plt.figure()
# sns.set_theme(style="white", rc={"axes.facecolor": "#1f1f1f", "figure.facecolor": "#1f1f1f", "grid.color": "#444444", 
#                                  "axes.labelcolor": "white", "xtick.color": "white", "ytick.color": "white"})
# sns.scatterplot(x=data_x, y=data_y)
# plt.title("Minimalist Dark Theme")
# st.pyplot(plt)

# # 4. Custom Dark Palette with 'Deep' Seaborn Colors
# plt.figure()
# dark_palette = sns.color_palette("deep")
# sns.set_theme(style="dark", palette=dark_palette, rc={"axes.facecolor": "#2E3440", "figure.facecolor": "#2E3440"})
# sns.barplot(x=["A", "B", "C"], y=[10, 20, 30])
# plt.title("Custom Dark Palette")
# st.pyplot(plt)

# # 5. Solarized Dark
# plt.figure()
# sns.set_theme(style="whitegrid", rc={"axes.facecolor": "#002b36", "figure.facecolor": "#002b36", "grid.color": "#586e75", 
#                                      "axes.labelcolor": "#93a1a1", "xtick.color": "#839496", "ytick.color": "#839496"})
# sns.lineplot(x=data_x, y=data_y)
# plt.title("Solarized Dark")
# st.pyplot(plt)



# # 6. Dark Background with Bright Accent Colors
# plt.figure()
# sns.set_theme(style="dark", palette="bright", rc={"axes.facecolor": "#212121", "figure.facecolor": "#212121", 
#                                                   "grid.color": "#444444", "axes.labelcolor": "white", 
#                                                   "xtick.color": "white", "ytick.color": "white"})
# sns.histplot([1, 2, 3, 4, 2.5, 3.5])
# plt.title("Dark Background with Bright Accent Colors")
# st.pyplot(plt)

# # 7. Deep Blue Background
# plt.figure()
# sns.set_theme(style="darkgrid", rc={"axes.facecolor": "#0D1B2A", "figure.facecolor": "#0D1B2A", "grid.color": "#1B263B", 
#                                     "axes.labelcolor": "white", "xtick.color": "white", "ytick.color": "white"})
# sns.boxplot(x=["A", "B", "C"], y=[1, 2, 3])
# plt.title("Deep Blue Background")
# st.pyplot(plt)

# # 8. Monochrome Dark
# plt.figure()
# sns.set_theme(style="ticks", rc={"axes.facecolor": "#202020", "figure.facecolor": "#202020", "grid.color": "#333333", 
#                                  "axes.labelcolor": "#AAAAAA", "xtick.color": "#AAAAAA", "ytick.color": "#AAAAAA"})
# sns.kdeplot([1, 2, 3, 4], fill=True)
# plt.title("Monochrome Dark")
# st.pyplot(plt)

# # 9. Custom Dark Mode with High Contrast
# plt.figure()
# sns.set_theme(style="dark", rc={"axes.facecolor": "#222831", "figure.facecolor": "#222831", "grid.color": "#393E46", 
#                                 "axes.labelcolor": "#EEEEEE", "xtick.color": "#EEEEEE", "ytick.color": "#EEEEEE"})
# sns.barplot(x=["X", "Y", "Z"], y=[5, 9, 7])
# plt.title("Custom Dark Mode with High Contrast")
# st.pyplot(plt)

# # 10. Ocean Dark Theme
# plt.figure()
# sns.set_theme(style="whitegrid", rc={"axes.facecolor": "#1B262C", "figure.facecolor": "#1B262C", "grid.color": "#0F4C75", 
#                                      "axes.labelcolor": "#3282B8", "xtick.color": "#BBE1FA", "ytick.color": "#BBE1FA"})
# sns.lineplot(x=data_x, y=data_y)
# plt.title("Ocean Dark Theme")
# st.pyplot(plt)
