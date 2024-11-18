import pandas as pd
import pickle

# Step 1: Load the dataset
data = pd.read_csv('heart_disease.csv')  # Replace with your dataset's filename

# Step 2: Save the dataset as a Pickle file
with open('heart_disease.pkl', 'wb') as file:
    pickle.dump(data, file)

print("Dataset successfully saved as Pickle!")

# Step 3: Reload the Pickle file to verify
with open('heart_disease.pkl', 'rb') as file:
    loaded_data = pickle.load(file)

print(loaded_data.head())
