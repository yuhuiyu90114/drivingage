driving = input('你有沒有開車?')
if driving != '有' and driving != '沒有':
	print('你只能輸入 有/沒有')
	raise SystemExit
age = input('你的年齡:')
age = int(age)
if driving == '有':
	if age >= 18:
		print('你通過驗證')
	else:
		print('不行喔!')
elif driving == '沒有':
	if age >=18:
		print('你可以考駕照')
	else:
		print('再等等吧!')