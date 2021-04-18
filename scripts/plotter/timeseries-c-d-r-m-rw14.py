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

# Should be >= 7 to be meaningful.
win_width = 14
win = RKIDataRef.pad().rolling(window=14)

# Clean window
win_clean = win.sum()/14 

def main():

    def plotDe():

        fig,ax1 = plt.subplots()
        # add second y axis
        ax2 = ax1.twinx()
        # Figure size
        fig.set_figheight(8.0)
        fig.set_figwidth(14.0)

        ax = plt.gca()
        formatter = mdates.DateFormatter("%Y/%m/%d")
        ax.xaxis.set_major_formatter(formatter)
        locator = mdates.DayLocator()
        ax.xaxis.set_major_locator(locator)

        # Solution by: https://stackoverflow.com/questions/50820043/hiding-xticks-labels-every-n-th-label-or-on-value-on-pandas-plot-make-x-axis-r
        # Print just x datetime dates
        plt.gca().xaxis.set_major_locator(plt.MaxNLocator(8))

        ax1.plot(
            meldedatum, 
            RKIDataMelde['AnzahlFall'], 
            color = 'red', 
            marker='o',
            markersize=0.4,
            linestyle='None',

            label='Anzahl Fälle nach Meldedatum'
        )

        # Cases for 'Refdatum'
        ax1.plot(
            refdatum, 
            win_clean['AnzahlFall'], 
            color = 'red', 
            marker=None, 
            linestyle='solid',

            label='Anzahl Fälle nach Referenzdatum, gleitender Durchschnitt über 14 Tage', 
        )

        # deaths for 'Meldedatum'
        ax2.plot(
            meldedatum, 
            RKIDataMelde['AnzahlTodesfall'], 
            color="black",
            marker='o',
            markersize=0.4,
            linestyle='None',

            label='Anzahl Todesfälle nach Meldedatum', 
        )

        # deaths for 'Refdatum'
        ax2.plot(
            refdatum, 
            win_clean['AnzahlTodesfall'], 
            color="black",
            linestyle="solid", 
            marker=None, 

            label='Anzahl Todesfälle nach Referenzdatum, gleitender Durchschnitt über 14 Tage', 
        )
    
        plt.title('Gemeldete Fälle und Todesfälle')
        ax1.set_ylabel('Anzahl Fälle')
        ax2.set_ylabel('Anzahl Tode')

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
        graph_ax1, _ = ax1.get_legend_handles_labels()
        graph_ax2, _ = ax2.get_legend_handles_labels()

        plt.legend(
            graph_ax1 + graph_ax2,
            [
                'Anzahl Fälle nach Meldedatum',
                'Anzahl Fälle nach Referenzdatum, gleitender Durchschnitt über 14 Tage',
                'Anzahl Todesfälle nach Meldedatum',
                'Anzahl Todesfälle nach Referenzdatum, gleitender Durchschnitt über 14 Tage',
            ],
            loc="upper left",
            frameon=False,
            # Add more then one dot to legend + set handels longer: https://matplotlib.org/stable/api/figure_api.html?highlight=handlelength#module-matplotlib.figure 
            handlelength=2.5,
            numpoints=2,
        )

        # Save plot
        plt.savefig(os.path.join('plots/rki','timeseries-c-d-r-m-rw14.de.png'),dpi=200,pad_inches=5)

    def plotEn():

        # Figure size
        fig,ax1 = plt.subplots()
        # add second y axis
        ax2 = ax1.twinx()
        # Figure size
        fig.set_figheight(8.0)
        fig.set_figwidth(14.0)

        ax = plt.gca()
        formatter = mdates.DateFormatter("%Y/%m/%d")
        ax.xaxis.set_major_formatter(formatter)
        locator = mdates.DayLocator()
        ax.xaxis.set_major_locator(locator)

        # Solution by: https://stackoverflow.com/questions/50820043/hiding-xticks-labels-every-n-th-label-or-on-value-on-pandas-plot-make-x-axis-r
        # Print just x datetime dates
        plt.gca().xaxis.set_major_locator(plt.MaxNLocator(8))

        # Cases for 'Meldedatum' 
        ax1.plot(
            meldedatum, 
            RKIDataMelde['AnzahlFall'], 
            color = 'red', 
            marker='o',
            markersize=0.4,
            linestyle='None',

            label='Count cases by reporting date', 
        )

        # Cases for 'Refdatum'
        ax1.plot(
            refdatum, 
            win_clean['AnzahlFall'], 
            color = 'red', 
            marker=None, 
            linestyle='solid',

            label='Count cases by reference date, rolling window 14 days width', 
        )


        # deaths for 'Meldedatum'
        ax2.plot(
            meldedatum, 
            RKIDataMelde['AnzahlTodesfall'], 
            color="black",
            marker='o',
            markersize=0.4,
            linestyle='None',

            label='Count deaths by reporting date', 
        )

        # deaths for 'Refdatum'
        ax2.plot(
            refdatum, 
            win_clean['AnzahlTodesfall'], 
            color="black",
            marker=None, 
            linestyle='solid',


            label='Count deaths by reference date, rolling window 14 days width', 
        )
    
        plt.title('Reported Cases and Deaths')
        ax1.set_ylabel('Count Cases')
        ax2.set_ylabel('Count Death')

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
                # Add legend 
        graph_ax1, _ = ax1.get_legend_handles_labels()
        graph_ax2, _ = ax2.get_legend_handles_labels()

        plt.legend(
            graph_ax1 + graph_ax2,
            [
                'Count cases by reporting date',
                'Count cases by reference date, rolling window 14 days width',
                'Count deaths by reporting date',
                'Count deaths by reference date, rolling window 14 days width',
            ],
            loc="upper left",
            frameon=False,
            # Add more then one dot to legend + set handels longer: https://matplotlib.org/stable/api/figure_api.html?highlight=handlelength#module-matplotlib.figure 
            handlelength=2.5,
            numpoints=2,
        )

        # Save plot
        plt.savefig(os.path.join('plots/rki','timeseries-c-d-r-m-rw14.en.png'),dpi=200,pad_inches=5)

    plotDe()
    plotEn()

if __name__ == "__main__":
    main()