def on_bingo_tabel(table):
    
    result = True
    
    for j in range(5):
        for i in range(5):
            if (j * 15 + 1) <= table[i][j] <= ((j + 1) * 15):
                pass
            else:
                result = False
    return result
        
print(on_bingo_tabel ([[1, 30, 34, 55, 1],
                [10, 16, 40, 50, 67],
                [5, 20, 38, 48, 61],
                [4, 26, 43, 49, 70],
                [15, 17, 33, 51, 66]]))

