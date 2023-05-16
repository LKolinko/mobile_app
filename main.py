import os
import random
import shutil
import string
import matplotlib.pyplot as plt
import numpy as np
from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.floatlayout import FloatLayout
from kivy.core.window import Window
from kivy.uix.image import Image
from kivy.lang import Builder
from kivy.uix.label import Label
import time

#Массивчик результатов
results = [0] * 6
sm = ScreenManager()
#Builder.load_file('bg.kv')

#Экран приветсвия
class Main_screen(Screen):
    def __init__(self):
        super().__init__()
        self.name = 'Main'

        Icon = Image(source="img_1.png", size_hint=(1, 1), pos_hint={'center_x': .5, 'center_y': .7})
        self.add_widget(Icon)

        im = Image(source="img.png", size_hint=(.3, .3), pos_hint={'center_x': .2, 'center_y': 0.95})
        self.add_widget(im)

        l = Label(text='Приветствую вас в нашем приложении! С помощью\nтеста вы получите точные данные по уровню вашей\nстрессоустойчивости. По результатам теста вы\nувидите график, показывающий динамику вашей\nстрессоустойчивости.',
                  pos_hint={'center_x': .5, 'center_y': .3},color=(0,0,0,1))
        self.add_widget(l)

        btn = Button(text='Далее', size_hint=(.7, .1), pos_hint={'center_x': .5, 'center_y': .1})
        btn.bind(on_press=self.to_second_scrn)
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

        btn = Button(text='Начать', size_hint=(.7, .1), pos_hint={'center_x': .5, 'center_y': .1})
        btn.bind(on_press=self.to_test_scrn)
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

        btn1 = Button(text='Область для отмечания точек',  size_hint=(.8, .5), pos_hint={'center_x': .5, 'center_y': .5})
        btn1.bind(on_press=self.callback)
        self.add_widget(btn1)

        im = Image(source="img.png", size_hint=(.3, .3), pos_hint={'center_x': .2, 'center_y': 0.95})
        self.add_widget(im)

        l = Label(text='Test №1', pos_hint={'center_x': .5, 'center_y': .8},color=(0,0,0,1))
        self.add_widget(l)

        l2 = Label(text='Отсчёт времени начнётся\n  после первого нажатия',pos_hint={'center_x': .5, 'center_y': .2},color=(0,0,0,1))
        self.add_widget(l2)

    def callback(self, *args):
        if (results[0] == 0):
            self.t = time.time()
        if (time.time() - self.t >= 5):
            self.manager.current = 'Test2'
            return 0
        results[0] += 1

#второй тест
class test_screen2(Screen):
    def __init__(self):
        self.t = time.time()
        Window.clearcolor = (1, 1, 1, 1)
        super().__init__()
        self.name = 'Test2'
        test_screen1_layout = FloatLayout()
        self.add_widget(test_screen1_layout)
        btn1 = Button(text='Область для отмечания точек',  size_hint=(.8, .5), pos_hint={'center_x': .5, 'center_y': .5})
        btn1.bind(on_press=self.callback)
        test_screen1_layout.add_widget(btn1)

        l = Label(text='Test №2', pos_hint={'center_x': .5, 'center_y': .8},color=(0,0,0,1))
        self.add_widget(l)

        l2 = Label(text='Отсчёт времени начнётся\n  после первого нажатия',pos_hint={'center_x': .5, 'center_y': .2},color=(0,0,0,1))
        self.add_widget(l2)

        im = Image(source="img.png", size_hint=(.3, .3), pos_hint={'center_x': .2, 'center_y': 0.95})
        self.add_widget(im)


    def callback(self, *args):
        if (results[1] == 0):
            self.t = time.time()
        if (time.time() - self.t >= 5):
            self.manager.current = 'Test3'
            return 0
        results[1] += 1

#третий тест
class test_screen3(Screen):
    def __init__(self):
        self.t = time.time()
        Window.clearcolor = (1, 1, 1, 1)
        super().__init__()
        self.name = 'Test3'
        test_screen1_layout = FloatLayout()
        self.add_widget(test_screen1_layout)
        btn1 = Button(text='Область для отмечания точек',  size_hint=(.8, .5), pos_hint={'center_x': .5, 'center_y': .5})
        btn1.bind(on_press=self.callback)
        test_screen1_layout.add_widget(btn1)

        l = Label(text='Test №3', pos_hint={'center_x': .5, 'center_y': .8},color=(0,0,0,1))
        self.add_widget(l)

        l2 = Label(text='Отсчёт времени начнётся\n  после первого нажатия',pos_hint={'center_x': .5, 'center_y': .2},color=(0,0,0,1))
        self.add_widget(l2)

        im = Image(source="img.png", size_hint=(.3, .3), pos_hint={'center_x': .2, 'center_y': 0.95})
        self.add_widget(im)

    def callback(self, *args):
        if (results[2] == 0):
            self.t = time.time()
        if (time.time() - self.t >= 5):
            self.manager.current = 'Test4'
            return 0
        results[2] += 1

#четвёртый тест
class test_screen4(Screen):
    def __init__(self):
        self.t = time.time()
        Window.clearcolor = (1, 1, 1, 1)
        super().__init__()
        self.name = 'Test4'
        test_screen1_layout = FloatLayout()
        self.add_widget(test_screen1_layout)
        btn1 = Button(text='Область для отмечания точек',  size_hint=(.8, .5), pos_hint={'center_x': .5, 'center_y': .5})
        btn1.bind(on_press=self.callback)
        test_screen1_layout.add_widget(btn1)

        im = Image(source="img.png", size_hint=(.3, .3), pos_hint={'center_x': .2, 'center_y': 0.95})
        self.add_widget(im)

        l = Label(text='Test №4', pos_hint={'center_x': .5, 'center_y': .8},color=(0,0,0,1))
        self.add_widget(l)

        l2 = Label(text='Отсчёт времени начнётся\n  после первого нажатия',pos_hint={'center_x': .5, 'center_y': .2},color=(0,0,0,1))
        self.add_widget(l2)


    def callback(self, *args):
        if (results[3] == 0):
            self.t = time.time()
        if (time.time() - self.t >= 5):
            self.manager.current = 'Test5'
            return 0
        results[3] += 1

#пятый тест
class test_screen5(Screen):
    def __init__(self):
        self.t = time.time()
        Window.clearcolor = (1, 1, 1, 1)
        super().__init__()
        self.name = 'Test5'
        test_screen1_layout = FloatLayout()
        self.add_widget(test_screen1_layout)
        btn1 = Button(text='Область для отмечания точек',  size_hint=(.8, .5), pos_hint={'center_x': .5, 'center_y': .5})
        btn1.bind(on_press=self.callback)
        test_screen1_layout.add_widget(btn1)

        im = Image(source="img.png", size_hint=(.3, .3), pos_hint={'center_x': .2, 'center_y': 0.95})
        self.add_widget(im)

        l = Label(text='Test №5', pos_hint={'center_x': .5, 'center_y': .8},color=(0,0,0,1))
        self.add_widget(l)

        l2 = Label(text='Отсчёт времени начнётся\n  после первого нажатия',pos_hint={'center_x': .5, 'center_y': .2},color=(0,0,0,1))
        self.add_widget(l2)

    def callback(self, *args):
        if (results[4] == 0):
            self.t = time.time()
        if (time.time() - self.t >= 5):
            self.manager.current = 'Test6'
            return 0
        results[4] += 1


#шестой тест
class test_screen6(Screen):
    def __init__(self):
        self.t = time.time()
        Window.clearcolor = (1, 1, 1, 1)
        super().__init__()
        self.name = 'Test6'
        test_screen1_layout = FloatLayout()
        self.add_widget(test_screen1_layout)
        btn1 = Button(text='Область для отмечания точек',  size_hint=(.8, .5), pos_hint={'center_x': .5, 'center_y': .5})
        btn1.bind(on_press=self.callback)
        test_screen1_layout.add_widget(btn1)

        im = Image(source="img.png", size_hint=(.3, .3), pos_hint={'center_x': .2, 'center_y': 0.95})
        self.add_widget(im)

        l = Label(text='Test №6', pos_hint={'center_x': .5, 'center_y': .8}, color=(0, 0, 0, 1))
        self.add_widget(l)

        l2 = Label(text='Отсчёт времени начнётся\n  после первого нажатия', pos_hint={'center_x': .5, 'center_y': .2},
                   color=(0, 0, 0, 1))
        self.add_widget(l2)

    def callback(self, *args):
        if (results[5] == 0):
            self.t = time.time()
        if (time.time() - self.t >= 5):
            self.manager.current = 'Res'
            return 0
        results[5] += 1


class res_screen(Screen):
    def __init__(self):
        super().__init__()
        self.name = 'Res'
        test_screen1_layout = FloatLayout()
        self.add_widget(test_screen1_layout)

        btn1 = Button(text='Показать результаты', size_hint=(.7, .07), pos_hint={'center_x': .5, 'center_y': .05})
        btn1.bind(on_press=self.print_res)
        test_screen1_layout.add_widget(btn1)

        btn2 = Button(text='Пройти тест снова', size_hint=(.7, .07), pos_hint={'center_x': .5, 'center_y': .13})
        btn2.bind(on_press=self.to_main_screen)
        test_screen1_layout.add_widget(btn2)


    def to_main_screen(self, *args):
        #сброс результатов для следующего тестирования
        for i in range(0, 6):
            results[i] = 0
        self.manager.current = 'Main'
        self.remove_widget(self.im)
        return 0

    def print_res(self, *args):

        x = [1, 2, 3, 4, 5, 6]
        y = np.array(results)
        plt.title("Результаты теста")
        plt.xlabel("№  попытки")
        plt.ylabel("количество нажатий")
        plt.plot(x, y, color="green")

        plt.savefig('res.png')
        plt.close()

        self.im = Image(source='res.png', pos_hint={'center_x': .5, 'center_y': .6}, size_hint=(1,1))

        self.add_widget(self.im)



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