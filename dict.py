# dictionary
from collections import _odict_keys


d={} # empty dictionary
print(d)
print(type(d)) # data set type

d1={1:'one', 2:'two', 3:'three'} # dictionary with integer keys
print(d1)
d1=dict({1:'one', 2:'two', 3:'three'}) # create dictionary using dict()
print(d1)

d1={'A':'one', 'B':'two', 'C':'three'} # create dictionary with string
print(d1)

d1={1:'one', 'two':'two', 1.3:'three'} # dictionary with mixed keys
print(d1)
print(type(1.3))
print(d1.keys()) # return dictionary keys using keys()

print(d1.values())




d2={'one':1, 'two':2, 'three':3}
print(d1)
print(d2)
print(d1.values)
print(d1.keys)

d1={'Name': 'Bharadwaz Putta', 'age': 40, 'Gender': 'Male'}
print(d1)
print(d1.items()) # access each key value pair with a dictionary

d1={'Name': 'Bharadwaz', 'Age': 40, 'Gender': 'Male', 'Diagnois': ['thyrod', 'prostrate', 'alopecia']} # dictionary with list
print(d1)

d1={'Name': 'Bharadwaz', 'Age': 40, 'Gender': 'Male', 'Diagnois': ('thyrod', 'prostrate', 'alopecia')} # dictionary with tuple
print(d1)

d1={'Name': 'Bharadwaz', 'Age': 40, 'Gender': 'Male', 'Location': ['india', 'Pakistan', 'Srilanka'], 'Diagnosis': ('thyrod', 'prostrate', 'alopecia')} # dictionary with list and tupple
print(d1)

print(d1['Name'])
print(d1['Age'])
print(d1['Gender'])
print(d1['Location'])
print(d1['Diagnosis'])

d1['Name']= 'Keosha'
d1['Age']= 10
d1['Gender'] = 'Female'
print(d1)
d1['Designation'] = 'Internee'
print(d1)
print(d1.pop('Designation'))
print(d1)

d1={'Name': 'Bharadwaz', 'Age': 40, 'Gender': 'Male', 'Location': ['india', 'Pakistan', 'Srilanka'], 'Diagnosis': ('thyrod', 'prostrate', 'alopecia')} # dictionary with list and tupple
print(d1)
del[d1['Name']]
print(d1)

print(d1[0])