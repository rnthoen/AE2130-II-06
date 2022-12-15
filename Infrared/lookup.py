import os

sorted_measurements_2D = [
    "-3",
    "-2",
    "-1",
    "0",
    "1",
    "2",
    "3",
    "3.5",
    "4",
    "4.5",
    "5",
    "5.5",
    "6",
    "6.5",
    "7",
    "7.5",
    "8",
    "8.5",
    "9",
    "9.5",
    "10",
    "10.5",
    "11",
    "11.5",
    "12",
    "12.5",
    "13",
    "14",
    "15",
    "15.5",
    "16",
    "16.5",
    "17",
    "17.5",
    "18",
    "17.5R",
    "17R",
    "16.5R",
    "16R",
    "15.5R",
    "15R",
    "14.5R",
    "14R",
    "13.5R",
    "13R",
]

sorted_measurements_3D = [
    "-3",
    "-2",
    "-1",
    "0",
    "1",
    "2",
    "3",
    "3.5",
    "4",
    "4.5",
    "5",
    "5.5",
    "6",
    "6.5",
    "7",
    "7.5",
    "8",
    "8.5",
    "9",
    "9.5",
    "10",
    "10.5",
    "11",
    "11.5",
    "12",
    "12.5",
    "13",
    "13.5",
    "14",
    "15",
    "16",
    "16.5",
    "17",
    "17.5",
    "18",
    "18.5",
    "19",
    "18.5R",
    "18R",
    "17.5R",
    "17R",
    "16.5R",
    "16R",
    "15.5R",
    "15R",
    "14.5R",
    "14R",
    "13.5R"
]

# data_folder = "C:/Users/ruben/Documents/Github/AE2130-II-06/data/Group 6 - IR Images"
# output_folder = "C:/Users/ruben/Documents/Github/AE2130-II-06/Infrared/Output/VerticalAverageTemperatures"

# # Check 2D list
# experiment = "2D"
# all_alphas = os.listdir(f"{data_folder}/{experiment}")

# # Check if length is the same
# problem = False
# if (len(all_alphas) == len(sorted_measurements_2D)):
#     for alpha in all_alphas:
#         if not(alpha in sorted_measurements_2D):
#             print(f"WARNING! {alpha} is not in the {experiment} list")
#             problem = True
# else:
#     print(f"WARNING! Lenght of the {experiment} lists is not the same!")
# if not(problem):
#     print(f"No problems with the {experiment} list!")

# # Check 3D list
# experiment = "3D"
# all_alphas = os.listdir(f"{data_folder}/{experiment}")

# # Check if length is the same
# problem = False
# if (len(all_alphas) == len(sorted_measurements_3D)):
#     for alpha in all_alphas:
#         if not(alpha in sorted_measurements_3D):
#             print(f"WARNING! {alpha} is not in the {experiment} list")
#             problem = True
# else:
#     print(f"WARNING! Lenght of the {experiment} lists is not the same!")
# if not(problem):
#     print(f"No problems with the {experiment} list!")
