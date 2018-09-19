def isInsidePolygon(pt, poly):
    c = False
    i = -1
    l = len(poly)
    j = l - 1
    while i < l-1:
        i += 1
        #print (i,poly[i], j,poly[j])
        if ((poly[i]["x"] <= pt["x"] and pt["x"] < poly[j]["x"]) or (poly[j]["x"] <= pt["x"] and pt["x"] < poly[i]["x"])):
            if (pt["y"] < (poly[j]["y"] - poly[i]["y"]) * (pt["x"] - poly[i]["x"]) / (poly[j]["x"] - poly[i]["x"]) + poly[i]["y"]):
                c = not c
        j = i
    return c

def count(num_2, array_c, poly):
    for i in range(num_2):
        count = 0
        if isInsidePolygon(array_c[i], poly):
            count += 1
    return count


if __name__ == '__main__':
    line1 = input()
    line2 = input()
    list_1 = line1.split()
    list_2 = line2.split()
    num_1 = int(list_1[0])
    num_2 = int(list_2[0])
    array = []
    array_c = []
    dic = {}
    dic_c = {}
    for i in range(1, num_1, 2):
        dic["x"] = int(list_1[i])
        dic["y"] = int(list_1[i+1])
        array.append(dic)
        dic = {}
    for i in range(1, num_2, 2):
        dic["x"] = int(list_2[i])
        dic["y"] = int(list_2[i+1])
        array_c.append(dic_c)
        dic_c = {}
    print(array_c, array)
    result = count(num_2, array_c, array)
    print(result)
