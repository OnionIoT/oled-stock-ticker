from OmegaExpansion import oledExp

oledExp.driverInit()
oledExp.clear()

def writeLines(lines, startingRow):

    # set the cursor to the beginning of the row where you want to start printing
    oledExp.setCursor(startingRow, 0)
    
    # write the lines row by row
    for i in range (0,len(lines)):
        oledExp.setCursor(startingRow + i, 0)
        oledExp.write(lines[i])
        