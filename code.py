import sys
konto = 0
nummer = 1
print("Wer wird Millionaer?")
def Auswertung():
    global konto
    if antwort == "a" and frage[-1] == "A":
        print("Richtig!")
        konto += konto
        if konto == 0:
            konto = 50

    elif antwort == "b" and frage[-1] == "B":
        print("Richtig!")
        konto += konto
        if konto == 0:
            konto = 50

    elif antwort == "c" and frage[-1] == "C":
        print("Richtig!")
        konto += konto
        if konto == 0:
            konto = 50

    elif antwort == "d" and frage[-1] == "D":
        print("Richtig!")
        konto += konto
        if konto == 0:
            konto = 50

    else:
        print("Falsch!")
        print("Sie haben gewonnen: ", konto,"Euro")
        print("-- ENDE --")
        sys.exit()

    print("Ihr Kontostand: ", konto,"Euro\n\n")


        #Frage,A,B,C,D,Richtig
fragen = []
fragen.append(["Frage 1 (€ 50): Was ist landläufig auch als Porree bekannt?","A:Lilawa","B:Lottschalk","C:Leckmann","D:Lauch","D"])
fragen.append(["Frage 2 (€ 100): Was wird aus Hefeteig hergestellt?","A:Vickipediahupf","B:Jahuhupf","C:Gugelhupf","D:Ihbäihupf","C"])
fragen.append(["Frage 3 (€ 200): Was hört man oft, wenn es um berühmte Universitäten geht?","A:Kuuverschunden","B:Pfärtwech","C:Schwainnichda","D:Oxford","D"])
fragen.append(["Frage 4 (€ 400): Womit beschäftigten sich schon die Neandertaler?","A:Schmidt","B:Andrack","C:Feuerstein","D:Pocher","C"])
fragen.append(["Frage 5 (€ 800): Mit dem Nobelpreis ausgezeichnet wurde Robert ...?","A:Koch","B:Rüttgers","C:Althaus","D:Platzeck","A"])
fragen.append(["Frage 6 (€ 1.000): Wofür begeistern sich derzeit besonders die jungen Kino-Zuschauer?","A:Univerity Song 1","B:College Symphony 2","C:High School Musical 3","D:Kindergarten Opera 4","C"])
fragen.append(["Frage 7 (€ 2.000): Mit welchem Sportstar ist die Pussycat-Dolls-Sängerin Nicole Scherzinger liiert?","A:Roger Federer","B:Lewis Hamilton","C:Vitali Klitschko","D:Christiano Ronaldo","B"])
fragen.append(["Frage 8 (€ 4.000): Was könnte Andrea Ypsilanti treffenderweise über die Ereignisse in Hessen sagen?","A:Oh, Susi","B:Mein Gott, Walter","C:Dirty Diana","D:Erna kommt","B"])
fragen.append(["Frage 9 (€ 8.000): Worum ging es 1963 beim \"Wunder von Lengede\"?","A:Marienerscheinung","B:Fußball-WM-Sieg","C:Neulingsgeburt","D:Rettung von Bergleuten","D"])
fragen.append(["Frage 10 (€ 16.000): Welcher Krimiautor war als Agent für den britischen Geheimdienst tätig?","A:Frederick Forsyth","B:Edgar Wallace","C:John le Carre","D:Arthur Conan Doyle","C"])
fragen.append(["Frage 11 (€ 32.000): MIt welchem Album stürmte Poplegende Grace Jones im Herbst auf die große Bühne zurück?","A:Blizzard","B:Tornado","C:Hurricane","D:Monsoon","C"])




zaeler = 0

for anzahl in fragen:
    frage = fragen[zaeler]
    print(frage[0])
    print(frage[1])
    print(frage[2])
    print(frage[3])
    print(frage[4])
    antwort = ""
    while antwort == "":
        antwort = input(">> ").strip().lower()
        antwort = antwort[0]

    print("Ihre Eingabe:",antwort,"\n")
    Auswertung()
    zaeler = zaeler + 1

print("\nEnde!!! \nSie haben das Quiz und",konto,"Euro gewonnen!")
