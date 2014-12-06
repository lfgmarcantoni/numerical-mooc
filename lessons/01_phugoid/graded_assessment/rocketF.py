import numpy as np 
"""		
assessment 1
course: Practical Numerical Methods with Python
year: 2014
by: Luis F. Gutierrez
Description: 
Solve the rocket equation model for purely verical flight. 
"""
dt=0.01 # time step 
t=100.0 # time of computation
nts=t/dt # number of time steps 
nts=np.int(nts) 
ms= 50.0  #Rocket shell weight
g = 9.81 #Gravitational acceleration
rho = 1.091 #Air density
r = 0.5  #Rocket radius 
A=np.pi*r*r  #Rocket area
ve = 325.0 # exhaust gas velocity
CD=0.15 #Drag coeficient
mp0= 100  #propelant mass at t=0.0
mpdot = 20.0 #propelant burn rate
print 't',t
print 'dt',dt
times=np.arange(0.0,(t+dt),dt)
h=np.zeros(times.size)
v=np.zeros(times.size)
h[0]=0.0 #Ic
v[0]=0.0 #Ic
print'times[1]',times[1]
print 'times',times  
print 'dim.times',times.size

# Euler method: 
for i in range(times.size-1):
	mp = mp0 - mpdot*times[i]
	if (times[i]<0.0)|(times[i]>5.0):
   	   mp=0.0
	   mpdot=0.0
        v[i+1]=(-g+(mpdot/(ms+mp))*ve-(1.0/2.0)*rho*A*CD*v[i]*np.abs(v[i])*(1/(mp+ms)))*dt+v[i]
        h[i+1]=h[i]+v[i]*dt  
import time as tm

print 'h max',np.max(h)
print 'v max',np.max(v)
print 'h size',h.size
for i in range(0,h.size):
#	print 'i',i, 'times',times[i],'vel',v[i]
 #       tm.sleep(1.0)  
        if (v[i]<0.0):
	      print 'max alt time',times[i-1]
              print 'max alt',h[i-1]
              hmax=h[i-1]
	      thmax=times[i-1]
              break
for i in range(0,h.size):
        if(times[i]>5.0)&(h[i]<0.03):
        	print 'imp time',times[i]
                print 'imp velocity',v[i]
		impv=v[i]
		impt=times[i]
	        break

import matplotlib.pyplot as plt

plt.figure(1)
plt.title('altitude')
plt.plot(times,h)
plt.xlabel('time[s]')
plt.ylabel('h[m]')

plt.annotate('hmax= %s'%hmax, xy=(thmax, hmax),  xycoords='data',
                xytext=(15,15), textcoords='offset points',
                arrowprops=dict(arrowstyle="->")
                )

plt.annotate('imp vel time= %s'%impv, xy=(impt, impv),  xycoords='data',
                xytext=(15,15), textcoords='offset points',
                arrowprops=dict(arrowstyle="->")
                )


plt.figure(2)
plt.title('velocity')
plt.plot(times,v)
plt.xlabel('time[s]')
plt.ylabel('v[m]')


plt.figure(3)
plt.title('velocity vs. altitude')
plt.plot(h,v)
plt.xlabel('h')
plt.ylabel('v[m]')
plt.show()
