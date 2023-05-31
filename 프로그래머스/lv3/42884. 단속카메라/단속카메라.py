def solution(routes):
    answer = len(routes)

    total_routes = {}
    for i in range(-30000, 30001):
        total_routes[i] = 0

    answer = 0
    cam = []
    routes = sorted(routes, key= lambda x:x[1])
    for route in routes:
        start, end = route[0], route[1]
        joongbok = False
        for c in cam:
            if c in range(start, end+1):
                joongbok = True
                break
        if not joongbok:
            cam.append(end)
            answer += 1

    return answer