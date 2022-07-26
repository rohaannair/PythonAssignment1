from operator import sub
import math


def closestpoint(p_1,angle,origin):
    m_0 = (math.tan((angle * math.pi) / 180))
    c_0 = origin[1] - m_0 * origin[0]
    print("Slope of dir line",m_0)
    print(c_0)
    slope_1 = map(sub, p_1[1], p_1[0])
    slope_1 = list(slope_1)
    m_1 = slope_1[1] / slope_1[0]
    #print(slope_1)
    # We are checking the lines will intersect or not
    a_1 = p_1[0][1] - m_0 * p_1[0][0] - c_0
    a_2 = p_1[1][1] - m_0 * p_1[1][0] - c_0
    print(a_1, a_2)
    c_1 = p_1[0][1] - m_1 * p_1[0][0]
    #print(c_1)
    if ((a_1 * a_2) > 0):
        print("Line is excluded" )
    else:
        point=[]
        point.append(p_1)
        print("Point list",point)

        return (calDist(m_1,c_1,p_1,m_0,c_0,origin))

def calDist(m_1,c_1,p_1,m_0,c_0,origin):
    dist={}
    X=(m_0-m_1)/(c_1-c_0)
    Y=m_0*(X)+c_0

    distance= math.sqrt((origin[0]-X)**2+(origin[1]-Y)**2)
    print("Distance from origin to line segment",distance)
    dist=[]
    dist.append(distance)
    print("Distance list",dist)
    return dist

allSegment=[]
allDist=[]
origin=[]
for j in range(2):
    z = int(input("Enter Points for Origin ", ))
    origin.append(z)
print(origin)

angle =int(input("Enter direction :"))
p=[]
d1=[]

l = int(input("Enter number Line Segments:"))
for k in range(l):
    input_list = []
    for i in range(2):
        list1 = []
        for j in range(2):
            z = int(input("Enter Points for line ",))
            list1.append(z)
        input_list.append(list1)
    p=input_list
    d1=closestpoint(p,angle,origin)
    if(d1==None):
        d1=[100000000]
    allSegment.append(p)
    allDist.append(d1)

print("All segment", allSegment)
print("All dist", allDist)

minDist=allDist.index(min(allDist))
print(minDist)
print("the Closest line segment to ",origin,"is",allSegment[minDist])
