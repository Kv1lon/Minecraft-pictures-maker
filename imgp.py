from mine import *
from PIL import Image

mc = Minecraft()

playerPos = mc.player.getPos()
img = Image.open("imgs/hhh.jpg")
img = Image.open("imgs/hhh_1.jpg")
img = img.convert("P", palette=Image.ADAPTIVE, colors=8)
img = img.convert("RGB")
img.save("imgs/hhh_1.jpg", quality=60)

pixels = img.load()
possibleBlocks = (
    (block.AIR, 0, ( (0, 136, 255) ,),0),
    (block.STONE_GRANITE_SMOOTH, 1, ( (125,125, 125) ,),0),
    (block.DIRT, 3, ( (133,96,66),),0),
    (block.COBBLESTONE, 4, ( (117,117,117),),0),
    (block.WOOD_PLANKS, 5, ( (156,127,78),),0),
    (block.BEDROCK, 7, ( (83,83,83),),0),
    (block.SAND, 12, ( (217,210,158),),0),
    (block.GRAVEL, 13, ( (136, 126, 125),),0),
    (block.GOLD_ORE, 14, ( (143,139,124),),0),
    (block.IRON_ORE, 15, ( (135,130,126),),0),
    (block.DIAMOND_ORE, 16, ( (115,115,115),),0),
    (block.WOOD, 17, ( (154,125,77),),0),
    (block.SPONGE, 19, ( (182,182,57),),0),
    (block.WOOL_WHITE, 35, ( (221,221,221),),0),
    (block.WOOL_ORANGE, 35, ( (233,126,55),),1),
    (block.WOOL_MAGENTA, 35, ( (179,75,200),),2),
    (block.WOOL_LIGHT_BLUE, 35, ( (103,137,211),),3),
    (block.WOOL_YELLOW, 35, ( (192,179,28),),4),
    (block.WOOL_LIME, 35, ( (59,187,47),),5),
    (block.WOOL_PINK, 35, ( (217,132,153),),6),
    (block.WOOL_GRAY, 35, ( (66,67,67),),7),
    (block.WOOL_GRAY, 35, ( (157,164,165),),8),
    (block.WOOL_CYAN, 35, ( (39,116,148),),9),
    (block.WOOL_PURPLE, 35, ( (128,53,195),),10),
    (block.WOOL_BLue, 35, ( (39,51,153),),11),
    (block.WOOL_BROWN, 35, ( (85,51,27),),12),
    (block.WOOL_GREEN, 35, ( (55,76,24),),13),
    (block.WOOL_RED, 35, ( (162,44,42),),14),
    (block.WOOL_BLACK, 35, ( (26,23,23),),15),
    (block.GOLD_BLOCK, 41, ( (249,236,77),),0),
    (block.IRON_BLOCK, 42, ( (230,230,230),),0),
    (block.WOOL_WHITE, 43, ( (159,159,159),),0),
    (block.BRICK_BLOCK, 45, ( (155,110,97),),0),
    (block.COBBLESTONE, 48, ( (90,108,90),),0),
    (block.OBSIDIAN, 49, ( (20,18,29),),0),
    (block.DIAMOND_ORE, 56, ( (129,140,143),),0),
    ("Diamond Block", 57, ( (99,219,213),),0),
    ("Workbench", 58, ( (107,71,42),),0),
    ("Redstone Ore", 73, ( (132,107,107),),0),
    ("Snow Block", 80, ( (239,251,251),),0),
    ("Clay", 82, ( (158,164,176),),0),
    ("Jukebox", 84, ( (107,73,55),),0),
    ("Pumpkin", 86, ( (192,118,21),),0),
    ("Netherrack", 87, ( (110,53,51),),0),
    ("Soul Sand", 88, ( (84,64,51),),0),
    ("Glowstone", 89, ( (137,112,64),),0)
)

def getBlockFromColor(RGB):
	smallestDistIndex = -1
	smallestDist = 300000
	curIndex = 0
	for block in possibleBlocks:
		for blockRGB in block[2]:
			curDist = getColorDist(RGB, blockRGB)

			if (curDist < smallestDist):
				smallestDist = curDist
				smallestDistIndex = curIndex

		curIndex = curIndex + 1

	if (smallestDistIndex == -1):
		return -1

	return possibleBlocks[smallestDistIndex]
width, height = img.size
for x in range(width):
    for y in range(height):
        if img.getpixel((x, y)) not in colors_list:
            colors_list.append(img.getpixel((x, y)))

for k in range(len(colors_list)):
    colors[str(colors_list[k])] = blocks_list[k]
for x in range(width):
    for y in range(height):
        mc.setBlock(playerPos.x - 60 + width - x, playerPos.y + height - y, playerPos.z + 50,
                    colors[str(img.getpixel((x, y)))])

mc.postToChat("Фото готово")
