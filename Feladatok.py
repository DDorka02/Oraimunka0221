#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile

class Feladatok():

    def __init__(self):
        self.ev3 = EV3Brick()
        self.jm = Motor(Port.B)
        self.bm = Motor(Port.C)
        self.km = Motor(Port.A)
        self.cs = ColorSensor(Port.S3)
        self.ts = TouchSensor(Port.S1)
        self.gs = GyroSensor(Port.S2)
        self.us = UltrasonicsSensor(Port.S4)

        self.robot = DriveBase(self.jm,self.bm,55,115) 

    def elsoFeladat(self):
        self.robot.straight(300)

    def masodikFeladat(self):
        self.robot.turn(90)

    def harmadikFeladat(self):
        ut = 100
        fordul = 90
        self.robot.straight(ut)
        self.robot.straight(ut*(-1))
        self.robot.turn(fordul)
        self.robot.turn(-1*fordul)


    def csipog(self):
        self.ev3.speaker.beep()