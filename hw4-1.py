from mcpi.minecraft import Minecraft
mc=Minecraft.create()

Taiwan=[]
Japan=[]
Canada=[]

for i in range(1,4):
    Taiwan.append(2*i)
for i in range(1,4):
    Japan.append(123)
for i in range(1,4):
    Canada.append(321)
x,y,z = mc.player.getPos()
mc.setSign(x,y,z,63,8,str(Taiwan),str(Japan),str(Canada))