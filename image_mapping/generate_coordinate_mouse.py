#generate coordinates of the item location using mouse click
#xdata and y data gives you the coordinates with which you can plot the item


import matplotlib.pyplot as plt
import matplotlib.image as mpimg

column="abcdefghijklmnopqrstuvwxyz"
row="123456"
rack="123"
location_list=[]
counter=0

for i in column:
    for j in row:
        for k in rack:
            location_list.append(str(i)+'-'+str(j)+'-'+str(k))
def onclick(event): 
    global counter
    print("location=%s, xdata=%f, ydata=%f" % (location_list[counter], event.xdata, event.ydata)) 

    counter+=1

def onrelease(event):
    pass
img = mpimg.imread('E:/projects/smart trolley/image_mapping/imgs/floor_1.png')
plt.figure(figsize = (12,12))
ax = plt.imshow(img)
fig = ax.get_figure()
cid = fig.canvas.mpl_connect('button_press_event', onclick) 
cid = fig.canvas.mpl_connect('button_press_event', onrelease)
plt.show()