screenPlay = open("C:\\Users\\Snades\\Desktop\\roteiros\\roteiro1.txt", "r")


scene_bool_1 = "EXT"
scene_bool_2 = "INT"
lines = []

    
for block in screenPlay:
    line = block.split('\n')
    lines.append(line)

for x in lines:
    if x.__contains__('EXT'):
        print(x)


