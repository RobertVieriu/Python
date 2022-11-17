from operator import le
import pyautogui
import keyboard
class PianoTiles:
    def __init__(self):
        print("apasa tasta esc pentru a inchide programul")
        x1 = self._mouse_pos('STANGA')[0]
        while keyboard.is_pressed('enter') : pass
        x2 = self._mouse_pos('DREAPTA')[0]
        self.left_x, self.right_x = min (x1,x2), max(x1,x2)
        self.center_y = pyautogui.size()[1]// 2
        self.tiles = self._tiles_pos()
        print("Coordonatele jocului sunt", self.left_x, self.right_x, self.center_y)
 
    def _mouse_pos(self, border):
        print(f'Pune cursorul in {border} marginii ferestrei jocului si apasa enter')
        x,y = 0 , 0
        while not keyboard.is_pressed('enter') and not keyboard.is_pressed('esc'):
            x,y= pyautogui.position()
            position = 'X: ' + str(x).rjust(4) + 'Y:' + str(y).rjust(4)
            print(position, end='')
            print('\b' * len(position) , end='', flush=True)
        print(f'{border} border: {x,y}')
        return x,y
 
    def _tiles_pos(self):
        lenght = self.right_x - self.left_x
        step= lenght // 4
        return[(self.left_x + i, self.center_y) for i in range (step//2, lenght, step)]
 
    def _is_tile(self,pixel,threshold):
        color= pyautogui.pixel(*pixel)
        return True if color[0]<=threshold else False
 
    def run(self, *, tile_rgb=10):
        while not keyboard.is_pressed('esc'):
            for pos in self.tiles:
                if self._is_tile(pos, tile_rgb):
                    pyautogui.click(*pos)
                    break
if __name__ == '__main__':
    PianoTiles().run()