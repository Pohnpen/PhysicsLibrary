ALLOWED_ARG_TYPES = [int, float, complex]

STANDARD_EARTH_GRAVITY = 9.80665 # m/s²

SPECIFIC_HEAT_CAPACITY_STANDARDIZED_WATER_0_DEGREE = 4217.6 # specific heat capacity standardized water, liquid, 0 °C (J/kg K) https://physics.info/heat-sensible/
SPECIFIC_LATENT_HEAT_STANDARDIZED_WATER_0_DEGREE = 334 # specific latent heat standardized to water 0 degree (kJ/kg) https://physics.info/heat-latent/
GAS_CONSTANT = 8.314462618 # gas constant(J/mol K) https://physics.info/gas-laws/
BOLTZMANN_CONSTANT = 1.380649*(10**-23) # Boltz­mann constant (J/K) https://physics.info/gas-laws/


PREFIX = {
    # More prefix needed
    "nano": {
        "symbol": "n",
        "factor": 10**-9
    },
    "micro": {
        "symbol": "mu",
        "factor": 10**-6
    },
    "milli": {"symbol": "m", "factor": 10**-3},
    "centi": {"symbol": "c", "factor": 10**-2},
    "normal": {"symbol": "", "factor": 10**0},
    "kilo": {"symbol": "k", "factor": 10**3},
    "mega": {"symbol": "M", "factor": 10**6},
    "giga": {"symbol": "G", "factor": 10**9}
}
