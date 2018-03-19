# 24 Loops - Willekeur in while
"""---------------- OPGAVE ----------------
Vervolmaak het programma.
-  Voeg een while-loop toe die termineert 
   als het getal 444 is.
-  In de while-loop: break en continue.
-  getal is 334 => break
-  Getal ontbreekt in 'betekenisboek' => continue
-  Géén break, géén continue: Toon getal en symboliek.
-  Else: => print "Waarom heeft", getal, "niets te melden?"
---------------------------------------"""
# betekenisboek, init getal
import random
symbolint = {0: 'Onstoffelijk, Abstract',
             1: 'Eenheid, Elementair',
             2: 'Het Kwaad',
             3: 'Perfectie, Holy Trinity',
             4: 'Superduo 2**2, old skool materie: lucht, aarde, water, vuur',
             5: 'Pentagram, Thora',
             6: 'Hexagram, Davidster, Wijsheid van Solomon',
             7: 'Overvloed, maagdelijk, Deus ex Machina',
             8: 'Rechtvaardigheid',
             9: 'Duisternis, Überheilig',
             10: "Woord van God, Orde, Absolutie",
             11: 'Waanzin, Gekte, Geluk',
             12: 'Dierenriem, Apostelen, Harmonie',
             13: 'Onheil, Ongeluk, Rampspoed',
             14: 'White Supremacy', 18: 'Adolf Hitler', 22: 'Het Leed, Lijden', 27: 'Openbaring',
             28: 'Conservatisme, Reactionair',
             33: 'JC de Verlosser', 40: 'Beproeving', 42: 'Zin van het Bestaan',
             50: 'Heilige Geest, Thora', 69: 'Orale Liefde, Kreeft (sterrenbeeld)',
             70: 'De Wereldvolken', 88: 'Heil Hitler', 248: 'Eeuwig, Echt',
             333: 'Hoog Bewust, Met God, Dasein', 420: 'Marihuana', 666: 'Antichrist'}
getal = 10

# willekeur in while
while getal != 444:
	getal = random.randint(0,667)
	# print(getal, "??-??")
	if getal == 334: break
	if getal not in symbolint: continue
	# do it!
	print(getal,'=>',symbolint[getal])
else:
	print('Waarom heeft', getal, 'niets te melden?') 
		
