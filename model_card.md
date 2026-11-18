Model Card: VibeMatch 2.0
1. Model name and overview
VibeMatch 2.0 is a classroom music recommendation project that extends my Module 3 Music Recommender Simulation (VibeMatch 1.0). It has two recommendation methods:
1. Preference-based scoring: a rule-based content-filtering system that ranks songs using genre, mood, and target energy.
2. Song similarity: a scikit-learn NearestNeighbors model that finds songs with similar numerical musical features.
The two methods run in the same Python application, but they produce separate recommendation lists. The nearest-neighbor results do not currently re-rank the preference-based recommendations.
2. Intended use and users
VibeMatch is intended for classroom learning, demonstration, and experimentation with explainable recommendations and basic machine-learning similarity. It is not a commercial streaming service, a predictor of long-term taste, or a system trained on real user listening behavior.
3. How the system works
Original preference-based recommender
For each song, the program adds:
- 2 points for an exact genre match (case-insensitive).
- 1 point for an exact mood match (case-insensitive).
- Up to 1 point for energy similarity: max(0, 1 - abs(song_energy - target_energy)).
The maximum possible score is 4.00. The program ranks songs from highest to lowest and prints an explanation of each score.
New machine-learning similarity component
The new AIMusicRecommender uses four numeric song attributes: energy, danceability, valence, and acousticness. It standardizes those values with StandardScaler, then fits scikit-learn's NearestNeighbors using Euclidean distance. Given an existing song title, it retrieves nearby songs in that standardized feature space, excluding the query song itself.

A smaller distance indicates greater similarity under these four features. The distance is not a probability, a quality score, or evidence that a user will like the song. This model does not learn preferences from user feedback. Although the model is fitted to the dataset, it does not train a predictive neural network or learn individual tastes.
4. Data
The project uses data/songs.csv, a dataset of 20 fictional songs, expanded from 10 songs in the original project. Fields include song title, artist, genre, mood, energy, tempo, valence, danceability, and acousticness.

The preference-based scorer uses genre, mood, and energy. The nearest-neighbor model uses energy, danceability, valence, and acousticness. Neither method currently uses lyrics, language, listening history, likes, skips, or real listener feedback. The dataset is too small to represent music broadly.
5. Strengths
- The preference-based method explains exactly how its scores are calculated.
- The nearest-neighbor method considers more numeric musical features than the original scoring system.
- Input validation rejects missing genre or mood and invalid target-energy values.
- The application logs startup and the number of songs loaded.
- Automated tests check core recommendation behavior and selected invalid inputs.
6. Limitations, bias, and risks
- Small and synthetic dataset: 20 fictional songs cannot represent the range of genres, languages, cultures, or listeners.
- Weighting bias: genre is worth twice as much as mood or maximum energy similarity in the rule-based scorer. This can rank a genre match above a song with better energy alignment.
- Feature-selection bias: the similarity model uses four numeric attributes but ignores genre, lyrics, context, and personal meaning. Standardization makes feature variation in this small dataset influential.
- No feedback loop: neither method learns from likes, skips, or listening history. Recommendations are not truly personalized beyond the entered preferences or selected example song.
- Potential filter bubble: repeatedly emphasizing similar genres or acoustic features could limit musical variety.
- No quality or fairness guarantee: passing software tests does not establish that recommendations are enjoyable, diverse, culturally representative, or fair.
The system should not be presented as knowing users' tastes or as a substitute for a full-scale recommendation platform.
7. Evaluation and observed results
Original profile-based evaluation
The original recommender was run on four profiles:
Profile	Top recommendation	Score
High-Energy Pop	Sunrise City	3.97
Chill Lofi	Library Rain	4.00
Deep Intense Rock	Storm Runner	3.96
Conflicting Sad Energy	Blue Window	3.37


The first three profiles produced different top songs. The conflicting sad/high-energy profile exposed a limitation: Blue Window ranked first despite a weaker energy match because genre and mood contributed more to its score.
Original scoring-weight experiment
In VibeMatch 2.0, I temporarily reduced the genre weight from 2 to 1 and increased the maximum energy-similarity contribution from 1 to 2, leaving mood at 1. I restored the original weights afterward.
Profile	Original top result	Experimental top result
High-Energy Pop	Sunrise City (3.97)	Sunrise City (3.94)
Chill Lofi	Library Rain (4.00)	Library Rain (4.00)
Deep Intense Rock	Storm Runner (3.96)	Storm Runner (3.92)
Conflicting Sad Energy	Blue Window (3.37)	Blue Window (2.74)


The top song stayed the same for each profile, but lower-ranked songs changed. For High-Energy Pop, Weekend Bounce moved from third to second and Gym Hero dropped from second to fourth. For Conflicting Sad Energy, Desert Lights moved from fourth to third and Quiet Thoughts left the top five. This showed that manually chosen weights influence rankings.
New nearest-neighbor example
Input: recommend_similar("Sunrise City", k=5)
Result	Artist	Euclidean distance
Rooftop Lights	Indigo Parade	0.588
Weekend Bounce	City Motion	0.783
Gym Hero	Max Pulse	0.833
Desert Lights	Nova Sky	0.945
Electric Heart	Crystal Pulse	1.041


These are observed similarity results, not human preference ratings. No user study or relevance-accuracy benchmark has been performed.
Automated reliability tests
The latest reported command was:
python -m pytest -v
Observed result: 10 passed in 1.81s on the development Mac with Python 3.14.7.
- 2 original recommender tests: ranking and nonempty explanations.
- 4 preference-validation tests: valid preferences, out-of-range energy, missing genre, and nonnumeric energy.
- 4 similarity-model tests: returns five results, excludes the input song, rejects an unknown song, and rejects negative k.
The application also printed:
INFO: Starting Music Recommendation System
INFO: Successfully loaded 20 songs
These tests establish behavior for the listed cases only. They do not measure recommendation accuracy, fairness, or robustness against every possible malformed input.
8. Guardrails and reliability
validate_preferences checks that genre and mood are nonempty strings and that energy is numeric and between 0.0 and 1.0. The nearest-neighbor method raises a ValueError for an unknown song title or a nonpositive k. The application logs startup and dataset loading. Tests exercise several of these guardrails.

Possible future improvements include better handling of empty or corrupted CSV files, explicit validation of all numerical song features, additional edge-case tests, and a reusable evaluation harness.
9. AI collaboration and verification
I evaluated the project by running four user profiles, inspecting recommendation scores, and testing the final extension locally. I verified the updated application by running it and observing 10 passing tests.

Verification decision: I added automated tests for invalid user preferences and missing song titles, then verified that those tests passed.

I used AI assistance to explore improvements to my original recommender. One suggestion I accepted was adding input validation and automated tests for invalid preferences and unknown song titles. I implemented these checks and verified that the tests passed.

One suggestion I revised was describing the machine-learning feature as personalized. I clarified that the nearest-neighbor model finds songs with similar audio features, but does not learn from individual listening histories. I reviewed the results and verified all 10 automated tests.

The reported command outputs and recommendation results were checked in the local project.
10. Future work
I would expand the dataset with more songs, artists, genres, and languages; allow users to adjust feature weights; incorporate optional listening feedback; and evaluate recommendation diversity and relevance. I would also compare similarity-model results against the rule-based baseline with defined evaluation criteria rather than assuming one is better.
11. Personal reflection
This project helped me understand how recommendation systems use data and scoring rules to generate suggestions. My biggest learning moment was seeing how changing feature weights affected the rankings. I was also surprised that Blue Window ranked first for someone who preferred high-energy sad R&B, even though its energy was much lower than requested. This showed me that an algorithm can follow its rules correctly while still producing recommendations that may not fully match a user's expectations.

Extending VibeMatch taught me that adding a machine-learning component is only part of building a reliable system. I also needed to validate inputs, test failure cases, examine actual outputs, and explain what the model can and cannot do. In the future, I would expand the dataset, include user feedback, and evaluate additional features to improve recommendations.