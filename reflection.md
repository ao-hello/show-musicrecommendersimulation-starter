# Reflection: Profile Comparisons

## High-Energy Pop vs. Chill Lofi

These two profiles are near-opposites, and the outputs reflect that cleanly. The pop profile surfaces fast, bright tracks (Sunrise City, Gym Hero, Festival Pulse) in the 120–130 BPM range with low acousticness. The lofi profile returns slow, mellow, acoustic-heavy tracks (Library Rain, Midnight Coding, Study Fog) around 70–80 BPM.
This makes sense: the genre and energy targets pull in exactly opposite directions, so almost no song can score well on both.

## Chill Lofi vs. Deep Intense Rock

Lofi tops out with a near-perfect 4.50 (Library Rain hits genre + mood + energy + acoustic). Rock tops out at 3.99. It's high, but the rock *runner-up* drops all the way to 1.98 because there's only one rock song in the catalog. After Storm Runner, the rock profile falls back to mood-only matches (Trap House Sunrise, Gym Hero, Basement Riot). This is the dataset-skew limitation showing up in practice.

## High-Energy Pop vs. Adversarial "Conflicted Listener"

Both profiles ask for pop and high energy, but the adversarial one swaps "happy" for "sad" (a mood that doesn't exist in the dataset). The top two results are nearly the same, Gym Hero and Sunrise City, because the scorer quietly ignores the unknown mood and lets genre + energy take over. This confirms the limitation in the model
card: strict equality on mood means "sad" contributes zero rather than reshaping the ranking.

## Weight-shift experiment (energy ×2, genre ÷2)

I temporarily flipped the weights so energy was worth +2.0 and genre only +1.0, then
re-ran all four profiles (weights have since been reverted).

- **Top-1 didn't move** for any profile — Sunrise City, Library Rain, Storm Runner,
  and Gym Hero all stayed #1. When a song already matches genre *and* mood *and*
  energy, no reasonable weight change can dislodge it.
- **The middle of the list opened up.** Cross-genre songs started breaking in: the
  Deep Intense Rock list now includes Trap House Sunrise above Gym Hero by energy
  proximity, and the adversarial pop list pulled in Storm Runner and Trap House
  Sunrise at ranks 3–4 — songs the original weights kept out entirely.
- **Takeaway:** genre weighting mainly controls *diversity* in the tail, not the
  top pick. Lowering it is a cheap way to let the recommender surface songs that
  feel right *acoustically* even when the label doesn't match.

## Plain-language takeaway

The reason "Gym Hero" keeps showing up for people who say they want "Happy Pop" is that the system rewards *genre* twice as hard as anything else. "Gym Hero" is pop and it's very energetic, so it racks up a big genre bonus plus a big energy bonus, enough to beat songs that are actually happy but belong to a different genre. In other words, the recommender has decided that being the right *kind* of music matters
more than being the right *mood*, and until we rebalance the weights (or let genres partially match), that's the behavior we'll keep getting.
