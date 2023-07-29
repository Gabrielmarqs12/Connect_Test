from lib import procedure as prc

freq = str(input('Select a frequency: '))

who, stts = prc.frequency_select(freq)
print(stts)
print(who)

