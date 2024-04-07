import os
import pathlib
import numpy as np
import cv2
from PIL import Image
import RPi.GPIO as GPIO          
from time import sleep
import argparse
from pycoral.adapters.common import input_size
from pycoral.adapters.detect import get_objects
from pycoral.utils.dataset import read_label_file
from pycoral.utils.edgetpu import make_interpreter
from pycoral.utils.edgetpu import run_inference
import re
from pycoral.adapters import common
from pycoral.adapters import classify
import car

way = car.fn_fight()

result = ""
prescore = 0.0
GPIO.cleanup()
in1 = 24
in2 = 23
in3 = 16
in4 = 20
en1 = 25
en2 = 21
temp1=1
GPIO.setmode(GPIO.BCM)
GPIO.setup(in1,GPIO.OUT)
GPIO.setup(in2,GPIO.OUT)
GPIO.setup(in3,GPIO.OUT)
GPIO.setup(in4,GPIO.OUT)
GPIO.setup(en1,GPIO.OUT)
GPIO.setup(en2,GPIO.OUT)
GPIO.output(in1,GPIO.LOW)
GPIO.output(in2,GPIO.LOW)
GPIO.output(in3,GPIO.LOW)
GPIO.output(in4,GPIO.LOW)
p1=GPIO.PWM(en1,100)
p2=GPIO.PWM(en2,100)
p1.start(25)
p2.start(21)
num = 0

class motor:
  def forward():
    GPIO.output(in1, GPIO.HIGH)
    GPIO.output(in3, GPIO.HIGH)
    GPIO.output(in2, GPIO.LOW)
    GPIO.output(in4, GPIO.LOW)

  def lturn():
    GPIO.output(in1, GPIO.HIGH)
    GPIO.output(in3, GPIO.LOW)
    GPIO.output(in2, GPIO.LOW)
    GPIO.output(in4, GPIO.LOW)

  def rturn():
    GPIO.output(in1, GPIO.LOW)
    GPIO.output(in3, GPIO.HIGH)
    GPIO.output(in2, GPIO.LOW)
    GPIO.output(in4, GPIO.LOW)

  def stop():
    GPIO.output(in1, GPIO.LOW)
    GPIO.output(in3, GPIO.LOW)
    GPIO.output(in2, GPIO.LOW)
    GPIO.output(in4, GPIO.LOW)


default_model_dir = pathlib.Path(__file__).parent.absolute()


modelPath = os.path.join(default_model_dir, 'model_edgetpu.tflite')


labelPath = os.path.join(default_model_dir, 'labels.txt')


def classifyImage(interpreter, image):
    size = common.input_size(interpreter)
    common.set_input(interpreter, cv2.resize(image, size, fx=0, fy=0,
                                             interpolation=cv2.INTER_CUBIC))
    interpreter.invoke()
    return classify.get_classes(interpreter)

def main():
    global result, prescore, num

    interpreter = make_interpreter(modelPath)
    interpreter.allocate_tensors()
    labels = read_label_file(labelPath)

    cap = cv2.VideoCapture(0)
    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break

        #frame = cv2.flip(frame, 1)

        results = classifyImage(interpreter, frame)
        cv2.imshow('frame', frame)
        print(f'Label: {labels[results[0].id]}, Score: {results[0].score}')
        if results[0].score > prescore:
            prescore = results[0].score
        if labels[results[0].id] != result:
            prescore = 0.0
            motor.stop()
            sleep(0.5)
            if labels[results[0].id] != result:
                result = labels[results[0].id]
                num = num+1
                if result == "Forward":
                    print("Foward")
                    motor.forward()
                elif result == "Turn":
                  if num < len(way):
                    if way[num] == "➝":
                      motor.rturn()
                      print("Right turn")
                    elif way[num] == "←":
                      print("Left turn")
                      motor.lturn()
                elif result == "Round":
                    print("Round")
                else:
                    motor.stop()

            
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()
    
if __name__ == '__main__':
    main()
