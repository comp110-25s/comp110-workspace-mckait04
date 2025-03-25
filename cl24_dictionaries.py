"""examples of set and dictionary syntax"""

pids: set[int] = {730560970, 712345678}
pids.add(710000000)

ice_cream: dict[str, int] = {
    "chocolate": 12, 
    "vanilla": 8, 
    "strawberry": 4
    }

print(ice_cream["vanilla"] += 110) 
print(len(ice_cream))
