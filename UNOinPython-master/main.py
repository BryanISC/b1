import Card
import CurrentScreen
import EnumsCards

# 0: Player, 1: KI
numberOf = []
startPlayer = 0
numberOf.append(int(input("cuantos jugadores? ")))
numberOf.append(int(input("cuantas maquinas? ")))
# direction 1: en el sentido de las agujas del reloj, -1: en sentido antihorario
pointsOfPlayers = Card.initPointsOfPlayers(numberOf[0] + numberOf[1])
# drawCards[1] 0=> + Cartas no dibujadas, 1 => son dibujadas
drawCards = [0, 0]
names = Card.getNames(numberOf[0])
names.extend(Card.getKINames(numberOf[1]))
while(Card.someHasEnoughtPoints(pointsOfPlayers) == -1):
    cardStack = Card.initStackOfCards()
    Card.shuffleDeckofCards(cardStack)
    handsOfCards = []
    for player in range((numberOf[0] + numberOf[1])):
        handsOfCards.append(Card.initHand(cardStack))
    direction = 1
    otherColor = -1
    lastCard = Card.drawCard(cardStack)
    whichPlayer = startPlayer % (numberOf[0]+numberOf[1])
    startPlayer += 1
    if lastCard.getValue() == "dibujar2":
        if lastCard.backInDeck == 1:
            drawCards[0] = 0
        else:
            drawCards[0] += 2
    elif lastCard.getValue() == "dibujar4":
        if lastCard.backInDeck == 1:
            drawCards[0] = 0
        else:
            drawCards[0] += 4
        if(lastCard.getColor() == "salvaje"):
            if "Maquina" in names[whichPlayer]:
                colorCardsInHand = [0, 0, 0, 0]
                for card in handsOfCards[whichPlayer]:
                    if(card.color.value <= 4):
                        colorCardsInHand[card.color.value] += 1
                bestColor = colorCardsInHand.index(max(colorCardsInHand))
                otherColor = bestColor
            else:
                otherColor = CurrentScreen.showChooseColorScreen(
                    "", handsOfCards[whichPlayer], direction, lastCard, names[whichPlayer], drawCards)
    elif lastCard.getValue() == "elegir color" and lastCard.getColor() == "salvaje":
        if "Maquina" in names[whichPlayer]:
            colorCardsInHand = [0, 0, 0, 0]
            for card in handsOfCards[whichPlayer]:
                if(card.color.value <= 4):
                    colorCardsInHand[card.color.value] += 1
            bestColor = colorCardsInHand.index(max(colorCardsInHand))
            otherColor = bestColor
        else:
            otherColor = CurrentScreen.showChooseColorScreen(
                "", handsOfCards[whichPlayer], direction, lastCard, names[whichPlayer], drawCards)
    elif lastCard.getValue() == "marcha atras" and lastCard.backInDeck == 0:
        direction *= -1
        drawCards[1] = 0
    elif lastCard.getValue() == "omitir" and lastCard.backInDeck == 0:
        whichPlayer = (whichPlayer + 1 *
                       direction) % (numberOf[0] + numberOf[1])
        drawCards[1] = 0
    else:
        drawCards[1] = 0
    while Card.someoneWon(handsOfCards) == False:
        if(otherColor != -1):
            lastCard = Card.Card(EnumsCards.Colors(otherColor), lastCard.value)
            lastCard.backInDeck = 1
            otherColor = -1
        if "Maquina" not in handsOfCards[whichPlayer]:
            CurrentScreen.showCurrentScreen(
                handsOfCards[whichPlayer], direction, lastCard, names[whichPlayer], drawCards)
        lastCardTmp = Card.playCard(handsOfCards[whichPlayer], lastCard, cardStack,
                                    False, names[whichPlayer], direction, drawCards, False)
        if(lastCard.backInDeck == 0):
            cardStack.append(lastCard)
            lastCard.backInDeck = 1
        Card.shuffleDeckofCards(cardStack)
        lastCard = lastCardTmp
        if lastCard.getValue() == "dibujar2":
            if lastCard.backInDeck == 1:
                drawCards[0] = 0
            else:
                drawCards[0] += 2
        elif lastCard.getValue() == "dibujar4":
            if lastCard.backInDeck == 1:
                drawCards[0] = 0
            else:
                drawCards[0] += 4
                if(lastCard.getColor() == "salvaje"):
                    if "Maquina" in names[whichPlayer]:
                        colorCardsInHand = [0, 0, 0, 0]
                        for card in handsOfCards[whichPlayer]:
                            if(card.color.value <= 4):
                                colorCardsInHand[card.color.value] += 1
                            bestColor = colorCardsInHand.index(
                                max(colorCardsInHand))
                            otherColor = bestColor
                    else:
                        otherColor = CurrentScreen.showChooseColorScreen(
                            "", handsOfCards[whichPlayer], direction, lastCard, names[whichPlayer], drawCards)
        elif lastCard.getValue() == "elegir Color" and lastCard.getColor() == "salvaje":
            if "Maquina" in names[whichPlayer]:
                colorCardsInHand = [0, 0, 0, 0]
                for card in handsOfCards[whichPlayer]:
                    if(card.color.value <= 4):
                        colorCardsInHand[card.color.value] += 1
                    bestColor = colorCardsInHand.index(max(colorCardsInHand))
                    otherColor = bestColor
            else:
                otherColor = CurrentScreen.showChooseColorScreen(
                    "", handsOfCards[whichPlayer], direction, lastCard, names[whichPlayer], drawCards)
        elif lastCard.getValue() == "marcha atras" and lastCard.backInDeck == 0:
            direction *= -1
            drawCards[1] = 0
        elif lastCard.getValue() == "omitir" and lastCard.backInDeck == 0:
            whichPlayer = (whichPlayer + 1 *
                           direction) % (numberOf[0] + numberOf[1])
            drawCards[1] = 0
        else:
            drawCards[1] = 0
        whichPlayer = (whichPlayer + 1 *
                       direction) % (numberOf[0] + numberOf[1])
    winningPerson = (whichPlayer + 1 * direction * -
                     1) % (numberOf[0] + numberOf[1])
    print("enhorabuena a " +
          names[winningPerson] + " por ganar esta ronda!")
    Card.givePersonPoints(handsOfCards, winningPerson, pointsOfPlayers)
    CurrentScreen.showPointsOfPlayers(pointsOfPlayers, names)
    input("Pulse cualquier tecla para continuar")

print("enhorabuena a " + names[(whichPlayer - 1 * direction * -1) %
                                    (numberOf[0] + numberOf[1])] + " para ganar el juego!")
