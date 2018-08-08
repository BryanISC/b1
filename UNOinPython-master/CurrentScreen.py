import os
from EnumsCards import *


def showToDrawnCards(drawCards):
    print("+cartas: " + str(drawCards[0]) + "\t", end="")


def showDirection(direction):
    if(direction == 1):
        print("Direction: Clockwise\t", end="")
    else:
        print("Direction C-Clockwise\t", end="")


def showHand(hand):
    whichCard = 0
    for card in hand:
        print("" + str(card.getValue()) + " " +
              str(card.getColor()) + " \t\t\t->\t " + str(whichCard))
        whichCard += 1


def showOptions(hand):
    print()
    print("Pasar -> P")
    print("elegir carta(s) -> D")
    if(len(hand) == 2):
        print("UNO! -> U")


def showCurrentScreen(hand, direction, lastCard, playerName, drawCards):
    clearScreen()
    showPlayerName(playerName)
    showDirection(direction)
    showToDrawnCards(drawCards)
    showLastCard(lastCard)
    showHand(hand)
    showOptions(hand)


def showPlayerName(playerName):
    print("Nombre: " + playerName + "\t", end="")


def showLastCard(lastCard):
    print("ultima carta: " + str(lastCard.getValue()) +
          " " + str(lastCard.getColor()))


def clearScreen():
    os.system("cls" if os.name == "nt" else "clear")


def showChooseColorScreen(startMessage, hand, direction, lastCard, playerName, drawCards):
    clearScreen()
    showPlayerName(playerName)
    showDirection(direction)
    showToDrawnCards(drawCards)
    showLastCard(lastCard)
    showHand(hand)
    print(startMessage)
    print("Escoger un nuevo color:")
    print("Azul\t->\tb")
    print("Rojo\t->\tr")
    print("Amarillo\t->\ty")
    print("verde\t->\tg")
    newColor = input().lower()
    if(newColor == "b"):
        return 0
    elif(newColor == "r"):
        return 1
    elif(newColor == "y"):
        return 2
    elif(newColor == "g"):
        return 3
    else:
        return showChooseColorScreen("no es un color!")


def showPointsOfPlayers(pointsOfPlayers, names):
    i = 0
    for points in pointsOfPlayers:
        print("puntos de " + names[i] + ": " + str(pointsOfPlayers[i]))
        i += 1
