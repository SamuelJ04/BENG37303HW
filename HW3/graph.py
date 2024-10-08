import numpy as np
import matplotlib.pyplot as plt

# Given values
T1 = 350  # K
T2 = 300  # K
r1 = 0.05  # meters
r2 = 0.15  # meters

# Define the range of r between r1 and r2
r_values = np.linspace(r1, r2, 100)

# First form of T(r)
T_r_form1 = (T1 - T2) / np.log(r1 / r2) * np.log(r_values / r2) + T2

# Second form of T(r)
T_r_form2 = (T2 - T1) / np.log(r2 / r1) * np.log(r_values / r1) + T1

# Plotting
plt.figure(figsize=(8,6))
plt.plot(r_values, T_r_form1, label="Form 1: T(r)", linestyle='-', color='blue')
plt.plot(r_values, T_r_form2, label="Form 2: T(r)", linestyle='--', color='red')
plt.xlabel("Radius (r) [m]")
plt.ylabel("Temperature (T) [K]")
plt.title("Comparison of T(r) from Both Forms")
plt.legend()
plt.grid(True)

# Show the plot
plt.show()
