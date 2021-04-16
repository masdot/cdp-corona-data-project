"""

"""
import pandas as pd

# Remove max from cols + row for large dataframes
pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)

# Download newest CSV file with RKI data
RKIData = pd.read_csv('https://opendata.arcgis.com/datasets/c2f3c3b935a242169c6bec82e1fa573e_0.csv');

# Clean dataframe, removed unused cols
RKIData = RKIData.drop(['AnzAktivNeu', 'AnzAktiv', 'AnzGenesenNeu', 'AnzGenesen', 'AnzFall7T', 'ObjectId'],axis=1)

# RKI dataframe for AdmUnitId = 0 (DE gesamt)
class DataBR:
  RKIDataBR = RKIData.loc[RKIData['AdmUnitId'] == 0]
  AnzFall = int(RKIDataBR.iloc[0]['AnzFall'])
  AnzTodesfall = int(RKIDataBR.iloc[0]['AnzTodesfall'])
  Inz7T = RKIDataBR.iloc[0]['Inz7T']
  AnzFallNeu = int(RKIDataBR.iloc[0]['AnzFallNeu'])
  AnzTodesfallNeu = int(RKIDataBR.iloc[0]['AnzTodesfallNeu'])
  def __init__(self, AnzFall, AnzTodesfall, Inz7T):
    self.AnzFall = AnzFall
    self.AnzTodesfall = AnzTodesfall
    self.Inz7T = Inz7T


# RKI dataframe for Bundesländer, AdmUnitId = 1-16
class DataBundeslaender:
  class SH:
    RKIDataSH = RKIData.loc[RKIData['AdmUnitId'] == 1]
    AnzFall = int(RKIDataSH.iloc[0]['AnzFall'])
    AnzTodesfall = int(RKIDataSH.iloc[0]['AnzTodesfall'])
    Inz7T = RKIDataSH.iloc[0]['Inz7T']
    AnzFallNeu = int(RKIDataSH.iloc[0]['AnzFallNeu'])
    AnzTodesfallNeu = int(RKIDataSH.iloc[0]['AnzTodesfallNeu'])
    def __init__(self, AnzFall, AnzTodesfall, Inz7T, AnzFallNeu, AnzTodesfallNeu):
      self.AnzFall = AnzFall
      self.AnzTodesfall = AnzTodesfall
      self.Inz7T = Inz7T
      self.AnzFallNeu = AnzFallNeu
      self.AnzTodesfallNeu = AnzTodesfallNeu
  class HH:
    RKIDataHH = RKIData.loc[RKIData['AdmUnitId'] == 2]
    AnzFall = int(RKIDataHH.iloc[0]['AnzFall'])
    AnzTodesfall = int(RKIDataHH.iloc[0]['AnzTodesfall'])
    Inz7T = RKIDataHH.iloc[0]['Inz7T']
    AnzFallNeu = int(RKIDataHH.iloc[0]['AnzFallNeu'])
    AnzTodesfallNeu = int(RKIDataHH.iloc[0]['AnzTodesfallNeu'])
    def __init__(self, AnzFall, AnzTodesfall, Inz7T, AnzFallNeu, AnzTodesfallNeu):
      self.AnzFall = AnzFall
      self.AnzTodesfall = AnzTodesfall
      self.Inz7T = Inz7T
      self.AnzFallNeu = AnzFallNeu
      self.AnzTodesfallNeu = AnzTodesfallNeu
  class NI:
    RKIDataNI = RKIData.loc[RKIData['AdmUnitId'] == 3]
    AnzFall = int(RKIDataNI.iloc[0]['AnzFall'])
    AnzTodesfall = int(RKIDataNI.iloc[0]['AnzTodesfall'])
    Inz7T = RKIDataNI.iloc[0]['Inz7T']
    AnzFallNeu = int(RKIDataNI.iloc[0]['AnzFallNeu'])
    AnzTodesfallNeu = int(RKIDataNI.iloc[0]['AnzTodesfallNeu'])
    def __init__(self, AnzFall, AnzTodesfall, Inz7T, AnzFallNeu, AnzTodesfallNeu):
      self.AnzFall = AnzFall
      self.AnzTodesfall = AnzTodesfall
      self.Inz7T = Inz7T
      self.AnzFallNeu = AnzFallNeu
      self.AnzTodesfallNeu = AnzTodesfallNeu
  class HB:
    RKIDataHB = RKIData.loc[RKIData['AdmUnitId'] == 4]
    AnzFall = int(RKIDataHB.iloc[0]['AnzFall'])
    AnzTodesfall = int(RKIDataHB.iloc[0]['AnzTodesfall'])
    Inz7T = RKIDataHB.iloc[0]['Inz7T']
    AnzFallNeu = int(RKIDataHB.iloc[0]['AnzFallNeu'])
    AnzTodesfallNeu = int(RKIDataHB.iloc[0]['AnzTodesfallNeu'])
    def __init__(self, AnzFall, AnzTodesfall, Inz7T, AnzFallNeu, AnzTodesfallNeu):
      self.AnzFall = AnzFall
      self.AnzTodesfall = AnzTodesfall
      self.Inz7T = Inz7T
      self.AnzFallNeu = AnzFallNeu
      self.AnzTodesfallNeu = AnzTodesfallNeu
  class NW:
    RKIDataNW = RKIData.loc[RKIData['AdmUnitId'] == 5]
    AnzFall = int(RKIDataNW.iloc[0]['AnzFall'])
    AnzTodesfall = int(RKIDataNW.iloc[0]['AnzTodesfall'])
    Inz7T = RKIDataNW.iloc[0]['Inz7T']
    AnzFallNeu = int(RKIDataNW.iloc[0]['AnzFallNeu'])
    AnzTodesfallNeu = int(RKIDataNW.iloc[0]['AnzTodesfallNeu'])
    def __init__(self, AnzFall, AnzTodesfall, Inz7T, AnzFallNeu, AnzTodesfallNeu):
      self.AnzFall = AnzFall
      self.AnzTodesfall = AnzTodesfall
      self.Inz7T = Inz7T
      self.AnzFallNeu = AnzFallNeu
      self.AnzTodesfallNeu = AnzTodesfallNeu
  class HE:
    RKIDataHE = RKIData.loc[RKIData['AdmUnitId'] == 6]
    AnzFall = int(RKIDataHE.iloc[0]['AnzFall'])
    AnzTodesfall = int(RKIDataHE.iloc[0]['AnzTodesfall'])
    Inz7T = RKIDataHE.iloc[0]['Inz7T']
    AnzFallNeu = int(RKIDataHE.iloc[0]['AnzFallNeu'])
    AnzTodesfallNeu = int(RKIDataHE.iloc[0]['AnzTodesfallNeu'])
    def __init__(self, AnzFall, AnzTodesfall, Inz7T, AnzFallNeu, AnzTodesfallNeu):
      self.AnzFall = AnzFall
      self.AnzTodesfall = AnzTodesfall
      self.Inz7T = Inz7T
      self.AnzFallNeu = AnzFallNeu
      self.AnzTodesfallNeu = AnzTodesfallNeu
  class RP:
    RKIDataRP = RKIData.loc[RKIData['AdmUnitId'] == 7]
    AnzFall = int(RKIDataRP.iloc[0]['AnzFall'])
    AnzTodesfall = int(RKIDataRP.iloc[0]['AnzTodesfall'])
    Inz7T = RKIDataRP.iloc[0]['Inz7T']
    AnzFallNeu = int(RKIDataRP.iloc[0]['AnzFallNeu'])
    AnzTodesfallNeu = int(RKIDataRP.iloc[0]['AnzTodesfallNeu'])
    def __init__(self, AnzFall, AnzTodesfall, Inz7T, AnzFallNeu, AnzTodesfallNeu):
      self.AnzFall = AnzFall
      self.AnzTodesfall = AnzTodesfall
      self.Inz7T = Inz7T
      self.AnzFallNeu = AnzFallNeu
      self.AnzTodesfallNeu = AnzTodesfallNeu
  class BW:
    RKIDataBW = RKIData.loc[RKIData['AdmUnitId'] == 8]
    AnzFall = int(RKIDataBW.iloc[0]['AnzFall'])
    AnzTodesfall = int(RKIDataBW.iloc[0]['AnzTodesfall'])
    Inz7T = RKIDataBW.iloc[0]['Inz7T']
    AnzFallNeu = int(RKIDataBW.iloc[0]['AnzFallNeu'])
    AnzTodesfallNeu = int(RKIDataBW.iloc[0]['AnzTodesfallNeu'])
    def __init__(self, AnzFall, AnzTodesfall, Inz7T, AnzFallNeu, AnzTodesfallNeu):
      self.AnzFall = AnzFall
      self.AnzTodesfall = AnzTodesfall
      self.Inz7T = Inz7T
      self.AnzFallNeu = AnzFallNeu
      self.AnzTodesfallNeu = AnzTodesfallNeu
  class BY:
    RKIDataBY = RKIData.loc[RKIData['AdmUnitId'] == 9]
    AnzFall = int(RKIDataBY.iloc[0]['AnzFall'])
    AnzTodesfall = int(RKIDataBY.iloc[0]['AnzTodesfall'])
    Inz7T = RKIDataBY.iloc[0]['Inz7T']
    AnzFallNeu = int(RKIDataBY.iloc[0]['AnzFallNeu'])
    AnzTodesfallNeu = int(RKIDataBY.iloc[0]['AnzTodesfallNeu'])
    def __init__(self, AnzFall, AnzTodesfall, Inz7T, AnzFallNeu, AnzTodesfallNeu):
      self.AnzFall = AnzFall
      self.AnzTodesfall = AnzTodesfall
      self.Inz7T = Inz7T
      self.AnzFallNeu = AnzFallNeu
      self.AnzTodesfallNeu = AnzTodesfallNeu
  class SL:
    RKIDataSL = RKIData.loc[RKIData['AdmUnitId'] == 10]
    AnzFall = int(RKIDataSL.iloc[0]['AnzFall'])
    AnzTodesfall = int(RKIDataSL.iloc[0]['AnzTodesfall'])
    Inz7T = RKIDataSL.iloc[0]['Inz7T']
    AnzFallNeu = int(RKIDataSL.iloc[0]['AnzFallNeu'])
    AnzTodesfallNeu = int(RKIDataSL.iloc[0]['AnzTodesfallNeu'])
    def __init__(self, AnzFall, AnzTodesfall, Inz7T, AnzFallNeu, AnzTodesfallNeu):
      self.AnzFall = AnzFall
      self.AnzTodesfall = AnzTodesfall
      self.Inz7T = Inz7T
      self.AnzFallNeu = AnzFallNeu
      self.AnzTodesfallNeu = AnzTodesfallNeu
  class BE:
    RKIDataBE = RKIData.loc[RKIData['AdmUnitId'] == 11]
    AnzFall = int(RKIDataBE.iloc[0]['AnzFall'])
    AnzTodesfall = int(RKIDataBE.iloc[0]['AnzTodesfall'])
    Inz7T = RKIDataBE.iloc[0]['Inz7T']
    AnzFallNeu = int(RKIDataBE.iloc[0]['AnzFallNeu'])
    AnzTodesfallNeu = int(RKIDataBE.iloc[0]['AnzTodesfallNeu'])
    def __init__(self, AnzFall, AnzTodesfall, Inz7T, AnzFallNeu, AnzTodesfallNeu):
      self.AnzFall = AnzFall
      self.AnzTodesfall = AnzTodesfall
      self.Inz7T = Inz7T
      self.AnzFallNeu = AnzFallNeu
      self.AnzTodesfallNeu = AnzTodesfallNeu
  class BB:
    RKIDataBB = RKIData.loc[RKIData['AdmUnitId'] == 12]
    AnzFall = int(RKIDataBB.iloc[0]['AnzFall'])
    AnzTodesfall = int(RKIDataBB.iloc[0]['AnzTodesfall'])
    Inz7T = RKIDataBB.iloc[0]['Inz7T']
    AnzFallNeu = int(RKIDataBB.iloc[0]['AnzFallNeu'])
    AnzTodesfallNeu = int(RKIDataBB.iloc[0]['AnzTodesfallNeu'])
    def __init__(self, AnzFall, AnzTodesfall, Inz7T, AnzFallNeu, AnzTodesfallNeu):
      self.AnzFall = AnzFall
      self.AnzTodesfall = AnzTodesfall
      self.Inz7T = Inz7T
      self.AnzFallNeu = AnzFallNeu
      self.AnzTodesfallNeu = AnzTodesfallNeu
  class MV:
    RKIDataMV = RKIData.loc[RKIData['AdmUnitId'] == 13]
    AnzFall = int(RKIDataMV.iloc[0]['AnzFall'])
    AnzTodesfall = int(RKIDataMV.iloc[0]['AnzTodesfall'])
    Inz7T = RKIDataMV.iloc[0]['Inz7T']
    AnzFallNeu = int(RKIDataMV.iloc[0]['AnzFallNeu'])
    AnzTodesfallNeu = int(RKIDataMV.iloc[0]['AnzTodesfallNeu'])
    def __init__(self, AnzFall, AnzTodesfall, Inz7T, AnzFallNeu, AnzTodesfallNeu):
      self.AnzFall = AnzFall
      self.AnzTodesfall = AnzTodesfall
      self.Inz7T = Inz7T
      self.AnzFallNeu = AnzFallNeu
      self.AnzTodesfallNeu = AnzTodesfallNeu
  class SN:
    RKIDataSN = RKIData.loc[RKIData['AdmUnitId'] == 14]
    AnzFall = int(RKIDataSN.iloc[0]['AnzFall'])
    AnzTodesfall = int(RKIDataSN.iloc[0]['AnzTodesfall'])
    Inz7T = RKIDataSN.iloc[0]['Inz7T']
    AnzFallNeu = int(RKIDataSN.iloc[0]['AnzFallNeu'])
    AnzTodesfallNeu = int(RKIDataSN.iloc[0]['AnzTodesfallNeu'])
    def __init__(self, AnzFall, AnzTodesfall, Inz7T, AnzFallNeu, AnzTodesfallNeu):
      self.AnzFall = AnzFall
      self.AnzTodesfall = AnzTodesfall
      self.Inz7T = Inz7T
      self.AnzFallNeu = AnzFallNeu
      self.AnzTodesfallNeu = AnzTodesfallNeu
  class ST:
    RKIDataST = RKIData.loc[RKIData['AdmUnitId'] == 15]
    AnzFall = int(RKIDataST.iloc[0]['AnzFall'])
    AnzTodesfall = int(RKIDataST.iloc[0]['AnzTodesfall'])
    Inz7T = RKIDataST.iloc[0]['Inz7T']
    AnzFallNeu = int(RKIDataST.iloc[0]['AnzFallNeu'])
    AnzTodesfallNeu = int(RKIDataST.iloc[0]['AnzTodesfallNeu'])
    def __init__(self, AnzFall, AnzTodesfall, Inz7T, AnzFallNeu, AnzTodesfallNeu):
      self.AnzFall = AnzFall
      self.AnzTodesfall = AnzTodesfall
      self.Inz7T = Inz7T
      self.AnzFallNeu = AnzFallNeu
      self.AnzTodesfallNeu = AnzTodesfallNeu
  class TH:
    RKIDataTH = RKIData.loc[RKIData['AdmUnitId'] == 16]
    AnzFall = int(RKIDataTH.iloc[0]['AnzFall'])
    AnzTodesfall = int(RKIDataTH.iloc[0]['AnzTodesfall'])
    Inz7T = RKIDataTH.iloc[0]['Inz7T']
    AnzFallNeu = int(RKIDataTH.iloc[0]['AnzFallNeu'])
    AnzTodesfallNeu = int(RKIDataTH.iloc[0]['AnzTodesfallNeu'])
    def __init__(self, AnzFall, AnzTodesfall, Inz7T, AnzFallNeu, AnzTodesfallNeu):
      self.AnzFall = AnzFall
      self.AnzTodesfall = AnzTodesfall
      self.Inz7T = Inz7T
      self.AnzFallNeu = AnzFallNeu
      self.AnzTodesfallNeu = AnzTodesfallNeu