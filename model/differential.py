# model/differential.py

import math


class DifferentialDrive:
    def __init__(self, x=0.0, y=0.0, theta=0.0):
        """
        x, y    : posisi robot
        theta   : orientasi (rad)
        """
        self.x = x
        self.y = y
        self.theta = theta

    def step(self, v, omega, dt):
        """
        Update posisi robot berdasarkan model kinematika

        v     : kecepatan linear
        omega : kecepatan sudut
        dt    : timestep
        """

        self.x += v * math.cos(self.theta) * dt
        self.y += v * math.sin(self.theta) * dt
        self.theta += omega * dt

        # Normalisasi sudut
        self.theta = self.normalize_angle(self.theta)

    @staticmethod
    def normalize_angle(angle):
        while angle > math.pi:
            angle -= 2 * math.pi
        while angle < -math.pi:
            angle += 2 * math.pi
        return angle

    def pose(self):
        """
        Return pose robot
        """
        return self.x, self.y, self.theta
