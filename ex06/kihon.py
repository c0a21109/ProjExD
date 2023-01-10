import pygame as pg
import random
import sys

class Screen:
    # 初期化関数 タイトル，縦横幅，画像のパス
    def __init__(self, title, wh, img_path):
        pg.display.set_caption(title) 
        self.sfc = pg.display.set_mode(wh)
        self.rct = self.sfc.get_rect()
        self.bgi_sfc = pg.image.load(img_path)
        self.bgi_rct = self.bgi_sfc.get_rect() 

    # 画面の描画
    def blit(self, clock):
        self.sfc.blit(self.bgi_sfc, self.bgi_rct)
        # 真ん中にラインを描画
        pg.draw.line(
                        self.sfc, (255, 255, 255), (self.rct.centerx, 0),
                        (self.rct.centerx, 900), 10
                    )
        phase = clock//1000
        font = pg.font.Font(None, 55)
        text1 = font.render(F"{phase%4}", True, (0,0,0))   # 描画する文字列の設定
        self.sfc.blit(text1, [750, 55])# 文字列の表示位置

    # 以下追加機能
    """""
        phase = clock//1000
        font = pg.font.Font(None, 55)
        if phase > phase/2:
            text1 = font.render(F"{phase}", True, (0,0,0))   # 描画する文字列の設定
            text2 = font.render("unko", True, (0,0,0))
        else:
            text1 = font.render(F"{phase}", True, (0,0,0))   # 描画する文字列の設定
            text2 = font.render("hoge", True, (255,0,0))
        self.sfc.blit(text1, [750, 55])# 文字列の表示位置
        self.sfc.blit(text2, [750, 700] )
    """""
        
""""" # 残骸
class Bird1:
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
        for key, delta in Bird1.key_delta.items():
            if key_dct[key]:
                self.rct.centerx += delta[0]
                self.rct.centery += delta[1]  
            if check_bound(self.rct, scr.rct) != (+1, +1):
                self.rct.centerx -= delta[0]
                self.rct.centery -= delta[1]                   
class Bird2:
    key_delta = {
        pg.K_w: [0, -1],
        pg.K_s: [0, +1],
        pg.K_a: [-1, 0],
        pg.K_d: [+1, 0],
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
        for key, delta in Bird2.key_delta.items():
            if key_dct[key]:
                self.rct.centerx += delta[0]
                self.rct.centery += delta[1]  
            if check_bound(self.rct, scr.rct) != (+1, +1):
                self.rct.centerx -= delta[0]
                self.rct.centery -= delta[1]
"""""


# 各Playerのクラス。     貰いました m(__)m
class Player:
    # キーと方向の対応付け辞書
    key_delta = [{
        pg.K_w:     [0, -1],
        pg.K_s:     [0, +1],
        pg.K_a:     [-1, 0],
        pg.K_d:     [+1, 0],
    }, {
        pg.K_UP:    [0, -1],
        pg.K_DOWN:  [0, +1],
        pg.K_LEFT:  [-1, 0],
        pg.K_RIGHT: [+1, 0],
    }]

    # Playerの初期化関数
    def __init__(self, img_path, xy, no):
        self.sfc = pg.image.load(img_path)
        self.sfc = pg.transform.rotozoom(self.sfc, 0, 1)
        self.rct = self.sfc.get_rect()
        self.rct.center = xy
        self.pre_key = [1, 0]  # 以前の方向を記憶する変数
        self.number = no  # 0 or 1
        if self.number:
            self.bullet_direction = [-1, 0]
        else:
            self.bullet_direction = [1, 0]
        # 弾のリスト
        self.bullets = []

    # Playerの描画関数　画面のオブジェクトを入力
    def blit(self, scr: Screen):
        scr.sfc.blit(self.sfc, self.rct)

    # Playerの情報更新関数　画面のオブジェクトを入力
    def update(self, scr: Screen):
        key_dct = pg.key.get_pressed()
        for key, delta in Player.key_delta[self.number].items():
            if key_dct[key]:  # 移動処理
                self.rct.centerx += delta[0]
                self.rct.centery += delta[1]
            if check_bound(self.rct, scr.rct) != (+1, +1):  # 画面外に出ないようにする処理
                self.rct.centerx -= delta[0]
                self.rct.centery -= delta[1]
        self.blit(scr)  # 描画

    # 弾を設置する処理を行う関数
    def set_bullet(self):
        if len(self.bullets) < 5:  # 画面内に5発以上無ければ弾を撃てる
            self.bullets.append(
                Bullets((0, 0, 255), 20, self.bullet_direction, self))  # 弾追加


# 弾のクラス
class Bullets:
    def __init__(self, color, rad, vxy, player: Player):
        self.sfc = pg.Surface((2*rad, 2*rad))
        self.sfc.set_colorkey((0, 0, 0))
        pg.draw.circle(self.sfc, color, (rad, rad), rad)
        self.rct = self.sfc.get_rect()
        self.rct.centerx = player.rct.centerx
        self.rct.centery = player.rct.centery
        self.vx, self.vy = vxy
    # blit
    def blit(self, scr: Screen):
        scr.sfc.blit(self.sfc, self.rct)
    # update
    def update(self, scr: Screen):
        self.rct.move_ip(self.vx, self.vy)
        scr.sfc.blit(self.sfc, self.rct)
        yoko, tate = check_bound(self.rct, scr.rct)
        return yoko == -1 or tate == -1


def check_bound(obj_rct, scr_rct):
    yoko, tate = +1, +1
    if obj_rct.left < scr_rct.left or scr_rct.right < obj_rct.right:
        yoko = -1
    if obj_rct.top < scr_rct.top or scr_rct.bottom < obj_rct.bottom:
        tate = -1
    return yoko, tate

def main():
    clock =pg.time.Clock()

    # 画面を宣言
    scr = Screen("うんこうかとん", (1500,800), "fig/pg_bg.png")

    # こうか豚達を宣言
    kkt1 = Player("fig/2.png", (100,400), 0)
    kkt2 = Player("fig/6.png", (1400,400), 1)

    counter = 8000 # 弾の設置時間

    # メインループ 拝借
    while True:       
        for event in pg.event.get():
            # 終了判定
            if event.type == pg.QUIT:
                return
            # eを押したとき
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_e and counter >= 4000:
                    # 弾を置く
                    kkt1.set_bullet()
                if event.key == pg.K_SPACE and counter >= 4000:
                    # 弾を置く
                    kkt2.set_bullet()

        # 画面の描画
        scr.blit(counter)

        # 弾のうごくやつ
        if counter < 0:
            counter += 8000
        elif counter < 4000:
            for bullet in kkt1.bullets:
                if bullet.update(scr):
                    kkt1.bullets.pop(kkt1.bullets.index(bullet))
                if bullet.rct.colliderect(kkt2.rct):
                    return
            for bullet in kkt2.bullets:
                if bullet.update(scr):
                    kkt2.bullets.pop(kkt2.bullets.index(bullet))
                if bullet.rct.colliderect(kkt1.rct):
                    return
        else:
            for bullet in kkt1.bullets:
                bullet.blit(scr)
            for bullet in kkt2.bullets:
                bullet.blit(scr)

        kkt1.update(scr)
        kkt2.update(scr)

        pg.display.update()
        eta = clock.tick(1000)
        counter -= eta

if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()