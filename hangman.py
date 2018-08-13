import random

def hangman ():
	word_list = ["Python", "java", "computer", "hacker", "painter"]
	random_number = random.randint(0,4)
	word = word_list[random_number]
	wrong = 0
	stages = ["",
					"____________________  ",
					" |                                        ",
					" |                  |                     ",
					" |                  0                    ",
					" |                / | \                   ",
					" |                /   \                   ",
					" |                                        "
					]
	#引数wordはお題となる単語
	rletters = list(word)
	#入力された単語の文字数だけ＿を作成し，リストに入れる
	board = ["_"] * len(word)
	win = False
	print ("ハングマンへようこそ！")
	

	while wrong < len(stages) - 1 :
		print ("\n")
		msg = "1文字を予想してね"
		char = input(msg)
	
		#単語の中に入力された文字があれば
		if char in rletters:
		#その文字がある場所のインデックスを返す
			cind = rletters.index(char)
		#boardリスト内の_を入力された単語で更新
			board[cind] =  char
		#お題の文字の中から正解した文字を記号で置き換える
			rletters[cind] = '$'
		else:
			wrong += 1
		#現時点の文字列
		print(" ".join(board))
		#間違いの数に応じた絵を表示
		e = wrong + 1
		print ("\n".join(stages[0:e]))
	
		#boardの中に＿がない場合
		if "_" not in board:
			print ("あなたの勝ち！")
			print (" ".join(board))
			win = True
			break
	if not win:
		print ("\n".join(stages[0:wrong+1]))
		print ("あなたの負け！正解は {}.".format (word))

hangman()
	