import pygame,sys,os,time

main_dir = os.path.split(os.path.abspath(__file__))[0]

def mainloop():
    width = 640
    height = 480
    size = width, height
    right =0
    pygame.init()
    screen = pygame.display.set_mode(size) #窗口大小
    bgcolour = 0x00, 0x00, 0x00 #背景颜色

    font =  pygame.font.SysFont('microsoft Yahei',25)
    GameName = font.render('Hyperdimension Neptunia card',False,(255,200,10))
    Grade = 0#游戏分数

    file = os.path.join(main_dir, '0.png') #卡面背景
    cardback = pygame.image.load(file)
    cardback.convert()
    cardbackrect = cardback.get_rect()
    cardheigh=cardbackrect.height
    cardwidth=cardbackrect.width
    
    card_list_rec=[#每一张卡的角色编号和状态，0为未翻面，1为已反面
        [[8,0],[7,0],[6,0],[5,0]],
        [[1,0],[2,0],[3,0],[4,0]],
        [[5,0],[6,0],[7,0],[8,0]],
        [[4,0],[3,0],[2,0],[1,0]]
    ]

    clock = pygame.time.Clock()
    Empty_flag=True #记录已翻面卡数是否为奇数
    cur=0,0#记录已翻面的最新一张奇数卡的卡位置
    while True:
        clock.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                pos=list(pygame.mouse.get_pos())
                temp=[-1,-1]#存储目前翻面卡的位置
                temp[0]=(pos[0]-140)//90
                temp[1]=(pos[1]-45)//90
                
                if temp[0]>=0 and temp[0]<4 and temp[1]>=0 and temp[1]<4:
                    if Empty_flag:#若是第奇数张，直接翻面
                        cur=temp
                        card_list_rec[cur[1]][cur[0]][1]=1
                        Empty_flag=False
                    else:#若是偶数张
                        if card_list_rec[cur[1]][cur[0]][0]==card_list_rec[temp[1]][temp[0]][0]:#和上一张一样，本张卡翻面并保留
                            card_list_rec[temp[1]][temp[0]][1]=1
                            Grade+=1
                            Empty_flag= True
                        else:#和上一张不一样，本张卡展示0.3秒，同时和上张卡一起翻回背面
                            card_list_rec[cur[1]][cur[0]][1]=0
                            file = os.path.join(main_dir,str(card_list_rec[temp[1]][temp[0]][0])+'.png')
                            cardfront = pygame.image.load(file)
                            cardfront.convert()
                            cardfrontrect = cardback.get_rect()
                            cardfrontrect = cardfrontrect.move(140+temp[0]*cardwidth,45+temp[1]*cardheigh)
                            screen.blit(cardfront,cardfrontrect)
                            pygame.display.flip()
                            time.sleep(0.3)
                            Empty_flag= True

        screen.fill(bgcolour)
        GameGrade = font.render('GameGrade: '+str(Grade),False,(255,200,10))
        screen.blit(GameName,(190,10))
        screen.blit(GameGrade,(0,240))
        x=140
        y=-45
        for i in card_list_rec:#显示每一张卡
            y+=cardheigh
            x=140
            for j in i:
                if j[1]==0:
                    new_rec=cardback.get_rect()
                    new_rec=new_rec.move(x,y)
                    screen.blit(cardback,new_rec)
                    x+=cardwidth
                else:
                    file = os.path.join(main_dir,str(j[0])+'.png') 
                    cardfront = pygame.image.load(file)
                    cardfront.convert()
                    cardfrontrect = cardback.get_rect()
                    cardfrontrect = cardfrontrect.move(x,y)
                    screen.blit(cardfront,cardfrontrect)
                    x+=90
        pygame.display.flip()

mainloop()