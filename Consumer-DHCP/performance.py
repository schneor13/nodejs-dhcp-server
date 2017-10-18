import matplotlib.pyplot as plt
import matplotlib.animation as animation
import time

fig = plt.figure()
ax1 = fig.add_subplot(1,1,1)

def animate(i):
    num = 0
    pullData = open("Log.txt","r").read()
    dataArray = pullData.split('\n')
    num = 0
    for i in dataArray:
	num += 1
    xar = []
    yar = []
    c = 0
    sum = 0
    last = 0
    start = 1
    amount = 0
    curr = 0
    pullData = open("Log.txt","r").read()
    dataArray = pullData.split('\n')
    for eachTime in dataArray:
        if len(eachTime)>1:
	    if num - amount > 10:
		amount += 1
		#print 'need more update \n'
		curr += 1
		continue
            x = (int(eachTime.split(".")[0])) % 10000
	    sum += x - last
	    c += 1
            xar.append(x)
	    start += x - last
            yar.append((c / (x - last + 1)) * 1 )
	    last = x 
    ax1.clear()
    ax1.plot(xar,yar)
ani = animation.FuncAnimation(fig, animate, interval=5000)
plt.show()
