import os
import shutil
from random import choice
from string import ascii_letters
from kivy.clock import *
import matplotlib.pyplot as plt
import numpy as np
from kivy.app import App
from kivy.utils import platform
from kivy.uix.button import Button
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.floatlayout import FloatLayout
from kivy.core.window import Window
from kivy.uix.image import Image
from kivy.uix.textinput import TextInput
from kivy.uix.checkbox import CheckBox
from kivy.lang import Builder
from kivy.uix.label import Label
from kivy.core.window import Window
import time
from os import path

if platform == 'android':
    from android.storage import primary_external_storage_path

    dir = primary_external_storage_path()
    download_dir_path = os.path.join(dir, 'Download')

# Массивчик результатов
results = [0] * 6
sm = ScreenManager()


# Builder.load_file('bg.kv')

# Экран приветсвия
class Main_screen(Screen):
    def __init__(self):

        Window.size = (400, 800)


        super().__init__()
        self.name = 'Main'

        Icon = Image(source="img_1.png", pos_hint={'center_x': .5, 'center_y': .7})
        self.add_widget(Icon)

        im = Image(source="img.png", size_hint=(.3, .3), pos_hint={'center_x': .2, 'center_y': 0.95})
        self.add_widget(im)

        l = Label(
            text='Приветствую вас в нашем приложении! С помощью теста вы получите точные данные по уровню вашей стрессоустойчивости. По результатам теста вы увидите график, показывающий динамику вашей стрессоустойчивости.',
            pos_hint={'center_x': .5, 'center_y': .3}, color=(0, 0, 0, 1),text_size=(Window.width - 25, None), halign="justify", valign="middle")
        self.add_widget(l)

        btn = Button(text='Далее', size_hint=(.7, .1), pos_hint={'center_x': .5, 'center_y': .1}, font_size='15sp',
                     color=(0, 0, 0, 1))
        btn.bind(on_press=self.to_second_scrn)
        btn.opacity = 0.5
        self.add_widget(btn)

    def to_second_scrn(self, *args):
        set_screen('Second')
        return 0


# экран с инструкцией
class Second_screen(Screen):
    def __init__(self):
        super().__init__()
        self.name = 'Second'

        im = Image(source="img.png", size_hint=(.3, .3), pos_hint={'center_x': .2, 'center_y': 0.95})
        self.add_widget(im)

        l = Label(text='Инструкция по прохождению теста:', pos_hint={'center_x': .5, 'center_y': .7},
                  color=(0, 0, 0, 1), font_size='20sp',text_size=(Window.width - 50, None))
        self.add_widget(l)

        l2 = Label(text='1. На протяжении всего теста нам нужно держать локоть навесу, на уровне кисти.\n\n'
                        '2. Для прохождения теста рекомендуем использование стилуса.\n\n'
                        '3. Вам нужно отметить наибольшее количество точек на экране в течение 5 секунд, 6 раз.',
                   color=(0, 0, 0, 1), font_size='15sp', pos_hint={'center_x': .5, 'center_y': .5},text_size=(Window.width - 50, None))
        self.add_widget(l2)

        btn = Button(text='Начать', size_hint=(.7, .1), pos_hint={'center_x': .5, 'center_y': .1}, font_size='15sp',
                     color=(0, 0, 0, 1))
        btn.bind(on_press=self.to_test_scrn)
        btn.opacity = 0.5
        self.add_widget(btn)

    def to_test_scrn(self, *args):
        set_screen("Test1")
        return 0


# первый тест
class test_screen1(Screen):
    def __init__(self):
        self.clear_widgets()
        super().__init__()
        self.name = 'Test1'

        self.timer_scoreboard = Label(text="05:00",pos_hint={'center_x': .5, 'center_y': .85},
                                      color=(0,0,0,1),font_size='20pt')
        self.add_widget(self.timer_scoreboard)

        self.cnt = 0

        btn1 = Button(text='    Область для\n\nотмечания точек', size_hint=(.8, .7), pos_hint={'center_x': .5, 'center_y': .4},
                      font_size='20sp', color=(0, 0, 0, 1))
        btn1.opacity = 0.5
        btn1.bind(on_press=self.callback)
        self.add_widget(btn1)

        im = Image(source="img.png", size_hint=(.3, .3), pos_hint={'center_x': .2, 'center_y': 0.95})
        self.add_widget(im)

        l = Label(text='Test №1', pos_hint={'center_x': .9, 'center_y': .95}, color=(0, 0, 0, 1))
        self.add_widget(l)

        self.timer_ss = lambda x: self.timer_widget()

        self.ss = lambda x: set_screen('Test2')

    def callback(self, *args):
        Clock.schedule_once(self.ss, 5)
        if results[0] == 0:
            self.cnt = 0
            Clock.schedule_once(self.timer_ss, 0.02)
        results[0] += 1

    def timer_widget(self, *args):
        self.cnt += 2
        flag = True
        if 4 - self.cnt / 100 < 0:
            time_str = "00:00"
            flag = False

        elif self.cnt % 100 == 0:
            time_str = "0" + str(4 - int(self.cnt / 100)) + ":" + "00"

        elif 100 - self.cnt % 100 < 10:
            time_str = "0" + str(4 - int(self.cnt / 100)) + ":" + "0" + str(100 - self.cnt % 100)

        else:
            time_str = "0" + str(4 - int(self.cnt / 100)) + ":" + str(100 - self.cnt % 100)

        self.timer_scoreboard.text = time_str
        if flag:
            Clock.schedule_once(self.timer_ss, 0.02)

# второй тест
class test_screen2(Screen):
    def __init__(self):
        self.clear_widgets()
        Window.clearcolor = (1, 1, 1, 1)
        super().__init__()
        self.name = 'Test2'

        self.timer_scoreboard = Label(text="05:00", pos_hint={'center_x': .5, 'center_y': .85}, color=(0, 0, 0, 1),
                                      font_size='20pt')
        self.add_widget(self.timer_scoreboard)

        self.cnt = 0

        btn1 = Button(text='    Область для\n\nотмечания точек', size_hint=(.8, .7), pos_hint={'center_x': .5, 'center_y': .4},
                      font_size='20sp', color=(0, 0, 0, 1))
        btn1.bind(on_press=self.callback)
        btn1.opacity = 0.5
        self.add_widget(btn1)

        l = Label(text='Test №2', pos_hint={'center_x': .9, 'center_y': .95}, color=(0, 0, 0, 1))
        self.add_widget(l)

        im = Image(source="img.png", size_hint=(.3, .3), pos_hint={'center_x': .2, 'center_y': 0.95})
        self.add_widget(im)

        self.ss = lambda x: set_screen('Test3')

        self.timer_ss = lambda x: self.timer_widget()

    def callback(self, *args):
        Clock.schedule_once(self.ss, 5)
        if results[1] == 0:
            self.cnt = 0
            Clock.schedule_once(self.timer_ss, 0.02)
        results[1] += 1

    def timer_widget(self, *args):
        self.cnt += 2
        flag = True
        if 4 - self.cnt / 100 < 0:
            time_str = "00:00"
            flag = False

        elif self.cnt % 100 == 0:
            time_str = "0" + str(4 - int(self.cnt / 100)) + ":" + "00"

        elif 100 - self.cnt % 100 < 10:
            time_str = "0" + str(4 - int(self.cnt / 100)) + ":" + "0" + str(100 - self.cnt % 100)

        else:
            time_str = "0" + str(4 - int(self.cnt / 100)) + ":" + str(100 - self.cnt % 100)

        self.timer_scoreboard.text = time_str
        if flag:
            Clock.schedule_once(self.timer_ss, 0.02)


# третий тест
class test_screen3(Screen):
    def __init__(self):
        self.clear_widgets()
        Window.clearcolor = (1, 1, 1, 1)
        super().__init__()
        self.name = 'Test3'

        self.timer_scoreboard = Label(text="05:00", pos_hint={'center_x': .5, 'center_y': .85}, color=(0, 0, 0, 1),
                                      font_size='20pt')
        self.add_widget(self.timer_scoreboard)

        self.cnt = 0

        btn1 = Button(text='    Область для\n\nотмечания точек', size_hint=(.8, .7), pos_hint={'center_x': .5, 'center_y': .4},
                      font_size='20sp', color=(0, 0, 0, 1))
        btn1.bind(on_press=self.callback)
        btn1.opacity = 0.5
        self.add_widget(btn1)

        l = Label(text='Test №3', pos_hint={'center_x': .9, 'center_y': .95}, color=(0, 0, 0, 1))
        self.add_widget(l)

        im = Image(source="img.png", size_hint=(.3, .3), pos_hint={'center_x': .2, 'center_y': 0.95})
        self.add_widget(im)

        self.ss = lambda x: set_screen('Test4')

        self.timer_ss = lambda x: self.timer_widget()

    def callback(self, *args):
        Clock.schedule_once(self.ss, 5)
        if results[2] == 0:
            self.cnt = 0
            Clock.schedule_once(self.timer_ss, 0.02)
        results[2] += 1

    def timer_widget(self, *args):
        self.cnt += 2
        flag = True
        if 4 - self.cnt / 100 < 0:
            time_str = "00:00"
            flag = False

        elif self.cnt % 100 == 0:
            time_str = "0" + str(4 - int(self.cnt / 100)) + ":" + "00"

        elif 100 - self.cnt % 100 < 10:
            time_str = "0" + str(4 - int(self.cnt / 100)) + ":" + "0" + str(100 - self.cnt % 100)

        else:
            time_str = "0" + str(4 - int(self.cnt / 100)) + ":" + str(100 - self.cnt % 100)

        self.timer_scoreboard.text = time_str
        if flag:
            Clock.schedule_once(self.timer_ss, 0.02)


# четвёртый тест
class test_screen4(Screen):
    def __init__(self):
        self.clear_widgets()
        Window.clearcolor = (1, 1, 1, 1)
        super().__init__()
        self.name = 'Test4'

        self.timer_scoreboard = Label(text="05:00", pos_hint={'center_x': .5, 'center_y': .85}, color=(0, 0, 0, 1),
                                      font_size='20pt')
        self.add_widget(self.timer_scoreboard)

        self.cnt = 0

        btn1 = Button(text='    Область для\n\nотмечания точек', size_hint=(.8, .7), pos_hint={'center_x': .5, 'center_y': .4},
                      font_size='20sp', color=(0, 0, 0, 1))
        btn1.bind(on_press=self.callback)
        btn1.opacity = 0.5
        self.add_widget(btn1)

        im = Image(source="img.png", size_hint=(.3, .3), pos_hint={'center_x': .2, 'center_y': 0.95})
        self.add_widget(im)

        l = Label(text='Test №4', pos_hint={'center_x': .9, 'center_y': .95}, color=(0, 0, 0, 1))
        self.add_widget(l)

        self.ss = lambda x: set_screen('Test5')

        self.timer_ss = lambda x: self.timer_widget()

    def callback(self, *args):
        Clock.schedule_once(self.ss, 5)
        if results[3] == 0:
            self.cnt = 0
            Clock.schedule_once(self.timer_ss, 0.02)
        results[3] += 1

    def timer_widget(self, *args):
        self.cnt += 2
        flag = True
        if 4 - self.cnt / 100 < 0:
            time_str = "00:00"
            flag = False

        elif self.cnt % 100 == 0:
            time_str = "0" + str(4 - int(self.cnt / 100)) + ":" + "00"

        elif 100 - self.cnt % 100 < 10:
            time_str = "0" + str(4 - int(self.cnt / 100)) + ":" + "0" + str(100 - self.cnt % 100)

        else:
            time_str = "0" + str(4 - int(self.cnt / 100)) + ":" + str(100 - self.cnt % 100)

        self.timer_scoreboard.text = time_str
        if flag:
            Clock.schedule_once(self.timer_ss, 0.02)


# пятый тест
class test_screen5(Screen):
    def __init__(self):
        self.clear_widgets()
        Window.clearcolor = (1, 1, 1, 1)
        super().__init__()
        self.name = 'Test5'

        self.timer_scoreboard = Label(text="05:00", pos_hint={'center_x': .5, 'center_y': .85}, color=(0, 0, 0, 1),
                                      font_size='20pt')
        self.add_widget(self.timer_scoreboard)

        self.cnt = 0

        btn1 = Button(text='    Область для\n\nотмечания точек', size_hint=(.8, .7), pos_hint={'center_x': .5, 'center_y': .4},
                      font_size='20sp', color=(0, 0, 0, 1))
        btn1.bind(on_press=self.callback)
        btn1.opacity = 0.5
        self.add_widget(btn1)

        im = Image(source="img.png", size_hint=(.3, .3), pos_hint={'center_x': .2, 'center_y': 0.95})
        self.add_widget(im)

        l = Label(text='Test №5', pos_hint={'center_x': .9, 'center_y': .95}, color=(0, 0, 0, 1))
        self.add_widget(l)

        self.ss = lambda x: set_screen('Test6')

        self.timer_ss = lambda x: self.timer_widget()

    def callback(self, *args):
        Clock.schedule_once(self.ss, 5)
        if results[4] == 0:
            self.cnt = 0
            Clock.schedule_once(self.timer_ss, 0.02)
        results[4] += 1

    def timer_widget(self, *args):
        self.cnt += 2
        flag = True
        if 4 - self.cnt / 100 < 0:
            time_str = "00:00"
            flag = False

        elif self.cnt % 100 == 0:
            time_str = "0" + str(4 - int(self.cnt / 100)) + ":" + "00"

        elif 100 - self.cnt % 100 < 10:
            time_str = "0" + str(4 - int(self.cnt / 100)) + ":" + "0" + str(100 - self.cnt % 100)

        else:
            time_str = "0" + str(4 - int(self.cnt / 100)) + ":" + str(100 - self.cnt % 100)

        self.timer_scoreboard.text = time_str
        if flag:
            Clock.schedule_once(self.timer_ss, 0.02)


# шестой тест
class test_screen6(Screen):
    def __init__(self):
        self.clear_widgets()
        Window.clearcolor = (1, 1, 1, 1)
        super().__init__()
        self.name = 'Test6'

        self.timer_scoreboard = Label(text="05:00", pos_hint={'center_x': .5, 'center_y': .85}, color=(0, 0, 0, 1),
                                      font_size='20pt')
        self.add_widget(self.timer_scoreboard)

        self.cnt = 0

        btn1 = Button(text='    Область для\n\nотмечания точек', size_hint=(.8, .7), pos_hint={'center_x': .5, 'center_y': .4},
                      font_size='20sp', color=(0, 0, 0, 1))
        btn1.bind(on_press=self.callback)
        btn1.opacity = 0.5
        self.add_widget(btn1)

        im = Image(source="img.png", size_hint=(.3, .3), pos_hint={'center_x': .2, 'center_y': 0.95})
        self.add_widget(im)

        l = Label(text='Test №6', pos_hint={'center_x': .9, 'center_y': .95}, color=(0, 0, 0, 1))
        self.add_widget(l)

        self.ss = lambda x: set_screen('Res')

        self.timer_ss = lambda x: self.timer_widget()

    def callback(self, *args):
        Clock.schedule_once(self.ss, 5)
        if results[5] == 0:
            self.cnt = 0
            Clock.schedule_once(self.timer_ss, 0.02)
        results[5] += 1

    def timer_widget(self, *args):
        self.cnt += 2
        flag = True
        if 4 - self.cnt / 100 < 0:
            time_str = "00:00"
            flag = False

        elif self.cnt % 100 == 0:
            time_str = "0" + str(4 - int(self.cnt / 100)) + ":" + "00"

        elif 100 - self.cnt % 100 < 10:
            time_str = "0" + str(4 - int(self.cnt / 100)) + ":" + "0" + str(100 - self.cnt % 100)

        else:
            time_str = "0" + str(4 - int(self.cnt / 100)) + ":" + str(100 - self.cnt % 100)

        self.timer_scoreboard.text = time_str
        if flag:
            Clock.schedule_once(self.timer_ss, 0.02)


class res_screen(Screen):
    def __init__(self):
        self.clear_widgets()
        super().__init__()
        self.name = 'Res'

        l = Label(text="Результат тестирования", pos_hint={'center_x': .5, "center_y": .95}, color=(0, 0, 0, 1),font_size=Window.width / 16)
        self.add_widget(l)

        self.btn1 = Button(text='Показать результат', size_hint=(.7, .3), pos_hint={'center_x': .5, 'center_y': .5},
                           color=(0, 0, 0, 1))
        self.btn1.bind(on_press=self.print_res)
        self.btn1.opacity = 0.5
        self.add_widget(self.btn1)

    def download_file(self, *args):

        self.clear_widgets()
        l = Label(text="Результат тестирования", pos_hint={'center_x': .5, "center_y": .95}, color=(0, 0, 0, 1),
                  font_size=Window.width / 16)
        self.add_widget(l)

        self.btn1 = Button(text='Показать результат', size_hint=(.7, .3), pos_hint={'center_x': .5, 'center_y': .5},
                           color=(0, 0, 0, 1))
        self.btn1.bind(on_press=self.print_res)
        self.btn1.opacity = 0.5
        self.add_widget(self.btn1)

        set_screen("Download")
        return 0

    def print_res(self, *args):

        self.remove_widget(self.btn1)

        btn3 = Button(text='Скачать результат', size_hint=(.7, .05), pos_hint={'center_x': .5, 'center_y': .1},
                      color=(0, 0, 0, 1))
        btn3.bind(on_press=self.download_file)
        btn3.opacity = 0.5
        self.add_widget(btn3)

        self.name_png = ''.join(choice(ascii_letters) for i in range(12)) + ".png"

        l = Label(
            text="Результаты уровня вашей стрессоустойчивасти представлены на графике. Для большей информации по графику, вам следует обратиться к врачу.",
            pos_hint={'center_x': .5, 'center_y': .3}, color=(0, 0, 0, 1), text_size=(Window.width - 50, None),halign="justify", valign="middle")
        self.add_widget(l)

        l2 = Label(text="Спасибо за прохождение теста!", pos_hint={'center_x': .5, 'center_y': .2}, color=(0, 0, 0, 1))
        self.add_widget(l2)

        btn4 = Button(text="Пройти тест снова", size_hint=(.7, .05), pos_hint={'center_x': .5, 'center_y': .04},color=(0,0,0,1))
        btn4.bind(on_press=self.to_main_screen)
        btn4.opacity = 0.5
        self.add_widget(btn4)

        x = [1, 2, 3, 4, 5, 6]
        y = np.array(results)
        plt.title("Результат теста")
        plt.xlabel("№  попытки")
        plt.ylabel("количество нажатий")
        plt.plot(x, y, color="green")

        plt.savefig(self.name_png)
        plt.close()

        self.im = Image(source=self.name_png, pos_hint={'center_x': .5, 'center_y': .6})

        os.remove(self.name_png)

        self.add_widget(self.im)

    def to_main_screen(self, *args):

        self.clear_widgets()
        l = Label(text="Результат тестирования", pos_hint={'center_x': .5, "center_y": .95}, color=(0, 0, 0, 1),
                  font_size=Window.width / 16)
        self.add_widget(l)

        self.btn1 = Button(text='Показать результат', size_hint=(.7, .3), pos_hint={'center_x': .5, 'center_y': .5},
                           color=(0, 0, 0, 1))
        self.btn1.bind(on_press=self.print_res)
        self.btn1.opacity = 0.5
        self.add_widget(self.btn1)

        set_screen("Main")


class Download_screen(Screen):
    def __init__(self):
        self.clear_widgets()
        super().__init__()
        self.name = "Download"

        l = Label(text="Скачивание результата", pos_hint={'center_x': .5, 'center_y': .95}, font_size=Window.width / 16,
                  color=(0, 0, 0, 1))
        self.add_widget(l)

        self.text_input = TextInput(pos_hint={'center_x': .5, 'center_y': .75}, size_hint=(.9, .1))
        self.add_widget(self.text_input)

        l2 = Label(text='Введите имя файла:', pos_hint={'center_x': .5, 'center_y': .82}, color=(0, 0, 0, 1),
                   font_size='10pt')
        self.add_widget(l2)

        l3 = Label(text='Выберите формат файла:', pos_hint={'center_x': .5, 'center_y': .6}, color=(0, 0, 0, 1),
                   font_size='10pt')
        self.add_widget(l3)

        self.flag = 1

        lable_first_check = Label(text="<имя файла>.png", pos_hint={'center_x': .2, 'center_y': .5}, color=(0, 0, 0, 1))
        self.add_widget(lable_first_check)
        first_check = CheckBox(group='test', pos_hint={'center_x': .9, 'center_y': .5}, size_hint=(.2, .2),
                               color=(0, 0, 0, 1), active=True, on_press=self.first_check_enter)
        self.add_widget(first_check)

        lable_second_check = Label(text="<имя файла>.pdf", pos_hint={'center_x': .2, 'center_y': .4},
                                   color=(0, 0, 0, 1))
        self.add_widget(lable_second_check)
        second_check = CheckBox(group='test', pos_hint={'center_x': .9, 'center_y': .4}, size_hint=(.2, .2),
                                color=(0, 0, 0, 1), on_press=self.second_check_enter)
        self.add_widget(second_check)

        btn = Button(text="Скачать файл", pos_hint={'center_x': .5, 'center_y': .1}, size_hint=(.7, .05),
                     color=(0, 0, 0, 1))
        btn.bind(on_press=self.Download)
        btn.opacity = 0.5
        self.add_widget(btn)

        btn2 = Button(text="Пройти тест снова", pos_hint={'center_x': .5, 'center_y': .04}, size_hint=(.7, .05), color=(0,0,0,1))
        btn2.bind(on_press=self.to_main_screen)
        btn2.opacity = 0.5
        self.add_widget(btn2)

    def first_check_enter(self, *args):
        self.flag = 1

    def second_check_enter(self, *args):
        self.flag = 2

    def Download(self, *args):

        if (self.text_input.text != ""):
            name_save = self.text_input.text
        else:
            name_save = ''.join(choice(ascii_letters) for i in range(12))

        if (self.flag == 1):
            name_save += ".png"
        else:
            name_save += ".pdf"

        l = Label(text="Файл " + name_save, pos_hint={'center_x': .5, 'center_y': .23}, color=(0, 0, 0, 1))
        self.test_screen1_layout.add_widget(l)

        l2 = Label(text="успешно сохранён в папку Download", pos_hint={'center_x': .5, 'center_y': .2},
                   color=(0, 0, 0, 1))
        self.test_screen1_layout.add_widget(l2)

        x = [1, 2, 3, 4, 5, 6]
        y = np.array(results)
        plt.title("Результаты теста")
        plt.xlabel("№  попытки")
        plt.ylabel("количество нажатий")
        plt.plot(x, y, color="green")
        plt.savefig(name_save)
        plt.close()
        shutil.move(name_save, download_dir_path)

    def to_main_screen(self, *args):

        self.clear_widgets()

        l = Label(text="Скачивание результата", pos_hint={'center_x': .5, 'center_y': .95}, font_size=Window.width / 16,
                  color=(0, 0, 0, 1))
        self.add_widget(l)

        self.text_input = TextInput(pos_hint={'center_x': .5, 'center_y': .75}, size_hint=(.9, .1))
        self.add_widget(self.text_input)

        l2 = Label(text='Введите имя файла:', pos_hint={'center_x': .5, 'center_y': .82}, color=(0, 0, 0, 1),
                   font_size='10pt')
        self.add_widget(l2)

        l3 = Label(text='Выберите формат файла:', pos_hint={'center_x': .5, 'center_y': .6}, color=(0, 0, 0, 1),
                   font_size='10pt')
        self.add_widget(l3)

        self.flag = 1

        lable_first_check = Label(text="<имя файла>.png", pos_hint={'center_x': .2, 'center_y': .5}, color=(0, 0, 0, 1))
        self.add_widget(lable_first_check)
        first_check = CheckBox(group='test', pos_hint={'center_x': .9, 'center_y': .5}, size_hint=(.2, .2),
                               color=(0, 0, 0, 1), active=True, on_press=self.first_check_enter)
        self.add_widget(first_check)

        lable_second_check = Label(text="<имя файла>.pdf", pos_hint={'center_x': .2, 'center_y': .4},
                                   color=(0, 0, 0, 1))
        self.add_widget(lable_second_check)
        second_check = CheckBox(group='test', pos_hint={'center_x': .9, 'center_y': .4}, size_hint=(.2, .2),
                                color=(0, 0, 0, 1), on_press=self.second_check_enter)
        self.add_widget(second_check)

        btn = Button(text="Скачать файл", pos_hint={'center_x': .5, 'center_y': .1}, size_hint=(.7, .05),
                     color=(0, 0, 0, 1))
        btn.bind(on_press=self.Download)
        btn.opacity = 0.5
        self.add_widget(btn)

        btn2 = Button(text="Пройти тест снова", pos_hint={'center_x': .5, 'center_y': .04}, size_hint=(.7, .05),
                      color=(0, 0, 0, 1))
        btn2.bind(on_press=self.to_main_screen)
        btn2.opacity = 0.5
        self.add_widget(btn2)

        set_screen("Main")


def set_screen(name_screen):
    if name_screen == "Main":
        for i in range(0, 6):
            results[i] = 0

    sm.current = name_screen


class TapT_Test(App):
    def build(self):
        sm.add_widget(Main_screen())
        sm.add_widget(Second_screen())
        sm.add_widget(test_screen1())
        sm.add_widget(test_screen2())
        sm.add_widget(test_screen3())
        sm.add_widget(test_screen4())
        sm.add_widget(test_screen5())
        sm.add_widget(test_screen6())
        sm.add_widget(res_screen())
        sm.add_widget(Download_screen())
        return sm


if __name__ == '__main__':
    TapT_Test().run()