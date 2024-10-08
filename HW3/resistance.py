import numpy as np
import matplotlib.pyplot as plt

# Given values
r1 = 0.0263  # meters
r2 = 0.0302  # meters
r3 = 0.0429 # meters
h_in = 27 # W/ m^2 K
h_out = 5 # W/ m^2 K
kins = 0.03 # W/mK
kss = 13.4 # W/mK
Tin = 270.15 #K
Tout = 298.15 #K

rh1 = 1/(2* np.pi * h_in * r1)
rc1 = np.log(r2/r1) / (2* np.pi * kss)
rc2 = np.log(r3/r2) / (2* np.pi * kins)
rh2 = 1/ (2* np.pi * h_out * r3)

R_total = rh1 + rc1 + rc2+ rh2

Q = (Tin -Tout) / R_total

print (f"R inside convection: {rh1} (mK/W)")
print (f"R stainless steel conduction: {rc1} (mK/W)")
print (f"R insulation conduction: {rc2} (mK/W)")
print (f"R outside convection: {rh2} (mK/W)")
print()
print (f"R total {R_total} (mK/W)")
print (f"Q Total {Q} (W/m)")

TS3 = Q * (rh2) + Tout
TS2 = Q * (rc2 + rh2) + Tout
TS1 = Q * (rc1 + rc2 +rh2) + Tout
TS3 = np.round(TS3, 3)
TS2 = np.round(TS2, 3)
TS1 = np.round(TS1, 3)

print(f"Temperature Surface 3: {TS3} K or {np.round(TS3 -273.15, 3)} deg C")
print(f"Temperature Surface 2: {TS2} K or {np.round(TS2 -273.15, 3) } deg C")
print(f"Temperature Surface 1: {TS1} K or {np.round(TS1 -273.15,3) } deg C")




