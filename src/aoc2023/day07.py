from collections import Counter
from itertools import starmap


# Number of occurences for types in order of increasing strength
TYPES = [
    (1, 1, 1, 1, 1),  # High card
    (2, 1, 1, 1),  # One pair
    (2, 2, 1),  # Two pair
    (3, 1, 1),  # Three of a kind
    (3, 2),  # Full house
    (4, 1),  # Four of a kind
    (5,),  # Five of a kind
]
TYPE_TO_STRENGTH = dict(zip(TYPES, range(len(TYPES))))


def parse_input(raw_input):
    lines = raw_input.strip().split("\n")
    return list(starmap(
        lambda hand, bid: (hand, int(bid)),
        (line.split() for line in lines)
    ))


def solve_part1(hand_bid_pairs):
    # Cards in order of increasing strength
    cards = "23456789TJQKA"
    key = make_sort_key(cards)
    return compute_total_winnings(hand_bid_pairs, key)


def solve_part2(hand_bid_pairs):
    # Cards in order of increasing strength
    cards = "J23456789TQKA"
    key = make_sort_key(cards, joker="J")
    return compute_total_winnings(hand_bid_pairs, key)


def make_sort_key(cards, joker=""):
    assert len(joker) < 2
    card_to_strength = dict(zip(cards, range(len(cards))))

    def sort_key(hand_bid_pair):
        hand, bid = hand_bid_pair
        type_strength = get_type_strength(hand, joker)
        card_strengths = [card_to_strength[card] for card in hand]
        return [type_strength] + card_strengths

    return sort_key


def get_type_strength(hand, joker):
    if joker:
        hand_without_jokers = [card for card in hand if card != joker]
        joker_count = len(hand) - len(hand_without_jokers)
        if not hand_without_jokers:
            occurences = [0]
        else:
            occurences = list(
                dict(Counter(hand_without_jokers).most_common()).values()
            )
        # Best type-outcome is when the joker becomes the most frequent card,
        # i.e. the number of the most frequent card is increased by the number
        # of jokers
        occurences[0] += joker_count
    else:
        occurences = dict(Counter(hand).most_common()).values()
    return TYPE_TO_STRENGTH[tuple(occurences)]


def compute_total_winnings(hand_bid_pairs, key):
    return sum(
        rank * bid for
        rank, (hand, bid) in
        enumerate(sorted(hand_bid_pairs, key=key), start=1)
    )
