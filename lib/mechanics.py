"""
Mechanic equations
https://physics.info/equations/#eq-mechanics
"""

from .constants import STANDARD_EARTH_GRAVITY


def weight(mass, gravity=STANDARD_EARTH_GRAVITY):
    """
    https://physics.info/weight/

    :param mass in kg
    :param gravity in m/s²
    :return: weight in Newton (N)
    """
    return mass * gravity


def velocity(delta_speed, delta_time):
    """
    https://physics.info/velocity/

    :param delta_speed: in meters
    :param delta_time: in second
    :return: velocity in meters per second
    """
    pass

def acceleration(delta_velocity, delta_time):
    """
    https://physics.info/acceleration/
    :param delta_velocity: in m/s
    :param delta_time: in seconds
    :return: acceleration in m/s²
    """
    pass

def newton_second():
    """
    https://physics.info/newton-second/
    :return:
    """
    pass

def momentum():
    """
    https://physics.info/momentum/
    :return:
    """
    pass

def kinetic_energy():
    """
    https://physics.info/energy-kinetic/
    :return:
    """
    pass

def density():
    """
    https://physics.info/density/
    :return:
    """

def pressure():
    """
    https://physics.info/pressure/
    :return:
    """