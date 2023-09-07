#!/usr/bin/env python
# coding: utf-8

# In[6]:


import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

#Path to read the data 

file_path = "D:\\Data_Analytics_Portfolio\\Projects\\Completed_Projects\\Data_science_jobs_OZ\\AustraliaDataScienceJobs.csv"

# Loading the Excel data
data = pd.read_csv(file_path)

# Display basic information about the DataFrame
print(data.info())

# Display the first few rows of the DataFrame
print(data.head())





# In[7]:


#Data Cleaning 

# Remove rows with missing values
data_cleaned = data.dropna()


print(data.head())


# In[11]:


# Analysis

# (1) Industries demanding data analysts the most
top_industries = data_cleaned['Company Sector'].value_counts().head(12)
print("Top Industries Demanding Data Analysts:")
print(top_industries)

# (2) Cities in demand for data analysts
top_cities = data_cleaned['Job Location'].value_counts().head(12)
print("\nCities in Demand for Data Analysts:")
print(top_cities)

# (3) Average base salary of data analysts
avg_salary = data_cleaned['Estimate Base Salary'].mean()
print("\nAverage Base Salary of Data Analysts:")
print(avg_salary)

avg_low_salary = data_cleaned['Low Estimate'].mean()
print("\nAverage Low Base Salary of Data Analysts:")
print(avg_low_salary)

avg_High_salary = data_cleaned['High Estimate'].mean()
print("\nAverage High Base Salary of Data Analysts:")
print(avg_High_salary)


# (4) Most common job titles
top_titles = data_cleaned['Job Title'].value_counts().head(12)
print("\nMost Common Job Titles:")
print(top_titles)


# In[8]:


# Count the number of job positions in each state
state_counts = data_cleaned['State'].value_counts()

# Print the top 5 states with the highest number of jobs
top_states = state_counts.head(5)
print("Top 5 States by Number of Jobs:")
print(top_states)


# In[9]:


# Select the columns containing the yes/no skills
skills_columns = data_cleaned.columns[25:54]  

# Calculate the total count of each skill (sum across rows)
skills_counts = data_cleaned[skills_columns].sum()

# Sort the skills by count in descending order
sorted_skills = skills_counts.sort_values(ascending=False)

# Print the top recurring skills
print("Top In-Demand Skills:")
print(sorted_skills.head(6))


# In[12]:


# Create a bar plot

plt.figure(figsize=(10,6))

top_industries.plot(kind='bar')

plt.title('Top Industries Demanding Data Analysts')

plt.xlabel('Industry')

plt.ylabel('Number of Jobs')

plt.xticks(rotation=45)

plt.tight_layout()

# Show the plot
plt.show()


# In[13]:


# Exclude rows with city name 'Australia'

top_cities = top_cities[top_cities.index != 'Australia']

# Select the top 8 cities from the DataFrame
top_8_cities = top_cities.head(8)

# Create a bar plot
plt.figure(figsize=(10, 6))
top_8_cities.plot(kind='bar')
plt.title('Top Cities Demanding Data Analysts')
plt.xlabel('Industry')
plt.ylabel('Number of Jobs')
plt.xticks(rotation=45)
plt.tight_layout()

# Show the plot
plt.show()


# In[15]:


#Visualization of in-demand skills 

# Selecting top- skills 
sorted_skills =(sorted_skills.head(6))

# Create a bar plot
plt.figure(figsize=(10, 6))
sorted_skills.plot(kind='bar')
plt.title('Top Skills')
plt.xlabel('Skillset')
plt.ylabel('Number of repition in job description')
plt.xticks(rotation=45)
plt.tight_layout()

# Show the plot
plt.show()


# In[ ]:




