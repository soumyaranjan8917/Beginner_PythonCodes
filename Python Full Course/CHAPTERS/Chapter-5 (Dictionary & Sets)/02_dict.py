marks ={
    "Sohan" : 100,
    "Pranat": 23,
    "Chunak": 56,
    67: "Csan"
}

# print(marks.items()) # Returns a list of (key,value)tuples.
# print(marks.keys()) # Returns a list containing dictionary's keys.
# print(marks.values()) # Updates the dictionary with supplied key-value pairs.
# marks.update({"Chunak": 65, "Sohan": 99}) # Returns the value of the specified keys (and value is returned eg."Sohan" is returned here).
# print(marks)


print(marks.get("Sohan2")) # Print None
print(marks["Sohan2"]) # Returns an error