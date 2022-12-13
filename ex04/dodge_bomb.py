import pygame as pg
import sys
import random
import time

def check_bound(obj_rect, scr_rect): #画面外チェック
    #第１引数：〇〇_rect
    #第２引数：scr_rect
    x, y = 1, 1
    if obj_rect.left < scr_rect.left or obj_rect.right > scr_rect.right:
        x = -1
    if obj_rect.top < scr_rect.top or obj_rect.bottom > scr_rect.bottom:
        y = -1
    return x, y

def main():
    count = 0 #今何フレーム目？
    clock =pg.time.Clock()
    pause = False
    #追加される玉の速度の初期設定
    vx1, vy1 = 1, 1 
    vx2, vy2 = 0, 0
    vx3, vy3 = 0, 0
    vx4, vy4 = 0, 0

    LIFE = 3 #工科豚のライフ
    dismith = 0 #被弾後の無敵時間

    LV2 = False #2つ目の玉が動き出す
    LV3 = False #3つ目の球が動き出す
    LV4 = False #4つ目の球が動きだす
    # 練習１
    pg.display.set_caption("逃げろこうかとん")
    scrn_sfc = pg.display.set_mode((1600, 900))
    scrn_rct = scrn_sfc.get_rect()
    pgbg_sfc = pg.image.load("fig/pg_bg.png")
    pgbg_rct = pgbg_sfc.get_rect()

    # 練習３
    tori_sfc = pg.image.load("fig/6.png")
    tori_sfc = pg.transform.rotozoom(tori_sfc, 0, 2.0)
    tori_rct = tori_sfc.get_rect()
    tori_rct.center = 900, 400
    scrn_sfc.blit(tori_sfc, tori_rct) 

    bomb_sfc = pg.Surface((200, 200)) #正方形のからのサーフェイス
    bomb_sfc.set_colorkey((0, 0, 0))
    pg.draw.circle(bomb_sfc, (255, 0, 0), (100, 100), 100) 
    bomb_rct = bomb_sfc.get_rect()
    bomb_rct.centerx = 0
    bomb_rct.centery = 0

    #練習５
    bomb1_sfc = pg.Surface((20, 20)) #正方形のからのサーフェイス
    bomb1_sfc.set_colorkey((0, 0, 0))
    pg.draw.circle(bomb1_sfc, (255, 0, 0), (10, 10), 10) 
    bomb1_rct = bomb1_sfc.get_rect()
    bomb1_rct.centerx = random.randint(11, scrn_rct.width-11)
    bomb1_rct.centery = random.randint(11, scrn_rct.height-11)

    #２つ目の爆弾
    bomb2_sfc = pg.Surface((30, 30)) #正方形のからのサーフェイス
    bomb2_sfc.set_colorkey((0, 0, 0))
    pg.draw.circle(bomb2_sfc, (255, 0, 0), (15, 15), 15) 
    bomb2_rct = bomb2_sfc.get_rect()
    bomb2_rct.centerx = 51 #2個目の玉の初期位置
    bomb2_rct.centery = 51

    #3つ目の爆弾
    bomb3_sfc = pg.Surface((40, 40)) #正方形のからのサーフェイス
    bomb3_sfc.set_colorkey((0, 0, 0))
    pg.draw.circle(bomb3_sfc, (255, 0, 0), (20, 20), 20) 
    bomb3_rct = bomb3_sfc.get_rect()
    bomb3_rct.centerx = 51 #3個目の玉の初期位置
    bomb3_rct.centery = 51

    #4つ目の爆弾
    bomb4_sfc = pg.Surface((50, 50)) #正方形のからのサーフェイス
    bomb4_sfc.set_colorkey((0, 0, 0))
    pg.draw.circle(bomb4_sfc, (255, 0, 0), (25, 25), 25) 
    bomb4_rct = bomb4_sfc.get_rect()
    bomb4_rct.centerx = 51 #4個目の玉の初期位置
    bomb4_rct.centery = 51

    #ハートを描画
    #1コメ
    heart1_sfc = pg.image.load("fig/heart.png")
    heart1_sfc = pg.transform.rotozoom(heart1_sfc, 0, 0.1)
    heart1_rct = heart1_sfc.get_rect()
    heart1_rct.center = 1560, 40
    scrn_sfc.blit(heart1_sfc, heart1_rct)
    #2コメ
    heart2_sfc = pg.image.load("fig/heart.png")
    heart2_sfc = pg.transform.rotozoom(heart2_sfc, 0, 0.1)
    heart2_rct = heart2_sfc.get_rect()
    heart2_rct.center = 1520, 40
    scrn_sfc.blit(heart2_sfc, heart2_rct)
    #3コメ
    heart3_sfc = pg.image.load("fig/heart.png")
    heart3_sfc = pg.transform.rotozoom(heart3_sfc, 0, 0.1)
    heart3_rct = heart3_sfc.get_rect()
    heart3_rct.center = 1480, 40
    scrn_sfc.blit(heart3_sfc, heart3_rct)

    font = pg.font.Font(None, 30)


    # 練習２
    while True: #フレームごとに更新
        count += 1
        scrn_sfc.blit(pgbg_sfc, pgbg_rct) 
        for event in pg.event.get():
            if event.type == pg.QUIT:
                return

        #練習４ 矢印キーだけではなく，wasdでも動かせる
        key_dict = pg.key.get_pressed()
        if key_dict[pg.K_UP] or key_dict[pg.K_w]:
            tori_rct.centery -= 1
        if key_dict[pg.K_DOWN] or key_dict[pg.K_s]:
            tori_rct.centery += 1
        if key_dict[pg.K_LEFT] or key_dict[pg.K_a]:
            tori_rct.centerx -= 1
        if key_dict[pg.K_RIGHT] or key_dict[pg.K_d]:
            tori_rct.centerx += 1
        if check_bound(tori_rct, scrn_rct) != (1, 1) :
            if key_dict[pg.K_UP] or key_dict[pg.K_w]:
                tori_rct.centery += 1
            if key_dict[pg.K_DOWN] or key_dict[pg.K_s]:
                tori_rct.centery -= 1
            if key_dict[pg.K_LEFT] or key_dict[pg.K_a]:
                tori_rct.centerx += 1
            if key_dict[pg.K_RIGHT] or key_dict[pg.K_d]:
                tori_rct.centerx -= 1
        scrn_sfc.blit(tori_sfc, tori_rct) #座標を更新したら貼り付ける

        #爆弾4つの設定
        #1
        bomb1_rct.move_ip(vx1, vy1)
        scrn_sfc.blit(bomb1_sfc, bomb1_rct)
        yoko,tate  = check_bound(bomb1_rct, scrn_rct)
        vx1 *= yoko
        vy1 *= tate
        if tori_rct.colliderect(bomb1_rct):
            if dismith < count:
                LIFE -= 1
                dismith = count + 500  #無敵時間を設定
            else:
                pass

        #2
        bomb2_rct.move_ip(vx2, vy2)
        scrn_sfc.blit(bomb2_sfc, bomb2_rct)
        yoko,tate  = check_bound(bomb2_rct, scrn_rct)
        vx2 *= yoko
        vy2 *= tate
        if tori_rct.colliderect(bomb2_rct):
            if dismith < count:
                LIFE -= 1
                dismith = count + 1000
            else:
                pass
        #3
        bomb3_rct.move_ip(vx3, vy3)
        scrn_sfc.blit(bomb3_sfc, bomb3_rct)
        yoko,tate  = check_bound(bomb3_rct, scrn_rct)
        vx3 *= yoko
        vy3 *= tate
        if tori_rct.colliderect(bomb3_rct):
            if dismith < count:
                LIFE -= 1
                dismith = count + 1000
        #4
        bomb4_rct.move_ip(vx4, vy4)
        scrn_sfc.blit(bomb4_sfc, bomb4_rct)
        yoko,tate  = check_bound(bomb4_rct, scrn_rct)
        vx4 *= yoko
        vy4 *= tate
        if tori_rct.colliderect(bomb4_rct):
            if dismith < count:
                LIFE -= 1
                dismith = count + 1000

        #時間経過で次の玉が出てくる。
        if count == 5000 and LV2 == False:
            LV2 = True
            vx2 = 1
            vy2 = 1
        
        if count == 10000 and LV3 == False:
            LV3 = True
            vx3 = -1
            vy3 = 2

        if count == 15000 and LV4 == False:
            LV4 = True
            vx4 = 2
            vy4 = -1
        
        #LIFEの描画
        if LIFE == 3:
            scrn_sfc.blit(heart3_sfc, heart3_rct)
        if LIFE >= 2:
            scrn_sfc.blit(heart2_sfc, heart2_rct)
        if LIFE >= 1:
            scrn_sfc.blit(heart1_sfc, heart1_rct)
        
        if LIFE == 0:
            print(f"{count}フレーム生き残りました。")
            return
        scrn_sfc.blit(bomb_sfc, bomb_rct)  #でっかい爆弾  
        
        #現在のフレーム数を描画
        text = font.render(f"{count}", True, (255,255,255)) # 描画する文字列の設定
        scrn_sfc.blit(text, [20, 100])# 文字列の表示位置

        pg.display.update()
        clock.tick(1000)



if __name__ == "__main__":
    vx, vy = 1, 1
    pg.init()
    main()
    pg.quit()
    sys.exit()