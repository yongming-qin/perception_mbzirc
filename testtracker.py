import math
def dist(x,y):
    return math.sqrt(math.pow(x[0]-y[0],2)+math.pow(x[1]-y[1],2))

count=0
xprev=0
yprev=0
zprev=0

xframe=600
yframe=450

phi=0*math.pi/180

boxinfo={'Red':(33,28.5,16)}
target='Red'


correction=1.35
tmaj=boxinfo[target][0]*correction
theta=78*math.pi/180


#xa=math.asin(2*(x-300)*math.sin(theta/2)/600)
#ya=math.asin(2*(y-225)*math.sin(theta/2)/450)
#phi=math.asin(math.sqrt(math.sin(xa)**2+math.sin(ya)**2))
#r=radius#/math.cos(phi)

cpc = 2*math.tan(theta/2)


t=(10,10)
r=(30,10)
l=(10,20)

b=(r[0]+l[0]-t[0],r[1]+l[1]-t[1])

print(b)

a1=dist(t,r)
a2=dist(t,l)

x=(r[0]+l[0])/2
y=(r[1]+l[1])/2

phi-=theta*(y-yframe/2)/yframe

major=max(a1,a2)
minor=min(a1,a2)
var=l
if major==a1:
    var=r
else:
    var=l

rot=(math.atan2(t[1]-var[1],var[0]-t[0]))+math.pi/2
tmaj*=1-(1-math.cos(phi))*math.cos(rot)

framewidth=tmaj*xframe/major

z=framewidth/cpc


xp=framewidth*(x-xframe/2)/xframe
yp=framewidth*(y-yframe/2)/yframe
count+=1
xprev=(xprev*19/20+xp/20)*20
yprev=(yprev*19/20+yp/20)*20
zprev=(zprev*19/20+z/20)*20

print(major,minor)

if count%20==1:
    print("X dist: "+str(round(zprev)), "Y dist: "+str(round(xprev)),"Z dist: "+ str(round(yprev)), "Absolute distance: "+str(round((math.sqrt(xprev**2+yprev**2+zprev**2)))))


#def dist(x,y):
#    return math.sqrt((x[0]-y[0])^2+(x[1]-y[1])^2)
