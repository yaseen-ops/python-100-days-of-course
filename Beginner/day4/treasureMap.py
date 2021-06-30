row1 = ["⬜", "⬜", "⬜"]
row2 = ["⬜", "⬜", "⬜"]
row3 = ["⬜", "⬜", "⬜"]
puzzle_map = [row1, row2, row3]

position = input("Enter the position \n")
horizontal = int(position[0])
vertical = int(position[1])

puzzle_map[horizontal - 1][vertical - 1] = "X"

print(f"{row1}\n{row2}\n{row3}")
