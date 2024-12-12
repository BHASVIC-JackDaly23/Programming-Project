def expectedPoints():








def attackerPredictedPoints(xG, xA, mp, ha, fdr ):
    xG_points = xG * 4
    xA_points = xA * 3

    totalPoints = (xG_points + xA_points) * (mp/90) * ha * fdr




    print(totalPoints)




attackerPredictedPoints(0.46, 0.89, 570, 0.8, 0.5  )


def defenderPredictedPoints(xG, xA, xCleansheets, mp, ha, fdr ):
    xG_points = xG * 4
    xA_points = xA * 3
    xCS_points = xCleansheets * 4 #have added the percentage of getting a clean sheet in and represented as a decimal

    totalPoints = (xG_points + xA_points + xCS_points) * (mp / 90) * ha * fdr

    print(totalPoints)


defenderPredictedPoints(0,0.12 , 0.38, 660, 0.8, 0.5 )


def goalkeeperPredictedPoints(xG, xA,xCleansheets, xSaves, mp, ha, fdr ):
    xG_points = xG * 4
    xA_points = xA * 3
    xCS_points = xCleansheets * 4  # have added the percentage of getting a clean sheet in and represented as a decimal
    xS_points = xSaves * 1
    totalPoints = (xG_points + xA_points + xCS_points) * (mp / 90) * ha * fdr


    print(totalPoints)



goalkeeperPredictedPoints(0, 0.06, 0.25, 2.12, 720, 0.8, 1 )








