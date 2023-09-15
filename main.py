# Required packages are imported
# Please install the packages to run the code (Details at "Read_Me" file)

import pandas as pd
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
from geopy.distance import geodesic

# Load data from CSV file, please change the folder path based on the placement at your computer!
# Details is provided at "Read_Me" file
data = pd.read_csv(r"C:\Users\USERNAME\Downloads\Machine_Learning_(K_Means_Clustering)_for_Sub_Station_Positioning\Data_for_Sub_Station.csv")

# "data" refers to original dataframe that is loaded from the CSV file
# data[['latitude', 'longitude']] refers to the latitude and longitude column of the loaded dataframe
coords = data[['latitude', 'longitude']]

# Requesting the user for the number of clusters
# It's based on the flowchart shown in figure 5.5 of the book
# Starting with the "Number of Substation" as 1. Finding the power loss, the efficiency of each house is calculated
# Then average efficiency with all houses is calculated
# If avg efficiency is less than 95 percent, increment the number of substation by one and check avg efficiency again
# Once the average efficiency reaches at least 95 percent, that number of substation is considered as sufficient for that place

n_clusters = int(input("Enter the number of clusters (Alternatively number of substation you want): "))

# Running KMeans clustering algorithm
kmeans = KMeans(n_clusters=n_clusters)      # Creating a KMeans object with the specified number of clusters
kmeans.fit(coords)                          # Fitting the KMeans model to the "coords" data
centroids = kmeans.cluster_centers_         # Getting the coordinates of the cluster centroids (Substation Position)
labels = kmeans.labels_                     # Getting the cluster labels to each data point in "coords"

# Calculating distances from each house to the nearest centroid
distances = []                                         # An empty list is created to store the distances

for i in range(len(coords)):                           # For loop is used to iterate over each house coordinate in "coords"
    house_coord = coords.iloc[i]                       # Getting the coordinate of the current house
    centroid_distances = []                            # Creatting an empty list to store distances from the current house to each centroid

    for j, centroid in enumerate(centroids):           # For loop is used to iterate over each centroid
        dist = geodesic(house_coord, centroid).m       # The distance between house and current centroid is calculated
        centroid_distances.append(dist)                # The distances are appended
    min_dist = min(centroid_distances)                 # Using "min" function, the minimum distance is calculated among all centroid distances

    min_idx = centroid_distances.index(min_dist)       # Finding the centroid with index that has the lowest distance

    # Details is appended to the "distances" list
    distances.append({'house': i, 'centroid': min_idx, 'distance(m)': min_dist})

# Printing the distances from each house to the nearest centroid
print('Distances from each house to the nearest centroid (in meters):')
for dist in distances:
    print(f"House {dist['house']} is {dist['distance(m)']} meters away from centroid {dist['centroid']}")

# Print the latitude and longitude of the centroids
print('\nCentroid Coordinates:')

for i, centroid in enumerate(centroids):                # Iterating over each dictionary in the "distances" list
    print(f"Centroid {i} is located at latitude {centroid[0]} and longitude {centroid[1]}")

# Plot the results
fig, ax = plt.subplots()

# Scattering plot is done with different colors. Same color is kept for all houses under one cluster (substation)
ax.scatter(coords.iloc[:,0], coords.iloc[:,1], c=labels)

# Scattering plot is done for all centroids (substations) with a red star mark
ax.scatter(centroids[:, 0], centroids[:, 1], marker='*', s=200, c='r')

# Setting the x-axis, y-axis and the title
ax.set_xlabel('Latitude')
ax.set_ylabel('Longitude')
ax.set_title('K-means Clustering')

# Mirroring image the plot to synchronous with the OSM view
ax.set_xlim(ax.get_xlim()[::-1])
plt.show()
