""" Analysis of US census data """

#### Loading the required packages ####

import pandas as pd
import seaborn as sb
import plotly.express as px
from plotly.offline import plot
import matplotlib.pyplot as plt
import numpy as np

######## Load US data CSV file ########## 

US_census_data=pd.read_csv('US_CensusData.csv', encoding = "latin")


dataviz=US_census_data[['State','TotalPop', 'Men', 'Women', 'Hispanic', 'White', 'Black', 'Native',
'Asian', 'Pacific', 'Citizen', 'Income','IncomePerCap','Poverty','ChildPoverty',
'Professional', 'Service',
'Office', 'Construction', 'Production', 'Drive', 'Carpool', 'Transit',
'Walk', 'OtherTransp', 'WorkAtHome', 'MeanCommute', 'Employed',
'PrivateWork', 'PublicWork', 'SelfEmployed', 'FamilyWork',
'Unemployment']]

######## Plot 1 Heatmap/Correlation graph for US Census Dataset #######

plt.figure(figsize=(30, 8))
heatmap = sb.heatmap(dataviz.corr(), vmin=-1, vmax=1, annot=True, cmap='BrBG')
heatmap.set_title('Correlation Heatmap for US Census Data', fontdict={'fontsize':18}, pad=12);


####### plot 2 Creating filled maps for US Census (Stae Vs Income per capita) ###########

state_codes = {
    'District of Columbia' : 'dc','Mississippi': 'MS', 'Oklahoma': 'OK', 
    'Delaware': 'DE', 'Minnesota': 'MN', 'Illinois': 'IL', 'Arkansas': 'AR', 
    'New Mexico': 'NM', 'Indiana': 'IN', 'Maryland': 'MD', 'Louisiana': 'LA', 
    'Idaho': 'ID', 'Wyoming': 'WY', 'Tennessee': 'TN', 'Arizona': 'AZ', 
    'Iowa': 'IA', 'Michigan': 'MI', 'Kansas': 'KS', 'Utah': 'UT', 
    'Virginia': 'VA', 'Oregon': 'OR', 'Connecticut': 'CT', 'Montana': 'MT', 
    'California': 'CA', 'Massachusetts': 'MA', 'West Virginia': 'WV', 
    'South Carolina': 'SC', 'New Hampshire': 'NH', 'Wisconsin': 'WI',
    'Vermont': 'VT', 'Georgia': 'GA', 'North Dakota': 'ND', 
    'Pennsylvania': 'PA', 'Florida': 'FL', 'Alaska': 'AK', 'Kentucky': 'KY', 
    'Hawaii': 'HI', 'Nebraska': 'NE', 'Missouri': 'MO', 'Ohio': 'OH', 
    'Alabama': 'AL', 'Rhode Island': 'RI', 'South Dakota': 'SD', 
    'Colorado': 'CO', 'New Jersey': 'NJ', 'Washington': 'WA', 
    'North Carolina': 'NC', 'New York': 'NY', 'Texas': 'TX', 
    'Nevada': 'NV', 'Maine': 'ME','Puerto Rico': 'PR'}

US_census_data['state_code'] = US_census_data['State'].apply(lambda x : state_codes[x])
grouped_US_data=US_census_data.groupby(["State", "state_code"],as_index=False)["IncomePerCap"].mean()

fig = px.choropleth(grouped_US_data,
                    locations='state_code', 
                    locationmode="USA-states", 
                    scope="usa",
                    color='IncomePerCap',
                    color_continuous_scale="Viridis_r")

fig=fig.add_scattergeo(
    locations=grouped_US_data['state_code'],
    locationmode="USA-states", 
    text=grouped_US_data['State'],
    mode='text',
)

plot(fig)

####### Plot 3 Happiness dataset/Heatmap correlation plot ########

Happiness_data=pd.read_csv('Happinessdataset_combined.csv')

plt.figure(figsize=(30, 8))
heatmap = sb.heatmap(Happiness_data.corr(), vmin=-1, vmax=1, annot=True, cmap='BrBG')
heatmap.set_title('Correlation Heatmap for HappinessData', fontdict={'fontsize':18}, pad=12);

####### PLot 4 Happiness data/Animated Scatter plot #########

fig=px.scatter(data_frame = Happiness_data, 
           x = 'Trust',
           y = 'Generosity', 
           size = 'HappinessRank', 
           hover_name = 'Country', 
           color = 'Country',
           animation_frame = 'Year',
           animation_group = 'Country',
           range_x = [0,0.5],
           range_y = [0,0.5])

fig.layout.updatemenus[0].buttons[0].args[1]["frame"]["duration"] = 2000

plot(fig)




