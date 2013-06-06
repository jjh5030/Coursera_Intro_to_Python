# Mini-project #6 - Blackjack

import simplegui
import random

# load card sprite - 949x392 - source: jfitz.com
CARD_SIZE = (73, 98)
CARD_CENTER = (36.5, 49)
card_images = simplegui.load_image("http://commondatastorage.googleapis.com/codeskulptor-assets/cards.jfitz.png")

CARD_BACK_SIZE = (71, 96)
CARD_BACK_CENTER = (35.5, 48)
card_back = simplegui.load_image("http://commondatastorage.googleapis.com/codeskulptor-assets/card_back.png")    

# initialize some useful global variables
in_play = False
outcome = ""
score = 0
p_hand = [] #Players Hand
d_hand = [] #Dealers Hand
p_deck = [] #Playing Deck

# define globals for cards
SUITS = ('C', 'S', 'H', 'D')
RANKS = ('A', '2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K')
VALUES = {'A':1, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9, 'T':10, 'J':10, 'Q':10, 'K':10}

# define card class
class Card:
    def __init__(self, suit, rank):
        if (suit in SUITS) and (rank in RANKS):
            self.suit = suit
            self.rank = rank
        else:
            self.suit = None
            self.rank = None
            print "Invalid card: ", suit, rank

    def __str__(self):
        return self.suit + self.rank

    def get_suit(self):
        return self.suit

    def get_rank(self):
        return self.rank

    def draw(self, canvas, pos):
        card_loc = (CARD_CENTER[0] + CARD_SIZE[0] * RANKS.index(self.rank), 
                    CARD_CENTER[1] + CARD_SIZE[1] * SUITS.index(self.suit))
        canvas.draw_image(card_images, card_loc, CARD_SIZE, [pos[0] + CARD_CENTER[0], pos[1] + CARD_CENTER[1]], CARD_SIZE)
        
# define hand class
class Hand:
    def __init__(self):
        self.cards = []	# create Hand object

    def __str__(self):
        # return a string representation of a hand
        cards_in_hand = "Hand contains "
        for card in self.cards:
            cards_in_hand += str(card) + " "
        return cards_in_hand

    def add_card(self, card):
        self.cards.append(card)	# add a card object to a hand

    def get_value(self):
        # count aces as 1, if the hand has an ace, then add 10 to hand value if it doesn't bust
        # compute the value of the hand, see Blackjack video
        value = 0
        aces = False
        for card in self.cards:
            value += VALUES[card.get_rank()]
            if card.get_rank() == "A":
                aces = True
        if value + 10 <= 21 and aces:
            value += 10
        return value
   
    def draw(self, canvas, pos, hand_type):
        # draw a hand on the canvas, use the draw method for cards
        if hand_type == "Player": #draw all cards for player
            for i in range(len(self.cards)):
                self.cards[i].draw(canvas, [pos[0] + (i % 5) * 100, pos[1]])
        else: #show back of dealers first card when in play        
            if not in_play:
                for i in range(len(self.cards)):
                    self.cards[i].draw(canvas, [pos[0] + (i % 5) * 100, pos[1]])
            else:
                canvas.draw_image(card_back, CARD_BACK_CENTER, CARD_BACK_SIZE,
                              [pos[0] + CARD_BACK_CENTER[0], pos[1] + CARD_BACK_CENTER[1]],
                              CARD_BACK_SIZE)
                for i in range(1, len(self.cards)):
                    self.cards[i].draw(canvas, [pos[0] + (i % 5) * 100, pos[1]])
        
# define deck class 
class Deck:
    def __init__(self):
        # create a Deck object
        self.cards = [Card(s ,r) for s in SUITS for r in RANKS]
        self.i = -1

    def shuffle(self):
        # add cards back to deck and shuffle
        # use random.shuffle() to shuffle the deck
        self.i = -1
        random.shuffle(self.cards)

    def deal_card(self):
        # deal a card object from the deck
        self.i += 1
        return self.cards[self.i]
    
    def __str__(self):
        # return a string representing the deck
        cards_in_deck = "Deck contains "
        for card in self.cards:
            cards_in_deck += str(card) + " "
        return cards_in_deck

#define event handlers for buttons
def deal():
    global outcome, in_play, p_hand, d_hand, p_deck
    p_hand = []
    d_hand = []
    p_deck = []
    
    # your code goes here
    p_deck = Deck()
    p_hand = Hand()
    d_hand = Hand()
    p_deck.shuffle()
        
    p_hand.add_card(p_deck.deal_card())
    p_hand.add_card(p_deck.deal_card())
    d_hand.add_card(p_deck.deal_card())
    d_hand.add_card(p_deck.deal_card())
    
    outcome = "Hit or stand?"
    
    in_play = True
    
    print "\nPlaying", p_deck
    print "Dealer's", d_hand
    print "Players", p_hand, "\n"

def hit():
    # replace with your code below
    global outcome, in_play, p_hand, d_hand, p_deck, score
 
    # if the hand is in play, hit the player
    if in_play:
        p_hand.add_card(p_deck.deal_card())        
        print "Players Hand Value:", p_hand.get_value() 
    
    # if busted, assign a message to outcome, update in_play and score
    if in_play and p_hand.get_value() > 21:
        outcome = "You have busted"
        print "outcome", outcome
        score -= 1
        in_play = False
        
    if in_play:    
        print "\nDealer's", d_hand
        print "Players", p_hand, "\n"
    
def stand():
    global outcome, in_play, p_hand, d_hand, p_deck, score	# replace with your code below
   
    # if hand is in play, repeatedly hit dealer until his hand has value 17 or more
    if in_play:
        in_play = False
        while d_hand.get_value() < 17:
            d_hand.add_card(p_deck.deal_card()) 
            
        print "\nDealer's final", d_hand
        print "Players final", p_hand, "\n"
        
        # assign a message to outcome, update in_play and score
        if d_hand.get_value() > 21:
            score += 1
            outcome = "You win!"
        elif d_hand.get_value() >= p_hand.get_value():
            score -= 1
            outcome = "You lose!"
        else:
            score += 1
            outcome = "You win!"       
        print outcome
            
# draw handler    
def draw(canvas):
    # test to make sure that card.draw works, replace with your code below 
    #card = Card("S", "A")
    #card.draw(canvas, [300, 300])
    canvas.draw_text("Blackjack", [175, 75], 60, "Aqua")
    canvas.draw_text("Dealer", [50, 150], 48, "Black")
    canvas.draw_text("Player", [50, 400], 48, "Black")
    canvas.draw_text("Score " + str(score), [450, 75], 36, "Black")
    canvas.draw_text(outcome, [250, 400], 36, "Black")
    d_hand.draw(canvas, [50, 200], "Dealer")
    p_hand.draw(canvas, [50, 450], "Player") 

# initialization frame
frame = simplegui.create_frame("Blackjack", 600, 600)
frame.set_canvas_background("Green")

#create buttons and canvas callback
frame.add_button("Deal", deal, 200)
frame.add_button("Hit",  hit, 200)
frame.add_button("Stand", stand, 200)
frame.set_draw_handler(draw)

# get things rolling
frame.start()
deal()
# remember to review the gradic rubric