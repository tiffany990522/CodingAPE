from mcpi.minecraft import Minecraft
mc=Minecraft.create()

a=input(你是誰)
mc.postToChat('Hello'+a+',我家前面有小河後面有山坡)