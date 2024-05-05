heights_of_hills = [141, 1, 17, -7, -17, 145, -27, 18, 541, 8, 7, 7, 1]

biggest_hill = heights_of_hills[0]

for hill_height in heights_of_hills:
    if hill_height > biggest_hill:
        biggest_hill = hill_height
        
print(biggest_hill)