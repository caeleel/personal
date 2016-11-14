import math

a = []
b = []
last_a = 0
last_b = 0
for x in range(180):
	last_a = 1/(x*0.01 + 0.4)
	a.append(last_a)

for x in range(400):
	last_b = 7/(x*0.02 + 1)
	b.append(last_b)

for i, x in enumerate(a):
	a[i] = str(x-last_a+0.3)
for i, x in enumerate(b):
	b[i] = str(x-last_b+0.3)

x = ['0']
y = ['0']
i = -3.141592 / 2

while True:
	aX = max(math.cos(i), 0)
	aY = max(math.sin(i), 0)
	if aX == 0 and aY == 0:
		break
	aX = aX*aX*aX
	aX = aX*aX*aX
	aY = aY*aY*aY;
	aY = aY*aY*aY;
	if aX < 0.001:
		aX = 0
	if aY < 0.001:
		aY = 0
	i += 0.03
	if aX == 0 and aY == 0:
		continue
	x.append(str(aX))
	y.append(str(aY))

with open('js/animation.js', 'w') as f:
	f.write('var rotX = [' + ', '.join(a) + '];\n')
	f.write('var rotZ = [' + ', '.join(b) + '];\n')
	f.write('var arrX = [' + ', '.join(x) + '];\n')
	f.write('var arrY = [' + ', '.join(y) + '];\n')
