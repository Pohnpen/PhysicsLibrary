"""
Mechanic equations
https://physics.info/equations/#eq-mechanics
"""

from .constants import STANDARD_EARTH_GRAVITY, ALLOWED_ARG_TYPES


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
    if type(delta_displacement) not in ALLOWED_ARG_TYPES or type(delta_time) not in ALLOWED_ARG_TYPES:
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
    if not all( [ type(p) in ALLOWED_ARG_TYPES for p in [mass, acceleration] ] ):
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

def density(mass, volume):
    """
    https://physics.info/density/
    :param mass in kg
    :param volume in m**3
    :return: density in kg/m**3
    """
    if type(mass) not in [int, float] or type(volume) not in [int, float]:
        raise TypeError("Use int or float!")
    return mass / volume

def pressure(force, area):
    """
    https://physics.info/pressure/
    :param force in Newton
    :param area in m**2
    :return: pressure in pascal
    """
    if type(force) not in [int, float] or type(area) not in [int, float]:
        raise TypeError("Use int or float!")
    return force / area

"""
equations of motion formula
"""

def velocity_with_time(velocity_at_the_beginnig, acceleration, time):
    """
    https://physics.info/equations/#eq-mechanics
    :param velocity_at_the_beginnig in m/s
    :param acceleration in m/s**2
    :param time in s
    :return velocity_with_time in m/s
    """
    if type(velocity_at_the_beginnig) not in [int, float] or type(acceleration) not in [int, float] or type(time) not in [int, float]:
        raise TypeError("Use int or float!")
    return velocity_at_the_beginnig + (acceleration * time)

def displacement_with_acceleration(velocity_at_the_beginnig, acceleration, time):
    """
    https://physics.info/equations/#eq-mechanics
    :param velocity_at_the_beginnig in m/s
    :param acceleration in m/s**2
    :param time in s
    :return displacement_with_acceleration in meter
    """
    if type(velocity_at_the_beginnig) not in [int, float] or type(acceleration) not in [int, float] or type(time):
        raise TypeError("Use int or float!")
    return (velocity_at_the_beginnig * time) + ((0.5) * acceleration * time**2)

def velocity_without_time(velocity_at_the_beginnig, displacement, acceleration):
    """
    https://physics.info/equations/#eq-mechanics
    :param velocity_at_the_beginnig in m/s
    :param displacement in meter
    :param acceleration in m/s**2
    :return velocity_without_time in m/s
    """
    if type(velocity_at_the_beginnig) not in [int, float] or type(displacement) not in [int, float] or type(acceleration) not in [int, float]:
        raise TypeError("Use int or float")
    return (velocity_at_the_beginnig**2) + (2 * acceleration * displacement)

def displacement_with_time(velocity_at_the_beginnig, velocity_at_the_end, time):
    """
    https://physics.info/equations/#eq-mechanics
    :param velocity_at_the_beginnig in m/s
    :param velocity_at_the_end in m/s
    :param time in s
    :return displacement_with_time in meter
    """
    if type(velocity_at_the_beginnig) not in [int, float] or type(velocity_at_the_end) not in [int, float] or type(time) not in [int, float]:
        raise TypeError("Use int or float")
    return ((velocity_at_the_beginnig + velocity_at_the_end)*(0.5) / 2)
