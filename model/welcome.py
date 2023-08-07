
print ("bonjour bienvenue sur l'application de gestion des livraisons\n")
a = input("tapez pour vous connecter en tant que:\n 1 Client\n 2 pour Livreur\n 3 pour Admin: ")
if (a == 1):
    b = input ("taper:\n1-se connecter\n2 s'inscrire si vous n'avez pas de compte")
if (b == 2):
    nom =input("entrez votre nom d'utilisateur:\n")
    mdp = input("votre mot de pass:\n")
    num_fone = input("votre numero:\n")
    addresse = input ("votre addresse:\n")
    new_client = client(nom,mdp,num_fone,addresse)
else:
    print("réessayer")
print(new_client.nom+"\n"+new_client.mdp+"\n"+new_client.num_fone+"\n")

