import os
import sys
import pygame as pg

os.chdir(os.path.dirname(os.path.abspath(__file__)))


def main():
    pg.display.set_caption("はばたけ！こうかとん")
    screen = pg.display.set_mode((800, 600))
    clock  = pg.time.Clock()
    bg_img = pg.image.load("fig/pg_bg.jpg")
    koka_img = pg.image.load("fig/3.png")
    bg2_img = pg.image.load("fig/pg_bg.jpg")
    koka_img = pg.transform.flip(koka_img,True,False)#画像反転
    bg2_img = pg.transform.flip(bg2_img,True,False)
    tmr = 0
    x = 0
    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT: return
        x = tmr%1600
        screen.blit(bg_img, [-x, 0])
        screen.blit(bg2_img, [-x+1600, 0])
        koka_rect = koka_img.get_rect()#こうかとんrect抽出
        koka_rect.center = 300,200
        screen.blit(koka_img,koka_rect)#koka_imgをkoka_rectの設定に従って貼り付け
        pg.display.update()
        tmr += 1        
        clock.tick(200)


if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()