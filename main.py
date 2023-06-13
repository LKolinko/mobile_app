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
from kivy.lang import Builder
from kivy.uix.label import Label
import time
from os import path

if platform == 'android':
    from android.storage import primary_external_storage_path
    dir = primary_external_storage_path()
    download_dir_path = os.path.join(dir, 'Download')


#Массивчик результатов
results = [0] * 6
sm = ScreenManager()
#Builder.load_file('bg.kv')

#Экран приветсвия
class Main_screen(Screen):
    def __init__(self):
        super().__init__()
        self.name = 'Main'

        Icon = Image(source="img_1.png", pos_hint={'center_x': .5, 'center_y': .7})
        self.add_widget(Icon)

        im = Image(source="img.png", size_hint=(.3, .3), pos_hint={'center_x': .2, 'center_y': 0.95})
        self.add_widget(im)

        l = Label(text='Приветствую вас в нашем приложении! С помощью\nтеста вы получите точные данные по уровню вашей\nстрессоустойчивости. По результатам теста вы\nувидите график, показывающий динамику вашей\nстрессоустойчивости.',
                  pos_hint={'center_x': .5, 'center_y': .3},color=(0,0,0,1))
        self.add_widget(l)

        btn = Button(text='Далее', size_hint=(.7, .1), pos_hint={'center_x': .5, 'center_y': .1},font_size='20sp',color=(0,0,0,1))
        btn.bind(on_press=self.to_second_scrn)
        btn.opacity = 0.5
        self.add_widget(btn)

    def to_second_scrn(self, *args):
        self.manager.current = 'Second'
        return 0

#экран с инструкцией
class Second_screen(Screen):
    def __init__(self):
        super().__init__()
        self.name = 'Second'

        im = Image(source="img.png", size_hint=(.3, .3), pos_hint={'center_x': .2, 'center_y': 0.95})
        self.add_widget(im)

        l = Label(text='Инструкция по прохождению теста:', pos_hint={'center_x': .5, 'center_y': .7},color=(0,0,0,1), font_size='20sp')
        self.add_widget(l)

        l2 = Label(text='1. На протяжении всего теста нам нужно держать\nлокоть навесу, на уровне кисти.\n\n'
                        '2. Для прохождения теста рекомендуем\nиспользование стилуса.\n\n'
                        '3. Вам нужно отметить наибольшее количество\nточек на экране в течение 5 секунд, 6 раз.',
                   color=(0,0,0,1), font_size='15sp', pos_hint={'center_x': .5, 'center_y': .5})
        self.add_widget(l2)

        btn = Button(text='Начать', size_hint=(.7, .1), pos_hint={'center_x': .5, 'center_y': .1},font_size='20sp',color=(0,0,0,1))
        btn.bind(on_press=self.to_test_scrn)
        btn.opacity = 0.5
        self.add_widget(btn)

    def to_test_scrn(self, *args):
        self.manager.current = 'Test1'
        return 0

#первый тест
class test_screen1(Screen):
    def __init__(self):
        self.t = time.time()
        super().__init__()
        self.name = 'Test1'

        btn1 = Button(text='Область для отмечания точек',  size_hint=(.8, .8), pos_hint={'center_x': .5, 'center_y': .5},font_size='20sp',color=(0,0,0,1))
        btn1.opacity = 0.5
        btn1.bind(on_press=self.callback)
        self.add_widget(btn1)

        im = Image(source="img.png", size_hint=(.3, .3), pos_hint={'center_x': .2, 'center_y': 0.95})
        self.add_widget(im)

        l = Label(text='Test №1', pos_hint={'center_x': .9, 'center_y': .95},color=(0,0,0,1))
        self.add_widget(l)

        self.ss = lambda x: set_screen('Test2')

    def callback(self, *args):
        results[0] += 1
        Clock.schedule_once(self.ss, 5)

#второй тест
class test_screen2(Screen):
    def __init__(self):
        self.t = time.time()
        Window.clearcolor = (1, 1, 1, 1)
        super().__init__()
        self.name = 'Test2'
        test_screen1_layout = FloatLayout()
        self.add_widget(test_screen1_layout)
        btn1 = Button(text='Область для отмечания точек',  size_hint=(.8, .8), pos_hint={'center_x': .5, 'center_y': .5},font_size='20sp',color=(0,0,0,1))
        btn1.bind(on_press=self.callback)
        btn1.opacity = 0.5
        test_screen1_layout.add_widget(btn1)

        l = Label(text='Test №2', pos_hint={'center_x': .9, 'center_y': .95},color=(0,0,0,1))
        self.add_widget(l)

        im = Image(source="img.png", size_hint=(.3, .3), pos_hint={'center_x': .2, 'center_y': 0.95})
        self.add_widget(im)

        self.ss = lambda x: set_screen('Test3')


    def callback(self, *args):
        results[1] += 1
        Clock.schedule_once(self.ss, 5)

#третий тест
class test_screen3(Screen):
    def __init__(self):
        self.t = time.time()
        Window.clearcolor = (1, 1, 1, 1)
        super().__init__()
        self.name = 'Test3'
        test_screen1_layout = FloatLayout()
        self.add_widget(test_screen1_layout)
        btn1 = Button(text='Область для отмечания точек',  size_hint=(.8, .8), pos_hint={'center_x': .5, 'center_y': .5},font_size='20sp',color=(0,0,0,1))
        btn1.bind(on_press=self.callback)
        btn1.opacity = 0.5
        test_screen1_layout.add_widget(btn1)

        l = Label(text='Test №3', pos_hint={'center_x': .9, 'center_y': .95},color=(0,0,0,1))
        self.add_widget(l)

        im = Image(source="img.png", size_hint=(.3, .3), pos_hint={'center_x': .2, 'center_y': 0.95})
        self.add_widget(im)

        self.ss = lambda x: set_screen('Test4')

    def callback(self, *args):
        results[2] += 1
        Clock.schedule_once(self.ss, 5)

#четвёртый тест
class test_screen4(Screen):
    def __init__(self):
        self.t = time.time()
        Window.clearcolor = (1, 1, 1, 1)
        super().__init__()
        self.name = 'Test4'
        test_screen1_layout = FloatLayout()
        self.add_widget(test_screen1_layout)
        btn1 = Button(text='Область для отмечания точек',  size_hint=(.8, .8), pos_hint={'center_x': .5, 'center_y': .5},font_size='20sp',color=(0,0,0,1))
        btn1.bind(on_press=self.callback)
        btn1.opacity = 0.5
        test_screen1_layout.add_widget(btn1)

        im = Image(source="img.png", size_hint=(.3, .3), pos_hint={'center_x': .2, 'center_y': 0.95})
        self.add_widget(im)

        l = Label(text='Test №4', pos_hint={'center_x': .9, 'center_y': .95},color=(0,0,0,1))
        self.add_widget(l)

        self.ss = lambda x: set_screen('Test5')


    def callback(self, *args):
        results[3] += 1
        Clock.schedule_once(self.ss, 5)

#пятый тест
class test_screen5(Screen):
    def __init__(self):
        self.t = time.time()
        Window.clearcolor = (1, 1, 1, 1)
        super().__init__()
        self.name = 'Test5'
        test_screen1_layout = FloatLayout()
        self.add_widget(test_screen1_layout)
        btn1 = Button(text='Область для отмечания точек',  size_hint=(.8, .8), pos_hint={'center_x': .5, 'center_y': .5},font_size='20sp',color=(0,0,0,1))
        btn1.bind(on_press=self.callback)
        btn1.opacity = 0.5
        test_screen1_layout.add_widget(btn1)

        im = Image(source="img.png", size_hint=(.3, .3), pos_hint={'center_x': .2, 'center_y': 0.95})
        self.add_widget(im)

        l = Label(text='Test №5', pos_hint={'center_x': .9, 'center_y': .95},color=(0,0,0,1))
        self.add_widget(l)

        self.ss = lambda x: set_screen('Test6')

    def callback(self, *args):
        results[4] += 1
        Clock.schedule_once(self.ss, 5)


#шестой тест
class test_screen6(Screen):
    def __init__(self):
        self.t = time.time()
        Window.clearcolor = (1, 1, 1, 1)
        super().__init__()
        self.name = 'Test6'
        test_screen1_layout = FloatLayout()
        self.add_widget(test_screen1_layout)
        btn1 = Button(text='Область для отмечания точек',  size_hint=(.8, .8), pos_hint={'center_x': .5, 'center_y': .5},font_size='20sp',color=(0,0,0,1))
        btn1.bind(on_press=self.callback)
        btn1.opacity = 0.5
        test_screen1_layout.add_widget(btn1)

        im = Image(source="img.png", size_hint=(.3, .3), pos_hint={'center_x': .2, 'center_y': 0.95})
        self.add_widget(im)

        l = Label(text='Test №6', pos_hint={'center_x': .9, 'center_y': .95}, color=(0, 0, 0, 1))
        self.add_widget(l)
        self.ss = lambda x: set_screen('Res')

    def callback(self, *args):
        results[5] += 1
        Clock.schedule_once(self.ss, 5)


class res_screen(Screen):
    def __init__(self):
        super().__init__()
        self.name = 'Res'
        self.test_screen1_layout = FloatLayout()
        self.add_widget(self.test_screen1_layout)

        l = Label(text="Результат тестирования", pos_hint={'center_x': .5, "center_y": .95}, color=(0,0,0,1), font_size='20pt')
        self.add_widget(l)

        self.btn1 = Button(text='Показать результат', size_hint=(.7, .3), pos_hint={'center_x': .5, 'center_y': .5},color=(0,0,0,1))
        self.btn1.bind(on_press=self.print_res)
        self.btn1.opacity = 0.5
        self.test_screen1_layout.add_widget(self.btn1)


    def download_file(self, *args):
        name_png = "save.png"
        x = [1, 2, 3, 4, 5, 6]
        y = np.array(results)
        plt.title("Результаты теста")
        plt.xlabel("№  попытки")
        plt.ylabel("количество нажатий")
        plt.plot(x, y, color="green")
        plt.savefig(name_png)
        plt.close()
        shutil.move(name_png, download_dir_path)

    def print_res(self, *args):

        btn3 = Button(text='Скачать результат', size_hint=(.7, .07), pos_hint={'center_x': .5, 'center_y': .09},
                      color=(0, 0, 0, 1))
        btn3.bind(on_press=self.download_file)
        btn3.opacity = 0.5
        self.test_screen1_layout.add_widget(btn3)

        self.test_screen1_layout.remove_widget(self.btn1)

        self.name_png = ''.join(choice(ascii_letters) for i in range(12)) + ".png"

        l = Label(text="Результаты уровня вашей стрессоустойчивасти\nпредставлены на графике. Для большей\nинформации по графику, вам следует\nобратиться к врачу.",pos_hint={'center_x':.5, 'center_y':.25},color=(0,0,0,1))
        self.test_screen1_layout.add_widget(l)

        l2 = Label(text="Спасибо за прохождение теста!",pos_hint={'center_x':.5, 'center_y':.17},color=(0,0,0,1))
        self.test_screen1_layout.add_widget(l2)

        x = [1, 2, 3, 4, 5, 6]
        y = np.array(results)
        plt.title("Результаты теста")
        plt.xlabel("№  попытки")
        plt.ylabel("количество нажатий")
        plt.plot(x, y, color="green")

        plt.savefig(self.name_png)
        plt.close()

        self.im = Image(source=self.name_png, pos_hint={'center_x': .5, 'center_y': .6})

        os.remove(self.name_png)

        self.add_widget(self.im)


def set_screen(name_screen):
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
        return sm


if __name__ == '__main__':
    TapT_Test().run()