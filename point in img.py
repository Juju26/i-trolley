import folium



map=folium.Map(location=[0,1],
           zoom_start=0, min_zoom=0, max_zoom=0,
           max_bounds=False,
           min_lon=0, max_lon=0, min_lat=0, max_lat=0,
           tiles='image mapping/Group 5.png',
           attr='Textures and Icons from https://www.textures.com/ & https://thenounproject.com/'
)

map.save('map.html')


















# from matplotlib import image, markers
# from matplotlib import pyplot as plt

# img = image.imread('image mapping/Group 5.png')

# f,ax=plt.subplots(1)
# xdata=[10,20,30]
# ydata=[10,20,30]
# plt.plot(xdata,ydata,marker=markers.CARETDOWN,color='r')
# # plt.plot(100,100,marker="v",color="red")
# # plt.imshow(img)
# ax.set_ylim(bottom=0)
# ax.set_xlim(left=0)
# plt.imshow(img)