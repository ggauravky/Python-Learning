essential_spices = {"cardamom", "ginger", "cinnamon"}
optional_spices = {"cloves", "ginger", "black pepper"}

all_spices = essential_spices | optional_spices  # union
print(f"All spices: {all_spices}")

common_spices = essential_spices & optional_spices  # intersection
print(f"common spices: {common_spices}")

only_in_essential = essential_spices - optional_spices  # difference
print(f"Only in essential spices: {only_in_essential}")

print(f"Is 'cloves' in optional spices? {'cloves' in optional_spices}") 

unique_spices = essential_spices ^ optional_spices  # symmetric difference
print(f"Unique spices: {unique_spices}")

frozen_spices = frozenset(["nutmeg", "star anise", "fennel"])
print(f"Frozen spices: {frozen_spices}")

spice_list = list(essential_spices)
spice_list.append("turmeric")
print(f"Spice list: {spice_list}")
spice_set = set(spice_list)
print(f"Spice set: {spice_set}")

