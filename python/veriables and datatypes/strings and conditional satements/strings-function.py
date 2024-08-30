#        (endswith) returns true if string ends with strings

inbox = "I am a coder and artist"
print(inbox.endswith("er"))         # False
print(inbox.endswith("ist"))        # True

#        (capitalize) capitalizes 1st character

inbox = "networking-protocols-cpp"
inbox = inbox.capitalize()
print(inbox)


#        (replace(old, new)) replace all occurrences of old with new

inbox = "web-development-html-css"    
print(inbox.replace("html-css", "python"))

#        (find) return 1st index of 1st occurrences 

inbox = "data-analysis-python"
print(inbox.find("python"))

#        (count) counts the occurrences of substring in strings

inbox = "machine-learning-algorithms"
print(inbox.count("i"))