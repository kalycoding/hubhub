droplet = []
with open('instructions2.txt', 'r') as f:
    for line in f:
        x,y,z = map(int, line.strip().split(','))
        droplet.append((x,y,z))


def calculate_area(droplet):
    empty = set()
    for x,y,z in droplet:
        empty.add((x,y,z))

    ans = 0

    for x,y,z in empty:
        cover = 0
        #check adjacent cubes in all direction
        for dx, dy, dz in [(1,0,0), (-1,0,0), (0,1,0), (0,-1,0),(0,0,1), (0,0,-1)]:
            adj_cube = (x+dx, y+dy, z+dz)

            if adj_cube in empty:
                cover+=1

        ans+=6-cover

    return ans



print(calculate_area(droplet))