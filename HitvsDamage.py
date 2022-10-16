import numpy as np
import matplotlib.pyplot as plt

iters = 100000

ACs = [i for i in range(10, 28)]
attackHits = [[] for i in range(len(ACs))]
damageHits = [[] for i in range(len(ACs))]

proficiencyScore = 3
abilityScore = 3

for i in range(iters):
    baseHit = np.random.randint(1, 21) + proficiencyScore + abilityScore
    baseDamage = np.random.randint(1, 9) + proficiencyScore
    bonusHit = baseHit + 1
    bonusDamage = baseDamage + 1
    for i in range(len(ACs)):
        #Calculate hit for damage bonus attack
        if baseHit > ACs[i]:
            damageHits[i].append(bonusDamage)
        if bonusHit > ACs[i]:
            #Calculate hit for attack bonus attack
            attackHits[i].append(baseDamage)

attackSum = list(map(np.sum, attackHits))
damageSum = list(map(np.sum, damageHits))

ind = np.arange(len(ACs))
width = 0.35
fig, ax = plt.subplots()
rects1 = ax.bar(ind, attackSum, width, color='g')
rects2 = ax.bar(ind+width, damageSum, width, color='r')
ax.set_xlabel('Target AC')
ax.set_ylabel(f'Cumulative Damage After {iters} Attacks')
ax.set_title('Comparison of Attack and Damage Bonuses')
ax.set_xticks(ind+width/2)
ax.set_xticklabels(ACs)
ax.ticklabel_format(style='plain', axis='y')
ax.legend((rects1[0], rects2[0]), ('Attack Bonus', 'Damage Bonus'))

plt.show()