"""
To store and draw lines showing paths...
path_columns()  will give the path through the particular column ..6
"""


from tokenize import cookie_re
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
   
def path_EF():
    coordinates=[[1057.110985, 1232.375735],
    [1046.335041, 1132.698255],
    [1046.335041, 1027.632802],
    [1051.723013, 949.507209],
    [1043.641055, 860.605673],
    [1051.723013, 766.316164]]
    x_points=[coordinates[0][0],coordinates[len(coordinates)-1][0]]
    y_points=[coordinates[0][1],coordinates[len(coordinates)-1][1]]
    plt.plot(x_points, y_points, color='green', linestyle='dashed', marker='o',markerfacecolor='blue', markersize=10)


def path_GH():
    coordinates=[ [1057.874002, 595.219610],
    [1060.393966, 577.579858],
    [1055.354037, 476.781278],
    [1047.794144, 381.022626],
    [1050.314108, 290.303904],
    [1057.874002, 199.585182],
    [1062.913931, 111.386424],
    [1060.393966, 53.427240]]
    x_points=[coordinates[0][0],coordinates[len(coordinates)-1][0]]
    y_points=[coordinates[0][1],coordinates[len(coordinates)-1][1]]
    plt.plot(x_points, y_points, color='green', linestyle='dashed', marker='o',markerfacecolor='blue', markersize=10)

def path_IJ():
    coordinates=[[644.599823, 582.619787],
    [639.559894, 471.741349],
    [632.000000, 378.502662],
    [632.000000, 287.783940],
    [634.519965, 197.065217],
    [642.079858, 106.346495],
    [644.599823, 66.027063]]
    x_points=[coordinates[0][0],coordinates[len(coordinates)-1][0]]
    y_points=[coordinates[0][1],coordinates[len(coordinates)-1][1]]
    plt.plot(x_points, y_points, color='green', linestyle='dashed', marker='o',markerfacecolor='blue', markersize=10)

def path_KL():
    coordinates=[ [206.125998, 620.419255],
    [208.645963, 572.539929],
    [216.205856, 474.261313],
    [216.205856, 381.022626],
    [211.165927, 295.343833],
    [208.645963, 197.065217],
    [211.165927, 113.906389],
    [211.165927, 48.387311]]
    x_points=[coordinates[0][0],coordinates[len(coordinates)-1][0]]
    y_points=[coordinates[0][1],coordinates[len(coordinates)-1][1]]
    plt.plot(x_points, y_points, color='green', linestyle='dashed', marker='o',markerfacecolor='blue', markersize=10)

def path_LJ():
    coordinates=[[208.645963, 685.938332],
    [299.364685, 685.938332],
    [395.123336, 688.458296],
    [495.921917, 690.978261],
    [571.520852, 690.978261],
    [632.000000, 673.338509]]
    x_points=[coordinates[0][0],coordinates[len(coordinates)-1][0]]
    y_points=[coordinates[0][1],coordinates[len(coordinates)-1][1]]
    plt.plot(x_points, y_points, color='green', linestyle='dashed', marker='o',markerfacecolor='blue', markersize=10)

def path_IG():
    coordinates=[[672.319432, 685.938332],
    [775.637977, 680.898403],
    [894.076309, 683.418367],
    [977.235138, 680.898403],
    [1052.834073, 678.378438],
    [1093.153505, 675.858474]]
    x_points=[coordinates[0][0],coordinates[len(coordinates)-1][0]]
    y_points=[coordinates[0][1],coordinates[len(coordinates)-1][1]]
    plt.plot(x_points, y_points, color='green', linestyle='dashed', marker='o',markerfacecolor='blue', markersize=10)

if __name__=="__main__":
    path_AB()
    path_CD()
    path_EF()
    path_GH()
    path_IJ()
    path_KL()
    path_LJ()
    path_IG()
    plt.show()