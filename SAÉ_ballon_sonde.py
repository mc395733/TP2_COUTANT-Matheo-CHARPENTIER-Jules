import csv
from matplotlib import pyplot as plt

def temp_altitude(f):
	alti=[]
	tint=[]
	text=[]
	with open(f,newline='',encoding="utf-8") as csvfile:
		reader=csv.reader(csvfile,delimiter=';')
		next(reader)
		for r in reader:
			if len(r)>=5:
				alti.append(float(r[3]))
				tint.append(float(r[5]))
				text.append(float(r[6]))
	return alti,tint,text

altitude,temp_int,temp_ext=temp_altitude("Donnees.csv")

plt.plot(temp_int,altitude)
plt.plot(temp_ext,altitude)
plt.title("Les Températures en fonction de l'altitude")
plt.xlabel("Température (°C)")
plt.ylabel("Altitude (m)")
plt.show()
