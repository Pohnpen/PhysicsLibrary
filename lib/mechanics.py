"""
Mechanic equations
https://physics.info/equations/#eq-mechanics
"""

from constants import STANDARD_EARTH_GRAVITY


def weight(mass, gravity=STANDARD_EARTH_GRAVITY):
    """
    https://physics.info/weight/

    :param mass in kg
    :param gravity in m/s²
    :return: weight in Newton (N)
    """
    if type(mass) not in [int, float] or type(gravity) not in [int, float]:
        raise TypeError("Use int or float!")
    return mass * gravity


def velocity(delta_displacement, delta_time):
    """
    https://physics.info/velocity/

    :param delta_displacement: in meters
    :param delta_time: in second
    :return: velocity in meters per second
    """
    if type(delta_displacement) not in [int, float] or type(delta_time) not in [int, float]:
        raise TypeError("Use int or float!")
    return delta_displacement / delta_time

def acceleration(delta_velocity, delta_time):
    """
    https://physics.info/acceleration/
    :param delta_velocity: in m/s
    :param delta_time: in seconds
    :return: acceleration in m/s²
    """
    if type(delta_velocity) not in [int, float] or type(delta_time) not in [int, float]:
        raise TypeError("Use int or float!")
    return delta_velocity / delta_time

def newton_second(mass, acceleration):
    """
    https://physics.info/newton-second/
    :param mass in kg
    :param acceleration in m/s²
    :return: Force in Newton
    """
    if type(mass) not in [int, float] or type(acceleration) not in [int, float]:
        raise TypeError("Use int or float!")
    return mass * acceleration

def momentum(mass, velocity):
    """
    https://physics.info/momentum/
    :param mass in kg
    :param velocity: in m/s
    :return: momentum in kg*m/s
    """
    if type(mass) not in [int, float] or type(velocity) not in [int, float]:
        raise TypeError("Use int ot float!")
    return mass * velocity

def kinetic_energy(mass, velocity):
    """
    https://physics.info/energy-kinetic/
    :param mass in kg
    ;param velocity in m/s
    :return: kinetic_energy in Joules
    """
    if type(mass) not in [int, float] or type(velocity) not in [int, float]:
        raise TypeError("Use int or float!")
    return (0.5) * mass * velocity**2

def density(mass, Volume):
    """
    https://physics.info/density/
    :param mass in kg
    :param Volume in m**3
    :return: density in kg/m**3
    """
    if type(mass) not in [int, float] or type(Volume) not in [int, float]:
        raise TypeError("Use int or float!")
    return mass / Volume

def pressure(Force, area):
    """
    https://physics.info/pressure/
    :param Force in Newton
    :param area in m**2
    :return: pressure in pascal
    """
    if type(Force) not in [int, float] or type(area) not in [int, float]:
        raise TypeError("Use int or float!")
    return Force / area
