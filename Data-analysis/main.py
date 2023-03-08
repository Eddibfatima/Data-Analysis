import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt
import numpy as np


st.set_page_config(page_title='Financialy results')
st.header('Financialy result 2013/2014')
st.subheader('Financiale sample 📈')


### --- LOAD DATAFRAME
uploaded_file = st.file_uploader('Choose a XLSX file', type='xlsx')
if uploaded_file:
    st.markdown('---')
    df = pd.read_excel(uploaded_file, engine='openpyxl')
    st.dataframe(df)
    groupby_column = st.selectbox(
        'What would you like to analyse?',
        ('contry', 'product', 'units sold', 'manufacteur','sale price','gross sale','sale','COGC','profit','date','month','year'),
    )
excel_file = 'Financial Sample.xlsx'

df= pd.read_excel(excel_file,
                   usecols='A:M',
                   header=3)

 # -- GROUP DATAFRAME
output_columns = ['Sales', 'Profit']

# Create data for the bar graph

Data = np.random.rand(5)

st.markdown('### Graph of financial sample ==> Sales-of-month')
data = {
    'profit': ['sales', 'CoGs', 'product', 'country'],
    'sales': [10, 15, 5, 20],
    'profit': ['product', 'units sold', 'gros sales', 'sale price'],
    'sales': [20, 30, 40, 50]
}
df = pd.DataFrame(data)

# Display the bar chart:
st.bar_chart(df['sales'])
####################################
####################################
st.markdown('### Years sales: 2013-2014')
# Create Data for the bar graph 'years':
Data = {
    'profit': ['month', 'year'],
    'Years': [50, 30]
}

df = pd.DataFrame(Data)

#Display the bar chart:
st.bar_chart(df['Years'])
#########################


#Totaly graph results:

x = np.linspace(0, 10, 100)
y = np.sin(x)

# Create a figure and plot the data
fig, ax = plt.subplots()
ax.plot(x, y)

# Set the plot title and axis labels
ax.set_title('Financial')
ax.set_xlabel('sales')
ax.set_ylabel('years')

st.pyplot(fig)