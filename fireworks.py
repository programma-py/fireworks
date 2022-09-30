import pyxel

SCREEN_WIDTH = 256
SCREEN_HEIGHT = 256
FIREWORKS_NUM = 10          # 表示する花火の数
global staate

def sound_set():
    pyxel.sound(0).set("b3","t", "7", "s" ,3)

class Firework():
    def __init__(self):
        self.dot_size = 2   # ドットの半径
        self.dot_num = 20   # 1周のドットの数
        self.speed = 3      # 広がる速さ
        self.make(0, 0)     # 花火の初期値をセット

    def update(self):
        if self.r > self.radius:
            self.erase = True
        else:
            self.r += self.speed

    def draw(self):
        if self.erase == True:
            return
        for i in range(self.dot_num):
            x = pyxel.cos(360/self.dot_num * i) * self.r  + self.center_x
            y = pyxel.sin(360/self.dot_num * i) * self.r  + self.center_y
            pyxel.circ(x, y, self.dot_size, self.color)

    def make(self, x, y):
        self.center_x = x                   # 中心のX座標
        self.center_y = y                   # 中心のY座標
        self.r = 0                          # 中心からの位置
        self.color = pyxel.rndi(8,12)       # ドットの色
        self.radius = pyxel.rndi(80,120)    # 花火の半径の最大値
        self.erase = False                  # True:最大値を超えたら表示しない

class App:
    def __init__(self):
        pyxel.init(SCREEN_WIDTH, SCREEN_HEIGHT, fps=24, title="Fireworks")
        pyxel.mouse(True)
        sound_set()
        global state
        state = "START"
        self.fireworks = []
        pyxel.run(self.update, self.draw)

    def update(self):
        if pyxel.btnp(pyxel.KEY_Q):
            pyxel.quit()

        #if pyxel.btnp(pyxel.MOUSE_BUTTON_LEFT):    # btnpだとフレームごとにマウスの押下を判定
        if pyxel.btn(pyxel.MOUSE_BUTTON_LEFT):      # btnだとマウスを押し続けているか判定できる
            global state
            state = "PLAY"
            if len(self.fireworks) > FIREWORKS_NUM:
                self.fireworks.clear()              # 花火の数が設定数を超えたらすべて削除
            # 花火の生成
            firework = Firework() 
            firework.make(pyxel.mouse_x, pyxel.mouse_y)
            pyxel.play(0, 0)
            self.fireworks.append(firework)
        
        for firework in self.fireworks:
            firework.update()
        

    def draw(self):
        pyxel.cls(0)
        if state == "START":
            pyxel.rect(80, 100, 85, 60, 5)
            pyxel.text(98, 120, "CLICK OR TAP", 7)
            pyxel.text(90, 130, "TO SEE FIREWORKS", 7)
            return

        for firework in self.fireworks:
            firework.draw()

App()