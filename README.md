# plantAvailableWater
Script for converting raw moisture (V) to PAW (in/ft)

AWC/PAW is the maximum amount of water that soil can store to be extracted by the plants. It is the water held between field capacity and permanent wilting point.

Run moisture.py to test. (Soil texture values stored in soil_tex)

This script shows steps for:
1) Converting raw volts to permitivitty 
2) Converting perm to VWC
3) Converting VWC to available water capacity (AWC) as decimal / percentage
4) Converting AWC to Plant Available Water (in/ft)


Notes

- raw moisture for 6in, 18in, 36in hardcoded in script, along with soil texture values. Replace these lines with api calls to Teralytic sensor and soils data

- soil texture coefs derived from: #https://extension.umn.edu/irrigation/basics-irrigation-scheduling#table-1.-available-water-capacity-%28awc%29-by-soil-texture.-1846610

