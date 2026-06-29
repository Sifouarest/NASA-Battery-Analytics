import scipy.io as sio
import matplotlib.pyplot as plt

# 1. Always reload the file fresh to clear any cached data pointers
data = sio.loadmat('B0005.mat')
battery_object = data['B0005'][0, 0]
all_cycles = battery_object['cycle'][0]

# 2. Hard-reset the lists to empty arrays every single time the script runs
capacities = []
cycle_numbers = []
discharge_count = 0

# 3. Look through the data
for cycle in all_cycles:
    cycle_type = cycle['type'][0]

    if cycle_type == 'discharge':
        discharge_count += 1

        # Extract the real float value
        cap_val = cycle['data'][0, 0]['Capacity'][0][0]

        # 🔍 DOUBLE CHECK THIS PART IN YOUR CODE:
        capacities.append(cap_val)  # Must be the capacity float!
        cycle_numbers.append(discharge_count)  # Must be the cycle integer count

print(f"Total points collected: {len(capacities)}")

# 4. Re-plot the true degradation physics
plt.figure(figsize=(10, 6))
plt.plot(cycle_numbers, capacities, 'r-', marker='o', markersize=4, label='Measured Capacity')
plt.axhline(y=1.4, color='b', linestyle='--', label='80% EOL Threshold (1.4 Ah)')

plt.title('NASA B0005 Battery Capacity Degradation Curve')
plt.xlabel('Discharge Cycle Number')
plt.ylabel('Capacity (Ah)')
plt.grid(True)
plt.legend()
plt.show()
