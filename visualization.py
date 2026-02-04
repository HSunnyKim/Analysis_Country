# Visualization Utilities for Analysis Results

# Import necessary libraries
import matplotlib.pyplot as plt
import seaborn as sns

# Set visualization style
sns.set(style='whitegrid')

# Function to create a bar chart

def create_bar_chart(data, x, y, title='Bar Chart', xlabel='X-axis', ylabel='Y-axis'):
    plt.figure(figsize=(10, 6))
    sns.barplot(data=data, x=x, y=y)
    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.show()

# Function to create a line chart

def create_line_chart(data, x, y, title='Line Chart', xlabel='X-axis', ylabel='Y-axis'):
    plt.figure(figsize=(10, 6))
    sns.lineplot(data=data, x=x, y=y)
    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.show()

# Function to create a scatter plot

def create_scatter_plot(data, x, y, title='Scatter Plot', xlabel='X-axis', ylabel='Y-axis'):
    plt.figure(figsize=(10, 6))
    sns.scatterplot(data=data, x=x, y=y)
    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.show()