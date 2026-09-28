"""
Practical 05b: Shuffle a Deck of Cards
Subject : 504 - Artificial Intelligence
Aim     : To build a standard 52-card deck and shuffle it randomly
          using the Fisher-Yates (Knuth) shuffle algorithm, and deal
          hands to multiple players.
"""

import random

SUITS = ["Hearts", "Diamonds", "Clubs", "Spades"]
RANKS = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King", "Ace"]


def build_deck() -> list:
    """Build a standard, ordered 52-card deck as a list of (rank, suit) tuples."""
    return [(rank, suit) for suit in SUITS for rank in RANKS]


def fisher_yates_shuffle(deck: list, seed: int = None) -> list:
    """
    Shuffle the deck in place using the Fisher-Yates (Knuth) algorithm,
    which guarantees a uniformly random permutation in O(n) time.

    Args:
        deck: The list of cards to shuffle.
        seed: Optional random seed for reproducible shuffles.

    Returns:
        The same list object, shuffled in place.
    """
    if seed is not None:
        random.seed(seed)

    for current_index in range(len(deck) - 1, 0, -1):
        random_index = random.randint(0, current_index)
        deck[current_index], deck[random_index] = deck[random_index], deck[current_index]

    return deck


def deal_hands(deck: list, num_players: int, cards_per_hand: int) -> list:
    """Deal `cards_per_hand` cards to each of `num_players` players from the top of the deck."""
    hands = []
    for player_index in range(num_players):
        start = player_index * cards_per_hand
        end = start + cards_per_hand
        hands.append(deck[start:end])
    return hands


def format_card(card: tuple) -> str:
    """Format a (rank, suit) tuple as a readable string, e.g. 'Ace of Spades'."""
    rank, suit = card
    return f"{rank} of {suit}"


def main() -> None:
    """Entry point that drives the card-shuffling demonstration."""
    print("=" * 60)
    print("PRACTICAL 05b : SHUFFLE A DECK OF CARDS (FISHER-YATES)")
    print("=" * 60)

    deck = build_deck()
    print(f"\nOrdered deck (first 5 cards): "
          f"{[format_card(card) for card in deck[:5]]}")
    print(f"Total cards in deck: {len(deck)}")

    shuffled_deck = fisher_yates_shuffle(deck.copy(), seed=42)
    print(f"\nShuffled deck (first 5 cards): "
          f"{[format_card(card) for card in shuffled_deck[:5]]}")

    num_players = 4
    cards_per_hand = 5
    hands = deal_hands(shuffled_deck, num_players, cards_per_hand)

    print(f"\nDealing {cards_per_hand} cards each to {num_players} players:")
    for player_number, hand in enumerate(hands, start=1):
        formatted_hand = ", ".join(format_card(card) for card in hand)
        print(f"  Player {player_number}: {formatted_hand}")

    print("\nProgram executed successfully.")


if __name__ == "__main__":
    main()
