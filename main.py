import mcpi.minecraft as minecraft
import mcpi.block as block
from PIL import Image
import numpy as np
import time

def RGB2Block(rgb):
    if (rgb[0] == 255) and (rgb[1] == 255) and (rgb[2] == 255):
        return np.array([251, 0])
    elif (rgb[0] == 0) and (rgb[1] == 0) and (rgb[2] == 0):
        return np.array([251, 15])
    elif (rgb[0] == 237) and (rgb[1] == 28) and (rgb[2] == 36):
        return np.array([100, 1])
    elif (rgb[0] == 255) and (rgb[1] == 127) and (rgb[2] == 39):
        return np.array([251, 1])
    elif (rgb[0] == 163) and (rgb[1] == 73) and (rgb[2] == 164):
        return np.array([251, 10])
    elif (rgb[0] == 239) and (rgb[1] == 228) and (rgb[2] == 176):
        return np.array([5, 2])
    elif (rgb[0] == 153) and (rgb[1] == 217) and (rgb[2] == 234):
        return np.array([252, 3])
    elif (rgb[0] == 255) and (rgb[1] == 242) and (rgb[2] == 0):
        return np.array([35, 4])
    elif (rgb[0] == 34) and (rgb[1] == 177) and (rgb[2] == 76):
        return np.array([251, 13])
    elif (rgb[0] == 185) and (rgb[1] == 122) and (rgb[2] == 87):
        return np.array([5, 1])
    elif (rgb[0] == 255) and (rgb[1] == 174) and (rgb[2] == 201):
        return np.array([35, 6])
    elif (rgb[0] == 181) and (rgb[1] == 230) and (rgb[2] == 29):
        return np.array([251, 5])
    elif (rgb[0] == 0) and (rgb[1] == 162) and (rgb[2] == 232):
        return np.array([251, 3])
    elif (rgb[0] == 127) and (rgb[1] == 127) and (rgb[2] == 127):
        return np.array([159, 9])
    elif (rgb[0] == 136) and (rgb[1] == 0) and (rgb[2] == 21):
        return np.array([251, 14])
    elif (rgb[0] == 63) and (rgb[1] == 72) and (rgb[2] == 204):
        return np.array([251, 11])
    elif (rgb[0] == 200) and (rgb[1] == 191) and (rgb[2] == 231):
        return np.array([159, 3])
    elif (rgb[0] == 112) and (rgb[1] == 146) and (rgb[2] == 190):
        return np.array([251, 9])
    elif (rgb[0] == 255) and (rgb[1] == 201) and (rgb[2] == 14):
        return np.array([159, 4])
    elif (rgb[0] == 195) and (rgb[1] == 195) and (rgb[2] == 195):
        return np.array([35, 8])
    else:
        return np.array([20, 0])

#Postion
#Resolution 192 x 108
x1 = -95
z1 = 24
x2 = 96
z2 = 131
y = 0

pos1 = (x1, y, z1)
pos2 = (x2, y, z2)
i=16

print("Res: ",(x2-x1)+1," x ",(z2-z1)+1)

#Code
mc = minecraft.Minecraft.create()
#mc.setBlocks(pos1[0], pos1[1]-1, pos1[2], pos2[0], pos2[1]-1, pos2[2], block.BEDROCK)

#MSG
mc.postToChat("[Server] placed")
while True:
    img = Image.open('image.png', 'r')
    pix = np.array(img)

    for z in range(z1, (z2 + 1)):
        for x in range(x1, (x2+1)):
            mc.setBlock(x, 1, z, RGB2Block(pix[z-z1][x-x1])[0], RGB2Block(pix[z-z1][x-x1])[1])
    #delay auto place block
    time.sleep(2)

#mc.setBlock(x, y, z, 1)
