a = "DRAWING CANVAS"

# OUTPUT = CAN [USE -INDEXING]
output1 = a[-6] + a[-5] + a[-4]  # 'C' + 'A' + 'N'

# OUTPUT = VA N [USE +INDEXING]
output2 = a[11] + a[12] + a[7]  # 'V' + 'A' + ' ' (space from index 7)

# OUTPUT = RAW [USE -INDEXING]
output3 = a[-13] + a[-12] + a[-11]  # 'R' + 'A' + 'W'

# OUTPUT = ING [USE +INDEXING]
output4 = a[3] + a[4] + a[5]  # 'I' + 'N' + 'G'

# Print results
print("OUTPUT1:", output1)
print("OUTPUT2:", output2)
print("OUTPUT3:", output3)
print("OUTPUT4:", output4)
