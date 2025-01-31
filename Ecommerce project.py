#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import plotly.io as pio
import plotly.colors as colors
pio.templates.default= 'plotly_white'


# In[4]:


data = pd.read_csv("Sample - Superstore.csv", encoding='latin-1')


# In[6]:


data.head()


# In[8]:


data.describe()


# In[9]:


data.info()


# cleaning the data to make necessary changes(date's data type to date time format)

# In[17]:


data['Order Date'] = pd.to_datetime(data['Order Date'])
data['Ship Date']=pd.to_datetime(data['Ship Date'])


# In[18]:


data.info()


# creating 3 new coloums Month, Year and order day of week to further clean and make data more usable

# In[19]:


data['Order Month']= data['Order Date'].dt.month
data['Order Year']= data['Order Date'].dt.year
data['Order day of week']= data['Order Date'].dt.dayofweek


# In[20]:


data.head()


# MONTHLY SALES ANALYSIS

# In[22]:


sales_by_month=data.groupby('Order Month')['Sales'].sum().reset_index()

sales_by_month


# In[23]:


fig = px.line (sales_by_month,
              x= 'Order Month',
              y= 'Sales',
              title= 'Monthly Sales Analysis')
fig.show()


# Analyse sales by categories

# In[25]:


sales_by_category=data.groupby('Category')['Sales'].sum().reset_index()


# In[26]:


sales_by_category


# In[32]:


fig=px.pie(sales_by_category,
          values='Sales',
          names='Category',
          hole=0.5,
          color_discrete_sequence=px.colors.qualitative.Pastel)
fig.update_traces(textposition='inside', textinfo='percent+label')
fig.update_layout(title_text='Sales analysis by category',title_font=dict(size=24))

fig.show()


# Analysis of the sales of sub categories

# In[33]:


sales_by_subcategory=data.groupby('Sub-Category')['Sales'].sum().reset_index()


# In[34]:


sales_by_subcategory


# In[36]:


fig=px.bar(sales_by_subcategory,
           x= 'Sub-Category',
           y='Sales',
           title='Sales analysis by sub category')


# In[37]:


fig.show()


# #monthly profit analysis 

# In[38]:


profit_by_month=data.groupby('Order Month')['Profit'].sum().reset_index()


# In[39]:


profit_by_month


# In[40]:


fig=px.bar(profit_by_month,
           x= 'Order Month',
           y='Profit',
           title='Monthly Profit Analysis')


# In[41]:


fig.show()


# Profit by category

# In[43]:


profit_by_category=data.groupby('Category')['Profit'].sum().reset_index()


# In[44]:


profit_by_category


# In[45]:


fig=px.pie(profit_by_category,
          values='Profit',
          names='Category',
          hole=0.5,
          color_discrete_sequence=px.colors.qualitative.Pastel)
fig.update_traces(textposition='inside', textinfo='percent+label')
fig.update_layout(title_text='Profit analysis by category',title_font=dict(size=24))

fig.show()


# Profit by sub category

# In[46]:


profit_by_subcategory=data.groupby('Sub-Category')['Profit'].sum().reset_index()


# In[47]:


profit_by_subcategory


# In[48]:


fig = px.line (profit_by_subcategory,
              x= 'Sub-Category',
              y= 'Profit',
              title= 'Profit Analysis by sub-category')
fig.show()


# sales and profit for customer segment

# In[49]:


sales_profit_by_segment=data.groupby('Segment').agg({'Sales':'sum','Profit':'sum'}).reset_index()


# In[50]:


sales_profit_by_segment


# In[56]:


color_palette=colors.qualitative.Pastel
fig=go.Figure()
fig.add_trace(go.Bar(x=sales_profit_by_segment['Segment'],
                    y=sales_profit_by_segment['Sales'],
                    name='Sales',
                    marker_color=color_palette[0]))
fig.add_trace(go.Bar(x=sales_profit_by_segment['Segment'],
                    y=sales_profit_by_segment['Profit'],
                    name='Profit',
                    marker_color=color_palette[1]))
fig.update_layout(title='sales and profit for customer segment',
                 xaxis_title='Customer Segment', yaxis_title='Amount')
fig.show()


# Sales to profit ratio

# In[62]:


sales_profit_by_segment=data.groupby('Segment').agg({'Sales':'sum','Profit':'sum'}).reset_index()
sales_profit_by_segment['Sales_to_Profit_Ratio']=sales_profit_by_segment['Sales']/sales_profit_by_segment['Profit']
print(sales_profit_by_segment[['Segment','Sales_to_Profit_Ratio']])


# In[ ]:




