maps = [{
    "Dg set": "Diesel generator"
}, {
    "Organization": "Organisation"
}, {
    "Group": "Organization"
}, {
    "Orange": "Kinnu"
}, {
    "Orange": "narangi"
}]

# taking dict so that only unique outputs are considered 
# it will map strings to lists (of synonyms) 
output = {}

# iterating over the dicts
for d in maps:
    # taking out the key
    key = list(d.keys())[0]
    # so we will try to access the dict key as if it already exists
    try:
        output[key].append(d[key])
        # print(d[key])
    # if the key doesn't exist we will try to access with the value as key instead
    except:
        try:
            output[d[key]].append(key)
        # if even that doesn't exist we will just add this new word
        except:
            output[key] = [d[key],key]

# type casting to get the desired form
print(list(output.values()))

# i don't think we can do this question with a faster time complexity than O(n)