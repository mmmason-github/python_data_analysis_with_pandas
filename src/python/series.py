#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# # Create a Series Object from a Python List

# In[2]:


ice_cream = ["Chocolate", "Vanilla", "Strawberry", "Rum Raisin"]
print(pd.Series(ice_cream))


# In[3]:


lottery = [4, 8, 15, 16, 23, 42]
print(pd.Series(lottery))


# In[4]:


registrations = [True, False, False, False, True]
print(pd.Series(registrations))


# # Create a Series Object from a Python Dictionary

# In[5]:


sushi = {"Salmon": "Orange", "Tuna": "Red", "Eel": "Brown"}
print(pd.Series(sushi))


# # Coding Exercise
# ***
#
# ### Import the pandas library and assign it its "pd" alias
# ### Create a list with 4 countries - United States, France, Germany, Italy
# ### Create a new Series by passing in the list of countries
# ### Assign the Series to a "countries" variable
# ***
#
# ### Create a list with 3 colors - red, green, blue
# ### Create a new Series by passing in the list of colors
# ### Assign the Series to a "colors" variable
# ***
#
# ### Given the "recipe" dictionary below,
# ### create a new Series by passing in the dictionary as the data source
# ### Assign the resulting Series to a "series_dict" variable
# ### recipe = { "Flour": True, "Sugar": True, "Salt": False }
# ***

# In[6]:


countries = pd.Series(["United States", "France", "Germany", "Italy"])


colors = pd.Series(["red", "green", "blue"])


series_dict = pd.Series({"Flour": True, "Sugar": True, "Salt": False})


print(countries, "\n")
print(colors, "\n")
print(series_dict, "n")


# # Introduction to Methods

# In[7]:


print("hello".upper())
values = [1, 2, 3]
values.append(4)
print(values)


# In[8]:


prices = pd.Series([2.99, 4.45, 1.36])
print(prices)


# In[9]:


print(f"sum: {prices.sum()}")


# In[10]:


print(f"product: {prices.product()}")


# In[11]:


print(f"mean: {prices.mean()}")
print(f"variance: {prices.var()}")
print(f"standard deviation: {prices.std()}")


# # Introduction to Attributes

# In[12]:


# Method is a behaviour
# Attribute describes the object

# Method on a car -> drive
# Attribute on a car -> color


# In[13]:


adjectives = pd.Series(
    ["Smart", "Handsome", "Charming", "Brilliant", "Humble"]
)
print(adjectives)


# In[14]:


print(f"Size of the series: {adjectives.size}")


# In[15]:


print(f"Each element unique? {adjectives.is_unique}")


# In[16]:


adjectives = pd.Series(
    ["Smart", "Handsome", "Charming", "Brilliant", "Humble", "Smart"]
)
print(adjectives)


# In[17]:


print(f"Each element unique? {adjectives.is_unique}")


# In[18]:


print(adjectives.values)


# In[19]:


print(type(adjectives.values))


# In[20]:


print(adjectives.index)


# In[21]:


print(type(adjectives.index))


# In[22]:


print(adjectives.dtype)


# In[23]:


print(type(adjectives.dtype))


# # Coding Exercise
# ***
#
# ### The Series below stores the number of home runs
# ### that a baseball player hit per game
# ### home_runs = pd.Series([3, 4, 8, 2])
# ***
#
# ### Find the total number of home runs (i.e. the sum) and assign it
# ### to the total_home_runs variable below
# ### total_home_runs =
# ***
#
# ### Find the average number of home runs and assign it
# ### to the average_home_runs variable below
# ### average_home_runs =
# ***

# In[24]:


home_runs = pd.Series([3, 4, 8, 2])
total_home_runs = home_runs.sum()
average_home_runs = home_runs.mean()
print(home_runs, "\n")
print(f"Total number of home runs: {total_home_runs}")
print(f"Average home runs: {average_home_runs}")


# # Parameters and Arguments
# ***
# ### Parameter - The name we give to an expected input
# ### Argument - The concrete value that we provide to a parameter
#
# ***
# ### Example -> Difficulty
# ### Difficulty(Parameter) - Easy(Argument), Medium(Argument), Hard(Argument)
# ### Volume(Parameters) - 1 through 10 (Arguments)
# ### Subtitles(Parameters) - True(Argument), False(Argument)

# In[30]:


fruits = ["Apple", "Orange", "Plum", "Grape", "Blueberry"]
weekdays = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]
print(pd.Series(data=fruits, index=weekdays, name="Days|Fruits"), "\n")
print(pd.Series(data=weekdays, index=fruits, name="Fruits|Days"), "\n")


# In[ ]:


# In[ ]:


# In[ ]:


# In[ ]:


# In[ ]:


# In[ ]:


# In[ ]:


# In[ ]:


# In[ ]:
