'''
Alexandra Lebron
Final Project
'''


# In[11]:


import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px


# In[12]:


### Data Acquisition


# In[13]:


df = pd.read_csv("openipf.csv")
print(df.shape)
df.info()


# In[14]:


### Data Processing


# In[15]:


df = df.drop(['Division'], axis = 1)
new_names = {'BodyweightKg':'BW Kg', 'MeetState':'State'}
df.rename(columns = new_names, inplace = True)
df.head()


# In[16]:


df = df.drop(['Federation'], axis = 1)


# In[17]:


df = df.iloc[[435, 765, 2073, 10453, 40356, 94660, 152415, 185735]]


# In[18]:


df


# In[19]:


### Data Visualization


# In[21]:


#Scatter Plot
df.plot(kind = 'scatter', x = 'Total Kg', y = 'Dots', color = 'blue')
plt.xlabel("Total Kg")
plt.ylabel("Dots")
plt.show()

df.plot(kind = 'scatter', x = 'WeightClassKg', y = 'Total Kg', color = 'red')
plt.xlabel("Weight Class Kg")
plt.ylabel("Total Kg")
plt.show()


# In[22]:


fig = px.bar(df, x = "Best Squat Kg", y = "Name", text_auto = "0.7")
fig.update_traces(textposition = 'inside')
fig.update_layout(yaxis = {'categoryorder':"total ascending"})


# In[23]:


fig = px.bar(df, x = "Best Bench Kg", y = "Name", text_auto = "0.7")
fig.update_traces(textposition = 'inside')
fig.update_layout(yaxis = {'categoryorder':"total ascending"})


# In[24]:


fig = px.bar(df, x = "Best Deadlift Kg", y = "Name", text_auto = "0.7")
fig.update_traces(textposition = 'inside')
fig.update_layout(yaxis = {'categoryorder':"total ascending"})


# In[25]:


px.bar(df, x = "Name", y = ["Best Squat Kg", "Best Bench Kg", "Best Deadlift Kg"], barmode = "group",text_auto = True, color_discrete_sequence = ["red", "yellow", "blue"])


# In[26]:


px.bar(df, x = "Name", y = "Total Kg", barmode = "group",text_auto = True, color_discrete_sequence = ["green"])
