#http://tinyurl.com/h9q2cpc

def hangman(word):
    wrong=0
    stages=["",
            "__________          ",
            "|                   ",
            "|                   ",
            "|         |         ",
            "|         0         ",
            "|        /|>        ",
            "|        / >        ",
            "|                   "
            ]
    rletters=list(word)
    board=["_"]*len(word)
    win=False
    print("ハングマンへようこそ！")
    while wrong < len(stages)-1:
        print("\n")
        msg="１文字を予想してね"
            char=input(msg)
            if char in rletters:
                cind =rletters.index(char)
                board[cind]=char
                rletters[cind]'$'
            
    
