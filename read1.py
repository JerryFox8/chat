def read_file(filename):
	lines = []
	#macos上讀取中文沒有發生編碼的問題不代表其他os上就沒有
	#'\ufeffAllen\n'存檔的時候有時會偷存一個有關於編碼的資料(記事本通常不會顯示，獨進電腦記憶體時實際上是存在的)
	with open(filename, 'r', encoding = 'utf-8-sig') as f:
		for line in f:
			lines.append(line.strip())
	return lines

def convert(lines):
	new = []
	person = '123'#預設值
	for line in lines:
		if line == 'Allen':
			person = 'Allen'
			continue #跳到下一個回圈
		elif line == 'Tom':
			person = 'Tom'
			continue

		new.append(person + ': ' + line)
	print(new)

def main():
	lines = read_file('input.txt')#進到read_file
	convert(lines)
	

main()#程式的進入點