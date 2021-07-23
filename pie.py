# -*- coding: utf-8 -*-

import pandas as pd
import pickle
import webbrowser
import dash
import plotly.express as px
import plotly.graph_objects as go


def plot():
    result = pd.read_csv('scrappedReviewsLables.csv')

    pie_r = result.groupby(["lables"])["lables"].count()
    pie_result = pd.DataFrame(pie_r)
    pie_result["names"] = ["Negative","Positive"]
    pie_result.rename(columns = {'lables':'Count'}, inplace = True)
    print(pie_result)
    plot.pie_fig = go.Figure(px.pie(pie_result, values='Count',names='names'))
    plot.pie_fig.update_layout(
        paper_bgcolor='rgba(0,0,0,0)',
        font=dict(
            size=22,
        )
    )
