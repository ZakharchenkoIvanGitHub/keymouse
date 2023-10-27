import time
from pynput.mouse import Button, Controller
from pynput import keyboard

mouse = Controller()


##while True:
##    print(f'Текущее положение указателя: {mouse.position}')
## В этом блоке будет работать слушатель событий.
# with keyboard.Events() as events:
#
#    for event in events:
#        if event.key == keyboard.Key.esc:
#            break
#        if event.key == "1":
#            break
#        else:
#            print(f'Получено событие клавиатуры {event}')
#            print(f'Получено 111 клавиатуры {event.key}')


def set_page(x, y, sl=1, next=1):
    mp = mouse.position
    if next:
        mouse.position = (1758, 185)
        mouse.press(Button.left)
        mouse.release(Button.left)
    mouse.position = (x, y)
    if sl:
        time.sleep(0.14)
    mouse.press(Button.left)
    mouse.release(Button.left)
    mouse.position = mp



def click(x,y):
    mp = mouse.position
    mouse.position = (x, y)
    mouse.press(Button.left)
    mouse.release(Button.left)
    mouse.position = mp

#mouse position (903, 975)

def test():
    print(f'mouse position {mouse.position}')




def on_release(key):
    try:
        print(f'released {key}')
        if key == keyboard.Key.space :  # Нерел1
            set_page(1040, 980)
        if key.char == "q":  # Вит
            set_page(1040, 213)
        if key.char == "a":  # ПодВит
            set_page(1040, 249)
        if key.char == "z":  # Вит-r
            set_page(1040, 283)
        if key.char == "2":  # next
            click(1866, 159)
        if key.char == "1":  # back
            click(1760, 159)
        if key.char == "3":  # Отличныйt
            set_page(1040, 410, 1)
        if key.char == "e":  # Хороший
            set_page(1040, 553, 1)
        if key.char == "d":  # Приемлемый
            set_page(1040, 705, 1)
        if key.char == "c":  # Плохой
            set_page(1040, 846, 1)
        if key.char == "r":  # Рел-
            set_page(1040, 909)
        if key.char == "f":  # Тем нерел
            set_page(1040, 949)

        if key.char == "4":  # отправить
            set_page(1837, 1017,next=0)

        if key.char == "t":  # 404
            click(903, 975)

    except AttributeError:
        print(f'released special key q{key}')

    if key == keyboard.Key.esc:
        # Stop listener
        return False


# Collect events until released
with keyboard.Listener(on_release=on_release) as listener:
    listener.join()
