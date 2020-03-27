import math
import matplotlib.pyplot as plt


##### Input all the terms, mass,c,ro,area,g,initial velocity
ro=1.225
c=0.5
r=0.0366
area=(math.pi*r*r)
mass=0.145
dt=0.001     #time interval
v0=50
angle=30

g=9.8
t=0  
tmax=10

theta=math.radians(angle)   #angle in radians

vy=[v0*math.sin(theta)] 
vx=[v0*math.cos(theta)]


x=[0]#initial coordinates
y=[0]#initial y cordinate


# functions
def v(v_x,v_y):
    v=math.sqrt(v_x**2+v_y**2)
    return v

def DE(ro,area):       # drag 
    DD=float((ro*area*c)/2)
    return DD

p=0

accel_x=[]
accel_y=[]
#-----------------------------------------------------------------------------------------------------------#
# with drag #

while y[p]>=0:
    
    D=DE(ro,area)  # D in eqn
    
    vxx=float(vx[p]) # x coponent of velocity at pth position in list
    vyy=float(vy[p]) # y component of velocity at pth position in list
    vv=v(vxx,vyy)
    ayy=-g-((D/mass)*vyy*vv) #acceleration y component
    axx=-(D/mass)*vxx*vv   #acceleration x component

    accel_x.append(axx) #acceleration in x direction
    accel_y.append(ayy)    #acceleration in y direction

    delta_x=(vxx*dt)+(accel_x[p]*(dt**2)/2)  # dx
    delta_y=(vyy*dt)+(accel_y[p]*(dt**2)/2)   #dy
    

    accelxx=accel_x[p]
    accelyy=accel_y[p]
    
    
    vx.append(vxx+(accelxx*dt) )# vx + delta vx
    vy.append(vyy+(accelyy*dt)) #  vy + delta vy


    x.append(x[p]+delta_x) #adding the value of x to list
    y.append(y[p]+delta_y) #adding the value of y to list

    t=t+dt
    p=p+1


##########for d=0
#  without drag
#--------------------------------------------------------------------------------------------------------------------#

x0=[0]
y0=[0]

t0=0
accel_x0=[]
accel_y0=[]

vy0=[v0*math.sin(theta)] 
vx0=[v0*math.cos(theta)]

p=0

while y0[p]>=0:
    
    d=0  # D in eqn
    
    vxx=float(vx0[p]) # x coponent of velocity at pth position in list
    vyy=float(vy0[p]) # y component of velocity at pth position in list
    vo=math.sqrt(vxx**2+vyy**2)
    ayy=-g-((d/mass)*vyy*vo) #acceleration y component
    axx=-(d/mass)*vxx*vo   #acceleration x component

    accel_x0.append(axx) #acceleration in x direction
    accel_y0.append(ayy)    #acceleration in y direction

    delta_x=(vxx*dt)+(accel_x0[p]*(dt**2)/2)  # dx
    delta_y=(vyy*dt)+(accel_y0[p]*(dt**2)/2)   #dy
    

    accelxx=accel_x0[p]
    accelyy=accel_y0[p]
    
    
    vx0.append(vxx+(accelxx*dt) )# vx + delta vx
    vy0.append(vyy+(accelyy*dt)) #  vy + delta vy


    x0.append(x0[p]+delta_x) #adding the value of x to list
    y0.append(y0[p]+delta_y) #adding the value of y to list

    t0=t0+dt
    p=p+1
    

####### Graph
print("Maximum range with drag is ",x[-1])
print("Maximum range without drag is ",x0[-1])


plt.plot(x,y,'r-',label='With drag')
plt.plot(x0,y0,'b-',label='without drag')
plt.grid()
plt.ylabel("Y axis")
plt.xlabel("X axis")
plt.show()

