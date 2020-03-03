delta_t = 1
cycles = 25
larvae = [980000]
young_juveniles = [92]
juveniles = [47]
reproducing = [56]
mature = [250]

#Larvae
larvae_birth_rate = 17500
larvae_death_rate = 0.999
larvae_growth_rate = 1

#Young juveniles
larvae_growth_rate = 1
young_juveniles_growth_rate = 0.0909
young_juveniles_death_rate = 0.0484


#Juveniles (start to be caught)
young_juveniles_growth_rate = 0.0909
juveniles_growth_rate = 0.0833
juveniles_death_rate = 0.0484
fishing_rate = 0

#Reproducing
juveniles_growth_rate = 0.0833
reproducing_death_rate = 0.0484
reproducing_growth_rate = 0.0625
fishing_rate = 0

#Mature
reproducing_growth_rate = 0.0625
mature_death_rate = 0.0484
fishing_rate = 0

#Iterative for loop
for t in range(0, cycles):
    updated_larvae = larvae[t] + (larvae_birth_rate)*(reproducing[t])*(delta_t) - (larvae_death_rate)*(larvae[t])*(delta_t) - (larvae_growth_rate)*(larvae[t])*(delta_t)
    updated_young_juveniles = young_juveniles[t] + (larvae_growth_rate)*(larvae[t])*(delta_t) - (young_juveniles_death_rate)*(young_juveniles[t])*(delta_t) - (young_juveniles_growth_rate)*(young_juveniles[t])*(delta_t)
    updated_juveniles = juveniles[t] + (young_juveniles_growth_rate)*(young_juveniles[t])*(delta_t) - (juveniles_death_rate)*(juveniles[t])*(delta_t) - (juveniles_growth_rate)*(juveniles[t])*(delta_t) - (fishing_rate)*(juveniles[t])*(delta_t)
    updated_reproducing = reproducing[t] + (juveniles_growth_rate)*(juveniles[t])*(delta_t) - (reproducing_death_rate)*(reproducing[t])*(delta_t) - (reproducing_growth_rate)*(reproducing[t])*(delta_t) - (fishing_rate)*(reproducing[t])*(delta_t)
    updated_mature = mature[t] + (reproducing_growth_rate)*(reproducing[t])*(delta_t) - (mature_death_rate)*(mature[t])*(delta_t) - (fishing_rate)*(mature[t])*(delta_t)
    larvae.append(updated_larvae)
    young_juveniles.append(updated_young_juveniles)
    juveniles.append(updated_juveniles)
    reproducing.append(updated_reproducing)
    mature.append(updated_mature)



import matplotlib.pyplot as plt
time_points = range(cycles + 1)
plt.plot(time_points, larvae, 'b')  
plt.plot(time_points, young_juveniles, 'r')
plt.plot(time_points, juveniles, 'g')
plt.plot(time_points, reproducing, 'm')
plt.plot(time_points, mature, 'c')
plt.xlabel('Time (each increment representing 0.25 years)')
plt.ylabel('Population (in millions)')
plt.show()
