# Week 1.3, Session 1: Task 5b

rivers = {
  "London": "Thames", 
  "Leeds": "Aire", 
  "Liverpool": "Mersey",
  "York": "Ouse"
}

# Loop through the dict extracting key and value

for c, r in rivers.items() :
    print(c, r)

# 1. Iterate Keys
for city in rivers.keys() :
  print(city)

# 2. Iterate Values
for river in rivers.values() :
  print(river)

# Create 2 further for loops to iterate: 1. just through the keys, 2. just through the values
# Hint: we looked at built in function for dicts last session