from ...core.card import Card, Rank
from ...core.table import Table
from ...core.player import Player


class BlackjackTable(Table):
    def __init__(self):
        super().__init__()
        self.dealer = Player("Blackjack Dealer")

        for _ in range(2):
            self._dealer_take_card()

    def initial_deal(self):
        """
        Deal 2 cards to each player at the start of the round
        """
        self.give_cards()

    def dealer_turn(self):
        """
        Dealer hits until hand value is 17 or more
        """
        while self._summarize_hand(self.dealer.cards) < 17:
            self._dealer_take_card()

    def determine_winner(self):
        """
        Compare each player against dealer
        """
        dealer_total = self._summarize_hand(self.dealer.cards)

        for player in self.players:
            player_total = self._summarize_hand(player.cards)

            if player_total > 21:
                print(f"{player.name} busts ({player_total})")
            elif dealer_total > 21 or player_total > dealer_total:
                print(f"{player.name} wins! ({player_total})")
            elif player_total == dealer_total:
                print(f"{player.name} ties dealer ({player_total})")
            else:
                print(f"{player.name} loses ({player_total})")

    def _dealer_take_card(self):
        card = self.deck.draw()
        self.dealer.receive_card(card)

    def _card_to_value(self, card: Card) -> int:
        """
        Return possible card value,
        Ace has 11 points
        """
        match card.rank:
            case Rank.JACK | Rank.QUEEN | Rank.KING:
                return 10
            case Rank.ACE:
                return 11
            case _:
                return card.rank.value

    def _summarize_hand(self, cards: list[Card]) -> int:
        """
        Summarize cards total value
        """
        return sum(self._card_to_value(card) for card in cards)
