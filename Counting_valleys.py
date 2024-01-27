def countingValleys(steps, path):
    count = 0
    altitude = 0
    inValley = False

    for step in path:
        if step == 'U':
            altitude += 1
        elif step == 'D':
            altitude -= 1
        
        if altitude < 0 and not inValley:
            inValley = True
        elif altitude == 0 and inValley:
            inValley = False
            count += 1
    
    return count