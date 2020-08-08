# list contains homogeneous items, i.e. of same type
# however we can store almost any type in list

flowers = [
    "Daffodil",
    "Evening Primrose",
    "Hydrangea",
    "Iris",
    "Lavender",
    "Sunflower",
    "Tiger Lily"
]

# for flower in flowers:
#     print(flower)

separator = " | "
output = separator.join(flowers)  # join is method in str class, and iterates over the list
print(output)
