import matplotlib.pyplot as plt
import numpy as np


x = ['Mum-Oregon', 'Paris-SA','Canada-London','Ohio-Singapore' ]
y1 = [57.6,  56.8,  79.1,55.7 ]
y2 = [51.5, 39.5, 79.5 ,54.9]

plt.xlabel('Server - Client')
plt.ylabel('Bandwidth (Mbits/sec)')
plt.plot(x, y1, label = 'BBR' )
plt.plot(x, y2 , label = 'Cubic')
#plt.plot(x, y3, label = 'our approach local')
#plt.plot (x, y4 , label ='our approach remote')
plt.legend()
plt.show()


x = ['0%', '0.01%','0.1%','1%','10%' ]
y1 = [731, 724 , 664 ,  511,228 ]
y2 = [715, 456 , 20.8, 6.15 ,1.10]
#y3= [ 731, 679, 682, 675 ,666]
#y4 = [715,87 , 54 , 70.1, 26.2]
plt.xlabel('Loss Rate')
plt.ylabel('Bandwidth (Mbits/sec)')
plt.plot(x, y1, label = 'BBR - sender' )
plt.plot(x, y2 , label = 'Cubic - sender')
#plt.plot(x, y3, label = 'BBR - receiver')
#plt.plot (x, y4 , label ='Cubic-receiver')
plt.legend()
plt.show()

x = ['0%', '0.01%','0.1%','1%','10%' ]
#y1 = [731, 724 , 664 ,  511,228 ]
#y2 = [715, 456 , 20.8, 6.15 ,1.10]
y3= [ 731, 679, 682, 675 ,666]
y4 = [715,87 , 54 , 70.1, 26.2]
plt.xlabel('Loss Rate')
plt.ylabel('Bandwidth (Mbits/sec)')
#plt.plot(x, y1, label = 'BBR - sender' )
#plt.plot(x, y2 , label = 'Cubic - sender')
plt.plot(x, y3, label = 'BBR - receiver')
plt.plot (x, y4 , label ='Cubic-receiver')
plt.legend()
plt.show()


x = [10, 1770, 1780, 1790, 1800, 1810, 1820, 1830, 1840, 1850, 1860, 1870,1880, 1890, 1900 ,3590 ]
y1 = [126,126, 115, 115, 94.4, 73.4, 52.4, 73.4, 62.9, 52.4, 62.9, 62.9, 52.4, 62.9 , 62.9, 62.9]
#y2 = [715, 456 , 20.8, 6.15 ,1.10]
#y3= [ 731, 679, 682, 675 ,666]
#y4 = [715,87 , 54 , 70.1, 26.2]
plt.xlabel('Time (in seconds)')
plt.ylabel('Bandwidth (Mbits/sec)')
plt.plot(x, y1, label = 'BBR:Server:London, Client:Canada,Total Retires # = 383236' )
#plt.plot(x, y2 , label = 'Cubic - sender')
#plt.plot(x, y3, label = 'BBR - receiver')
#plt.plot (x, y4 , label ='Cubic-receiver')
plt.legend()
plt.show()

x = [10, 770, 780, 790,800, 810,820, 830,840,850, 3590]
y1 = [ 147, 147, 136, 147, 52.4, 52.4 , 62.9, 73.4, 52.4, 62.9, 62.9  ]
y2 = [83.9, 94.4, 147, 62.9, 73.4, 83.9, 73.4, 105, 52.4, 83.9, 73.4 ]
plt.xlabel('Time (in seconds)')
plt.ylabel('Bandwidth (Mbits/sec)')
plt.plot(x, y1, label = 'BBR:Server:London, Client:Canada, Total Retires # = 593791' )
plt.plot(x, y2, label = 'Cubic:Server:London, Client:Canada, Total Retires # = 35779' )
plt.legend()
plt.show()


x = [10, 770, 780, 790,800, 810,820, 830,840,850, 3590]
y1 = [ 147, 147, 136, 147, 52.4, 52.4 , 62.9, 73.4, 52.4, 62.9, 62.9  ]
#y2 = [715, 456 , 20.8, 6.15 ,1.10]
#y3= [ 731, 679, 682, 675 ,666]
#y4 = [715,87 , 54 , 70.1, 26.2]
plt.xlabel('Time (in seconds)')
plt.ylabel('Bandwidth (Mbits/sec)')
plt.plot(x, y1, label = 'Server:London, Client:Canada, Total Retires # = 593791' )
#plt.plot(x, y2 , label = 'Cubic - sender')
#plt.plot(x, y3, label = 'BBR - receiver')
#plt.plot (x, y4 , label ='Cubic-receiver')
plt.legend()
plt.show()


x = [10, 770, 780, 790,800, 810,820, 830,840,850, 3590]
y1 = [ 147, 147, 136, 147, 52.4, 52.4 , 62.9, 73.4, 52.4, 62.9, 62.9  ]
#y2 = [715, 456 , 20.8, 6.15 ,1.10]
#y3= [ 731, 679, 682, 675 ,666]
#y4 = [715,87 , 54 , 70.1, 26.2]
plt.xlabel('Time (in seconds)')
plt.ylabel('Bandwidth (Mbits/sec)')
plt.plot(x, y1, label = ' BBR:Server:London, Client:Canada, Total Retires # = 593791' )
#plt.plot(x, y2 , label = 'Cubic - sender')
#plt.plot(x, y3, label = 'BBR - receiver')
#plt.plot (x, y4 , label ='Cubic-receiver')
plt.legend()
plt.show()

