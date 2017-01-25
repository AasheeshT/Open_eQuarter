# coding: utf8
# OeQ autogenerated lookup function for 'U-Values of Walls in correlation to year of construction, based on the source data of the survey for the "German Building Typology developed by the "Institut für Wohnen und Umwelt", Darmstadt/Germany, 2011-2013'

import math
import numpy as np
import oeqLookuptable as oeq
def get(*xin):


    l_lookup = oeq.lookuptable(
[0,1.85,
1849,1.85,
1850,1.85,
1851,1.85,
1852,1.85,
1853,1.85,
1854,1.85,
1855,1.85,
1856,1.848,
1857,1.846,
1858,1.843,
1859,1.84,
1860,1.837,
1861,1.834,
1862,1.832,
1863,1.83,
1864,1.829,
1865,1.829,
1866,1.83,
1867,1.83,
1868,1.83,
1869,1.83,
1870,1.83,
1871,1.83,
1872,1.83,
1873,1.83,
1874,1.83,
1875,1.83,
1876,1.83,
1877,1.83,
1878,1.83,
1879,1.83,
1880,1.83,
1881,1.83,
1882,1.83,
1883,1.83,
1884,1.83,
1885,1.83,
1886,1.83,
1887,1.83,
1888,1.83,
1889,1.83,
1890,1.83,
1891,1.83,
1892,1.83,
1893,1.83,
1894,1.83,
1895,1.83,
1896,1.83,
1897,1.83,
1898,1.83,
1899,1.83,
1900,1.83,
1901,1.83,
1902,1.83,
1903,1.83,
1904,1.83,
1905,1.831,
1906,1.831,
1907,1.83,
1908,1.829,
1909,1.828,
1910,1.828,
1911,1.83,
1912,1.834,
1913,1.837,
1914,1.837,
1915,1.83,
1916,1.814,
1917,1.79,
1918,1.761,
1919,1.73,
1920,1.699,
1921,1.67,
1922,1.646,
1923,1.63,
1924,1.623,
1925,1.623,
1926,1.626,
1927,1.63,
1928,1.632,
1929,1.632,
1930,1.631,
1931,1.63,
1932,1.63,
1933,1.63,
1934,1.63,
1935,1.63,
1936,1.63,
1937,1.629,
1938,1.629,
1939,1.63,
1940,1.632,
1941,1.634,
1942,1.634,
1943,1.63,
1944,1.62,
1945,1.604,
1946,1.579,
1947,1.546,
1948,1.503,
1949,1.451,
1950,1.393,
1951,1.337,
1952,1.287,
1953,1.25,
1954,1.229,
1955,1.221,
1956,1.218,
1957,1.215,
1958,1.207,
1959,1.196,
1960,1.186,
1961,1.18,
1962,1.181,
1963,1.185,
1964,1.187,
1965,1.18,
1966,1.161,
1967,1.131,
1968,1.095,
1969,1.055,
1970,1.015,
1971,0.979,
1972,0.949,
1973,0.93,
1974,0.923,
1975,0.924,
1976,0.928,
1977,0.93,
1978,0.924,
1979,0.907,
1980,0.877,
1981,0.83,
1982,0.766,
1983,0.695,
1984,0.629,
1985,0.58,
1986,0.557,
1987,0.555,
1988,0.566,
1989,0.58,
1990,0.59,
1991,0.595,
1992,0.592,
1993,0.58,
1994,0.559,
1995,0.533,
1996,0.505,
1997,0.48,
1998,0.461,
1999,0.446,
2000,0.434,
2001,0.42,
2002,0.404,
2003,0.387,
2004,0.371,
2005,0.36,
2006,0.36,
2007,0.36,
2008,0.36,
2009,0.36,
2010,0.361,
2011,0.361,
2012,0.361,
2013,0.36,
2014,0.36,
2015,0.36,
2016,0.36,
2017,0.36,
2018,0.36,
2019,0.36,
2020,0.36,
2021,0.36,
10000,0.2])
    return(l_lookup.lookup(xin))
