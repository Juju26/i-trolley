"""
To store and draw lines showing paths...
path_columns()  will give the path through the particular column ..6
"""


import matplotlib.pyplot as plt
import matplotlib.image as mpimg

img = mpimg.imread('E:/projects/smart trolley/image_mapping/imgs/floor_1.png')
plt.figure(figsize = (12,12))
ax = plt.imshow(img)

#  xdata=248.965395, ydata=1474.687223
#  xdata=342.204082, ydata=1444.447649

i=0
def path_AB():
    coordinates=[[211.090423, 1351.577047],
 [211.090423, 1300.926075],
 [211.090423, 1232.547262],
 [203.492777, 1156.570804],
 [203.492777, 1055.268860],
 [206.025325, 946.369271],
 [203.492777, 865.327715],
 [208.557874, 764.025771]]
    x_points=[coordinates[0][0],coordinates[len(coordinates)-1][0]]
    y_points=[coordinates[0][1],coordinates[len(coordinates)-1][1]]
    plt.plot(x_points, y_points, color='green', linestyle='dashed', marker='o',markerfacecolor='blue', markersize=10)
   

def path_CD():
    coordinates=[[637.039929, 1326.009317],
 [634.519965, 1268.050133],
 [634.519965, 1202.531056],
 [634.519965, 1147.091837],
 [634.519965, 1071.492902],
[ 637.039929, 1003.453860],
 [637.039929, 945.494676],
[ 632.000000, 869.895741 ],
 [632.000000, 789.256877],
 [647.119787, 743.897516]]
    x_points=[coordinates[0][0],coordinates[len(coordinates)-1][0]]
    y_points=[coordinates[0][1],coordinates[len(coordinates)-1][1]]
    plt.plot(x_points, y_points, color='green', linestyle='dashed', marker='o',markerfacecolor='blue', markersize=10)
   

if __name__=="__main__":
    path_AB()
    path_CD()
    plt.show()