def gen_sapin(height=10):
 
    symbols = ['o', '.']
    tree_char = '.'
    
    tree = []
    
    tree.append(" " * height + ".")
    
    # each level of the tree
    for i in range(height):
        level = ""
        padding = " " * (height - i)
        for j in range(2 * i + 1):
            char = symbols[(i + j) % 2] if j % 2 == 0 else tree_char
            level += char
        tree.append(padding + level)
    
    trunk_width = 1 if height % 2 == 0 else 3
    trunk = " " * (height - 1) + "|" * trunk_width
    tree.append(trunk)
    
    message = " " * (height - 6) + "Merry Christmas!"
    tree.append(message)
    
    return "\n".join(tree)

heightInput = int(input("Rentrez la hauteur du sapin svp:)"))
# Joyeux Noel:)))

sapin_noel = gen_sapin(height=heightInput)
print(sapin_noel)


