# -*- coding: utf-8 -*-
"""Heart_Disease_Prediction_Final.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/14HYnkU1IsSs8RvaEtWdNMzaAPWm4QDnE

## Heart Disease Dataset EDA
https://archive.ics.uci.edu/dataset/45/heart+disease

Abstract:

This study explores heart disease prediction using a UCI dataset, emphasizing age, gender, chest pain, blood pressure, and cholesterol levels. Employing advanced analytics and machine learning, our goal is to identify patterns for more effective prevention and intervention strategies in cardiovascular health.
"""

# Delete the dataset from drive.
import os

file_to_delete = '/content/heart_desease.csv'

if os.path.exists(file_to_delete):
    os.remove(file_to_delete)
    print(f"{file_to_delete} has been deleted.")
else:
    print(f"{file_to_delete} doesn't exist.")

from google.colab import drive
drive.mount('/content/drive')

from google.colab import files
uploaded = files.upload()

"""Introduction:

This investigation leverages the UCI dataset on heart disease, encompassing 303 patient records and 14 distinct features. The dataset comprises essential parameters, including ('age', 'sex', 'cp', 'trestbps', 'chol', 'fbs', 'restecg', 'thalach','exang', 'oldpeak', 'slope', 'ca', 'thal', 'target'). Through a comprehensive analysis of these variables, we aim to unravel clinically relevant insights and discern predictive patterns that can significantly contribute to the advancement of cardiovascular health research. This dataset serves as a valuable resource for probing the intricate interplay of factors influencing heart disease outcomes.

"""

# Commented out IPython magic to ensure Python compatibility.
# Libraries for Exploratory Data Analysis
import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
# %matplotlib inline

df = pd.read_csv('heart_desease.csv')
df.head(3)

df.shape

print(df['target'].unique())

df.columns

df.info()

"""there are no nulls

## Check data type
"""

# to know the type of variable
df.nunique()

df.dtypes

# Change categorical type to categorical variables
categorical_columns = ['sex', 'cp', 'fbs', 'restecg', 'exang', 'slope', 'ca', 'thal']

for column in categorical_columns:
    df[column] = df[column].astype('object')

# Display data types after the conversion
print(df.dtypes)

unique_values_ca = df['ca'].unique()
print("Unique values in 'ca' column:", unique_values_ca)

# Count the number of occurrences of each category in descending order
ca_value_counts = df['ca'].value_counts(ascending=False)
print("Count of each category in 'ca' column (descending order):")
print(ca_value_counts)

# Check for missing values in the DataFrame
missing_values = df.isnull().sum()
print("Missing values in the DataFrame:")
print(missing_values)

# Change labels for better interpretation/visualization understanding
df['target'] = df['target'].replace({1: "Disease", 0: "No Disease"})
df['sex'] = df['sex'].replace({1: "Male", 0: "Female"})
df['cp'] = df['cp'].replace({1: "Typical Angina",
                             2: "Atypical Angina",
                             3: "Non-Anginal Pain",
                             4: "Asymptomatic"})
df['exang'] = df['exang'].replace({1: "Yes", 0: "No"})
df['slope'] = df['slope'].replace({1: "Upsloping",
                                   2: "Flat",
                                   3: "Downsloping"})
df['thal'] = df['thal'].replace({1: "Fixed Defect", 2: "Reversible Defect", 3: "Normal"})

# Display basic statistics of the DataFrame
basic_stats = df.describe()
print("Basic Statistics of the DataFrame:")
print(basic_stats)

"""## EDA on Heart Disease Dataset"""

df.columns

# Display the count of each class in the 'target' column
target_value_counts = df['target'].value_counts()
print("Count of each class in the 'target' column:")
print(target_value_counts)

# Plot a bar chart for better visualization of class distribution
target_value_counts.plot(kind='bar').set_title('Heart Disease Classes')

# Display the count of each age in the 'age' column
age_value_counts = df['age'].value_counts()
print("Count of each age in the 'age' column:")
print(age_value_counts)

# Plot a bar chart for better visualization of age distribution
age_value_counts.plot(kind='bar').set_title('Age Distribution')

# Display the count of the top 10 age values in the 'age' column
top_10_age_value_counts = df['age'].value_counts()[:10]
print("Top 10 age values and their counts:")
print(top_10_age_value_counts)

# Plot a bar chart for the distribution of the top 10 age values
sns.barplot(x=top_10_age_value_counts.index,
            y=top_10_age_value_counts.values,
            palette='Set2')
plt.xlabel('Age')
plt.ylabel('Age Distribution')
plt.title('Distribution of Top 10 Age Values')
plt.show()

# Display the youngest, oldest, and mean age in the 'age' column
youngest_age = min(df['age'])
oldest_age = max(df['age'])
mean_age = df['age'].mean()

print(f"Youngest Age: {youngest_age}")
print(f"Oldest Age: {oldest_age}")
print(f"Mean Age: {mean_age}")

# Display the count of each gender in the 'sex' column
sex_value_counts = df['sex'].value_counts()
print("Count of each gender in the 'sex' column:")
print(sex_value_counts)

# Plot a bar chart for the distribution of genders
sex_value_counts.plot(kind='bar').set_title('Gender Distribution')
plt.xlabel('Gender')
plt.ylabel('Count')
plt.show()

# Display the count of each chest pain type in the 'cp' column
chest_pain_value_counts = df['cp'].value_counts()
print("Count of each chest pain type in the 'cp' column:")
print(chest_pain_value_counts)

# Plot a bar chart for the distribution of chest pain types
chest_pain_value_counts.plot(kind='bar').set_title('Chest Pain Distribution')
plt.xlabel('Chest Pain Type')
plt.ylabel('Count')
plt.show()

# Display the count of each resting ECG result in the 'restecg' column
rest_ecg_value_counts = df['restecg'].value_counts()
print("Count of each resting ECG result in the 'restecg' column:")
print(rest_ecg_value_counts)

# Plot a bar chart for the distribution of resting ECG results
rest_ecg_value_counts.plot(kind='bar').set_title('Resting ECG Distribution')
plt.xlabel('Resting ECG Result')
plt.ylabel('Count')
plt.show()

# Display the count of exercise-induced angina in the 'exang' column
exercise_angina_value_counts = df['exang'].value_counts()
print("Count of exercise-induced angina in the 'exang' column:")
print(exercise_angina_value_counts)

# Plot a bar chart for the distribution of exercise-induced angina
exercise_angina_value_counts.plot(kind='bar').set_title('Exercise Induced Angina Distribution')
plt.xlabel('Exercise Induced Angina')
plt.ylabel('Count')
plt.show()

# Display the count of each number of major vessels in the 'ca' column
major_vessel_value_counts = df['ca'].value_counts()
print("Count of each number of major vessels in the 'ca' column:")
print(major_vessel_value_counts)

# Plot a bar chart for the distribution of the number of major vessels
major_vessel_value_counts.plot(kind='bar').set_title('Number of Major Vessel Distribution')
plt.xlabel('Number of Major Vessels')
plt.ylabel('Count')
plt.show()

# Display the count of each thalassemia type in the 'thal' column
thal_value_counts = df['thal'].value_counts()
print("Count of each thalassemia type in the 'thal' column:")
print(thal_value_counts)

# Plot a bar chart for the distribution of thalassemia types
thal_value_counts.plot(kind='bar').set_title('Thal Distribution')
plt.xlabel('Thalassemia Type')
plt.ylabel('Count')
plt.show()

"""# Visualize categorical data distribution"""

# Create a count plot for disease classes according to sex
sns.countplot(x='sex', hue='target', data=df, palette='Set2').set_title('Disease Classes According to Sex')
plt.xlabel('Sex')
plt.ylabel('Count')
plt.show()

# Create a count plot for disease classes according to chest pain
sns.countplot(x='cp', hue='target', data=df, palette='Set2').set_title('Disease Classes According to Chest Pain')
plt.xlabel('Chest Pain Type')
plt.ylabel('Count')
plt.show()

# Create a count plot for disease classes according to thalassemia type
sns.countplot(x='thal', hue='target', data=df, palette='Set2').set_title('Disease Classes According to Thalassemia')
plt.xlabel('Thalassemia Type')
plt.ylabel('Count')
plt.show()

# Create a count plot for disease classes according to exercise-induced angina
sns.countplot(x='exang', hue='target', data=df, palette='Set2').set_title('Disease Classes According to Exercise Induced Angina')
plt.xlabel('Exercise Induced Angina')
plt.ylabel('Count')
plt.show()

# Create a count plot for disease classes according to fasting blood sugar (fbs)
sns.countplot(x='fbs', hue='target', data=df, palette='Set2').set_title('Disease Classes According to Fasting Blood Sugar (fbs)')
plt.xlabel('Fasting Blood Sugar')
plt.ylabel('Count')
plt.show()

# Create a count plot for disease classes according to the number of major vessels ('ca')
sns.countplot(x='ca', hue='target', data=df, palette='Set2').set_title('Disease Classes According to Number of Major Vessels')
plt.xlabel('Number of Major Vessels')
plt.ylabel('Count')
plt.show()

# Visualize Thalassemia with heart disease
labels = 'Normal', 'Fixed defect', 'Reversible defect'
sizes = [6, 130, 28]
colors = ['pink', 'orange', 'purple']

plt.pie(sizes, labels=labels, colors=colors, autopct='%.1f%%', startangle=140)
plt.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
plt.title('Thalassemia with Heart Disease')
plt.show()

# Visualize Thalassemia with NO heart disease
labels = 'Normal', 'Fixed defect', 'Reversible defect'
sizes = [12, 36, 89]
colors = ['pink', 'orange', 'purple']

plt.pie(sizes, labels=labels, colors=colors, autopct='%.1f%%', startangle=140)
plt.axis('equal')
plt.title('Thalassemia with NO Heart Disease')
plt.show()

"""## Visualize the distribution of continuous variable across target variable"""

# Define continuous variables
continuous_features = ['age', 'chol', 'thalach', 'oldpeak', 'trestbps']

# Create a pair plot for continuous features along with the target variable
sns.pairplot(df[continuous_features + ['target']], hue='target')
plt.suptitle('Pair Plot of Continuous Features with Target', y=1.02)
plt.show()

# Understand the relationship between age and chol in each target based on sex
sns.lmplot(x="age", y="chol", hue="sex", col="target",
           markers=["o", "x"],
           palette="Set1",
           data=df)
plt.show()

# Set the style to white
sns.set(style="white")

# Create a mask to hide the upper triangle of the heatmap
mask = np.zeros_like(df.corr(), dtype=np.bool)
mask[np.triu_indices_from(mask)] = True

# Create a figure and axis for the heatmap
fig, ax = plt.subplots(figsize=(5, 5))

# Choose a diverging color palette
cmap = sns.diverging_palette(255, 10, as_cmap=True)

# Generate the correlation heatmap with annotations
sns.heatmap(df.corr(), mask=mask, annot=True, square=True, cmap=cmap, vmin=-1, vmax=1, ax=ax)

# Fixing an issue where the top and bottom rows are partially cut off
bottom, top = ax.get_ylim()
ax.set_ylim(bottom + 0.5, top - 0.5)

# Display the heatmap
plt.show()

df['target']

"""Methodologies:

This research employs a tripartite methodological framework, integrating logistic regression, support vector machines (SVM), and random forest algorithms for comprehensive data exploration and predictive analysis. The selection of these methodologies is rooted in their distinct statistical properties and learning paradigms, aimed at discerning optimal models for enhancing predictive accuracy in the realm of heart disease analysis. The comparative assessment of results across these diverse approaches serves to validate findings robustly and facilitates a nuanced understanding of the underlying patterns within the dataset. This methodological diversity aligns with contemporary best practices in machine learning and statistical modeling, ensuring a rigorous and evidence-based approach to knowledge generation.
"""

from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix

df = pd.read_csv('heart_desease.csv')

# Separate features (X) and target variable (y)
X = df.drop('target', axis=1)
y = df['target']

# Identify categorical columns
categorical_cols = ['sex', 'cp', 'fbs', 'restecg', 'exang', 'slope', 'ca', 'thal']

# Create a ColumnTransformer to apply one-hot encoding to categorical columns
preprocessor = ColumnTransformer(
    transformers=[
        ('cat', OneHotEncoder(), categorical_cols)
    ],
    remainder='passthrough'  # Pass through the remaining columns
)

# Create a pipeline with the preprocessing and logistic regression steps
model = Pipeline(steps=[
    ('preprocessor', preprocessor),
    ('classifier', LogisticRegression())
])

X

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train the model on the training set
model.fit(X_train, y_train)

# Make predictions on the test set
y_pred = model.predict(X_test)

# Evaluate the model
accuracy = accuracy_score(y_test, y_pred)

print(f"Accuracy: {accuracy:.2f}")
print("\nClassification Report:")
print(classification_report(y_test, y_pred))
print("\nConfusion Matrix:")
print(confusion_matrix(y_test, y_pred))

from sklearn.ensemble import RandomForestClassifier

# Create a pipeline with the preprocessing and Random Forest Classifier steps
model_rf = Pipeline(steps=[
    ('preprocessor', preprocessor),
    ('classifier', RandomForestClassifier(random_state=42))
])

# Train the Random Forest model on the training set
model_rf.fit(X_train, y_train)

# Make predictions on the test set
y_pred_rf = model_rf.predict(X_test)

# Evaluate the Random Forest model
accuracy_rf = accuracy_score(y_test, y_pred_rf)

print(f"Random Forest Accuracy: {accuracy_rf:.2f}")
print("\nRandom Forest Classification Report:")
print(classification_report(y_test, y_pred_rf))
print("\nRandom Forest Confusion Matrix:")
print(confusion_matrix(y_test, y_pred_rf))

from sklearn.svm import SVC

# Create a pipeline with the preprocessing and Support Vector Machine steps
model_svm = Pipeline(steps=[
    ('preprocessor', preprocessor),
    ('classifier', SVC(random_state=42))
])

# Train the SVM model on the training set
model_svm.fit(X_train, y_train)

# Make predictions on the test set
y_pred_svm = model_svm.predict(X_test)

# Evaluate the SVM model
accuracy_svm = accuracy_score(y_test, y_pred_svm)

print(f"SVM Accuracy: {accuracy_svm:.2f}")
print("\nSVM Classification Report:")
print(classification_report(y_test, y_pred_svm))
print("\nSVM Confusion Matrix:")
print(confusion_matrix(y_test, y_pred_svm))

"""Results:

Following a rigorous comparison of the three models, logistic regression emerged as the top performer with an accuracy of 0.90. Random forest exhibited commendable accuracy at 0.87, while support vector machine (SVM) achieved a respectable, albeit comparatively lower, accuracy of 0.70. These outcomes highlight the superior predictive capacity of logistic regression in the context of heart disease analysis, providing valuable insights for model selection and refinement in future studies.

# Conclusion

In this analysis, we explored a dataset related to heart disease, employing various data visualization techniques to gain insights into the dataset's characteristics. Key highlights include:

1. **Categorical Variable Transformation:** We converted categorical variables to more meaningful labels for better interpretation and visualization.

2. **Distribution Analysis:** We examined the distribution of various features, such as age, chest pain types, and thalassemia, to understand their prevalence within the dataset.

3. **Disease Class Visualization:** Utilizing count plots, we visualized the distribution of disease classes concerning different categorical features, such as sex, chest pain, and thalassemia.

4. **Pair Plot for Continuous Features:** We generated a pair plot to visualize the relationships between continuous features and the target variable, gaining insights into potential patterns.

5. **Scatter Plots and Regression Analysis:** Scatter plots and regression plots were employed to explore relationships between variables, particularly examining age, cholesterol, and maximum heart rate based on gender and disease status.

6. **Correlation Heatmap:** We used a correlation heatmap to visualize the relationships between different numerical features, identifying potential correlations that could influence the target variable.

The comprehensive analysis provides a foundational understanding of the dataset, offering valuable insights for further exploration or predictive modeling. The visualization techniques applied enhance our ability to interpret complex relationships within the data.

Reference:

https://github.com/ksharma67/Heart-Failure-Prediction
"""

