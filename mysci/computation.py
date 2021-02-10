
import math

def compute_windchill(t, v):
    """
    Compute the windchill factor given the temperature and windspeed

    NOTE: This computation is valid only for temperatures between -45F and 45F
          and for wind speeds between 3 mph and 60 mph

    Parameters:
        t: the temperature in Fahrenheit
        v: the wind speed in miles per hour
    """

    a = 35.74
    b = 0.6215
    c = 35.75
    d = 0.4275

    v16 = v**0.16

    wci = a + (b*t) - (c*v16) + (d*t*v16)
    return wci


def compute_heatindex(t, hum):
    """
    Compute the heat index given the temperature and humidity

    Parameters:
        t: the temperature of units in F (float)
        hum:
    """

    a = -42.379
    b = 2.04901523
    c = 10.14333127
    d = 0.22475541
    e = 0.00683783
    f = 0.0481717
    g = 0.00122874
    h = 0.00085282
    i = 0.00000199

    rh = hum/100.

    hi = (a + (b * t) + (c * rh) + (d * t * rh) + (e * t**2) +
        (f * rh ** 2) + (g * t**2 * rh) + (h * t * rh**2) +
        (i * t**2 * rh**2))

    return hi


def compute_dewpoint(t,h):
    """
    Compute the dew point temperature given the temperature and humidity

    Parameters:
        t: the temperature in units of F (float)
        h: the relative humidity in units of % (float)
    """

     tempC  (t - 32)* 5/9  #convert temperature from deg F to deg C
     rh = h/100

     b = 18.678  # unitless
     c = 257.14  # deg C

     gamma = math.log(rh) + (b * tempC) /(c + tempC)

     tdp = c * gamma/(b - gamma)

     tdp_F = 9/5* tdp + 32  $ convert from C to F

     return tdp_F
