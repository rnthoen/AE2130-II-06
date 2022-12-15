import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

from detect_transition import detect_wing_boundaries, calculate_vertical_averages, detect_transition_line
from lookup import sorted_measurements_2D, sorted_measurements_3D

# Create dataframe of average temperatures
def calculate_averages(input_folder):
    # Read all temperature data for given folder
    images = os.listdir(input_folder)
    
    data = []
    n = len(images)

    for image in images:
        file = f"{input_folder}/{image}"
        data.append(pd.read_csv(file, sep=";", header=None))

    # Calculate average temperature for each point
    average_temperatures = data[0]

    for i in range(1, n):
        average_temperatures = average_temperatures + data[i]
    average_temperatures = average_temperatures / n

    return average_temperatures


# Make the heatmaps
data_folder = "C:/Users/ruben/Documents/Github/AE2130-II-06/data/Group 6 - IR Images"
output_folder = "C:/Users/ruben/Documents/Github/AE2130-II-06/Infrared/Output/Heatmaps"
all_experiments = os.listdir(data_folder)

image_number = 1
for experiment in all_experiments:
    # all_alphas = os.listdir(f"{data_folder}/{experiment}")

    if experiment == "2D":
        all_alphas = sorted_measurements_2D
    elif experiment == "3D":
        all_alphas = sorted_measurements_3D
    
    for alpha in all_alphas:
        input_folder = f"{data_folder}/{experiment}/{alpha}"
        image_number_padded = str(image_number).zfill(3)
        output_filepath = f"{output_folder}/{image_number_padded}_NoLines_Heatmap_{experiment}_{alpha}.png"
        title = f"{experiment} at α = {alpha}°"

        average_temperatures = calculate_averages(input_folder)
        vertical_average_temperatures = calculate_vertical_averages(average_temperatures)
        wing_boundaries = detect_wing_boundaries(vertical_average_temperatures)
        x_trailing_edge = wing_boundaries[0]
        x_leading_edge = wing_boundaries[1]
        chord_length = x_leading_edge - x_trailing_edge

        heatmap = plt.imshow(average_temperatures, cmap="rainbow")

        plot_lines = False

        if plot_lines:

            # I'm not particularly proud of the following code, but it works.
            if experiment == "2D" and alpha == "-3":
                x_transition_line = 234
                plt.axvline(x=x_transition_line, color="black", linestyle="dotted", label="Transition line")
            elif experiment == "2D" and alpha == "-2":
                x_transition_line = 239
                plt.axvline(x=x_transition_line, color="black", linestyle="dotted", label="Transition line")
            elif experiment == "2D" and alpha == "-1":
                x_transition_line = 246
                plt.axvline(x=x_transition_line, color="black", linestyle="dotted", label="Transition line")
            elif experiment == "2D" and alpha == "0":
                x_transition_line = 249
                plt.axvline(x=x_transition_line, color="black", linestyle="dotted", label="Transition line")
            elif experiment == "2D" and alpha == "1":
                x_transition_line = 258
                plt.axvline(x=x_transition_line, color="black", linestyle="dotted", label="Transition line")
            elif experiment == "2D" and alpha == "2":
                x_transition_line = 264
                plt.axvline(x=x_transition_line, color="black", linestyle="dotted", label="Transition line")
            elif experiment == "2D" and alpha == "3":
                x_transition_line = 272
                plt.axvline(x=x_transition_line, color="black", linestyle="dotted", label="Transition line")
            elif experiment == "2D" and alpha == "3.5":
                x_transition_line = 275
                plt.axvline(x=x_transition_line, color="black", linestyle="dotted", label="Transition line")
            elif experiment == "2D" and alpha == "4":
                x_transition_line = 283
                plt.axvline(x=x_transition_line, color="black", linestyle="dotted", label="Transition line")
            elif experiment == "2D" and alpha == "4.5":
                x_transition_line = 288
                plt.axvline(x=x_transition_line, color="black", linestyle="dotted", label="Transition line")
            elif experiment == "2D" and alpha == "5":
                x_transition_line = 304
                plt.axvline(x=x_transition_line, color="black", linestyle="dotted", label="Transition line")
            elif experiment == "2D" and alpha == "5.5":
                x_transition_line = 324
                plt.axvline(x=x_transition_line, color="black", linestyle="dotted", label="Transition lines")
                x_transition_line = 357
                plt.axvline(x=x_transition_line, color="black", linestyle="dotted")
            elif experiment == "2D" and alpha == "6":
                x_transition_line = 329
                plt.axvline(x=x_transition_line, color="black", linestyle="dotted", label="Transition lines")
                x_transition_line = 384
                plt.axvline(x=x_transition_line, color="black", linestyle="dotted")
            elif experiment == "2D" and alpha == "6.5":
                x_transition_line = 374
                plt.axvline(x=x_transition_line, color="black", linestyle="dotted", label="Transition lines")
                x_transition_line = 398
                plt.axvline(x=x_transition_line, color="black", linestyle="dotted")
            elif experiment == "2D" and alpha == "7":
                x_transition_line = 400
                plt.axvline(x=x_transition_line, color="black", linestyle="dotted", label="Transition lines")
                x_transition_line = 409
                plt.axvline(x=x_transition_line, color="black", linestyle="dotted")
            elif experiment == "2D" and alpha == "7.5":
                x_transition_line = 408
                plt.axvline(x=x_transition_line, color="black", linestyle="dotted", label="Transition lines")
                x_transition_line = 412
                plt.axvline(x=x_transition_line, color="black", linestyle="dotted")
            elif experiment == "2D" and alpha == "8":
                x_transition_line = 414
                plt.axvline(x=x_transition_line, color="black", linestyle="dotted", label="Transition line")
            elif experiment == "2D" and alpha == "8.5":
                x_transition_line = 416
                plt.axvline(x=x_transition_line, color="black", linestyle="dotted", label="Transition line")
            elif experiment == "2D" and (alpha == "9" or alpha == "9.5" or alpha == "10"):
                x_transition_line = 416
                plt.axvline(x=x_transition_line, color="black", linestyle="dotted", label="Transition line")
            elif experiment == "3D" and alpha == "-3":
                x_transition_line = 234
                plt.axvline(x=x_transition_line, color="black", linestyle="dotted", label="Transition line")
            elif experiment == "3D" and alpha == "-2":
                x_transition_line = 240
                plt.axvline(x=x_transition_line, color="black", linestyle="dotted", label="Transition line")
            elif experiment == "3D" and alpha == "-1":
                x_transition_line = 249
                plt.axvline(x=x_transition_line, color="black", linestyle="dotted", label="Transition line")
            elif experiment == "3D" and alpha == "0":
                x_transition_line = 250
                plt.axvline(x=x_transition_line, color="black", linestyle="dotted", label="Transition line")
            elif experiment == "3D" and alpha == "1":
                x_transition_line = 257
                plt.axvline(x=x_transition_line, color="black", linestyle="dotted", label="Transition line")
            elif experiment == "3D" and alpha == "2":
                x_transition_line = 263
                plt.axvline(x=x_transition_line, color="black", linestyle="dotted", label="Transition line")
            elif experiment == "3D" and alpha == "3":
                x_transition_line = 267
                plt.axvline(x=x_transition_line, color="black", linestyle="dotted", label="Transition line")
            elif experiment == "3D" and alpha == "3.5":
                x_transition_line = 272
                plt.axvline(x=x_transition_line, color="black", linestyle="dotted", label="Transition line")
            elif experiment == "3D" and alpha == "4":
                x_transition_line = 276
                plt.axvline(x=x_transition_line, color="black", linestyle="dotted", label="Transition line")
            elif experiment == "3D" and alpha == "4.5":
                x_transition_line = 284
                plt.axvline(x=x_transition_line, color="black", linestyle="dotted", label="Transition line")
            elif experiment == "3D" and alpha == "5":
                x_transition_line = 286
                plt.axvline(x=x_transition_line, color="black", linestyle="dotted", label="Transition line")
            elif experiment == "3D" and alpha == "5.5":
                x_transition_line = 290
                x_list = [283, 287, 318]
                y_list = [379, 317,  53]
                plt.plot(x_list, y_list, color="black", linestyle="dotted", label="Transition line")
            elif experiment == "3D" and alpha == "6":
                x_transition_line = 313
                x_list = [302, 306, 355]
                y_list = [386, 267, 139]
                plt.plot(x_list, y_list, color="black", linestyle="dotted", label="Transition line")
            elif experiment == "3D" and alpha == "6.5":
                x_transition_line = 356
                x_list = [315, 358, 389]
                y_list = [369, 233,  35]
                plt.plot(x_list, y_list, color="black", linestyle="dotted", label="Transition line")
            elif experiment == "3D" and alpha == "7":
                x_transition_line = 371
                x_list = [348, 381, 395]
                y_list = [352, 216,  41]
                plt.plot(x_list, y_list, color="black", linestyle="dotted", label="Transition line")
            elif experiment == "3D" and alpha == "7.5":
                x_transition_line = 396
                x_list = [373, 396, 407]
                y_list = [362, 215,  39]
                plt.plot(x_list, y_list, color="black", linestyle="dotted", label="Transition line")
            elif experiment == "3D" and alpha == "8":
                x_transition_line = 403
                x_list = [382, 406, 413]
                y_list = [371, 227,  37]
                plt.plot(x_list, y_list, color="black", linestyle="dotted", label="Transition line")
            elif experiment == "3D" and alpha == "8.5":
                x_transition_line = 412
                x_list = [396, 412, 416]
                y_list = [378, 217,  43]
                plt.plot(x_list, y_list, color="black", linestyle="dotted", label="Transition line")
            elif experiment == "3D" and alpha == "9":
                x_transition_line = 415
                x_list = [399, 414, 418]
                y_list = [386, 239,  66]
                plt.plot(x_list, y_list, color="black", linestyle="dotted", label="Transition line")
            elif experiment == "3D" and (alpha == "9.5" or alpha == "10"):
                x_transition_line = 415
                plt.axvline(x=x_transition_line, color="black", linestyle="dotted", label="Transition line")

            # x_transition_line = detect_transition_line(vertical_average_temperatures, wing_boundaries)
            # plt.axvline(x=x_transition_line, color="black", linestyle="dotted", label="Transition line")
            plt.axvline(x=x_trailing_edge, color="black", linestyle="dashed", label="Wing boundaries")
            plt.axvline(x=x_leading_edge, color="black", linestyle="dashed")
            plt.legend()

            
            print(experiment, alpha, x_transition_line, x_trailing_edge, x_leading_edge)

        plt.colorbar(heatmap, label="T_average [°C]")
        plt.xlabel("x [px]")
        plt.ylabel("y [px]")
        plt.title(title)
        plt.savefig(output_filepath)
        # plt.show()
        plt.clf()            
        # print(f"Saved heatmap for {title}")

        image_number += 1
