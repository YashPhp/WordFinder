import os
import fnmatch
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen, FadeTransition
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout

class Homepage(Screen):
    def submit(self, path, word, typeofexem):
        global post_text_data
        global abc
        global cdf
        global word_u
        word_u = word
        print(path)
        print(word)
        typeofexem = '*.'+typeofexem
        abc = 0
        cdf = 0
        post_text_data = []
        for path, subdirs, files in os.walk(path):
            for name in files:
                abc += 1
                if fnmatch.fnmatch(os.path.join(path, name), typeofexem):
                    f = open(os.path.join(path, name), 'r', encoding="utf8")
                    if word in f.read():
                        print(os.path.join(path, name))
                        post_text_data.append(os.path.join(path, name))
                        cdf += 1
        print(abc)
        print("select files are :" + str(cdf))
        print(str(post_text_data))
class result_now(Screen):
    def data_get(self):
        abc_world = self.ids['yash_sanathara']
        ac = ''
        if post_text_data == []:
            ac = 'word Not Find '
        else:
            for a in post_text_data:
                ac = ac + '\n' + a
        abc_world.text = str(abc) +' Out of '+ str(cdf)+ ' have "'+ word_u +'"\n' +ac
        print(post_text_data)
class Find_man(ScreenManager):
    transition = FadeTransition()
w = Builder.load_string('''Find_man:
    Homepage
    result_now
<Homepage>:
    name:'Homepage'
    id:Homepage
    BoxLayout:
        orientation: 'vertical'
        Label:
            id:header
            font_size:50
            color:[1,1,0,1]
            text:'Enter Folder Path'
        TextInput:
            id:folder_path
            font_size:30
            size_hint_y : None
            height:200
            hint_text: 'Enter Folder Path'
            width:self.height
        TextInput:
            id:word_path
            font_size:30
            size_hint_y : None
            height:50
            hint_text: 'Enter Word Which You want'
        TextInput:
            id:type_path
            font_size:30
            size_hint_y : None
            height:50
            hint_text: 'which type Files selecting php , html, txt or more '
        Button:
            id:submit
            font_size:40
            color:[1,9,1,1]
            text:'Submit'
            on_press:
                root.submit(folder_path.text,word_path.text,type_path.text)
                app.root.current='result_now'
<result_now>:
    name:'result_now'
    BoxLayout:
        orientation: 'vertical'
        BoxLayout:
            size_hint_y : None
            height:50
            Button:
                font_size:40
                text:'Back'
                on_press:
                    app.root.current='Homepage'
            Button:
                font_size:40
                text:'Get-Files'
                on_press:
                    root.data_get()
        TextInput:
            id:yash_sanathara
            font_size:20
''')
class WeatherApp(App):
    def build(self):
        return w

if __name__ == '__main__':
    WeatherApp().run()
