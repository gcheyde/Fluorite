from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.slider import Slider
from kivy.uix.button import Button
from kivy.uix.label import Label
import asyncio
from time import sleep

class globe():
    def __init__(self):
        #globally accessible values to pass them between concurrently running programs
        self.speed = 100
        self.camera_snap = False
        self.camera_video = False
        self.vid = 0
#instantiating global values
globy = globe()

class GUI(GridLayout):
    def __init__(self, **kwargs):
        super(GUI, self).__init__(**kwargs)

        #defining the number of rows and columns in the gui grid
        self.cols=4
        self.rows=5

        #blank widget to fill space
        self.add_widget(Label(text=''))

        #Create and add buttons to take a photo or video
        pic_button = Button(text='Take Photo')
        self.add_widget(pic_button)
        pic_button.bind(on_press=self.picpressed)

        vid_button = Button(text='Take Video')
        self.add_widget(vid_button)
        vid_button.bind(on_press=self.vidpressed)

        self.add_widget(Label(text=''))

        # Creating sliders
        self.speedslider = Slider(min=-100, max=100)
        #capping videos at 2 minutes to avoid overly long values crashing the rpi
        self.vidslider = Slider(min=20, max=120)

        # Add slider widgets and labels to the layout
        self.add_widget(Label(text="Speed"))
        self.add_widget(self.speedslider)
        self.add_widget(Label(text ='Percent of Max Speed:'))
        self.speedslider_value = Label(text ='0')
        self.add_widget(self.speedslider_value)

        self.add_widget(Label(text="Video Length"))
        self.add_widget(self.vidslider)
        self.add_widget(Label(text ='Seconds:'))
        self.vidslider_value = Label(text ='20')
        self.add_widget(self.vidslider_value)

        # Add a callback function to be called when the slider value changes
        self.speedslider.bind(value=self.on_slider_value_change)
        self.vidslider.bind(value=self.vidlength)

    def on_slider_value_change(self, instance, value):
        # Update the class variable with the new speed slider value
        globy.speed = value
        self.speedslider_value.text = "% d"% value
    
    def vidlength(self, instance, value):
        # Update the class variable with the new video length slider value
        globy.vid = value
        self.vidslider_value.text = "% d"% value
    
    def picpressed(self, instance):
        #detection of picture button being pressed
        globy.camera_snap = True
    
    def vidpressed(self, instance):
        #detection of video button being pressed
        print('button pressed')
        globy.camera_video = True

#app containing the gui layout, which the app will run
class MyApp(App):
    def build(self):
        layout = GUI()
        return layout

    #stuff for the async run
    async def kivycoro(self):
        await self.async_run(async_lib='asyncio')
    
    async def base(self):
        (done, pending) = await asyncio.wait({self.kivycoro()}, return_when='FIRST_COMPLETED')

#async part that is concurrently run, controlling the motors, etc
async def GlobalTask():
    #basic detection stuff to ensure it's all correctly running
    speed = 0
    vid = 20
    while True:
        if globy.speed != speed:
            print('global speed', int(globy.speed))
            speed = globy.speed
        if globy.camera_snap:
            print('detected press')
            globy.camera_snap = False
        if globy.camera_video:
            print(int(globy.vid), 'second video taken')
            globy.camera_video = False
        await asyncio.sleep(0.1)

if __name__ == '__main__':
    #async package that contains both concurrent tasks
    async def mainThread():
        app = MyApp()
        a = asyncio.create_task(app.base())
        b = asyncio.create_task(GlobalTask())
        (done,pending) = await asyncio.wait({a}, return_when='FIRST_COMPLETED')
    #running the concurrent package
    asyncio.run(mainThread())
