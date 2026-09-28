# Practical 05 — Tic-Tac-Toe (Minimax) & Shuffle Cards

**Subject:** 504 – Artificial Intelligence
**Files:** `tic_tac_toe_minimax.py`, `shuffle_cards.py`

## Aim
(a) To implement an unbeatable Tic-Tac-Toe agent using the Minimax
algorithm.
(b) To build a standard deck of 52 cards and shuffle it using the
Fisher-Yates algorithm, then deal hands to multiple players.

## Theory
**Minimax** is a decision-making algorithm for two-player,
zero-sum, perfect-information games. It recursively explores the game
tree, assuming the MAX player always picks the move maximizing their
score while the MIN player always picks the move minimizing it. For
Tic-Tac-Toe, this guarantees the computer never loses — it either wins
or forces a draw against optimal play.

**Fisher-Yates Shuffle** produces a uniformly random permutation of a
list in O(n) time: starting from the last index, repeatedly swap the
current element with a randomly chosen element at or before its
position. This avoids the bias present in naive shuffling approaches
(e.g. repeatedly swapping fully random pairs of indices).

## How to Run
```bash
python tic_tac_toe_minimax.py
python shuffle_cards.py
```

## Viva Questions & Answers
1. **Q: Why does the Minimax agent in Tic-Tac-Toe never lose?**
   A: Because it exhaustively evaluates all possible future game states
   and always picks the move that guarantees the best worst-case
   outcome, given optimal play from the opponent.
2. **Q: What is the time complexity of unoptimized Minimax on Tic-Tac-Toe?**
   A: O(b^d) where b is the branching factor (~9) and d is the depth
   (~9), though the actual game tree is much smaller due to early
   terminal states.
3. **Q: Why is Fisher-Yates preferred over naive shuffling methods?**
   A: It guarantees a truly uniform random permutation in O(n) time;
   naive approaches (like swapping random pairs a fixed number of
   times) can introduce statistical bias.
4. **Q: In the Minimax scoring scheme used here, why subtract/consider depth?**
   A: To make the agent prefer a faster win and a slower loss, rather
   than being indifferent between winning immediately or after several
   more moves (not fully implemented here, but a common refinement).
5. **Q: How would you extend Minimax to a game with a much larger branching
   factor, like Chess?**
   A: Combine it with Alpha-Beta pruning, limit search depth, and use
   a heuristic evaluation function for non-terminal states.

## Real-World Relevance
Minimax with Alpha-Beta pruning is the basis of classic
game-playing AI (Chess, Checkers); the Fisher-Yates shuffle is used
anywhere a fair random ordering matters, from card games to
randomized algorithms and A/B test assignment.
