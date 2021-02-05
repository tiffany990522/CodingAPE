from mcpi.minecraft import Minecraft
mc=Minecraft.create()
from random import randrange

anser = randrange(0,16)
myID = mc.getPlayerEntityId("Baymax1112")

while True:
    hits = mc.events.pollBlockHits()
    if (len)>0:
        hit = hits[0]
        
        block = mc.getBlockWithData(hit.pos)
        data = block.data
        
        if data>anser :
            mc.postToChat(猜錯
        