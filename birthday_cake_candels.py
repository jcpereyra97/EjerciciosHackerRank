"""
You are in charge of the cake for a child's birthday. You have decided the cake will have one 
candle for each year of their total age. They will only be able to blow out the tallest of the 
candles. Count how many candles are tallest.

Example


The maximum height candles are  units high. There are  of them, so return .
"""


def birthdayCakeCandles(candles):
    ord = sorted(candles)
    tam = (len(candles) -1)
    cant = 0
    x = True
    while(x == True):
        if ((ord[tam]) == (ord[(len(candles)-1)]) and (tam >= 0)):
            cant = cant + 1
            tam = tam - 1
        else:
            x = False
    return cant



print(birthdayCakeCandles([1,1,1,1,1,1,1,1,1,1,1,1]))

