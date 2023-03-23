def read_file(filename):
	lines = []
	#macos上讀取中文沒有發生編碼的問題不代表其他os上就沒有
	#'\ufeffAllen\n'存檔的時候有時會偷存一個有關於編碼的資料(記事本通常不會顯示，獨進電腦記憶體時實際上是存在的)
	with open(filename, 'r', encoding = 'utf-8-sig') as f:
		for line in f:
			lines.append(line.strip())
	return lines


def convert(lines):
	person = None#預設值
	allen_word_count = 0
	allen_sticker_count = 0
	allen_image_count = 0
	viki_word_count = 0
	viki_sticker_count = 0
	viki_image_count = 0
	for line in lines:
		s = line.split(' ')#遇到空白鍵切割
		time = s[0]
		name = s[1]
		if name == 'Allen':
			if s[2] == '貼圖':
				allen_sticker_count += 1
			elif s[2] == '圖片':
				allen_image_count += 1
			else:
				for msg in s[2:]:
					allen_word_count += len(msg)
		elif name == 'Viki':
			if s[2] == '貼圖':
				viki_sticker_count += 1
			elif s[2] == '圖片':
				viki_image_count += 1
			else:
				for msg in s[2:]:
					viki_word_count += len(msg)
	print('allend說了', allen_word_count, '個字') 
	print('allen傳了', allen_sticker_count, '個貼圖')
	print('allen傳了', allen_image_count, '張圖片')

	print('viki說了', viki_word_count, '個字')
	print('viki傳了', viki_sticker_count, '個貼圖')
	print('viki傳了', viki_image_count, '張圖片')


def write_file(filename, lines):
	with open(filename, 'w') as f:
		for line in lines:
			f.write(line + '\n')


def main():
	lines = read_file('LINE-Viki.txt')#進到read_file
	lines = convert(lines)#lines丟進去後回傳後又覆蓋原先的lines
	#write_file('outputFile.txt', lines)

	

main()#程式的進入點