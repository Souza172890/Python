larg = float(input('Digite a largura da parede: '))
alt = float(input('Digite a altura da parede: '))
área = larg*alt
print('Sua parede tem dimenssão de {} x {} e sua área é de {}m².'.format(larg,alt,área))
tinta = área/2
print('Para pintar essa parede, você precisará de {}L de tinta'.format(tinta))
