import random
start = input('請決定隨機數字範圍開始值: ')
end = input('請決定隨機數字範圍結束值: ')
start = int(start)
end = int(end)
r = random.randint(start,end)
count = 0
while True:
	count += 1
	number = input('請猜一個數字: ')
	number = int(number)
	if number == r:
		print('終於猜對了!')
		print('這是你猜的第', count, '次')
		break
	elif number > r:
		print('比答案大')
	elif number < r:
		print('比答案小')
	print('這是你猜的第', count, '次')

		

