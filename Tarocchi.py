import random
from time import sleep

class User:
    def __init__(self, name):
        self.name = name
    
    def __repr__(self):
        return 'Ciao, ' + self.name + '. Scegli il "gioco" che vuoi fare.'





class Deck:
    def __init__(self,game = 'Tarocchi'):
        self.game = game

    def play(self, game):
        self.game = game

        cards = {
        0: '" " - Il Matto', 
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


        
        if self.game == 'lettura classica':
            #scelta carte gioco pass pres fut evitando che siano uguali
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
                    break

            # funzione stampa carta
            def card_print():
                space_card1 = round(((28 - len(card1)) / 2)) * ' '
                space_card2 = round(((28 - len(card2)) / 2)) * ' '
                space_card3 = round(((28 - len(card3)) / 2)) * ' '
                space_pas = round((len(space_card1 + card1 + space_card1) - 7)/ 2) * ' ' 
                space_pre = round((len(space_card2 + card2 + space_card2) - 8)/ 2) * ' ' 
                space_fut = round((len(space_card3 + card3 + space_card3) - 6)/ 2) * ' ' 

                print((' ' + '-' * len(space_card1 + card1 + space_card1) + ' ' + '  ') + (' ' + '-' * len(space_card2 + card2 + space_card2) + ' ' + '  ') + (' ' + '-' * len(space_card3 + card3 + space_card3) + ' '))

                for x in range(10):
                    print(('|' + ' ' * len(space_card1 + card1 + space_card1) + '|' + '  ') + ('|' + ' ' * len(space_card2 + card2 + space_card2) + '|' + '  ') + ('|' + ' ' * len(space_card3 + card3 + space_card3) + '|' + '  '))        
                print('|' + space_card1 + card1 + space_card1 + '|' + '  ' + '|' + space_card2 + card2 + space_card2 + '|' + '  ' + '|' + space_card3 + card3 + space_card3 + '|' + '  ')
                for x in range(10):
                    print(('|' + ' ' * len(space_card1 + card1 + space_card1) + '|' + '  ') + ('|' + ' ' * len(space_card2 + card2 + space_card2) + '|' + '  ') + ('|' + ' ' * len(space_card3 + card3 + space_card3) + '|' + '  '))
                print((' ' + '-' * len(space_card1 + card1 + space_card1) + ' ' + '  ') + (' ' + '-' * len(space_card2 + card2 + space_card2) + ' ' + '  ') + (' ' + '-' * len(space_card3 + card3 + space_card3) + ' '))
                print()
                print(' ' + space_pas + 'Passato' + space_pas + ' ' + '  ' + ' ' + space_pre + 'Presente' + space_pre + ' ' + '  ' + ' ' + space_fut + 'Futuro' + space_fut + ' ' + '  ')


            # lettura tarocchi
            def read():
                index_card = []
                for element in cards.values():
                    index_card.append(element)
                print('\nLettura delle carte\n')
                print(card1 + ' - ' + definitions[index_card.index(card1)])
                print(card2 + ' - ' + definitions[index_card.index(card2)])
                print(card3 + ' - ' + definitions[index_card.index(card3)])

            card_print()
            read()
            sleep(5)
            input('\n\npremi il tasto "invio" per uscire')
            quit()

        elif self.game == 'lettura singola':
            card1 = cards[random.randint(1, 21)]

            # funzione stampa carta
            def card_print():
                space_card1 = round(((28 - len(card1)) / 2)) * ' '
                print(' ' + '-' * len(space_card1 + card1 + space_card1))
                for x in range(10):
                    print('|' + ' ' * len(space_card1 + card1 + space_card1) + '|')
                print('|' + space_card1 + card1 + space_card1 + '|')
                for x in range(10):
                    print('|' + ' ' * len(space_card1 + card1 + space_card1) + '|')
                print(' ' + '-' * len(space_card1 + card1 + space_card1))

            # lettura tarocchi
            def read():
                index_card = []
                for element in cards.values():
                    index_card.append(element)
                print('\nLettura delle carte\n')
                print(card1 + ' - ' + definitions[index_card.index(card1)])

            card_print()
            read()
            sleep(5)
            input('\n\npremi il tasto "invio" per uscire')
            quit()

        elif self.game == '5 carte':
            #scelta carte gioco pass pres fut evitando che siano uguali
            space = ' ' * 6
            while True:
                card1 = cards[random.randint(1, 21)]
                card2 = cards[random.randint(1, 21)]
                card3 = cards[random.randint(1, 21)]
                card4 = cards[random.randint(1, 21)]
                card5 = cards[random.randint(1, 21)]
                if card1 == card2 or card1 == card3 or card2 == card3:
                    card1 = cards[random.randint(1, 21)]
                    card2 = cards[random.randint(1, 21)]
                    card3 = cards[random.randint(1, 21)]
                    card4 = cards[random.randint(1, 21)]
                    card5 = cards[random.randint(1, 21)]
                else:
                    break

            # funzione stampa carta
            def card_print():
                space_card1 = round(((28 - len(card1)) / 2)) * ' '
                space_card2 = round(((28 - len(card2)) / 2)) * ' '
                space_card3 = round(((28 - len(card3)) / 2)) * ' '
                space_card4 = round(((28 - len(card3)) / 2)) * ' '
                space_card5 = round(((28 - len(card3)) / 2)) * ' '
                space_sita = round((len(space_card1 + card1 + space_card1) - 3)/ 2) * ' ' 
                space_osti = round((len(space_card2 + card2 + space_card2) - 16)/ 2) * ' ' 
                space_oste = round((len(space_card3 + card3 + space_card3) - 16)/ 2) * ' ' 
                space_arr = round((len(space_card4 + card4 + space_card4) - 6)/ 2) * ' ' 
                space_joll = round((len(space_card5 + card5 + space_card5) - 5)/ 2) * ' ' 



                print((' ' + '-' * len(space_card1 + card1 + space_card1) + ' ' + '  ') + (' ' + '-' * len(space_card2 + card2 + space_card2) + ' ' + '  ') + (' ' + '-' * len(space_card3 + card3 + space_card3) + ' '))

                for x in range(10):
                    print(('|' + ' ' * len(space_card1 + card1 + space_card1) + '|' + '  ') + ('|' + ' ' * len(space_card2 + card2 + space_card2) + '|' + '  ') + ('|' + ' ' * len(space_card3 + card3 + space_card3) + '|' + '  '))        
                print('|' + space_card1 + card1 + space_card1 + '|' + '  ' + '|' + space_card2 + card2 + space_card2 + '|' + '  ' + '|' + space_card3 + card3 + space_card3 + '|')
                for x in range(10):
                    print(('|' + ' ' * len(space_card1 + card1 + space_card1) + '|' + '  ') + ('|' + ' ' * len(space_card2 + card2 + space_card2) + '|' + '  ') + ('|' + ' ' * len(space_card3 + card3 + space_card3) + '|' + '  '))        
                print((' ' + '-' * len(space_card1 + card1 + space_card1) + ' ' + '  ') + (' ' + '-' * len(space_card2 + card2 + space_card2) + ' ' + '  ') + (' ' + '-' * len(space_card3 + card3 + space_card3) + ' '))
                print()
                print(' ' + space_sita + 'Ora' + space_sita + ' ' + '  ' + ' ' + space_osti + 'Ostacolo interno' + space_osti + ' ' + '  ' + ' ' + space_oste + 'Ostacolo Esterno' + space_oste + ' ' + '  ')

                print('\n\n')

                print((' ' + '-' * len(space_card4 + card4 + space_card4) + ' ' + '  ') + (' ' + '-' * len(space_card5 + card5 + space_card5) + ' ' + '  '))

                for x in range(10):
                    print(('|' + ' ' * len(space_card4 + card4 + space_card4) + '|' + '  ') + ('|' + ' ' * len(space_card5 + card5 + space_card5) + '|' + '  '))        
                print('|' + space_card4 + card4 + space_card4 + '|' + '  ' + '|' + space_card5 + card5 + space_card5 + '|' + '  ')
                for x in range(10):
                    print(('|' + ' ' * len(space_card4 + card4 + space_card4) + '|' + '  ') + ('|' + ' ' * len(space_card5 + card5 + space_card5) + '|' + '  '))        
                print((' ' + '-' * len(space_card4 + card4 + space_card4) + ' ' + '  ') + (' ' + '-' * len(space_card5 + card5 + space_card5) + ' ' + '  '))
                print()
                print(' ' + space_arr + 'Arrivo' + space_arr + ' ' + '  ' + ' ' + space_joll + 'Aiuto' + space_joll + ' ' + '  ')



            # lettura tarocchi
            def read():
                index_card = []
                for element in cards.values():
                    index_card.append(element)
                print('\nLettura delle carte\n')
                print(card1 + ' - ' + definitions[index_card.index(card1)])
                print(card2 + ' - ' + definitions[index_card.index(card2)])
                print(card3 + ' - ' + definitions[index_card.index(card3)])
                print(card4 + ' - ' + definitions[index_card.index(card4)])
                print(card5 + ' - ' + definitions[index_card.index(card5)])
            card_print()
            read()
            sleep(5)
            input('\n\npremi il tasto "invio" per uscire')
            quit()
        else:
            print('Non ho capito, riprova.')
regole = '''


------------------------------- I Tarocchi -------------------------------
_______________________________di Marsiglia_______________________________

Attenzione: le risposte devono essere interpretate da persone qualificate.
Non usare per la Divinazione.

'''

print(regole)
utente = User(input('Come ti chiami? '))
lettura = Deck()
print('Ciao ' + utente.name + '. Hai la possibilità di scegliere tra 3 giochi.\nIn base alla domanda da rivolgere ai Tarocchi, scegli quello corretto per te.')
sleep(2)
while True:
    lettura.play(input('\nA te la scelta. \nlettura classica, lettura singola, 5 carte: '))