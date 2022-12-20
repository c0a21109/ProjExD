import pygame as pg
import random
import sys


class Screen:
    def __init__(self, title, wh, img_path):
        pg.display.set_caption(title) 
        self.sfc = pg.display.set_mode(wh)
        self.rct = self.sfc.get_rect()
        self.bgi_sfc = pg.image.load(img_path)
        self.bgi_rct = self.bgi_sfc.get_rect() 

    def blit(self):
        self.sfc.blit(self.bgi_sfc, self.bgi_rct) 


class Bird:
    key_delta = {
        pg.K_UP:    [0, -1],
        pg.K_DOWN:  [0, +1],
        pg.K_LEFT:  [-1, 0],
        pg.K_RIGHT: [+1, 0],
    }

    def __init__(self, img_path, ratio, xy):
        self.sfc = pg.image.load(img_path)
        self.sfc = pg.transform.rotozoom(self.sfc, 0, ratio)
        self.rct = self.sfc.get_rect()
        self.rct.center = xy

    def blit(self, scr:Screen):
        scr.sfc.blit(self.sfc, self.rct)

    def update(self, scr:Screen):
        key_dct = pg.key.get_pressed()
        for key, delta in Bird.key_delta.items():
            if key_dct[key]:
                self.rct.centerx += delta[0]
                self.rct.centery += delta[1]  
            if check_bound(self.rct, scr.rct) != (+1, +1):
                self.rct.centerx -= delta[0]
                self.rct.centery -= delta[1]
        #self.blit(scr)                    


class Bomb:
    def __init__(self, color, rad, vxy, scr:Screen):
        self.sfc = pg.Surface((2*rad, 2*rad)) # 正方形の空のSurface
        self.sfc.set_colorkey((0, 0, 0))
        pg.draw.circle(self.sfc, color, (rad, rad), rad)
        self.rct = self.sfc.get_rect()
        self.rct.centerx = random.randint(0, scr.rct.width)
        self.rct.centery = random.randint(0, scr.rct.height)
        self.vx, self.vy = vxy

    def blit(self, scr:Screen):
        scr.sfc.blit(self.sfc, self.rct)

    def update(self, scr:Screen):
        self.rct.move_ip(self.vx, self.vy)
        yoko, tate = check_bound(self.rct, scr.rct)
        self.vx *= yoko
        self.vy *= tate
        self.blit(scr)


class Heart: #♡のクラス
    def __init__(self, znk):
        self.sfc = pg.image.load("fig/heart.png")
        self.sfc = pg.transform.rotozoom(self.sfc, 0, 0.1)
        self.rct = self.sfc.get_rect()
        self.rct.center = (1560 - znk*40), 40

    def blit(self, scr:Screen):
        scr.sfc.blit(self.sfc, self.rct)


class Dismiss(Bird): #dismiss(無敵時間)の時のクラス
    key_delta = {
        pg.K_UP:    [0, -2],
        pg.K_w:     [0, -2],
        pg.K_DOWN:  [0, +2],
        pg.K_s:     [0, +2],
        pg.K_LEFT:  [-2, 0],
        pg.K_a:     [-2, 0],
        pg.K_RIGHT: [+2, 0],
        pg.K_d:     [+2, 0]
    }

    def __init__(self, img_path, ratio, xy):
        self.sfc = pg.image.load(img_path)
        self.sfc = pg.transform.rotozoom(self.sfc, 0, ratio)
        self.rct = self.sfc.get_rect()
        self.rct.center = xy
        

class Soulorb: # ソウルオーブのクラス
    def __init__(self, xy):
        self.sfc = pg.Surface((20, 20)) 
        self.sfc.set_colorkey((0, 0, 0))
        pg.draw.circle(self.sfc, (164, 0, 26), (10, 10), 10)
        self.rct = self.sfc.get_rect()
        self.rct.center = xy

    def blit(self, scr:Screen):
        scr.sfc.blit(self.sfc, self.rct)
        

def check_bound(obj_rct, scr_rct):
    yoko, tate = +1, +1
    if obj_rct.left < scr_rct.left or scr_rct.right < obj_rct.right:
        yoko = -1
    if obj_rct.top < scr_rct.top or scr_rct.bottom < obj_rct.bottom:
        tate = -1
    return yoko, tate


def main():
    clock =pg.time.Clock()
    life = 3
    # 無敵関係
    soulorb = False # ♡が減るか，誰かを倒すとソウルオーブが出現
    soulorb_limit = 0 # ソウルオーブの持続時間のリミット
    dismiss = False # ディスミス中か否か
    dismiss_limit = 0 # ディスミスのタイムリミット

    # 練習１
    scr = Screen("逃げろ！こうかとん", (1600,900), "fig/pg_bg.png")

    # 練習３
    kkt = Bird("fig/6.png", 2.0, (900,400))
    kkt.update(scr)

    #dismiss
    reyna = Dismiss("fig/dismiss.png", 2.0, (900,400))
    reyna.update(scr)

    # 練習５
    bkd = Bomb((255, 0, 0), 10, (+1, +1), scr)
    bkd.update(scr)

    # ライフ
    # １個目
    heart1 = Heart(3)
    heart1.blit(scr)
    # ２個目
    heart2 = Heart(2)
    heart2.blit(scr)
    # ３個目
    heart3 = Heart(1)
    heart3.blit(scr)

    # 練習２
    while True:        
        scr.blit()

        for event in pg.event.get():
            if event.type == pg.K_e: # 推されたのがEで，ソウルオーブがあるならば
                if soulorb: # ソウルオーブの描画
                    dismiss = True
                    dismiss_limit = pg.time.get_ticks() + 3000
                    soulorb = False
            if event.type == pg.QUIT:
                return
        
        bkd.update(scr)

        # ディスミス中か否かで，画像を差し替え
        kkt.update(scr)
        reyna.update(scr)

        if dismiss:
            reyna.blit(scr)
            if dismiss_limit < pg.time.get_ticks():
                dismiss = False
        else:
            kkt.blit(scr)

        if dismiss_limit < pg.time.get_ticks(): # 通常時
            if kkt.rct.colliderect(bkd.rct): # 爆弾に当たるとライフが減る
                life -= 1
                dismiss_limit = pg.time.get_ticks() + 500 # ちょっとだけ無敵時間
                soulorb = True
                soulorb = Soulorb(kkt.rct.center)
                soulorb_limit = pg.time.get_ticks() + 3000
        
        if soulorb: # ソウルオーブの描画
            soulorb.blit(scr)
            if soulorb_limit < pg.time.get_ticks():
                soulorb = False

        for event in pg.event.get():
            if event.type == pg.K_e:
                if soulorb: # ソウルオーブの描画
                    dismiss = True
                    dismiss_limit = pg.time.get_ticks() + 3000
                    soulorb = False
        
        if life >= 1:
            heart1.blit(scr)
        if life >= 2:
            heart2.blit(scr)
        if life >= 3:
            heart3.blit(scr)
            
        pg.display.update()
        clock.tick(1000)


if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()
