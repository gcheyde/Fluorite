from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.slider import Slider
from kivy.uix.button import Button
from kivy.uix.label import Label
import asyncio
from time import sleep
import RPi.GPIO as GPIO
from picamera import PiCamera

class globe():
    def __init__(self):
        #globally accessible values to pass them between concurrently running programs
        self.speed = 100
        self.camera_snap = False
        self.camera_video = False
        self.vid = 20
        self.picnum = 0
        self.vidnum = 0
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

#rpi running part
GPIO.setmode(GPIO.BCM)
pins = [23,24,25,8,7,12,26] #LED pins
for i in pins:
    GPIO.setup(i, GPIO.OUT)
p = GPIO.PWM(23,100) #setting up PWM
w = GPIO.PWM(24,100)
m = GPIO.PWM(25,100)
pp = GPIO.PWM(8,100)
ww = GPIO.PWM(7,100)
mm = GPIO.PWM(12,100)
ppp = GPIO.PWM(26,100)
p.start(0)
w.start(0)
m.start(0)
pp.start(0)
ww.start(0)
mm.start(0)
ppp.start(0)
#motor 1
GPIO.setup(16,GPIO.OUT) #A1
GPIO.setup(17,GPIO.OUT) #A2
GPIO.setup(19,GPIO.OUT) #B1
GPIO.setup(18,GPIO.OUT) #B2
GPIO.setup(3,GPIO.OUT) #sleep
p1 = GPIO.PWM(16,50) #A1
ppp1 = GPIO.PWM(17,50) #A2
pp1 = GPIO.PWM(19,50) #B1
pppp1 = GPIO.PWM(18,50) #B2
GPIO.output(3,GPIO.HIGH)
p1.start(0)
pp1.start(0)
ppp1.start(0)
pppp1.start(0)
#motor 2
GPIO.setup(13,GPIO.OUT) #A1
GPIO.setup(6,GPIO.OUT) #A2
GPIO.setup(4,GPIO.OUT) #B1
GPIO.setup(5,GPIO.OUT) #B2
GPIO.setup(2,GPIO.OUT) #sleep
p2 = GPIO.PWM(13,50) #A1
ppp2 = GPIO.PWM(6,50) #A2
pp2 = GPIO.PWM(4,50) #B1
pppp2 = GPIO.PWM(5,50) #B2
GPIO.output(2,GPIO.HIGH)
p2.start(0)
pp2.start(0)
ppp2.start(0)
pppp2.start(0)

async def speeder():
    while True:
        if int(globy.speed)>0:
            sped = 100/int(globy.speed) * 0.02
            p.ChangeDutyCycle((i*4)%70)
            w.ChangeDutyCycle(((i*4+20))%70)
            m.ChangeDutyCycle(((i*4+40))%70)
            pp.ChangeDutyCycle((i*4)%70)
            ww.ChangeDutyCycle(((i*4+20))%70)
            mm.ChangeDutyCycle(((i*4+40))%70)
            ppp.ChangeDutyCycle((i*4)%70)
            p1.ChangeDutyCycle(100) #1000
            p2.ChangeDutyCycle(100) #1000
            sleep(sped)
            pp1.ChangeDutyCycle(100) #1100
            pp2.ChangeDutyCycle(100) #1100
            sleep(sped)
            p1.ChangeDutyCycle(0) #0100
            p2.ChangeDutyCycle(0) #0100
            sleep(sped)
            ppp1.ChangeDutyCycle(100) #0110
            ppp2.ChangeDutyCycle(100) #0110
            sleep(sped)
            pp1.ChangeDutyCycle(0) #0010
            pp2.ChangeDutyCycle(0) #0010
            sleep(sped)
            pppp1.ChangeDutyCycle(100) #0011
            pppp2.ChangeDutyCycle(100) #0011
            sleep(sped)
            ppp1.ChangeDutyCycle(0) #0001
            ppp2.ChangeDutyCycle(0) #0001
            sleep(sped)
            p1.ChangeDutyCycle(100) #1001
            p2.ChangeDutyCycle(100) #1001
            sleep(sped)
            pppp1.ChangeDutyCycle(0) #1000
            pppp2.ChangeDutyCycle(0) #1000
            sleep(sped)
            await asyncio.sleep(0.1)
        elif int(globy.speed) == 0:
            p.ChangeDutyCycle((i*4)%70)
            w.ChangeDutyCycle(((i*4+20))%70)
            m.ChangeDutyCycle(((i*4+40))%70)
            pp.ChangeDutyCycle((i*4)%70)
            ww.ChangeDutyCycle(((i*4+20))%70)
            mm.ChangeDutyCycle(((i*4+40))%70)
            ppp.ChangeDutyCycle((i*4)%70)
            await asyncio.sleep(0.1)
        elif int(globy.speed) < 0:
            sped = -100/int(globy.speed) * 0.02
            p.ChangeDutyCycle((i*4)%70)
            w.ChangeDutyCycle(((i*4+20))%70)
            m.ChangeDutyCycle(((i*4+40))%70)
            pp.ChangeDutyCycle((i*4)%70)
            ww.ChangeDutyCycle(((i*4+20))%70)
            mm.ChangeDutyCycle(((i*4+40))%70)
            ppp.ChangeDutyCycle((i*4)%70)
            p1.ChangeDutyCycle(100) #1000
            p2.ChangeDutyCycle(100) #1000
            sleep(sped)
            p1.ChangeDutyCycle(100) #1001
            p2.ChangeDutyCycle(100) #1001
            sleep(sped)
            ppp1.ChangeDutyCycle(0) #0001
            ppp2.ChangeDutyCycle(0) #0001
            sleep(sped)
            pppp1.ChangeDutyCycle(100) #0011
            pppp2.ChangeDutyCycle(100) #0011
            sleep(sped)
            pp1.ChangeDutyCycle(0) #0010
            pp2.ChangeDutyCycle(0) #0010
            sleep(sped)
            ppp1.ChangeDutyCycle(100) #0110
            ppp2.ChangeDutyCycle(100) #0110
            sleep(sped)
            p1.ChangeDutyCycle(0) #0100
            p2.ChangeDutyCycle(0) #0100
            sleep(sped)
            pp1.ChangeDutyCycle(100) #1100
            pp2.ChangeDutyCycle(100) #1100
            sleep(sped)
            pppp1.ChangeDutyCycle(0) #1000
            pppp2.ChangeDutyCycle(0) #1000
            sleep(sped)
            await asyncio.sleep(0.1)

async def take_photo():
    while True:
        if globy.camera_snap:
                camera = PiCamera()
                camera.start_preview()
                img = '/home/candy/Desktop/image'+str(globy.picnum)+'.jpg'
                camera.capture(img)
                globy.picnum+=1
                camera.stop_preview
                globy.camera_snap = False
                await asyncio.sleep(0.1)

async def take_video():
    while True:
        if globy.camera_video:
            camera = PiCamera()
            camera.start_preview()
            vid = '/home/candy/Desktop/video'+str(globy.vidnum)+'.h264'
            camera.start_recording(vid)
            globy.vidnum+=1
            sleep(globy.vid)
            camera.stop_recording()
            camera.stop_preview()
            await asyncio.sleep(0.1)

if __name__ == '__main__':
    #async package that contains both concurrent tasks
    async def mainThread():
        app = MyApp()
        a = asyncio.create_task(app.base())
        b = asyncio.create_task(speeder())
        c = asyncio.create_task(take_photo())
        d = asyncio.create_task(take_video())
        (done,pending) = await asyncio.wait({a}, return_when='FIRST_COMPLETED')
    #running the concurrent package
    asyncio.run(mainThread())
    p.stop()
    w.stop()
    m.stop()
    pp.stop()
    ww.stop()
    mm.stop()
    ppp.stop()
    p1.stop()
    pp1.stop()
    ppp1.stop()
    pppp1.stop()
    p2.stop()
    pp2.stop()
    ppp2.stop()
    pppp2.stop()
    GPIO.cleanup()

