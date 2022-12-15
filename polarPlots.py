import csv
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

import_filename = "2D Measurements/corr_test.txt"
export_filename_Cl = "2D, Cl.csv"
export_filename_Cd = "2D, Cd.csv"
export_filename_Cm = "2D, Cm.csv"

def importData(filename):
    # Takes : filename
    # Returns : Pandas DataFrame with the data
    maxIndex = 5
    data = pd.DataFrame([np.empty(maxIndex)])
    with open(filename, "r") as csvfile:
        reader = csv.reader(csvfile, delimiter="\t")
        index = 0
        for row in reader:
            if index == 0:
                # Meaning the first 2 lines which are actually strings
                header = []
                for value in row:
                    temp_string = value.strip()
                    header.append(temp_string)
                data.columns = header[0:maxIndex]
            elif index >= 2:
                temp_list = []
                for value in row:
                    try:
                        float_value = float(value)
                        temp_list.append(float_value)
                    except ValueError:
                        float_value = 0.0
                        temp_list.append(float_value)
                temp_df = pd.DataFrame([temp_list[0:maxIndex]], columns=data.columns)
                data = pd.concat([data, temp_df])
            index += 1
    return data


def plotLift(data):
    # Takes : DataFrame called data
    # Returns/Plots : seperated csv file w/ just the alpha and cl (that can be read by LaTex/overleaf), polar plot

    alpha_cl = data[["Alpha", "Cl"]]
    alpha_cl.plot(x="Alpha", y="Cl")
    plt.show()

    alpha_cl.to_csv(export_filename_Cl, index=False)

def plotDrag(data):
    # Takes : DataFrame called data
    # Returns/Plots : seperated csv file w/ just the alpha and Cd (that can be read by LaTex/overleaf), polar plot

    alpha_cd = data[["Alpha", "Cd"]]
    alpha_cd.plot(x="Alpha", y="Cd")
    plt.show()

    alpha_cd.to_csv(export_filename_Cd, index=False)

def plotMoment(data):
    # Takes : DataFrame called data
    # Returns/Plots : seperated csv file w/ just the alpha and Cm (that can be read by LaTex/overleaf), polar plot

    alpha_cd = data[["Alpha", "Cm"]]
    alpha_cd.plot(x="Alpha", y="Cm")
    plt.show()

    alpha_cd.to_csv(export_filename_Cm, index=False)

data = importData(import_filename)
plotLift(data)
plotDrag(data)
plotMoment(data)