try:
        import Image
        import ImageDraw
        import ImageFont
except:
        from PIL import Image
        from PIL import ImageDraw
        from PIL import ImageFont
try:
    font = ImageFont.truetype('/usr/share/fonts/truetype/freefont/FreeMono.ttf', 20)
except:
    font = ImageFont.truetype(r'C:\Windows\Fonts\consola.ttf', 20)
crossedout = []
def createGrid(name):
	img = Image.new('RGB', (900, 900), '#fff')
	draw = ImageDraw.Draw(img)
	for i in range(0, 900, 100):
		draw.line([0, i, 900, i], fill=0)
		draw.line([i, 0, i, 900], fill=0)
	
	for a in range(1, 10):
		for b in range(a+1):
			x = a-1
			y = b-1
			if [a, b] in crossedout:
				draw.line([x*100, y*100, x*100+100, y*100+100], fill=(255, 0, 0))
				draw.line([x*100+100, y*100, x*100, y*100+100], fill=(255, 0, 0))
			draw.text([x*100+30, y*100+30], '%i, %i' % (x+1, y+1), fill=0, font=font)
			
	del draw
	img.save(name)

for i in range(7):
	createGrid('grid%i.png' % i)
	newcrossedout = []
	for a in range(1, 10):
		for b in range(1, a+1):
			if [a, b] in crossedout:
				continue
			onlyPossibilityAddition = True
			onlyPossibilityMultiplication = True
			for c in range(1, 10):
				for d in range(1, c+1):
					if c == a and d == b:
						continue
					if d == a and c == b:
						continue
					if [c, d] in crossedout:
						continue
					if c + d == a + b:
						onlyPossibilityAddition = False
					if c * d == a * b:
						onlyPossibilityMultiplication = False
			
			if onlyPossibilityAddition or onlyPossibilityMultiplication:
				newcrossedout.append([a, b])

	crossedout += newcrossedout
