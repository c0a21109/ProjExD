import pygame as pg
import sys

def main():
    clock = pg.time.Clock()

    pg.display.set_caption("逃げろ工科豚") #タイトルバーに「逃げろ工科豚」と表示する
    scrn_sfc = pg.display.set_mode((1600, 900)) #1600x900の画面Surfaceを生成する

    pgbg_sfc = pg.image.load("fig/pg_bg.png") #Surface
    pgbg_sfc = pg.transform.rotozoom(pgbg_sfc, 90, 2.0)
    pgbg_rct = pgbg_sfc.get_rect() #Rect
    pgbg_rct.center = 400, 300
    scrn_sfc.blit(pgbg_sfc, pgbg_rct) #blit

    pg.display.update() #スクリーンを更新してこうかとんを表示
    clock.tick(0.2)

if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()