from collections import deque
def complete_path (start, end, topo):
    if start not in topo or end not in topo:
        return []
    maxlevel = 14
    space = deque ()
    for p in topo[start]:
        space.append ([p])
    while len (space) > 0:
        path = space.popleft ()
        if path[-1] in topo[end]:
            return path
        if len(path) == maxlevel:
            continue
        for p in topo[path[-1]]:
            if p in path:
                continue
            newp = path[:]
            newp.append (p)
            space.append (newp)
    return []

