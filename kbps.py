# exchange kbps 換算比特率 (function)
def exchange():
	kbps = int(input('請輸入比特率: ')) / 8
	sec = int(input('請輸入錄製秒長: '))
	answer = kbps * sec / 1024 / 1000 
	return answer

# exchange time 換算時間 (function)
def exchange_sec():
	ec_sec = int((input('請輸入要換算的數字: ')))
	ask = (input('請問您輸入的是分鐘還是小時?: '))
	if ask == '分鐘':
		ans = ec_sec * 60
	elif ask == '小時':
		ans = ec_sec * 60 * 60
	else:
		print('請輸入分鐘或小時')
	print('算出來的秒數是', ans, '秒')

# def main 
def main(function):
	if function == '換算秒數':
		exchange_sec()
	elif function == '轉換比特率':
		exchange_ans = exchange()
		print('算出來的GB:',int(exchange_ans))
		ex_ask = input('請問要看完整GB嗎(如果要 請輸入要):')
		if ex_ask == '要':
			print ('完整GB:',exchange_ans)
		else:
			print('不用也沒關係')
	else:
		print('請確認是否有打錯字(換算秒數) (轉換比特率)')

# run Program Code 執行程式碼
while True:
	function = input('請輸入要使用的功能 (換算秒數) (轉換比特率) (q): ')
	if function == 'q':
		print('感謝使用!!!')
		break		
	else:
		main(function)




