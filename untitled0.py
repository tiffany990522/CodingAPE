from mcpi.minecraft import Minecraft
mc=Minecraft.create()

for i in range(30):
    x,y,z = mc.player.getPos()
    x=x+i
    mc.setBlock(x,y-1,z,57)
mc.setBlocks(x,y,z,x+10,y+15,z+10,91)
mc.setBlocks(x+1,y+1,z+1,x+9,y+14,z+9,0)