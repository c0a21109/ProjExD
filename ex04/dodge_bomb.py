import pygame as pg
import sys


def main():
    clock =pg.time.Clock()
    # 練習１
    pg.display.set_caption("逃げろ工科豚")
    scrn_sfc = pg.display.set_mode((1600, 900))
    pgbg_sfc = pg.image.load("fig/pg_bg.png")
    pgbg_rct = pgbg_sfc.get_rect()

    # 練習３
    tori_sfc = pg.image.load("fig/6.png")
    tori_sfc = pg.transform.rotozoom(tori_sfc, 0, 2.0)
    tori_rct = tori_sfc.get_rect()
    tori_rct.center = 900, 400
    scrn_sfc.blit(tori_sfc, tori_rct) 

    # 練習２
    while True: #忘れないこと
        scrn_sfc.blit(pgbg_sfc, pgbg_rct) 
        for event in pg.event.get():
            if event.type == pg.QUIT:
                return

        #練習４
        key_dict = pg.key.get_pressed()
        if key_dict[pg.K_UP]:
            tori_rct.centery -= 1
        if key_dict[pg.K_DOWN]:
            tori_rct.centery += 1
        if key_dict[pg.K_LEFT]:
            tori_rct.centerx -= 1
        if key_dict[pg.K_RIGHT]:
            tori_rct.centerx += 1

        scrn_sfc.blit(tori_sfc, tori_rct) #座標を更新したら貼り付ける

        pg.display.update()
        clock.tick(1000)


if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()