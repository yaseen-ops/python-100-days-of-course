# Install prettytable package
from prettytable import PrettyTable

table = PrettyTable()
# table.add_column("Pokemon Name", ["Pikachu", "Squirtle", "Charmander"], "l", "m")
# table.add_column("Type", ["Electric", "Water", "Fire"], "l", "m")

# OR Align separately
table.add_column("Pokemon Name", ["Pikachu", "Squirtle", "Charmander"])
table.add_column("Type", ["Electric", "Water", "Fire"])
table.align = "l"
table.valign = "m"
print(table)
