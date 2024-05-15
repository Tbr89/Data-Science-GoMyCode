#!/usr/bin/env python
# coding: utf-8

# In[67]:


import numpy as np
grades = np.array ([85, 90, 88, 92, 95, 80, 75, 98, 89, 83])
mean_grades = np.mean(grades)
median_grades = np.median(grades)
standard_deviation = np.std(grades)
minimum = np.min(grades)
maximum = np.max(grades)
order = np.sort(grades)
a=np.argmax(grades)
A=np.sum(grades>90)
B=np.sum(grades<75)
percentage_above = (A / len(grades)) * 100
percentage_below= (B/len(grades)) * 100
B=np.sum(grades<75)

High_p = grades[grades>90]
passing_grades = grades[grades>75]
print("The median is ", median_grades)
print("the mean is ", mean_grades)
print("The standard deviation is", standard_deviation)
print("The minimum grade is", minimum)
print("The maximum grade is", maximum)
print("The grades when sorted are", order)
print("The student with the highest grade is the student number", a)
print("The number of student with a grade above 90 is ", A )
print("The percentage of students with a grade above 90 is ", percentage_above)
print("The percentage of students with a grade below 75 is ", percentage_below)
print("The high performers had these grades", High_p)
print ("The students who passed have the next grades", passing_grades)


# In[ ]:




