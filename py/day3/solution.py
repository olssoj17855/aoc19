def parse(path):
    with (open(path, "r")) as file:
        return [[(s[0], int(s[1:])) for s in w.split(",")] for w in file.readlines()]

def wire_segments(wire):
    pos = (0, 0)
    segs = []
    totsteps = 0

    for d, steps in wire:
        x, y = pos
        if d == 'U':
            seg = ('v', pos, steps, totsteps)
        elif d == 'D':
            seg = ('v', pos, steps*-1, totsteps)
        elif d == 'L':
            seg = ('h', pos, steps*-1, totsteps)
        elif d == 'R':
            seg = ('h', pos, steps, totsteps)
    
        if seg[0] == 'v':
            pos = (x, y+seg[2])
        else:
            pos = (x+seg[2], y)
        segs.append(seg)
        totsteps += abs(steps)
    return ([s for s in segs if s[0] == 'h'],[s for s in segs if s[0] == 'v'])

def crossing_point(hs, vs):
    _, (hx, hy), hl, ht = hs
    _, (vx, vy), vl, vt = vs
    if sorted([hx, hx+hl, vx])[1] != vx:
        return False
    if sorted([vy, vy+vl, hy])[1] != hy:
        return False
    return (vx, hy, ht+abs(vx-hx), vt+abs(hy-vy))

def manhattan_distance(p):
    x,y,_,_ = p
    return abs(x) + abs(y)
    

if __name__ == "__main__":
    wires = parse("input")
    w0h,w0v = wire_segments(wires[0])
    w1h,w1v = wire_segments(wires[1])

    x = (None, (0,0), 5)
    y = (None, (2,-3), 7)

    crossing_points = [p for p in

                       [crossing_point(hseg, vseg)
                        for hseg in w0h for vseg in w1v]
                       +
                       [crossing_point(hseg, vseg)
                        for hseg in w1h for vseg in w0v]

                       if p]

    print(min([manhattan_distance(p) for p in crossing_points]))
    print(min([p[2]+p[3] for p in crossing_points]))


