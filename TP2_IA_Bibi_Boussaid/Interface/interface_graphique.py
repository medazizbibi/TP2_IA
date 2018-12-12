from tkinter import *
from tkinter import filedialog
from Problemes import australia
#from ast import literal_eval
#from Problemes.Formalisations.fonc_australia import const_different
#from Problemes.Formalisations.fonc_australia import constraints

# def getAndParseFile():
#     file = filedialog.askopenfile(initialdir = r"/Desktop")
#     f = file.readlines()
#     i=0
#     while(i<len(f)-1):
#         v = f[i]
#         if(v[:9] == "variables"):
#             vars = f[i+1]
#             variables = literal_eval(vars)
#             i+=2
#             print("variables = ",variables)
#         elif(v[:7] == "domains"):
#             domainsT = []
#             i+=2
#             while(v[:1]!="]"):
#                 domainsT.append(literal_eval(f[i]))
#                 i+=1
#                 v=f[i]
#             domains = dict((v, domainsT) for v in variables)
#             print("domains = ",domains)
#         # elif(v[:3] == "def"):
#         #     delim = f[i].find("(")
#         #     functName = v[4:delim]
#         #     delim2 = f[i].find(":")
#         #     functSig = v[:delim2+1]
#         #     i+=2
#         #     print(functSig)
#         #elif(v[:11] == "constraints"):
#         #     constraints = []
#         #     i+=2
#         #     while(v[:1] != "]"):
#         #         constraints.append(literal_eval(f[i]))
#         #         i+=1
#         #         v=f[i]
#         #     print("constraints = ",constraints)
#         else:
#             i+=1



window = Tk()
logging = ""

window.title(" Projet 2 : Intelligence Artificielle ")
window.geometry('1100x800')
window.configure(background="wheat1")
lbl1 = Label(window, text="Bienvenu cher utilisateur, que l'expérience commence ! ",bg="wheat1", font=('Times', 18))
lbl1.place(x=250, y=10)
screen = Text(height=21, width=65)
screen.place(x=550, y=80)
logs = Label(window, text="Résultats & Logs ",bg="wheat1",fg="tan4", font=('Times', 14))
logs.place(x=770, y=50)




#*************************** TROISIEME NIVEAU : CHOIX DE L'ALGO ****************************

#----------- Australia -------------
def functionNiveau3Australia():
    global logging

    master0=Tk()
    master0.title("Choix de l'algorithme")
    master0.geometry("480x80")
    master0.configure(background="lightpink4")

    def clickedBacktracking():
        global logging
        screen.insert(END, "\nBacktracking avec AC3\n")
        logging = logging + "\nBacktracking avec AC3\n"
        australia.algo1
        screen.insert(END, australia.algo1)
        logging = logging + str(australia.algo1)

    algoAustralia1 = Button(master0, text="Backtracking avec AC3 ",bg="lightpink2", command=clickedBacktracking(), font=('Times', 10))
    algoAustralia1.place(x=200, y=550)
    algoAustralia1.grid(row=1,column=1)

    def clickedMRV():
        global logging
        screen.insert(END, "\nBacktracking MRV\n")
        logging = logging + "\nBacktracking MRV\n"
        australia.algo2
        screen.insert(END, australia.algo2)
        logging = logging + str(australia.algo2)

    algoAustralia2 = Button(master0, text="Backtracking MRV",bg="lightpink2", command=clickedMRV, font=('Times', 10))
    algoAustralia2.place(x=300, y=550)
    algoAustralia2.grid(row=1,column=2)


    def clickedAlgo3():
        global logging
        screen.insert(END, "\nBacktracking HDV\n")
        logging = logging + "\nBacktracking HDV\n"
        australia.algo3
        screen.insert(END, australia.algo3)
        logging = logging + str(australia.algo3)

    algoAustralia3 = Button(master0, text="Backtracking HDV", bg="lightpink2",command=clickedAlgo3, font=('Times', 10))
    algoAustralia3.place(x=300, y=550)
    algoAustralia3.grid(row=1,column=3)

    def clickedAlgo4():
        global logging
        screen.insert(END, "\nBacktracking LCV\n")
        logging = logging + "\nBacktracking LCV\n"
        australia.algo4
        screen.insert(END, australia.algo4)
        logging = logging + str(australia.algo4)

    algoAustralia4 = Button(master0, text="Backtracking LCV",bg="lightpink2", command=clickedAlgo4, font=('Times', 10))
    algoAustralia4.place(x=300, y=550)
    algoAustralia4.grid(row=2,column=1)

    def clickedAlgo5():
        global logging
        screen.insert(END, "\nBacktracking MRV&LCV\n")
        logging = logging + "\nBacktracking MRV&LCV\n"
        australia.algo5
        screen.insert(END, australia.algo5)
        logging = logging + str(australia.algo5)

    algoAustralia5 = Button(master0, text="Backtracking MRV&LCV",bg="lightpink2", command=clickedAlgo5, font=('Times', 10))
    algoAustralia5.place(x=300, y=550)
    algoAustralia5.grid(row=2,column=2)

    def clickedAlgo6():
        global logging
        screen.insert(END, "\nBacktracking HDV&LCV\n")
        logging = logging + "\nBacktracking HDV&LCV\n"
        australia.algo6
        screen.insert(END, australia.algo6)
        logging = logging + str(australia.algo6)

    algoAustralia6 = Button(master0, text="Backtracking HDV&LCV",bg="lightpink2", command=clickedAlgo6, font=('Times', 10))
    algoAustralia6.place(x=300, y=550)
    algoAustralia6.grid(row=2,column=3)

#--------- N Queens --------
def functionNiveau3NQueen():
    global logging
    master1=Tk()
    master1.title("Choix de l'algorithme")
    master1.geometry("480x80")
    master1.configure(background="Khaki4")
    from Problemes import nqueen
    def clickedAlgo1():
        global logging
        screen.insert(END, "\nBacktracking avec AC3 \n")
        logging = logging + "\nBacktracking avec AC3\n"
        nqueen.algo1
        screen.insert(END, nqueen.algo1)
        logging = logging + str(nqueen.algo1)

    algoNQueen1 = Button(master1, text="Backtracking avec AC3",bg="Khaki3", command=clickedAlgo1, font=('Times', 10))
    algoNQueen1.place(x=200, y=550)
    algoNQueen1.grid(row=1,column=1)

    def clickedAlgo2():
        global logging
        screen.insert(END, "\nBacktracking MRV\n")
        logging = logging + "\nBacktracking MRV\n"
        nqueen.algo1
        screen.insert(END, nqueen.algo2)
        logging = logging + str(nqueen.algo2)

    algoNQueen2 = Button(master1, text="Backtracking MRV",bg="Khaki3",command=clickedAlgo2, font=('Times', 10))
    algoNQueen2.place(x=315, y=550)
    algoNQueen2.grid(row=1,column=2)

    def clickedAlgo3():
        global logging
        screen.insert(END, "\nBacktracking HDV\n")
        logging = logging + "\nBacktracking HDV\n"
        nqueen.algo1
        screen.insert(END, nqueen.algo3)
        logging = logging + str(nqueen.algo3)

    algoNQueen3 = Button(master1, text="Backtracking HDV", bg="Khaki3",command=clickedAlgo3, font=('Times', 10))
    algoNQueen3.place(x=300, y=550)
    algoNQueen3.grid(row=1,column=3)

    def clickedAlgo4():
        global logging
        screen.insert(END, "\nBacktracking LCV\n")
        logging = logging + "\nBacktracking LCV\n"
        nqueen.algo4
        screen.insert(END, nqueen.algo4)
        logging = logging + str(nqueen.algo4)

    algoNQueen4 = Button(master1, text="Backtracking LCV", bg="Khaki3",command=clickedAlgo4, font=('Times', 10))
    algoNQueen4.place(x=300, y=550)
    algoNQueen4.grid(row=2,column=1)

    def clickedAlgo5():
        global logging
        screen.insert(END, "\nBacktracking MRV&LCV\n")
        logging = logging + "\nBacktracking MRV&LCV\n"
        nqueen.algo5
        screen.insert(END, nqueen.algo5)
        logging = logging + str(nqueen.algo5)

    algoNQueen5 = Button(master1, text="Backtracking MRV&LCV",bg="Khaki3", command=clickedAlgo5, font=('Times', 10))
    algoNQueen5.place(x=300, y=550)
    algoNQueen5.grid(row=2,column=2)

    def clickedAlgo6():
        global logging
        screen.insert(END, "\nBacktracking HDV&LCV\n")
        logging = logging + "\nBacktracking HDV&LCV\n"
        nqueen.algo6
        screen.insert(END, nqueen.algo6)
        logging = logging + str(nqueen.algo6)

    algoNQueen6 = Button(master1, text="Backtracking HDV&LCV",bg="Khaki3", command=clickedAlgo6, font=('Times', 10))
    algoNQueen6.place(x=300, y=550)
    algoNQueen6.grid(row=2,column=3)

#--------- Crypta ----------
def functionNiveau3Crypta():
    global logging
    master2 = Tk()
    master2.title("Choix de l'algorithme")
    master2.geometry("450x50")
    master2.configure(background="MediumOrchid3")

    def clickedAlgo1():
        global logging
        from Problemes import cryptarithmetic
        screen.insert(END, "\nBacktracking - Contraintes n-aires \n")
        logging = logging + "\nBacktracking - Contraintes n-aires\n"
        res=cryptarithmetic.algo1()
        screen.insert(END, res[0])
        screen.insert(END,"\nEn utilisant des contraintes n-aires, cela a pris, en secondes : ")
        screen.insert(END, res[1])


    algoCrypta1 = Button(master2, text="Backtracking - Contraintes n-aires", bg="plum2", command=clickedAlgo1, font=('Times', 10))
    algoCrypta1.place(x=200, y=550)
    algoCrypta1.grid(row=1, column=1)


    def clickedAlgo2():
        global logging
        screen.insert(END, "\nBacktracking - Contraintes binaires \n")
        logging = logging + "\nBacktracking - Contraintes binaires\n"
        from Problemes import cryptarithmetic
        res=cryptarithmetic.algo2()
        screen.insert(END, res[0])
        screen.insert(END,"\nEn utilisant des contraintes binaires, cela a pris, en secondes : ")
        screen.insert(END, res[1])


    algoCrypta2 = Button(master2, text="Backtracking - Contraintes binaires ", bg="plum2", command=clickedAlgo2, font=('Times', 10))
    algoCrypta2.place(x=200, y=550)
    algoCrypta2.grid(row=1, column=2)

#*************************** DEUXIEME NIVEAU : CHOIX DU FICHIER ****************************

# --------- Australia ---------

def functionNiveau2Australia():
    def getFile():
        global var
        global logging
        file2 = filedialog.askopenfile(initialdir=r"C:\Users\mbm info\PycharmProjects\TP2_IA_Bibi_Boussaid\Problemes\Formalisations")
        textAustralia.insert(END, file2.read())
        textAustralia.config(state=DISABLED)
        var = open(file2.name, "rt")
        screen.insert(END, "Formalisation ajoutée\n")
        logging = logging + "Formalisation ajoutée\n"
        functionNiveau3Australia()

    boutonAustraliaFichier = Button(window, text="Choisir le fichier de formalisation",bg="wheat3", command=getFile, font=('Times', 10))
    boutonAustraliaFichier.place(x=10, y=400)
    textAustralia = Text(height=16, width=42)
    textAustralia.place(x=200, y=400)

# --------- NQueen -----------

def functionNiveau2NQueen():

    def getFile():
        global var
        global logging
        file2 = filedialog.askopenfile(initialdir=r"C:\Users\mbm info\PycharmProjects\TP2_IA_Bibi_Boussaid\Problemes\Formalisations")

        textNQueen.insert(END, file2.read())
        textNQueen.config(state=DISABLED)
        var = open(file2.name, "rt")
        screen.insert(END, "Formalisation ajoutée\n")
        logging = logging + "Formalisation ajoutée\n"
        functionNiveau3NQueen()

    boutonNQueenFichier = Button(window, text="Choisir le fichier de formalisation", bg="wheat3",command=getFile,
                                        font=('Times', 10))
    boutonNQueenFichier.place(x=10, y=400)
    textNQueen= Text(height=16, width=42)
    textNQueen.place(x=200, y=400)

# --------- Crypta -----------

def functionNiveau2Crypta():

    def getFile():
        global var
        global logging
        file2 = filedialog.askopenfile(initialdir=r"C:\Users\mbm info\PycharmProjects\TP2_IA_Bibi_Boussaid\Problemes\Formalisations")

        textCrypta.insert(END, file2.read())
        textCrypta.config(state=DISABLED)
        var = open(file2.name, "rt")
        screen.insert(END, "Formalisation ajoutée\n")
        logging = logging + "Formalisation ajoutée\n"
        functionNiveau3Crypta()

    boutonCrypta = Button(window, text="Choisir le fichier de formalisation", bg="wheat3",command=getFile,
                                        font=('Times', 10))
    boutonCrypta.place(x=10, y=400)
    textCrypta= Text(height=16, width=42)
    textCrypta.place(x=200, y=400)


#*************************** PREMIER NIVEAU : CHOIX DU PROBLEME ****************************
label = Label(window, text="Veuillez choisir un problème ",bg="wheat1",fg="tan4",font=('Times', 13))
label.place(x=40, y=220)

def clickedBoutonAustralia():
    global logging
    screen.insert(END, "\nAustralia\n")
    logging = logging + "\nAustralia\n"
    functionNiveau2Australia()

boutonAustralia = Button(window, text="Australia", bg="wheat3",command=clickedBoutonAustralia, font=('Times', 10))
boutonAustralia.place(x=300, y=220)

def clickedBoutonNQueen():

     global logging
     screen.insert(END, "\nNQueen\n")
     logging = logging + "\nNQueen\n"
     functionNiveau2NQueen()

boutonNQueen = Button(window, text="NQueen",bg="wheat3", command=clickedBoutonNQueen, font=('Times', 10))
boutonNQueen.place(x=365, y=220)


label = Label(window, text="Bonus :",bg="wheat1",fg="tan4", font=('Times', 13))
label.place(x=40, y=260)

def clickedBoutonCrypta():
    global logging
    screen.insert(END, "\nCryptarithmetique\n")
    logging = logging + "\nCryptarithmetique\n"
    functionNiveau2Crypta()

boutonCrypta = Button(window, text="Cryptarithmétique",bg="wheat3", command=clickedBoutonCrypta, font=('Times', 10))
boutonCrypta.place(x=300, y=260)


#********************** Logging *******************
def saveClicked():
    f = open("logs.txt", "w+")
    f.write(logging)

boutonEnregistrer = Button(window, text="Enregistrer les résultats & les logs", bg="wheat3",command=saveClicked, font=('Times', 10))
boutonEnregistrer.place(x=760, y=450)



window.mainloop()