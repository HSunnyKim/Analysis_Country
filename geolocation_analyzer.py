import pandas as pd
import matplotlib.pyplot as plt

# Function to analyze user geolocation data

def analyze_geolocation(file_path):
    # Load the geolocation data
    data = pd.read_csv(file_path)

    # Display the first few rows of the dataset
    print("\nFirst 5 rows of the dataset:")
    print(data.head())

    # Check for missing values
    print("\nMissing values in the dataset:")
    print(data.isnull().sum())

    # Basic statistics
    print("\nBasic Statistics:")
    print(data.describe())

    # Plotting the geolocation data distribution
    plt.figure(figsize=(10, 6))
    plt.scatter(data['longitude'], data['latitude'], alpha=0.5, c='blue')
    plt.title('Geolocation Data Distribution')
    plt.xlabel('Longitude')
    plt.ylabel('Latitude')
    plt.grid()
    plt.show()

# Example usage
# analyze_geolocation('path_to_your_geolocation_data.csv')
