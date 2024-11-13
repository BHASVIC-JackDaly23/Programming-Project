

def attackerPredictedPoints(xG, xA, mp, ha, fdr ):
    xG_points = xG * 4
    xA_points = xA * 3

    totalPoints = (xG_points + xA_points) * (mp/90) * ha * fdr


def defenderPredictedPoints(xG, xA, xCleansheets, mp, ha, fdr ):
    xG_points = xG * 4
    xA_points = xA * 3
    xCS_points = xCleansheets * 4 #have added the percentage of getting a clean sheet in and represented as a decimal

    totalPoints = (xG_points + xA_points + xCS_points) * (mp / 90) * ha * fdr



def goalkeeperPredictedPoints(xG, xA,xCleansheets, xSaves, mp, ha, fdr ):
    xG_points = xG * 4
    xA_points = xA * 3
    xCS_points = xCleansheets * 4  # have added the percentage of getting a clean sheet in and represented as a decimal
    xS_points = xSaves * 1
    totalPoints = (xG_points + xA_points + xCS_points) * (mp / 90) * ha * fdr










