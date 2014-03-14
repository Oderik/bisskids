from bottle import route, run, debug, template, request
import pyttsx
import thread
import time

@route('/say', method='GET')
def say():
    text = request.GET.get('text', '')
    thread.start_new_thread( say, (text, ) )    	
    return text

@route('/count', method='GET')
def count():
    limit = request.GET.get('limit', 10)

    engine.say("Go now!")
    engine.runAndWait()

    result = ""
    for number in range(1, int(limit) + 1):
        result += str(number) + ", "
	thread.start_new_thread( say, (number, ) )  
	time.sleep(1)
    return result

def say(text):
    if engine.isBusy():
	engine.stop()

    engine.say(text)
    engine.runAndWait()
	
engine = pyttsx.init()
run(port=8080)
