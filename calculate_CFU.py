from matplotlib import pyplot as plt
from skimage import io
from skimage.transform import resize


##############################################圈出边界
def OnPress(event):
    if event.button == 1:
        dots.append((event.xdata, event.ydata))
        ax.scatter(dots[-1][0], dots[-1][1], color='red', s=10)
        fig.canvas.draw()

##############################################单个计算
pic = input('please input picture links:')
img = io.imread(pic)
#img = resize(img, (img.shape[0] / 3, img.shape[1] /3),anti_aliasing=True)
while True:
    dots = []
    fig = plt.figure()
    fig.canvas.mpl_connect('button_press_event', OnPress)
    ax = fig.add_subplot(111)
    ax.imshow(img)
    plt.show()
    print(len(dots))
    for dot in dots:
        for i in range(int(dot[1])-3,int(dot[1])+3):
            for j in range(int(dot[0])-3,int(dot[0])+3):
                img[i,j]=[0,0,1]

