  #----------------------------------T20 WORLD CUP 2022 DATA ANYALYSIS------------------------------------------------
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import plotly.io as pio
pio.templates.default = "plotly_white"

data = pd.read_csv('D:\\t20-world-cup-22.csv')
print(data.head())
#print(data.tail())
#print(data.info())

#figure = px.bar(data,
                #x=data["winner"],
                #title="Number of Matches Won by teams in t20 World Cup 2022")
#figure.show()

# won_by = data["won by"].value_counts()
# label = won_by.index
# counts = won_by.values
# colors = ['gold','lightgreen']

#fig = go.Figure(data=[go.Pie(labels=label, values=counts)])
#fig.update_layout(title_text='Number of Matches Won By Run or Wicket')
#fig.update_traces(hoverinfo='label+percent', textinfo='value', textfont_size=30,
                # marker=dict(colors=colors, line=dict(color='black', width=3)))
#fig.show()

#toss = data["toss decision"].value_counts()
#label = toss.index
#counts = toss.values
#colors = ['skyblue','yellow']

#fig = go.Figure(data=[go.Pie(labels=label, values=counts)])
#fig.update_layout(title_text='Toss Decisions in t20 World Cup 2022')
#fig.update_traces(hoverinfo='label+percent', textinfo='value', textfont_size=30,
                  #marker=dict(colors=colors, line=dict(color='black', width=3)))
#fig.show()

#figure = px.bar(data,
                #x=data["top scorer"],
                #y = data["highest score"],
                #color = data["highest score"],
                #title="Top Scorers in t20 World Cup 2022")
#figure.show()

#figure = px.bar(data,
                #x = data["player of the match"],
                #title="Player of the Match Awards in t20 World Cup 2022")
#figure.show()

#figure = px.bar(data,
                #x=data["best bowler"],
                #title="Best Bowlers in t20 World Cup 2022")
#figure.show()

#fig = go.Figure()
#fig.add_trace(go.Bar(
    #x=data["venue"],
    #y=data["first innings score"],
    #name='First Innings Runs',
    #marker_color='blue'
#))
#fig.add_trace(go.Bar(
    #x=data["venue"],
    #y=data["second innings score"],
    #name='Second Innings Runs',
    #marker_color='red'
#))
#fig.update_layout(barmode='group',
                  #xaxis_tickangle=-45,
                  #title="Best Stadiums to Bat First or Chase")
#fig.show()

