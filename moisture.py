import os
import json
import requests
from soil_tex import soilTex

########################
# define raw moisture (V)    
moistureRaw6 = 2.4
moistureRaw18 = 2.44
moistureRaw36 = 2.45
# convert raw moisture to permitivity 
def Perm(moistureRaw): 
    perm = 163+(-99.7*moistureRaw)+(14.9*(moistureRaw**2))+(0.216*(moistureRaw**3))
    return perm

## now convert permitivitty to VWC with Topp equation 
def VWC (perm):
    VWC = ((4.3 * 10**-6) * (perm**3)) - ((5.5 * (10**-4)) * (perm**2)) + (2.92 * (10**-2) * perm) - (5.3 * (10**-2))
    return VWC

perm6 = round(Perm(moistureRaw6),4)
perm18 = round(Perm(moistureRaw18),4)
perm36 = round(Perm(moistureRaw36),4)
print("Perm6:", perm6)
print("Perm18:", perm18)
print("Perm36:", perm36)
VWC6 = VWC(perm6)
VWC18 = VWC(perm18)
VWC36 = VWC(perm36)
print("VWC6:", VWC6)
print("VWC18:", VWC18)
print("VWC36:", VWC36)

# now bring in soil Texture (use carmack soils api for this)
soilTex6 = "Loamy fine sand"
soilTex18 = "Loamy fine sand"
soilTex36 = "Loamy fine sand"

#input texture return Field Capacity; Permanent wilting point, max plant available water, and coeff
soilTex6Props = soilTex(soilTex6)
soilTex18Props = soilTex(soilTex18)
soilTex36Props = soilTex(soilTex36)
FC6,PWP6,MPAW6,coef6 = soilTex6Props[0],soilTex6Props[1],soilTex6Props[2],soilTex6Props[3]
FC18,PWP18,MPAW18,coef18 = soilTex18Props[0],soilTex18Props[1],soilTex18Props[2],soilTex18Props[3]
FC36,PWP36,MPAW36,coef36 = soilTex36Props[0],soilTex36Props[1],soilTex36Props[2],soilTex36Props[3]

print("FC6:",FC6)
print("FC18:",FC18)
print("FC36:",FC36)
print("PWP6:",PWP6)
print("PWP18:",PWP18)
print("PWP36:",PWP36)
print("MPAW6:",MPAW6)
print("MPAW18:",MPAW18)
print("MPAW36:",MPAW36)

# management allowed defecit --> default 50%
MAD6,MAD18,MAD36 = MPAW6*0.5,MPAW18*0.5,MPAW36*0.5
#root  depth, constant for now (40cm)
rootDepth = 40.00
#management allowed lower limit of soil moisture -- don't go lower than this
MAL6 = FC6 - (MPAW6*MAD6)
MAL18 = FC18 - (MPAW18*MAD18)
MAL36 = FC36 - (MPAW36*MAD36)
# Available Water Capacity 
AWC6 = round((((VWC6*100)-MAL6)*rootDepth)/10000,2)
AWC18 = round((((VWC18*100)-MAL18)*rootDepth)/10000,2)
AWC36 = round((((VWC36*100)-MAL36)*rootDepth)/10000,2)
print("6in Soil Texture:",soilTex6)
print("18in Soil Texture:",soilTex18)
print("36in Soil Texture:",soilTex36)
print("6in AWC:",AWC6)
print("18in AWC:",AWC18)
print("36in AWC:",AWC36)
# convert to AWC (in/ft) -->soil texture coefs derived from:
#https://extension.umn.edu/irrigation/basics-irrigation-scheduling#table-1.-available-water-capacity-%28awc%29-by-soil-texture.-1846610
# AWC or the maximum amount of water that soil can store to be extracted by the plants. It is the water held between field capacity and permanent wilting point.
PAW6 = round(AWC6*coef6,2)
PAW18 = round(AWC18*coef18,2)
PAW36 = round(AWC36*coef36,2)
print("6in Plant Available Water (in/ft):",PAW6)
print("18in Plant Available Water (in/ft):",PAW18)
print("36in Plant Available Water (in/ft):",PAW36)


