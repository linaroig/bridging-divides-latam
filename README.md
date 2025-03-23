# bridging-divides-latam
Digital Media Usage, Social Trust, and Perceived Polarization in Latin America: A Cross-National Analysis Using the World Values Survey
This repository contains the data analysis, methodology, and results for my master's thesis on the relationship between digital media usage, social trust, and perceived political polarization in Latin America, using data from the World Values Survey (Wave 7).

# Project Overview
In an era of increasing digital media consumption, understanding its role in shaping societal dynamics is crucial. This project explores the following key questions:

How does digital media usage relate to social trust in Latin America?

Are these relationships different across countries, demographic groups, or age cohorts?

What factors mediate the impact of digital media on social trust and polarization?

The analysis employs various statistical methods, including z-score normalization, regression analysis, and correlation analysis, to examine the relationship between these variables and how they interact across multiple Latin American countries.

# Research Objectives
Construct three main indices:

## Social Trust Index

## Polarization Index

## Digital Media Usage Index

Normalize the indices using z-scores for comparability.

Explore the relationships between digital media usage, social trust, and perceived political polarization in a cross-national context.

# Data
The data used for this analysis is sourced from the World Values Survey (Wave 7), which provides rich information about social values, trust, and political beliefs across several countries.

The dataset includes responses from several Latin American countries, focusing on questions related to social trust, political polarization, and digital media usage.

# Methodology
Index Construction:
Three indices were created:

Social Trust Index: Based on questions about trust in various social groups and institutions.

Polarization Index: Derived from responses to a political leaning scale (1-10, left-right).

Digital Media Usage Index: Based on how often respondents use various media sources (mobile phone, internet, social media, etc.).

Z-score Normalization:
To make the indices comparable, z-score normalization was applied to each index, converting them to a standard scale (mean of 0, standard deviation of 1).

Exploratory Analysis:
The analysis explores the relationships between these indices and investigates whether these relationships differ by country, age, or other demographic factors.

Statistical Techniques:

Descriptive statistics

Correlation analysis

Regression models to assess the impact of digital media usage on social trust and polarization.

Directory Structure
/data: Contains the raw and processed data files.

/notebooks: Contains Jupyter notebooks used for analysis and modeling.

/scripts: Contains Python scripts for data cleaning, preprocessing, and analysis.

/outputs: Contains visualizations and results.

README.md: This file.

# Requirements
This project uses the following Python libraries:

pandas

numpy

scipy

pingouin

matplotlib

seaborn

scikit-learn

statsmodels

Streamlit (for visualization)

You can install the necessary libraries using:
To run the analysis, simply execute the Jupyter notebooks or Python scripts in the /scripts folder.

Data Preprocessing:
Load and preprocess the raw data by following the steps in the preprocessing script.

Analysis:
Run the analysis and generate the results by executing the notebooks.

Visualization:
Use Streamlit to interactively visualize the relationships between digital media usage, social trust, and polarization.

Expected Outcomes
The analysis will provide insights into:

Cross-national patterns of digital media usage, social trust, and political polarization in Latin America.

The impact of digital media usage on social trust and polarization across different demographic groups.

Potential mediating factors that influence these relationships.

Contributing
If you'd like to contribute to this project or improve the analysis, feel free to fork the repository and create a pull request with your suggestions or modifications.
