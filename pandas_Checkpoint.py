#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np

# Provided data
exam_data = {
    'name': ['Anastasia', 'Dima', 'Katherine', 'James', 'Emily', 'Michael', 'Matthew', 'Laura', 'Kevin', 'Jonas'],
    'score': [12.5, 9, 16.5, np.nan, 9, 20, 14.5, np.nan, 8, 19],
    'attempts': [1, 3, 2, 3, 2, 3, 1, 1, 2, 1],
    'qualify': ['yes', 'no', 'yes', 'no', 'no', 'yes', 'yes', 'no', 'no', 'yes']
}

labels = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']

# Create DataFrame
df = pd.DataFrame(exam_data, index=labels)

# Display the DataFrame
print(df)


# In[9]:


# Printing the first three rows
print(df.head(3))



# In[12]:


# Deleting rows with NaN values
print(df.dropna(inplace=True))



# In[13]:


# Extracting 'name' and 'score' columns
name_score_df = df[['name', 'score']]


# In[14]:


print(name_score_df)


# In[ ]:


# Adding a new column "Success" based on the score
df['Success'] = (df['score'] > 10).astype(int)

print(df['success'])


# In[17]:


print(df.to_csv('my_data.csv'))


# In[ ]:




