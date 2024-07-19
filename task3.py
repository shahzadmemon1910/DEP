import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the Titanic dataset
url = 'https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv'
titanic_data = pd.read_csv(url)

# Display the first few rows of the dataset
print("First few rows of the dataset:")
print(titanic_data.head())

# Display basic information about the dataset
print("\nDataset info:")
print(titanic_data.info())

# Summary statistics
print("\nSummary statistics:")
print(titanic_data.describe(include='all'))

# Check for missing values
print("\nMissing values:")
print(titanic_data.isnull().sum())

# Fill missing values for 'Age' with the median age
titanic_data['Age'].fillna(titanic_data['Age'].median(), inplace=True)

# Drop the 'Cabin' column due to too many missing values
titanic_data.drop(columns=['Cabin'], inplace=True)

# Drop 'Ticket' and 'PassengerId' columns as they are not useful for analysis
titanic_data.drop(columns=['Ticket', 'PassengerId'], inplace=True)

# Convert 'Sex' to a numerical value for analysis
titanic_data['Sex'] = titanic_data['Sex'].map({'male': 0, 'female': 1})

# Check for missing values again after cleaning
print("\nMissing values after cleaning:")
print(titanic_data.isnull().sum())

# Histograms for numerical features
plt.figure(figsize=(14, 7))

plt.subplot(2, 2, 1)
plt.hist(titanic_data['Age'], bins=30, edgecolor='black')
plt.title('Age Distribution')
plt.xlabel('Age')
plt.ylabel('Frequency')

plt.subplot(2, 2, 2)
plt.hist(titanic_data['Fare'], bins=30, edgecolor='black')
plt.title('Fare Distribution')
plt.xlabel('Fare')
plt.ylabel('Frequency')

# Bar plot for survival count
plt.subplot(2, 2, 3)
sns.countplot(data=titanic_data, x='Survived')
plt.title('Survival Count')
plt.xlabel('Survived')
plt.ylabel('Count')

# Bar plot for survival rate by gender
plt.subplot(2, 2, 4)
sns.barplot(data=titanic_data, x='Sex', y='Survived')
plt.title('Survival Rate by Gender')
plt.xlabel('Gender')
plt.ylabel('Survival Rate')
plt.xticks(ticks=[0, 1], labels=['Male', 'Female'])

plt.tight_layout()
plt.show()

# Pairplot to visualize relationships between features colored by survival
plt.figure(figsize=(10, 6))
sns.pairplot(titanic_data[['Age', 'Fare', 'Survived']], hue='Survived')
plt.suptitle('Pairplot of Age, Fare, and Survival')
plt.show()

# Survival rate by passenger class
plt.figure(figsize=(8, 6))
sns.barplot(data=titanic_data, x='Pclass', y='Survived')
plt.title('Survival Rate by Passenger Class')
plt.xlabel('Passenger Class')
plt.ylabel('Survival Rate')
plt.show()