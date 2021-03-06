"""
This file uses the current data CSV (^1) from RKI to plot infection and death cases in an timeseries.

^1: https://npgeo-corona-npgeo-de.hub.arcgis.com/datasets/dd4580c810204019a7b8eb3e0b329dd6_0
"""

import os
import datetime 
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates

# Change float format for pandas (1.0 -> 1)
pd.options.display.float_format = '{:,.0f}'.format


# Get data
# RKIData = pd.read_csv(
#     'https://opendata.arcgis.com/datasets/dd4580c810204019a7b8eb3e0b329dd6_0.csv',
     
#     parse_dates=True
# )

# last_row = RKIData.iloc[-1]
# last_datenstand = last_row['Datenstand']

# RKIDataMelde = RKIData.drop(["Altersgruppe2","ObjectId","IdBundesland","Bundesland","Landkreis","Altersgruppe","Geschlecht","IdLandkreis","Datenstand","NeuerFall","NeuerTodesfall","NeuGenesen","AnzahlGenesen","IstErkrankungsbeginn","Refdatum"],axis=1)
# RKIDataRef = RKIData.drop(["Altersgruppe2","ObjectId","IdBundesland","Bundesland","Landkreis","Altersgruppe","Geschlecht","IdLandkreis","Datenstand","NeuerFall","NeuerTodesfall","NeuGenesen","AnzahlGenesen","IstErkrankungsbeginn","Meldedatum"],axis=1)

# RKIDataMeldeClean = RKIDataMelde.groupby('Meldedatum').sum().reset_index()
# RKIDataMeldeClean = RKIDataMeldeClean.head(900)
# RKIDataMeldeClean.sum().reset_index()
# RKIDataMelde = RKIDataMeldeClean

# RKIDataRefClean = RKIDataRef.groupby('Refdatum').sum().reset_index()
# RKIDataRefClean  = RKIDataRefClean .head(900)
# RKIDataRefClean .sum().reset_index()

RKIDataMelde = pd.read_csv('./data/rki/rki-cdr-melde.csv')
RKIDataRef = pd.read_csv('./data/rki/rki-cdr-ref.csv')

last_row = RKIDataMelde.iloc[-1]
last_datenstand = last_row['Meldedatum']

# Meldedatum
dates = RKIDataMelde['Meldedatum']
meldedatum = [datetime.datetime.strptime(d[:-12],"%Y/%m/%d").date() for d in dates]

# Refdatum
refdates = RKIDataRef['Refdatum']
refdatum = [datetime.datetime.strptime(d[:-12],"%Y/%m/%d").date() for d in refdates]


def main():

    def plotDe():

        # Figure size
        plt.figure(figsize=(14.0, 8.0))

        ax = plt.gca()
        formatter = mdates.DateFormatter("%Y/%m/%d")
        ax.xaxis.set_major_formatter(formatter)
        locator = mdates.DayLocator()
        ax.xaxis.set_major_locator(locator)

        # Solution by: https://stackoverflow.com/questions/50820043/hiding-xticks-labels-every-n-th-label-or-on-value-on-pandas-plot-make-x-axis-r
        # Print just x datetime dates
        plt.gca().xaxis.set_major_locator(plt.MaxNLocator(8))

        # Cases for 'Meldedatum' 
        plt.plot(
            meldedatum, 
            RKIDataMelde['AnzahlFall'], 
            color = 'red', 
            marker=None, 
            linestyle='dotted',

            label='Anzahl F??lle nach Meldedatum', 
        )

        # Cases for 'Refdatum'
        plt.plot(
            refdatum, 
            RKIDataRef['AnzahlFall'], 
            color = 'red', 
            marker=None, 
            linestyle='solid',

            label='Anzahl F??lle nach Refdatum', 
        )


        # deaths for 'Meldedatum'
        plt.plot(
            meldedatum, 
            RKIDataMelde['AnzahlTodesfall'], 
            color="black",
            linestyle="dotted", 
            marker=None, 

            label='Anzahl Todesf??lle nach Meldedatum', 
        )

        # deaths for 'Refdatum'
        plt.plot(
            refdatum, 
            RKIDataRef['AnzahlTodesfall'], 
            color="black",
            linestyle="solid", 
            marker=None, 

            label='Anzahl Todesf??lle nach Refdatum', 
        )
    
        plt.title('Gemeldete F??lle und Todesf??lle')
        plt.ylabel('Anzahl')
        plt.xlabel('')

        # remove borders
        plt.gca().spines["top"].set_alpha(0.0)    
        plt.gca().spines["bottom"].set_alpha(0.5)
        plt.gca().spines["right"].set_alpha(0.0)    
        plt.gca().spines["left"].set_alpha(0.5)   
        plt.legend(loc='upper right', ncol=2, fontsize=12)

        # add link to repo 
        plt.text(
                0.005,
                0.01,
                "https://github.com/masdot/cdp-corona-data-project",
                fontsize=8,
                transform=ax.transAxes,
                color="#666666",
        )

        # added data source and last "Datenstand"
        plt.text(
        0.5,
        -0.12, 
        f"Datenquelle: Robert-Koch-Institut (Datenstand {last_datenstand[:-12]})", 
        size=10, 
        ha="center", 
        transform=ax.transAxes,
        color='black',
        )

        # Add legend 
        plt.legend()

        # Save plot
        plt.savefig(os.path.join('plots/rki','timeseries-cd-r-m.de.png'),dpi=200,pad_inches=5)

    def plotEn():

        # Figure size
        plt.figure(figsize=(14.0, 8.0))

        ax = plt.gca()
        formatter = mdates.DateFormatter("%Y/%m/%d")
        ax.xaxis.set_major_formatter(formatter)
        locator = mdates.DayLocator()
        ax.xaxis.set_major_locator(locator)

        # Solution by: https://stackoverflow.com/questions/50820043/hiding-xticks-labels-every-n-th-label-or-on-value-on-pandas-plot-make-x-axis-r
        # Print just x datetime dates
        plt.gca().xaxis.set_major_locator(plt.MaxNLocator(8))

        # Cases for 'Meldedatum' 
        plt.plot(
            meldedatum, 
            RKIDataMelde['AnzahlFall'], 
            color = 'red', 
            marker=None, 
            linestyle='dotted',

            label='Count cases by reporting date', 
        )

        # Cases for 'Refdatum'
        plt.plot(
            refdatum, 
            RKIDataRef['AnzahlFall'], 
            color = 'red', 
            marker=None, 
            linestyle='solid',

            label='Count cases by reference date', 
        )


        # deaths for 'Meldedatum'
        plt.plot(
            meldedatum, 
            RKIDataMelde['AnzahlTodesfall'], 
            color="black",
            linestyle="dotted", 
            marker=None, 

            label='Count deaths by reporting date', 
        )

        # deaths for 'Refdatum'
        plt.plot(
            refdatum, 
            RKIDataRef['AnzahlTodesfall'], 
            color="black",
            linestyle="solid", 
            marker=None, 

            label='Count deaths by reference date', 
        )
    
        plt.title('Reported Cases and Deaths')
        plt.ylabel('Count')
        plt.xlabel('')

        # remove borders
        plt.gca().spines["top"].set_alpha(0.0)    
        plt.gca().spines["bottom"].set_alpha(0.5)
        plt.gca().spines["right"].set_alpha(0.0)    
        plt.gca().spines["left"].set_alpha(0.5)   
        plt.legend(loc='upper right', ncol=2, fontsize=12)

        # add link to repo 
        plt.text(
                0.005,
                0.01,
                "https://github.com/masdot/cdp-corona-data-project",
                fontsize=8,
                transform=ax.transAxes,
                color="#666666",
        )

        # added data source and last "Datenstand"
        plt.text(
        0.5,
        -0.12, 
        f"Data source: Robert-Koch-Institut (Data status: {last_datenstand[:-12]})", 
        size=10, 
        ha="center", 
        transform=ax.transAxes,
        color='black',
        )

        # Add legend 
        plt.legend(frameon=False)

        # Save plot
        plt.savefig(os.path.join('plots/rki','timeseries-cd-r-m.en.png'),dpi=200,pad_inches=5)

    plotDe()
    plotEn()

if __name__ == "__main__":
    main()