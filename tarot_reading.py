'''
0. Intro --> Le carte danno un aiuto su come poter affrontare
    un problema, non fanno divinazione. La domanda domande deve essere: 
    come posso fare per uscire da una determ. situazione?
1. creare le carte
2. una descrizione per ogni carta richiamabile con un comando
3. far pescare le carte da 1 o 3
3.1 se una carta, scrivere il significato in sintesi
3.2 se tre carte, pass, pres, fut
4. mandarle in stampa con questo formato:
 ----------------
|                |
|                |
|                |
|                |      
|      carta     |
|                |
|                |
|                |
|                |
|                |
 ----------------

 5. scrivere la lettura per ogni carta

'''

import random

class User:
    pass


class Deck:
    pass

class Deck:
    pass

cards = {
    0: ' " " - Il Matto', 
    1: 'I - Il Bagatto', 
    2: 'II - La Papessa', 
    3: 'III - L\'Imperatrice', 
    4: 'IIII - L\'Imperatore', 
    5: 'V - Il Papa', 
    6: 'VI - Gli Anamanti',
    7: 'VII - Il Carro',
    8: 'VIII - La Giustizia',
    9: 'VIIII - L\'Eremita',
    10: 'X - La Ruota della Fortuna',
    11: 'XI - La Forza',
    12: 'XII - L\'Appeso',
    13: 'XIII - Senza Nome',
    14: 'XIIII - La Temperanza',
    15: 'XV - Il Diavolo',
    16: 'XVI - La Torre',
    17: 'XVII - La Stella',
    18: 'XVIII - La Luna',
    19: 'XVIIII - Il Sole',
    20: 'XX - Il Giudizio',
    21: 'XI - Il Mondo'
    }

definitions = {
    0: 'Va con ciò che posside in giro per il Mondo confiducia.',
    1: 'Ha tutto in mano, ha tutte le possibilità. Sta a lui a sceglire la cosa giusta per raggiungere il suo scopo',
    2: 'Sta studiando, è ancora ferma. E\' un momento di stasi.',
    3: 'Energia femminile allo stato puro',
    4: 'Potere in terra. Potere materiale.',
    5: 'Collegamento tra il terreno e il divino. Carta di passaggio ad un piano superiore.',
    6: 'La scelta. Ad esempio tra vecchio e nuovo.',
    7: 'la dimostrazione del proprio successo.',
    8: 'Tutto ciò che è inerente alla giustizia.',
    9: 'Ti invita a far luce sul passato',
    10: 'Momento di stallo che ha bisogno di un qualcosa per ripartire(la ruota)',
    11: 'Indica la forza morale, interiore.',
    12: 'Ci sono problemi da risolvere con il tuo albero genealogico',
    13: 'La trasformazione',
    14: 'La guarigione',
    15: 'Gli eccessi (ribellione, anticonformismo, riuscire a vedere oltre etc.)',
    16: 'Rappresenta il tuo corpo. Può essere una grande festa oppure l\'uscita da qualcosa di brutto',
    17: 'Il tuo posto.',
    18: 'La madre; rappresenta tutte le cose nascoste, interiori, profonde',
    19: 'Il padre; rappresenta tutto ciò che c\'è fuori',
    20: 'Il giudizio o la chiamata',
    21: 'Il completamento del tutto'
    }





### TEST AREA ###

#scelta carte gioco pass pres fut
space = ' ' * 6
while True:
    card1 = cards[random.randint(1, 21)]
    card2 = cards[random.randint(1, 21)]
    card3 = cards[random.randint(1, 21)]
    if card1 == card2 or card1 == card3 or card2 == card3:
        card1 = cards[random.randint(1, 21)]
        card2 = cards[random.randint(1, 21)]
        card3 = cards[random.randint(1, 21)]
    else:
        #print(card1 + space + card2 + space + card3)
        break

# funzione stampa carta
def card_print():
    space_card1 = round(((28 - len(card1)) / 2)) * ' '
    space_card2 = round(((28 - len(card2)) / 2)) * ' '
    space_card3 = round(((28 - len(card3)) / 2)) * ' '
    print((' ' + '-' * len(space_card1 + card1 + space_card1) + ' ' + '  ') + (' ' + '-' * len(space_card2 + card2 + space_card2) + ' ' + '  ') + (' ' + '-' * len(space_card3 + card3 + space_card3) + ' '))

    for x in range(10):
        print(('|' + ' ' * len(space_card1 + card1 + space_card1) + '|' + '  ') + ('|' + ' ' * len(space_card2 + card2 + space_card2) + '|' + '  ') + ('|' + ' ' * len(space_card3 + card3 + space_card3) + '|' + '  '))        
    print('|' + space_card1 + card1 + space_card1 + '|' + '  ' + '|' + space_card2 + card2 + space_card2 + '|' + '  ' + '|' + space_card3 + card3 + space_card3 + '|' + '  ')
    for x in range(10):
        print(('|' + ' ' * len(space_card1 + card1 + space_card1) + '|' + '  ') + ('|' + ' ' * len(space_card2 + card2 + space_card2) + '|' + '  ') + ('|' + ' ' * len(space_card3 + card3 + space_card3) + '|' + '  '))
    print((' ' + '-' * len(space_card1 + card1 + space_card1) + ' ' + '  ') + (' ' + '-' * len(space_card2 + card2 + space_card2) + ' ' + '  ') + (' ' + '-' * len(space_card3 + card3 + space_card3) + ' '))

card_print()