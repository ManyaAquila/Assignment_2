"""
PY1010_Høst 2026

Arbeidskrav 2

"""
#%% Oppgave 1

alder = int(input("Hvilket aar er du foedt?")) #  [Verdien til variabelen skrives inn i konsollen]

print("I loepet av aar 2024 blir du", 2024 - alder) # [Resultat ved fletting sammen tekst og variabelen]

 
#%% Oppgave 2

antall_elever = int(input("Skriv inn antall elever:")) #  [Antall elever skrives inn i konsollen]

totalt_pizzaer = antall_elever * 1/4 #  [Antall pizza som spiser hver elev]

avrundet = round(totalt_pizzaer) #  [Avrunding av antall pizza til heltall]

print(f"Antall pizzaer som skal kjoepes til festen er {avrundet}.")

#%% Oppgave 3

import numpy as np #  [Import av biblioteket]

v_grad = float(input("Skriv inn gradtallet:")) #  [Verdien av gradtallet skal skrives inn i konsollen]

v_rad = v_grad*np.pi/180 #  [Formellen til å beregne radiantallet til vinkelen]

print(f"Resultat ved omregning fra grader til radianer er {v_rad:.2f}.")

#%% Oppgave 4

# Del A. 

#  [Oppretting av dictionary]

data = {
    "Norge": ["Oslo", 0.634],
    "England": ["London", 8.982],
    "Frankrike": ["Paris", 2.161],
    "Italia": ["Roma", 2.873]
    }

# Del B. 

land = input("Skriv inn et land her: ") #  [Landet skal skrives inn i konsollen]

hovedstad = data[land][0] #  [Den 1.verdien]

befolkning = data[land][1] #  [Den 2.verdien]

print(hovedstad,"er hovedstaden i", land, "og det er", befolkning, " mill. innbyggere i", hovedstad)

# Del C.

#  [Dictionary]

data = {
    "Norge": ["Oslo", 0.634],
    "England": ["London", 8.982],
    "Frankrike": ["Paris", 2.161],
    "Italia": ["Roma", 2.873]
    }

#  [Oppdatering av informasjonen i ordboka]

land = input("Skriv inn nytt land her:") #  [Nytt land skal skrives i konsollen]
hovedstad = input(f"Skriv inn hovedstad til {land}:") #  [Hovedstaden av det "nye" landet]
befolkning = input(f"Skriv inn antall innbyggere til {hovedstad}:") #  [Antall innbyggere for det "nye" landet]

print(hovedstad,"er hovedstaden i", land, "og det er", befolkning, " mill. innbyggere i", hovedstad)

#%% Oppgave 5

import numpy as np #  [import av biblioteker]

import math

#  Forklaringer til omregning:
    
"""
Areal sirkel = pi*r^2
Omkrets sirkel = 2*pi*r
Areal trekant = g*h/2
Omkrets trekant = g + h + rot(g^2+h^2)
Radius(r) = h/2

"""

def figur_trekant_og_halvsirkel(b,a): #  [funksjonsnavn med inn-argumenter]
    
    areal = b*a/2 + (np.pi*(a**2))/8 #  [formellen til arealet av figur]
    
    omkrets = math.sqrt(a**2+b**2) + b + np.pi*a/2 #  [formellen til "ytre omkrets"]
    
    return (areal,omkrets) #  [ut-argumenter]

h = 4 #  [variabel 1]
g = 5 #  [variabel 2]

(resultat_areal,resultat_omkrets) = figur_trekant_og_halvsirkel(g,h) #  [call a function]

print("Areal =", resultat_areal) #  [resultat]
print("Omkrets =", resultat_omkrets) #  [resultat]

#%% Oppgave 6

import numpy as np #  [import av biblioteker]
import matplotlib.pyplot as plt

def f(x): 
    return -x**2 - 5 #  [funksjonen]

xa = np.linspace(-10,10,200) #  [definisjon av intervallet]

plt.plot(xa, f(xa)) #  [plotting av funksjonen]
plt.show() #  [vis resultatet]





    





















































