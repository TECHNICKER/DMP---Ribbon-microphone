from matplotlib import pyplot as plt
from scipy.interpolate import RectBivariateSpline
import numpy as np

angles = [0, 22.50, 45, 67.5, 90, 112.5, 135, 157.5, 180, 202.5, 225, 247.5, 270, 292.5, 315, 337.5, 360]
angles_ver = [0, 45, 90, 135, 180, 225, 270, 315, 360]
radians = np.deg2rad(angles)
radians_ver = np.deg2rad(angles_ver)

values_500 = [-45.8, -46.2, -47.9, -50.4, -58.3, -60, -52.9, -50.2, -49.9, -50.65, -52.75, -60, -57, -51.3, -47.5, -45.85, -45.8]
values_500_ver = [-46.25, -48.6, -63, -53.6, -49.7, -54.2, -55.95, -48.2, -45.65]
values_1000 = [-44.2, -45, -47.75, -52.15, -58.7, -50.45, -45.7, -43.85, -44.4, -45.65, -48.15, -59.5, -55.3, -51.3, -46.2, -43.25, -44.4] 
values_1000_ver = [-44.3, -47.65, -58, -45.85, -44.45, -49.55, -54.8, -46.85, -44.65]
values_4000 = [-47.65, -48.1, -48.85, -52.3, -63.5, -55.15, -50.8, -48.9, -48, -48.2, -50.6, -56.7, -64.5, -53.7, -50.4, -48.7, -48.5]
values_4000_ver = [-48.55, -50.7, -65.8, -51.4, -48.85, -51.1, -67.5, -49.85, -48.65]

polar = plt.subplot(1, 1, 1, projection="polar")
polar.set_theta_zero_location("N")
polar.set_theta_direction(-1)

# plt.plot(radians, values_500, color="red", label="500 Hz")
# plt.plot(radians_ver, values_500_ver, label="500 Hz ver.", linestyle=":", marker=".", markersize=10, markeredgecolor="black", color="orange")
plt.plot(radians, values_1000, color="blue", label="1000 Hz")
plt.plot(radians_ver, values_1000_ver, label="1000 Hz ver.", linestyle=":", marker=".", markersize=10, markeredgecolor="black", color="orange")
# plt.plot(radians, values_4000, color="green", label="4000 Hz")
# plt.plot(radians_ver, values_4000_ver, label="4000 Hzver. ")
plt.legend(bbox_to_anchor=(0.3, 0.065))


plt.show()