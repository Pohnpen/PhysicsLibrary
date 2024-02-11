"""
Thermal Physics equations
https://physics.info/equations/#eq-thermal
"""

def heat_evolved(mass, specific_heat_capacity, temperature_change):
    """
    https://physics.info/heat-sensible/

    :param mass in kg
    :param specific_heat_capacity in J/kg K
    :param temperature_change in K
    :return heat_evolved in J
    """
    if type(mass) not in [int, float] or type(specific_heat_capacity) not in [int, float] or type(temperature_change) in [int, float]:
        raise TypeError("Use int or float!")
    return mass * specific_heat_capacity * temperature_change

def latent_heat(mass, L):
    """
    https://physics.info/heat-sensible/

    :param mass in kg
    :param L in kJ/kg
    :return latent_heat in J
    """
    return mass * L


def ideal_gas_law(n,R,T):
    """
    https://physics.info/gas-laws/

    :param n
    :param R
    :param T
    :return PV
    """
    return n*R*T

def molecular_constants(N, k):
    """
    https://physics.info/gas-laws/

    :param N
    :param k
    :return nR
    """
    return N * k

def molecular_speeds_v_rms(k,T,m):
    """
    https://physics.info/gas-laws/
    :param k
    :param T
    :param m
    :return v_rms
    """
    return ((3*k*T) / m)**(0.5)

def molecular_speeds_vp(k,T,m):
    """
    https://physics.info/gas-laws/
    :param k
    :param T
    :param m
    :return v_vp
    """
    return ((2*k*T) / m)**(0.5)

def molecular_speeds_v(k,T,m):
    """
    https://physics.info/gas-laws/
    :param k
    :param T
    :param m
    :return v
    """
    return ((8*k*T) / m)**(0.5)
