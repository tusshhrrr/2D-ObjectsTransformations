#Name:Tushar
#Roll no.:2018201
#Section-A
#Group:1
from math import *
import matplotlib.pyplot as plt

plt.ion()

rt=input("want to perform trasformations around origin or center of the shape?(O/C)")
def com(x, y,rt):
    sumx = 0
    sumlenx = 0
    sumy = 0
    sumleny = 0
    for i in range(len(x)):
        if i == (len(x) - 1):
            sumx += (((x[i] - x[0]) ** 2 + (y[i] - y[0]) ** 2) ** 0.5) * (x[i] + x[0]) / 2
            sumlenx += (((x[i] - x[0]) ** 2 + (y[i] - y[0]) ** 2) ** 0.5)
        else:
            sumx += (((x[i + 1] - x[i]) ** 2 + (y[i + 1] - y[i]) ** 2) ** 0.5) * (x[i + 1] + x[i]) / 2
            sumlenx += (((x[i + 1] - x[i]) ** 2 + (y[i + 1] - y[i]) ** 2) ** 0.5)
    dx = sumx / sumlenx
    for i in range(len(y)):

        if i == (len(y) - 1):
            sumy += (((x[i] - x[0]) ** 2 + (y[i] - y[0]) ** 2) ** 0.5) * (y[i] + y[0]) / 2
            sumleny += (((x[i] - x[0]) ** 2 + (y[i] - y[0]) ** 2) ** 0.5)
        else:
            sumy += (((x[i + 1] - x[i]) ** 2 + (y[i + 1] - y[i]) ** 2) ** 0.5) * (y[i + 1] + y[i]) / 2
            sumleny += (((x[i + 1] - x[i]) ** 2 + (y[i + 1] - y[i]) ** 2) ** 0.5)

    dy = sumy / sumleny
    if rt.lower()=="c":
        return (dx, dy)
    else:
        return (0,0)
def translate(u,v,dx,dy):
    a=[]
    b=[]
    x=[[1,0,0],[0,1,0],[dx,dy,1]]
    y=[[u,v,1]]
    p = len(x)
    q = len(y)
    r = len(x[0])
    s = len(y[0])
    k = 0
    if p == s:
        while k < p:
            b = []
            for i in range(q):

                c = 0

                for j in range(p):
                    c += x[j][k] * y[i][j]

                b.append(c)
            a.append(b)

            k = k + 1

        return (a[0][0], a[1][0])

def scaling(u,v,sx,sy):
    a=[]
    b=[]
    x=[[sx,0,0],[0,sy,0],[0,0,1]]
    y=[[u,v,1]]
    p = len(x)
    q = len(y)
    r = len(x[0])
    s = len(y[0])
    k = 0
    if p == s:
        while k < p:
            b = []
            for i in range(q):

                c = 0

                for j in range(p):
                    c += x[j][k] * y[i][j]

                b.append(c)
            a.append(b)

            k = k + 1

        return(a[0][0],a[1][0])

def rotation(u,v,delta):
    a=[]
    b=[]
    theta=delta*pi/180
    x=[[cos(theta),sin(theta),0],[(-sin(theta)),cos(theta),0],[0,0,1]]
    y=[[u,v,1]]
    p = len(x)
    q = len(y)
    r = len(x[0])
    s = len(y[0])
    k = 0
    if p == s:
        while k < p:
            b = []
            for i in range(q):

                c = 0

                for j in range(p):
                    c += x[j][k] * y[i][j]

                b.append(c)
            a.append(b)

            k = k + 1

        return (round(a[0][0],2), round(a[1][0],2))



flag=0
while flag==0:
    pol = input("Enter the shape:")
    if pol.lower()=="disc":
        flag=1
        a,b,r=map(float,input("Enter a(x-coordinate of centre of disc) ,b(y-coordinate of centre of disc) and r(radius of disc) separated by spaces:").split())
        X=[]
        Y=[]
        ang=0
        while ang<=360:
            thet=ang*pi/180

            X.append(a+r*cos(thet))
            Y.append(b+r*sin(thet))
            ang += 0.25
        Xn = X[:]
        Yn = Y[:]
        Xn.append(Xn[0])
        Yn.append(Yn[0])
        plt.plot(Xn, Yn)
        plt.show()
        plt.pause(0.0001)
        comm = "y"
        while comm.lower() != "quit":
            comm = input("Enter the transformation you want to do:")
            if comm[0].upper() == "S":
                Li = map(float, comm[1:].split())
                if len(list(Li)) == 2:
                    Sx, Sy = map(float, comm[1:].split())
                    Xn = []
                    Yn = []
                    if rt=="c":
                        dx = a
                        dy = b
                    else:
                        dx=0
                        dy=0
                    for i in range(len(X)):
                        x1, y1 = translate(X[i], Y[i], -dx, -dy)
                        Xn.append(x1)
                        Yn.append(y1)
                    a,b=translate(a,b,-dx,-dy)
                    X = Xn
                    Y = Yn

                    Xn = []
                    Yn = []

                    for i in range(len(X)):
                        x1, y1 = scaling(X[i], Y[i], Sx, Sy)
                        Xn.append(x1)
                        Yn.append(y1)
                    p = Xn[0]
                    q = Yn[0]
                    r = Xn[360]
                    s = Yn[360]
                    a,b=scaling(a,b,Sx,Sy)
                    ma = ((p - a) ** 2 + (q - b) ** 2) ** 0.5
                    mia = ((r - a) ** 2 + (s - b) ** 2) ** 0.5
                    ma=round(ma,2)
                    mia=round(mia,2)
                    X = Xn
                    Y = Yn
                    Xn = []
                    Yn = []
                    for i in range(len(X)):
                        x1, y1 = translate(X[i], Y[i], dx, dy)
                        Xn.append(x1)
                        Yn.append(y1)
                    a, b = translate(a, b, dx, dy)
                    X = Xn[:]
                    Y = Yn[:]
                    Xn.append(Xn[0])
                    Yn.append(Yn[0])


                    if mia!=ma:
                        print("x,y-coordinates of center and length of semi-axises are: %0.2f %0.2f %0.2f %0.2f" %(a, b, ma, mia))
                    else:
                        print ("x,y-coordinates of center and radius are: %0.2f %0.2f %0.2f " %(a, b, mia))

                    plt.plot(Xn, Yn)
                    plt.pause(0.0001)
                    plt.show()
                else:
                    print("Enter a valid transformation!!!")


            elif comm[0].upper() == "R":
                Li = map(float, comm[1:].split())
                if len(list(Li)) == 1:
                    delt = map(float, comm[1:].split())
                    delt = list(delt)
                    delta = delt[0]
                    Xn = []
                    Yn = []
                    if rt=="c":
                        dx = a
                        dy = b
                    else:
                        dx=0
                        dy=0
                    for i in range(len(X)):
                        x1, y1 = translate(X[i], Y[i], -dx, -dy)
                        Xn.append(x1)
                        Yn.append(y1)
                    a, b = translate(a, b, -dx, -dy)
                    X = Xn
                    Y = Yn

                    Xn = []
                    Yn = []

                    for i in range(len(X)):
                        x1, y1 = rotation(X[i], Y[i], delta)
                        Xn.append(x1)
                        Yn.append(y1)
                    a,b=rotation(a,b,delta)
                    p = Xn[0]
                    q = Yn[0]
                    r = Xn[360]
                    s = Yn[360]

                    ma = ((p - a) ** 2 + (q - b) ** 2) ** 0.5
                    mia = ((r - a) ** 2 + (s - b) ** 2) ** 0.5
                    ma = round(ma, 2)
                    mia = round(mia, 2)
                    X = Xn
                    Y = Yn
                    Xn = []
                    Yn = []
                    for i in range(len(X)):
                        x1, y1 = translate(X[i], Y[i], dx, dy)
                        Xn.append(x1)
                        Yn.append(y1)
                    a, b = translate(a, b, dx, dy)
                    X = Xn[:]
                    Y = Yn[:]
                    Xn.append(Xn[0])
                    Yn.append(Yn[0])
                    if mia!=ma:
                        print("x,y-coordinates of center and length of semi-axises are: %0.2f %0.2f %0.2f %0.2f" %(a, b, ma, mia))
                    else:
                        print ("x,y-coordinates of center and radius are: %0.2f %0.2f %0.2f " %(a, b, mia))

                    plt.plot(Xn, Yn)
                    plt.pause(0.0001)
                    plt.show()
                else:
                    print("Enter a valid transformation!!!")
            elif comm[0].upper() == "T":
                Li = map(float, comm[1:].split())
                if len(list(Li)) == 2:
                    dx, dy = map(float, comm[1:].split())
                    Xn = []
                    Yn = []

                    for i in range(len(X)):
                        x1, y1 = translate(X[i], Y[i], dx, dy)
                        Xn.append(x1)
                        Yn.append(y1)
                    a,b=translate(a,b,dx,dy)
                    p = Xn[0]
                    q = Yn[0]
                    r = Xn[361]
                    s = Yn[361]

                    ma = ((p-a) ** 2 + (q-b) ** 2) ** 0.5
                    mia = ((r-a) ** 2 + (s-b) ** 2) ** 0.5
                    ma = round(ma, 2)
                    mia = round(mia, 2)
                    X=Xn
                    Y=Yn
                    Xn.append(Xn[0])
                    Yn.append(Yn[0])


                    if mia!=ma:
                        print("x,y-coordinates of center and length of semi-axises are: %0.2f %0.2f %0.2f %0.2f" %(a, b, ma, mia))
                    else:
                        print ("x,y-coordinates of center and radius are: %0.2f %0.2f %0.2f " %(a, b, mia))

                    plt.plot(Xn, Yn)
                    plt.pause(0.0001)
                    plt.show()
                else:
                    print("Enter a valid transformation!!!")
            elif comm.lower() != "quit":
                print("Enter a valid transformation!!!")
    elif pol.lower()=="polygon":
        flag=1
        flag2=0
        while flag2==0:
            X=list(map(float,input("Enter the x-coordinaters of the polygon separated by spaces:").split()))
            Y=list(map(float,input("Enter the y-coordinates of the polygon separated by spaces:").split()))
            if len(X)==len(Y):
                flag2=1
            else:
                print ("Enter valid polygon!!!")


        Xn=X[:]
        Yn=Y[:]
        Xn.append(Xn[0])
        Yn.append(Yn[0])
        plt.plot(Xn, Yn)
        plt.pause(0.0001)
        plt.show()
        comm = "y"
        while comm.lower() != "quit":
            comm = input("Enter the transformation you want to do:")
            if comm[0].upper() == "S":
                Li = map(float, comm[1:].split())
                if len(list(Li)) == 2:
                    Sx, Sy = map(float, comm[1:].split())
                    Xn = []
                    Yn = []
                    dx,dy=com(X,Y,rt)
                    for i in range(len(X)):
                        x1, y1 = translate(X[i], Y[i], -dx, -dy)
                        Xn.append(x1)
                        Yn.append(y1)
                    X = Xn
                    Y = Yn

                    Xn = []
                    Yn = []

                    for i in range(len(X)):
                        x1, y1 = scaling(X[i], Y[i], Sx,Sy)
                        Xn.append(x1)
                        Yn.append(y1)
                    X = Xn
                    Y = Yn
                    Xn = []
                    Yn = []
                    for i in range(len(X)):
                        x1, y1 = translate(X[i], Y[i], dx, dy)
                        Xn.append(x1)
                        Yn.append(y1)
                    X = Xn[:]
                    Y = Yn[:]
                    s=""
                    for c in X:
                        c=round(c,2)
                        s = s + " " + str(c)
                    print ("x-coordinates of the vertices %s" %s)
                    s = ""
                    for c in Y:
                        c=round(c, 2)
                        s = s + " " + str(c)
                    print ("y-coordinates of the vertices %s" %s)
                    Xn.append(Xn[0])
                    Yn.append(Yn[0])
                    plt.plot(Xn, Yn)
                    plt.pause(0.0001)
                    plt.show()
                else:
                    print("Enter a valid transformation!!!")

            elif comm[0].upper() == "R":
                Li = map(float, comm[1:].split())
                if len(list(Li)) == 1:
                    delt = map(float, comm[1:].split())
                    delt = list(delt)
                    delta = delt[0]
                    Xn = []
                    Yn = []
                    dx, dy = com(X, Y,rt)
                    for i in range(len(X)):
                        x1, y1 = translate(X[i], Y[i], -dx, -dy)
                        Xn.append(x1)
                        Yn.append(y1)
                    X = Xn
                    Y = Yn


                    Xn=[]
                    Yn=[]

                    for i in range(len(X)):
                        x1,y1=rotation(X[i],Y[i],delta)
                        Xn.append(x1)
                        Yn.append(y1)
                    X=Xn
                    Y=Yn

                    Xn = []
                    Yn = []
                    for i in range(len(X)):
                        x1, y1 = translate(X[i], Y[i], dx, dy)
                        Xn.append(x1)
                        Yn.append(y1)
                    X = Xn[:]
                    Y = Yn[:]
                    s=""
                    for c in X:
                        c=round(c, 2)
                        s=s+" "+str(c)
                    print ("x-coordinates of the vertices %s" %s)
                    s=""
                    for c in Y:
                        c=round(c, 2)
                        s=s+" " +str(c)
                    print ("y-coordinates of the vertices %s" %s)
                    Xn.append(Xn[0])
                    Yn.append(Yn[0])
                    plt.plot(Xn,Yn)
                    plt.pause(0.0001)
                    plt.show()
                else:
                    print("Enter a valid transformation!!!")

            elif comm[0].upper() == "T":
                Li = map(float, comm[1:].split())
                if len(list(Li)) == 2:

                    dx, dy = map(float, comm[1:].split())
                    Xn = []
                    Yn = []
                    for i in range(len(X)):
                        x1,y1=translate(X[i],Y[i],dx,dy)
                        Xn.append(x1)
                        Yn.append(y1)
                    X=Xn[:]
                    Y=Yn[:]
                    s=""
                    for c in X:
                        c=round(c, 2)
                        s=s+" "+str(c)
                    print ("x-coordinates of the vertices %s" %s)
                    s=""
                    for c in Y:
                        c=round(c, 2)
                        s=s+" " +str(c)
                    print ("y-coordinates of the vertices %s" %s)
                    Xn.append(Xn[0])
                    Yn.append(Yn[0])
                    plt.plot(Xn, Yn)
                    plt.pause(0.0001)
                    plt.show()
                else:
                    print("Enter a valid transformation!!!")
            elif comm.lower() != "quit":
                print("Enter a valid transformation!!!")
    else:
        print("Enter a valid shape!!!")