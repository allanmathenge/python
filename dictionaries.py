# Dictionaries
band = {
    "vocals": "plant",
    "guitar": "Page"
}

band2 = dict(vocals="plant", guitar="Page")  # Using dict constructor

# Both band and band2 create the same dictionary

print(band)
print(band2)
print(type(band))
print(len(band2))

# Access items in dicts

print(band["vocals"])
print(band.get("guitar"))

# list all keys/values
print(band.keys())
print(band.values())

# list of key/value pairs as tuples
print(band.items())

# Verify key exists
print("guitar" in band)
print("triangle" in band)

# Change values
band["vocals"] = "Coverdale"
band.update({"bass": "JPJ"})
print(band)

# Remove items
print(band.pop("bass"))
print(band)

band["drums"] = "Bonham"
print(band)

print(band.popitem())
print(band)

# Delete or clear items in a dictionary

band["drums"] = "Bonham"
print(band)
del band["drums"]
print(band)

band2.clear()
print(band2)

del band2

# Copy dictionaries
# Create reference of the same place in memory or the dictionary. if you add or remove to band2, it will do the same for band.
# band2 = band
# print("Bad copy")
# print(band2)
# print(band)

# band2["drums"] = "Allan"
# print(band)

band2 = band.copy()
band2["drums"] = "Allan"
print("Good copy")
print(band)
print(band2)

# Or use the dict() constructor function
band3 = dict(band)
print("Good copy")
band3["drums"] = "Sam"
print(band)
print(band3)

# Nested dictionaries

member1 = {
    "name": {
        "Plant": "Chord"
    },
    "instrument": "vocals"
}

member2 = {
    "name": "Page",
    "instrument": "guitar"
}

band = {
    "member1": member1,
    "member2": member2
}

print(band)
print(band["member1"]["name"]["Plant"])  # Can accomodate more levels

# Sets

nums = {1, 2, 3, 4}
nums2 = set((1, 2, 3, 4))
nums3 = set({1, 2, 3, 4})
print(nums)
print(nums2)
print(type(nums))
print(type(nums3) == set)
print(isinstance(nums, set))
print(len(nums))

# No duplicates are allowed in sets
nums = {1, 2, " ", 2, 3}
print(len(nums))
print(nums)

# True is a dupe of 1, 0 dupe of False
nums = {1, True, 2, False, 3, 4, 0}
print(nums)

# Check if a value is in a set
print(2 in nums)

# but you cannot refer to an element in a set with an index or a key
