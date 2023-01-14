#code written and project by Rajeev K R

#change directory to current folder for running

import pygame

pygame.init()

pygame.display.set_caption('Chess')
icon = pygame.image.load('Assets/chess-piece.png')
pygame.display.set_icon(icon)

font = pygame.font.Font('freesansbold.ttf',32)

screen = pygame.display.set_mode((600,600))
board = pygame.image.load('Assets/chess_board-01.png')
k = pygame.image.load('Assets/Pieces/k.png')
q = pygame.image.load('Assets/Pieces/q.png')
b = pygame.image.load('Assets/Pieces/b.png')
n = pygame.image.load('Assets/Pieces/n.png')
r = pygame.image.load('Assets/Pieces/r.png')
p = pygame.image.load('Assets/Pieces/p.png')
kk = pygame.image.load('Assets/Pieces/kk.png')
qq = pygame.image.load('Assets/Pieces/qq.png')
bb = pygame.image.load('Assets/Pieces/bb.png')
nn = pygame.image.load('Assets/Pieces/nn.png')
rr = pygame.image.load('Assets/Pieces/rr.png')
pp = pygame.image.load('Assets/Pieces/pp.png')

piece = ['rr','nn','bb','qq','kk','bb','nn','rr','pp','pp','pp','pp','pp','pp','pp','pp','p','p','p','p','p','p','p','p','r','n','b','q','k','b','n','r']

def piececolor(j):
    if j>=0 and j<16:
        return True # for white
    return False # for black

piecex = [1,2,3,4,5,6,7,8,1,2,3,4,5,6,7,8,1,2,3,4,5,6,7,8,1,2,3,4,5,6,7,8]
piecey = [1,1,1,1,1,1,1,1,2,2,2,2,2,2,2,2,7,7,7,7,7,7,7,7,8,8,8,8,8,8,8,8]
pieceicon = [rr,nn,bb,qq,kk,bb,nn,rr,pp,pp,pp,pp,pp,pp,pp,pp,p,p,p,p,p,p,p,p,r,n,b,q,k,b,n,r]
piecealive = [True]*32

running = True

def enable(x,y):
    if x<1 or x>8 or y<1 or y>8:
        return -2
    for j in range(32):
        if piecealive[j] and x == piecex[j] and y == piecey[j]:
            return j
    return -1


def attack(x,y):

    j = enable(x,y)
    attacklist = []

    if j == -1:
        return [[-1,-1]]

    #rook
    if piece[j]== 'rr' or piece[j] == 'r' or piece[j] =='qq' or piece[j] == 'q':
        
        for i in range(1,8):
            tmp_pos = enable(x+i,y)
            if tmp_pos == -1:
                attacklist.append([x+i,y])
            elif tmp_pos == -2:
                break
            else:
                attacklist.append([x+i,y])
                break
        
        for i in range(1,8):
            tmp_pos = enable(x-i,y)
            if tmp_pos == -1:
                attacklist.append([x-i,y])
            elif tmp_pos == -2:
                break
            else:
                attacklist.append([x-i,y])
                break

        for i in range(1,8):
            tmp_pos = enable(x,y+i)
            if tmp_pos == -1:
                attacklist.append([x,y+i])
            elif tmp_pos == -2:
                break
            else:
                attacklist.append([x,y+i])
                break

        for i in range(1,8):
            tmp_pos = enable(x,y-i)
            if tmp_pos == -1:
                attacklist.append([x,y-i])
            elif tmp_pos == -2:
                break
            else:
                attacklist.append([x,y-i])
                break

    #knight
    if piece[j]== 'nn' or piece[j] == 'n':

        tmp_pos = enable(x+2,y+1)
        if tmp_pos != -2:
            attacklist.append([x+2,y+1])
        tmp_pos = enable(x+2,y-1)
        if tmp_pos != -2:
            attacklist.append([x+2,y-1])
        tmp_pos = enable(x-2,y+1)
        if tmp_pos != -2:
            attacklist.append([x-2,y+1])
        tmp_pos = enable(x-2,y-1)
        if tmp_pos != -2:
            attacklist.append([x-2,y-1])

        tmp_pos = enable(x+1,y+2)
        if tmp_pos != -2:
            attacklist.append([x+1,y+2])
        tmp_pos = enable(x+1,y-2)
        if tmp_pos != -2:
            attacklist.append([x+1,y-2])
        tmp_pos = enable(x-1,y+2)
        if tmp_pos != -2:
            attacklist.append([x-1,y+2])
        tmp_pos = enable(x-1,y-2)
        if tmp_pos != -2:
            attacklist.append([x-1,y-2])

    #bishop or queen
    if piece[j] == 'bb' or piece[j] == 'b' or piece[j] =='qq' or piece[j] == 'q':
        
        for i in range(1,8):
            tmp_pos = enable(x+i,y+i)
            if tmp_pos == -1:
                attacklist.append([x+i,y+i])
            elif tmp_pos == -2:
                break
            else:
                attacklist.append([x+i,y+i])
                break
        
        for i in range(1,8):
            tmp_pos = enable(x-i,y-i)
            if tmp_pos == -1:
                attacklist.append([x-i,y-i])
            elif tmp_pos == -2:
                break
            else:
                attacklist.append([x-i,y-i])
                break

        for i in range(1,8):
            tmp_pos = enable(x-i,y+i)
            if tmp_pos == -1:
                attacklist.append([x-i,y+i])
            elif tmp_pos == -2:
                break
            else:
                attacklist.append([x-i,y+i])
                break

        for i in range(1,8):
            tmp_pos = enable(x+i,y-i)
            if tmp_pos == -1:
                attacklist.append([x+i,y-i])
            elif tmp_pos == -2:
                break
            else:
                attacklist.append([x+i,y-i])
                break
    

    #pawn
    if piece[j] == 'pp':
        tmp_pos = enable(x+1,y+1)
        if tmp_pos >0:
            attacklist.append([x+1,y+1])
        tmp_pos = enable(x-1,y+1)
        if tmp_pos >0:
            attacklist.append([x-1,y+1])
    
    if piece[j] == 'p':
        tmp_pos = enable(x+1,y-1)
        if tmp_pos >0:
            attacklist.append([x+1,y-1])
        tmp_pos = enable(x-1,y-1)
        if tmp_pos >0:
            attacklist.append([x-1,y-1])


    #king
    if piece[j] == 'kk' or piece[j] == 'k':
        tmp_pos = enable(x+1,y+1)
        if tmp_pos != -2:
            attacklist.append([x+1,y+1])

        tmp_pos = enable(x,y+1)
        if tmp_pos != -2:
            attacklist.append([x,y+1])

        tmp_pos = enable(x-1,y+1)
        if tmp_pos != -2:
            attacklist.append([x-1,y+1])

        tmp_pos = enable(x-1,y)
        if tmp_pos != -2:
            attacklist.append([x-1,y])

        tmp_pos = enable(x-1,y-1)
        if tmp_pos != -2:
            attacklist.append([x-1,y-1])

        tmp_pos = enable(x,y-1)
        if tmp_pos != -2:
            attacklist.append([x,y-1])

        tmp_pos = enable(x+1,y-1)
        if tmp_pos != -2:
            attacklist.append([x+1,y-1])

        tmp_pos = enable(x+1,y)
        if tmp_pos != -2:
            attacklist.append([x+1,y])

    return attacklist

def move(x,y):
    j = enable(x,y)
    if piece[j] != 'pp' and piece[j] != 'p':
        return attack(x,y)
    else:
        movelist = []
        if piece[j] == 'pp':
            if y == 2 and enable(x,3) == -1 and enable(x,4) == -1:
                movelist.append([x,4])
            tmp_pos = enable(x,y+1)
            if tmp_pos == -1:
                movelist.append([x,y+1])
        else:
            if y == 7 and enable(x,6) == -1 and enable(x,5) == -1:
                movelist.append([x,5])
            tmp_pos = enable(x,y-1)
            if tmp_pos == -1:
                movelist.append([x,y-1])
    return movelist

def moveattack(x,y):
    newlist = attack(x,y)
    newlist.extend(i for i in move(x,y) if i not in newlist)
    return newlist


def totalwhiteattack():
    total =[]
    for i in range(1,16):
        total.extend(attack(piecex[i],piecey[i]))
    return total

def totalblackattack():
    total = []
    for i in range(16,32):
        total.extend(attack(piecex[i],piecey[i]))
    return total

def whitecheck():
    if [piecex[28],piecey[28]] in totalwhiteattack():
        return True
    return False

def blackcheck():
    if [piecex[4],piecey[4]] in totalblackattack():
        return True
    return False

def movableattack(x,y):

    j = enable(x,y)
    movableattacklist = []
    for i in moveattack(x,y):
        if enable(i[0],i[1]) == -1 or piececolor(enable(i[0],i[1])) != piececolor(j):
            movableattacklist.append(i)

    if piece[j] == 'kk':
        for m in movableattacklist[:]:
            if m in totalblackattack():
                movableattacklist.remove(m)

    if piece[j] == 'k':
        for m in movableattacklist[:]:
            if m in totalwhiteattack():
                movableattacklist.remove(m)
            

    return movableattacklist

def finalmovable(x,y):
    j = enable(x,y)

    finalmove = []
    if piececolor(j) == True:
        for i in movableattack(x,y):
            piecex[j] = i[0]
            piecey[j] = i[1]
            if blackcheck() == False:
                finalmove.append(i)
            piecex[j] = x
            piecey[j] = y
    else:
        for i in movableattack(x,y):
            piecex[j] = i[0]
            piecey[j] = i[1]
            if whitecheck() == False:
                finalmove.append(i)
            piecex[j] = x
            piecey[j] = y
    
    return finalmove
            
def totalmovable(a):
    newlist = []
    if a:
        for i in range(16):
            if piecealive[i]:
                newlist.extend(finalmovable(piecex[i],piecey[i]))
    else:
        for i in range(16,32):
            if piecealive[i]:
                newlist.extend(finalmovable(piecex[i],piecey[i]))
    return newlist


rrook1 = False
kking = False
rrook2 = False
rook1 = False
king = False
rook2 = False


def capture(j,x,y):
    if enable(x,y) == -2:
        return -1
    elif enable(x,y) == -1:
        piecex[j] = x
        piecey[j] = y
    else:
        piecealive[enable(x,y)] = False
        piecex[j] = x
        piecey[j] = y
    
    if j == 0:
        rrook1 = True
    elif j == 4:
        kking = True
    elif j == 7:
        rrook2 = True
    elif j == 24:
        rook1 = True
    elif j == 28:
        king = True
    elif j == 31:
        rook2 = True
    
        
enable_status = False
move_order = True
win = 0

while running:
    screen.blit(board,(0,0))

    for i in range (32):
        if piecealive[i]:
            screen.blit(pieceicon[i],((piecex[i]-1)*75,75*(8-piecey[i])))


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:
                enable_status = False
                move_order = True
                piecex = [1,2,3,4,5,6,7,8,1,2,3,4,5,6,7,8,1,2,3,4,5,6,7,8,1,2,3,4,5,6,7,8]
                piecey = [1,1,1,1,1,1,1,1,2,2,2,2,2,2,2,2,7,7,7,7,7,7,7,7,8,8,8,8,8,8,8,8]
                piecealive = [True]*32
                win = 0
                rrook1 = False
                kking = False
                rrook2 = False
                rook1 = False
                king = False
                rook2 = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()
            if enable_status == False:
                if piececolor(enable((pos[0] // 75)+1,8-(pos[1] // 75))) == move_order:
                    print('click')
                    print(pos)
                    x = (pos[0] // 75)+1
                    y = 8-(pos[1] // 75)
                    print(x,y)

                    print(enable(x,y))
                    if enable(x,y) != -1:
                        enable_status = True
                    print(enable_status)
            else :
                x2 = (pos[0] // 75)+1
                y2 = 8-(pos[1] // 75)
                print(pos)
                print(x2,y2)
                if [x2,y2] in finalmovable(x,y):
                    capture(enable(x,y),x2,y2)
                    enable_status = False
                    move_order = not move_order

                castlewhite = totalmovable(False)
                castleblack = totalmovable(True)

                if [x,y] == [5,1] and [x2,y2] == [3,1] and kking == False and rrook1 == False and [enable(2,1),enable(3,1),enable(4,1)] == [-1,-1,-1] and [2,1] not in castlewhite and [3,1] not in castlewhite and [4,1] not in castlewhite:
                    piecex[4] = 3
                    piecex[0] = 4
                    enable_status = False
                    move_order = not move_order
                elif [x,y] == [5,1] and [x2,y2] == [7,1] and kking == False and rrook2 == False and [enable(6,1),enable(7,1)] == [-1,-1] and [6,1] not in castlewhite and [7,1] not in castlewhite:
                    piecex[4] = 7
                    piecex[7] = 6
                    enable_status = False
                    move_order = not move_order
                elif [x,y] == [5,8] and [x2,y2] == [3,8] and kking == False and rrook1 == False and [enable(2,8),enable(3,8),enable(4,8)] == [-1,-1,-1] and [2,8] not in castleblack and [3,8] not in castleblack and [4,8] not in castleblack:
                    piecex[28] = 3
                    piecex[24] = 4
                    enable_status = False
                    move_order = not move_order
                elif [x,y] == [5,8] and [x2,y2] == [7,8] and kking == False and rrook1 == False and [enable(6,1),enable(7,1)] == [-1,-1] and [6,8] not in castleblack and [7,8] not in castleblack:
                    piecex[28] = 7
                    piecex[31] = 6
                    enable_status = False
                    move_order = not move_order


                if blackcheck() == True and len(totalmovable(True)) == 0:
                    print('black win')
                    win = 1
                if whitecheck() == True and len(totalmovable(False))==0:
                    print('white win')
                    win = 2
                break
    if win == 1:
        score = font.render('Checkmate Black wins',True,(130,100,180))
        screen.blit(score,(120,280))
        newgame = font.render('Press RETURN for new game',True,(130,100,180))
        screen.blit(newgame,(100,400))
    elif win == 2:
        score = font.render('Checkmate White wins',True,(130,100,180))
        screen.blit(score,(120,280))
        newgame = font.render('Press RETURN for new game',True,(130,100,180))
        screen.blit(newgame,(90,400))
    pygame.display.update()