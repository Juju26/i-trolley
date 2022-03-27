import random
from matplotlib import image
from matplotlib import pyplot as plt
  
# to read the image stored in the working directory
data = image.imread('/content/floor_1.png')
  
# to draw a point on co-ordinate (200,300)
#plt.plot(800, 500, marker='v', color="red")
plt.figure(figsize = (12,12))
plt.imshow(data,aspect='auto')
# plt.plot(46.866249,1237.763707, marker='v', color="red")
# plt.plot(73.806109,1232.375735, marker='v', color="red")
# plt.plot(106.133940,1224.293777, marker='v', color="red")
# plt.plot(44.172263,1143.474198, marker='v', color="red")
# plt.plot(537.171694, 1235.069721, marker='v', color="red")
plt.show()