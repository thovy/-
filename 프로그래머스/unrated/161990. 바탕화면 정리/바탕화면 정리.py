def solution(wallpaper):
    answer = []
    
    xlist = []
    ylist = []
    
    for xi, x in enumerate(wallpaper):
        # print (xi, x)
        for yi, y in enumerate(x):
            # print(xi, yi, y)
            if y == '#':
                # print(xi, yi, y)
                xlist.append(xi)
                ylist.append(yi)
                
    # print(xlist, ylist)
    answer.append(min(xlist))
    answer.append(min(ylist))
    answer.append(max(xlist)+1)
    answer.append(max(ylist)+1)
    print(answer)
    
    return answer