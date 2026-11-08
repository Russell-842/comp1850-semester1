# Week 1.6, Session 1: Task 5

# Write a program here that uses the QuakeFeed and QuakeDataset
# classes to download earthquake data from a USGS data feed,
# analyze it and display the results

# See README.md for full details of what is required and what
# program output should look like

# Import QuakeFeed and QuakeDataset
from feed import QuakeFeed
from dataset import QuakeDataset

# Obtain Significance level and Time period from user
level = input("Significance Level : ")
period = input("Time Period : ")

feed = QuakeFeed(level, period)

dataset = QuakeDataset(feed)
dataset.read_feed()

print(dataset)
print(f"Mean depth = {dataset.mean_depth():.2f} km")
print(f"Mean magnitude = {dataset.mean_magnitude():.1f}")

strongest = dataset.strongest_quake()
