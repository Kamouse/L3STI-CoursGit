def calculer_mon_impot(revenu):
    if revenu < 11.497:
        print("aucun impot sur le revenu")

    elif 11498 < revenu and revenu < 29315 :
        impotSurRevenu = revenu * 0.11
        revenuApresImpot = revenu * 0.89
        print("votre impot sur le revenu est de : ", impotSurRevenu)
        print("votre revenu après impôt est de : ", revenuApresImpot)

    elif 29580 < revenu and revenu < 84577 :
        impotSurRevenu = revenu * 0.30
        revenuApresImpot = revenu * 0.70
        print("votre impot sur le revenu est de : ", impotSurRevenu)
        print("votre revenu après impôt est de : ", revenuApresImpot)

    elif 84578 < revenu and revenu < 181917 :
        impotSurRevenu = revenu * 0.41
        revenuApresImpot = revenu * 0.59
        print("votre impot sur le revenu est de : ", impotSurRevenu)
        print("votre revenu après impôt est de : ", revenuApresImpot)

    elif revenu > 181918 :  
        impotSurRevenu = revenu * 0.45
        revenuApresImpot = revenu * 0.55
        print("votre impot sur le revenu est de : ", impotSurRevenu)
        print("votre revenu après impôt est de : ", revenuApresImpot)

    else:
        if revenu < 0 or not (int or float):
            print("revenu non valide")
#coucou, juste pour le commit
    

        
print(calculer_mon_impot(64839))
