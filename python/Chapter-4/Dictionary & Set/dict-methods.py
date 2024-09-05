#     Dictionary Methods.

# (.Keys) returns all keys

MyDict = {
    "Name" : "John",
    "Age" : 30,
    "Country" : "USA"
}

print(list(MyDict.keys()))
print(MyDict.keys())

# (.Values) returns all values

MyDict = {
    "Name" : "John",
    "Age" : 30,
    "student" : {
        "phy" : 40,
        "eng" : 50
    }
}

print(list(MyDict.values()))
print(MyDict.values())

# (.Items) returns all key-value pairs as tuples

MyDict = {
    "Name" : "gen_Ze",
    "information" : {
        "country" : "korea",
        "age" : 21
    }
}

print(list(MyDict.items()))
print(MyDict.items())

pair = list(MyDict.items())
print(pair[0])

# (.Get("key")) returns the key according to value

MyDict = {
    "movie" : "Ratatouille",
    "drama" : "Queen_Of_Tears",
    "action" : "Spiderman",
    "country" : {
        "united_states" : "Animation",
        "korea" : "Drama",
        "japan" : "Action"
    }
}

print(MyDict.get("movie"))
print(MyDict.get("country"))

# (.update(newdict)) inserts the specified items of the dictionary

MyDict = {
    "name" : "misbah",
    "age" : 18,
    "country" : "pakistan",
    "city" : "karachi",
    "student" : {
        "phy" : 40,
        "eng" : 50
        }
}

newdict = {
    "age" : 19,
    "city" : "lahore",
    "student" : {
        "math" : 60
        }
}

MyDict.update(newdict)
print(MyDict)