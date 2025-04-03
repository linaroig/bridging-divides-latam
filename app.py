
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the data
df = pd.read_csv('cleaned_data.csv')

# Streamlit configuration
st.title("Data Distribution by Country and Age")

# Show a general view of the dataset
if st.checkbox('Show full data'):
    st.write(df_filtered)

# Filter relevant columns (adjust according to your column names)
df_filtered = df[['Country', 'Age']]  # Adjust according to your column names

# Show distribution by country
st.subheader("Distribution by Country")
country_counts = df_filtered['Country'].value_counts()
st.bar_chart(country_counts)

# Show distribution by age
st.subheader("Distribution by Age")
sns.histplot(df_filtered['Age'], kde=True, bins=30)
plt.title('Age Distribution')
st.pyplot(plt)

