import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# from make_heatmaps import calculate_averages
from lookup import sorted_measurements_2D, sorted_measurements_3D


# Calculate the vertical average temperatures
def calculate_vertical_averages(average_temperatures):
    vertical_average_temperatures = average_temperatures.mean()
    return vertical_average_temperatures

# Detect the wing boundaries with the average vertical temperatures
def detect_wing_boundaries(vertical_average_temperatures):
    n = len(vertical_average_temperatures)
    temperature_deltas = [0]
    for i in range(1, n):
        delta = vertical_average_temperatures[i] - vertical_average_temperatures[i-1]
        temperature_deltas.append(delta)

    x_trailing_edge = np.argmax(temperature_deltas[100:200]) + 100
    x_leading_edge = np.argmin(temperature_deltas[400:500]) + 400

    return (x_trailing_edge, x_leading_edge)

# Detect transition line
def detect_transition_line(vertical_average_temperatures, wing_boundaries):
    n = len(vertical_average_temperatures)
    window_size = 10

    group_average_temperatures = []

    start = wing_boundaries[0]
    end = wing_boundaries[1]

    j = start
    while j < end:
        grouped_temperatures = vertical_average_temperatures[j:j + window_size]
        group_average_temperature = np.mean(grouped_temperatures)
        group_average_temperatures.append(group_average_temperature)
        j += window_size

    m = len(group_average_temperatures)
    group_average_deltas = [0]
    crossed = False
    for k in range(1, m):
        delta = group_average_temperatures[k] - group_average_temperatures[k - 1]
        group_average_deltas.append(delta)
        if delta < 0 and not(crossed):
            crossed = True
            print(k)
            #TODO: Continue here

    plt.plot(group_average_deltas[2:-1], color="black")
    plt.axhline(y=0, color="red", linestyle="dashed")
    plt.show()
    plt.clf()

    x_transition_line = 330 #TODO: Continue with algorithm for detecting transition line
    return x_transition_line

# image_number = 1
# # Make the plots
# data_folder = "C:/Users/ruben/Documents/Github/AE2130-II-06/data/Group 6 - IR Images"
# output_folder = "C:/Users/ruben/Documents/Github/AE2130-II-06/Infrared/Output/VerticalAverageTemperatures"
# all_experiments = os.listdir(data_folder)

# locations_transition_line = []

# for experiment in all_experiments:
#     # all_alphas = os.listdir(f"{data_folder}/{experiment}")

#     if experiment == "2D":
#         all_alphas = sorted_measurements_2D
#     elif experiment == "3D":
#         all_alphas = sorted_measurements_3D
    
#     for alpha in all_alphas:
#         input_folder = f"{data_folder}/{experiment}/{alpha}"
#         image_number_padded = str(image_number).zfill(3)
#         output_filepath = f"{output_folder}/{image_number_padded}_VerticalAverageTemperatures_{experiment}_{alpha}.png"
#         title = f"{experiment} at α = {alpha}°"

#         average_temperatures = calculate_averages(input_folder)
#         vertical_average_temperatures = calculate_vertical_averages(average_temperatures)

#         wing_boundaries = detect_wing_boundaries(vertical_average_temperatures)
#         x_trailing_edge = wing_boundaries[0]
#         x_leading_edge = wing_boundaries[1]
#         chord_length = x_leading_edge - x_trailing_edge

#         x_transition_line = detect_transition_line(vertical_average_temperatures, wing_boundaries)
#         # print(x_transition_line)
#         location_transition_line = (x_leading_edge - x_transition_line) / chord_length
#         locations_transition_line.append(location_transition_line)

#         plt.plot(vertical_average_temperatures, color="black")
#         plt.axvline(x=x_trailing_edge, color="red", linestyle="dashed", label="Trailing edge")
#         plt.axvline(x=x_leading_edge, color="green", linestyle="dashed", label="Leading edge")
#         plt.axvline(x=x_transition_line, color="blue", linestyle="dotted", label="Transition line")
#         plt.legend()
#         plt.xlabel("x [px]")
#         plt.ylabel("T_verticalAverage [°C]")
#         plt.title(title)
#         plt.savefig(output_filepath)
#         # plt.show()
#         plt.clf()
#         print(f"Saved plot for {title}")

#         image_number += 1

#         # Stop for time purposes
#         if experiment == "2D" and alpha == "10":
#             quit()
