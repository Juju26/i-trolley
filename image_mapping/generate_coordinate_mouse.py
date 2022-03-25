#generate coordinates of the item location using mouse click
#xdata and y data gives you the coordinates with which you can plot the item

import matplotlib.pyplot as plt
import matplotlib.image as mpimg

def onclick(event): 
    print("button=%d, x=%d, y=%d, xdata=%f, ydata=%f" % ( 
         event.button, event.x, event.y, event.xdata, event.ydata)) 

img = mpimg.imread('E:/projects/smart trolley/image_mapping/imgs/floor_1.png')
plt.figure(figsize = (12,12))
ax = plt.imshow(img)
fig = ax.get_figure()
cid = fig.canvas.mpl_connect('button_press_event', onclick) 

plt.show()