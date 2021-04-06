import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)

plt.rcParams['agg.path.chunksize'] = 10000

RKIData = pd.read_csv('https://opendata.arcgis.com/datasets/dd4580c810204019a7b8eb3e0b329dd6_0.csv');
RKIData = RKIData[RKIData.Geschlecht.str.contains("unbekannt") == False]
RKIData = RKIData[RKIData.Altersgruppe.str.contains("unbekannt") == False]

# dataframe
frame_pr = RKIData.drop(['NeuGenesen', 'AnzahlGenesen', 'IstErkrankungsbeginn', 'ObjectId', 'IdBundesland', 'IdLandkreis', 'NeuerFall', 'NeuerTodesfall'],axis=1)
frame_pr.abs
#? frame = frame_pr.groupby(['Meldedatum']

# from dateutil.parser import parse 

# # Import Data
df = frame_pr
# # Prepare data
bundeslaender = df['Bundesland'].unique()
# # Draw Plot
# mycolors = ['tab:red', 'tab:blue', 'tab:green', 'tab:orange', 'tab:brown', 'tab:grey', 'tab:pink', 'tab:olive', 'deeppink', 'steelblue', 'firebrick', 'mediumseagreen']      
# plt.figure(figsize=(16,10), dpi= 80)

for i in enumerate(bundeslaender):
    plt.plot(df['AnzahlFall'], df['Meldedatum'], color='red', label='test')
    # plt.text(df.loc[df.year==y, :].shape[0]-.9, df.loc[df.year==y, 'traffic'][-1:].values[0], y, fontsize=12, color=mycolors[i])

plt.show()
# plt.plot(df['AnzahlFall'], df['Meldedatum'], color='red', label='test')

# # Decoration
# # plt.ylim(50,750)
# # plt.xlim(-0.3, 11)
# # plt.ylabel('Anzahl')
# # plt.yticks(fontsize=12, alpha=.7)
# # plt.title("Neuinfektionen nach Bundesländern", fontsize=22)
# # plt.grid(axis='y', alpha=.3)

# # Remove borders
# # plt.gca().spines["top"].set_alpha(0.0)    
# # plt.gca().spines["bottom"].set_alpha(0.5)
# # plt.gca().spines["right"].set_alpha(0.0)    
# # plt.gca().spines["left"].set_alpha(0.5)   
# # plt.legend(loc='upper right', ncol=2, fontsize=12)
# plt.show()

# #* Bundesländer alphabetisch
# Baden-Württemberg
# Bayern
# Berlin 
# Brandenburg
# Bremen 
# Hamburg 
# Hessen
# Mecklenburg-Vorpommern
# Niedersachsen
# Nordrhein-Westfalen
# Rheinland-Pfalz
# Saarland
# Sachsen
# Sachsen-Anhalt
# Schleswig-Holstein
# Thüringen
# x = np.linspace(0, 2, 100)

# fig, ax = plt.subplots()  # Create a figure and an axes.
# ax.plot(x, x, label='bl1')  # Plot some data on the axes.
# ax.plot(x, x**2, label='bl2')  # Plot more data on the axes...
# ax.plot(x, x**3, label='bl3')  # ... and some more.
# # ax.set_xlabel('x label')  # Add an x-label to the axes.
# # ax.set_ylabel('y label')  # Add a y-label to the axes.
# # ax.set_title("Simple Plot")  # Add a title to the axes.
# ax.legend()  # Add a legend.
