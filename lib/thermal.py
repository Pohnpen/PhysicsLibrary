"""
Thermal Physics equations
https://physics.info/equations/#eq-thermal
"""
from constants.py import (
SPECIFIC_LATENT_HEAT_STANDARDIZED_WATER_0_DEGREE,
SPECIFIC_HEAT_CAPACITY_STANDARDIZED_WATER_0_DEGREE,
GAS_CONSTANT, BOLTZMANN_CONSTANT
)

def heat_evolved(mass, temperature_change, c = SPECIFIC_HEAT_CAPACITY_STANDARDIZED_WATER_0_DEGREE):
    """
    https://physics.info/heat-sensible/

    :param mass in kg
    :param c in J/kg K "SPECIFIC_HEAT_CAPACITY_STANDARDIZED_WATER_0_DEGREE"
    :param temperature_change in K
    :return heat_evolved in J
    """
    if type(mass) not in [int, float] or type(specific_heat_capacity) not in [int, float] or type(temperature_change) in [int, float]:
        raise TypeError("Use int or float!")
    return mass * specific_heat_capacity * temperature_change

def latent_heat(mass, L = SPECIFIC_LATENT_HEAT_STANDARDIZED_WATER_0_DEGREE):
    """
    https://physics.info/heat-sensible/

    :param mass in kg
    :param L in kJ/kg "SPECIFIC_LATENT_HEAT_STANDARDIZED_WATER_0_DEGREE"
    :return latent_heat in J
    """
    return mass * L


def ideal_gas_law(number_of_moles, absolute_temperature, R = GAS_CONSTANT):
    """
    https://physics.info/gas-laws/

    :param  number_of_moles
    :param GAS_CONSTANT in J/mol K
    :param absolute_temperature in K
    :return PV (absolute pressure * volume)
    """
    return number_of_moles * absolute_temperature * R

def molecular_constants(number_of_particles, k = BOLTZMANN_CONSTANT):
    """
    https://physics.info/gas-laws/

    :param number of particles
    :param k = BOLTZMANN_CONSTANT in J/K
    :return nR (number of moles * GAS_CONSTANT)
    """
    return number_of_particles * k

def molecular_speeds_v_rms(absolute_temperature, mass ,k = BOLTZMANN_CONSTANT):
    """
    https://physics.info/gas-laws/
    :param k = BOLTZMANN_CONSTANT in J/K
    :param absolute_temperature in K
    :param mass in kg
    :return v_rms in m/s
    """
    return ((3*k*absolute_temperature) / mass)**(0.5)

def molecular_speeds_vp(absolute_temperature,mass ,k = BOLTZMANN_CONSTANT):
    """
    https://physics.info/gas-laws/
    :param k = BOLTZMANN_CONSTANT in J/K
    :param absolute_temperature in K
    :param mass in kg
    :return v_vp in m/s
    """
    return ((2*k*absolute_temperature) / mass)**(0.5)

def molecular_speeds_v_avg(absolute_temperature,mass ,k = BOLTZMANN_CONSTANT):
    """
    https://physics.info/gas-laws/
    :param k = BOLTZMANN_CONSTANT in J/K
    :param absolute_temperature in K
    :param mass in kg
    :return v_avg (average velocity of gass)in m/s
    """
    return ((8*k*absolute_temperature) / mass)**(0.5)
