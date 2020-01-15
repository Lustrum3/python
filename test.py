#!/usr/bin/env python
#coding:UTF-8
import sys
import time

reload(sys)
sys.setdefaultencoding('utf8')

import pyttsx3
engine = pyttsx3.init()

engine.setProperty('voice','zh')

i =0
while(i<10):
	engine.say('hello word!')
	engine.say('测试!')
	engine.say(i)
	print i
	engine.runAndWait()
	i+=1


engine.runAndWait()
engine.endLoop()

