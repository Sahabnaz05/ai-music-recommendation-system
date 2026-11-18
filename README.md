🎵 VibeMatch 2.0: AI Music Recommendation System
CodePath AI110 | Show What You Know: Applied AI System

Final project: https://github.com/Sahabnaz05/ai-music-recommendation-system
Original Module 3 project: https://github.com/Sahabnaz05/ai110-module3show-musicrecommendersimulation-starter
Project Summary
VibeMatch 2.0 is a Python music recommendation system built from my original Module 3 Music Recommender Simulation (VibeMatch 1.0). I expanded the original dataset from 10 to 20 fictional songs and created a rule-based scoring system that recommends songs using a person's preferred genre, mood, and energy level.

For this final project, I extended that foundation with a scikit-learn nearest-neighbor model that finds songs with similar musical characteristics. I also added preference validation, automated tests, and application logging. The program runs both recommendation methods from the same command-line application.
What Changed from VibeMatch 1.0?
Component	VibeMatch 1.0	VibeMatch 2.0
Song dataset	20 fictional songs (expanded from 10 during Module 3)	Same 20-song dataset
Preference-based ranking	Genre, mood, and energy scoring	Preserved
Machine-learning similarity	Not available	NearestNeighbors using numerical song features
Input guardrails	Limited	Validates genre, mood, and energy preferences
Automated tests	2	10 passing tests in the latest reported run
Logging	Not included	Logs startup and number of songs loaded
Architecture diagram	Not included	Mermaid source in diagrams/architecture.mmd


How the System Works
1. Preference-based recommendations
The original recommender uses content-based, rule-based scoring, not a trained machine-learning model. It compares each song to a user's preferences:
- Genre match: +2 points
- Mood match: +1 point
- Energy similarity: up to +1 point, calculated as max(0, 1 - abs(song_energy - target_energy))
It ranks all songs by their total scores and returns the top five with explanations. Each song also contains attributes such as tempo, valence, danceability, and acousticness.
2. Machine-learning song similarity
The new AIMusicRecommender uses scikit-learn's StandardScaler and NearestNeighbors to find songs with similar numerical attributes:
- Energy
- Danceability
- Valence
- Acousticness
The system standardizes those features, fits a nearest-neighbor model to the 20-song dataset, and finds the closest songs using Euclidean distance. A smaller distance means greater similarity according to these four features. The query song is excluded from its own recommendations.

This is a fitted similarity model, not a model trained on listener behavior. It does not automatically personalize the nearest-neighbor results based on a user's listening history. The preference-based rankings and nearest-neighbor recommendations are displayed as separate outputs in the same application.
3. Guardrails, logging, and reliability
The preference validator rejects missing or empty genre/mood values, nonnumeric energy values, and energy values outside the range 0.0 to 1.0. The similarity model rejects unknown song titles and invalid recommendation counts. Application logs report startup and successful loading of the dataset. Automated tests cover original functionality, preference validation, and the new similarity model.
Project Structure
ai-music-recommendation-system/
├── data/
│   └── songs.csv
├── diagrams/
│   └── architecture.mmd
├── src/
│   ├── main.py
│   ├── recommender.py
│   └── ai_recommender.py
├── tests/
│   ├── test_recommender.py
│   └── test_ai_recommender.py
├── README.md
├── model_card.md
├── ai_interactions.md
└── requirements.txt
Architecture diagram: [View Mermaid source](diagrams/architecture.mmd).
Getting Started
From the project folder on macOS:
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
python -m src.main
Run the automated tests with:
python -m pytest -v
The project uses Python, pandas, NumPy, scikit-learn, and pytest. The committed requirements.txt contains the installation dependencies.
Reproducible Execution Evidence
The examples below come from actual Terminal output during development. The current command-line runner executes four predefined preference profiles and then finds songs similar to Sunrise City.
Example 1: High-Energy Pop
Input (defined in src/main.py):
{"genre": "pop", "mood": "happy", "energy": 0.85}
Command: python -m src.main

Observed output:
--- High-Energy Pop ---
1. Sunrise City - Score: 3.97
Because: Genre match (+2.0), Mood match (+1.0), Energy similarity (+0.97)
2. Gym Hero - Score: 2.92
Because: Genre match (+2.0), Energy similarity (+0.92)
3. Weekend Bounce - Score: 1.97
Because: Mood match (+1.0), Energy similarity (+0.97)
4. Electric Heart - Score: 1.95
Because: Mood match (+1.0), Energy similarity (+0.95)
5. Rooftop Lights - Score: 1.91
Because: Mood match (+1.0), Energy similarity (+0.91)
Example 2: Chill Lofi
Input (defined in src/main.py):
{"genre": "lofi", "mood": "chill", "energy": 0.35}
Command: python -m src.main

Observed output:
--- Chill Lofi ---
1. Library Rain - Score: 4.00
Because: Genre match (+2.0), Mood match (+1.0), Energy similarity (+1.00)
2. Midnight Coding - Score: 3.93
Because: Genre match (+2.0), Mood match (+1.0), Energy similarity (+0.93)
3. Focus Flow - Score: 2.95
Because: Genre match (+2.0), Energy similarity (+0.95)
4. Spacewalk Thoughts - Score: 1.93
Because: Mood match (+1.0), Energy similarity (+0.93)
5. Coffee Shop Stories - Score: 0.98
Because: Energy similarity (+0.98)
Example 3: Conflicting Sad Energy
Input (defined in src/main.py):
{"genre": "r&b", "mood": "sad", "energy": 0.95}
Command: python -m src.main

Observed output:
--- Conflicting Sad Energy ---
1. Blue Window - Score: 3.37
Because: Genre match (+2.0), Mood match (+1.0), Energy similarity (+0.37)
2. After Hours - Score: 2.68
Because: Genre match (+2.0), Energy similarity (+0.68)
3. Quiet Thoughts - Score: 1.25
Because: Mood match (+1.0), Energy similarity (+0.25)
4. Desert Lights - Score: 0.99
Because: Energy similarity (+0.99)
5. Gym Hero - Score: 0.98
Because: Energy similarity (+0.98)
Additional original profile: Deep Intense Rock returned Storm Runner first (score 3.96), followed by Gym Hero (1.98), Street Rhythm (1.97), Desert Lights (0.99), and Electric Heart (0.95).
Example 4: Machine-Learning Similarity
Input: Sunrise City, k=5

Command:
python -c "from src.recommender import load_songs; from src.ai_recommender import AIMusicRecommender; songs = load_songs('data/songs.csv'); model = AIMusicRecommender(songs); print(model.recommend_similar('Sunrise City', 5))"
Observed output (formatted as a table for readability):
Similar song	Artist	Distance
Rooftop Lights	Indigo Parade	0.588
Weekend Bounce	City Motion	0.783
Gym Hero	Max Pulse	0.833
Desert Lights	Nova Sky	0.945
Electric Heart	Crystal Pulse	1.041


When running python -m src.main, these five songs also appear under === AI MUSIC RECOMMENDATIONS ===.
Logging Evidence
Command: python -m src.main

Observed output:
INFO: Starting Music Recommendation System
INFO: Successfully loaded 20 songs
Loaded songs: 20
Automated Reliability and Guardrail Tests
Command:
python -m pytest -v
Observed result:
tests/test_ai_recommender.py::test_ai_returns_five_songs PASSED
tests/test_ai_recommender.py::test_ai_does_not_recommend_same_song PASSED
tests/test_ai_recommender.py::test_ai_rejects_unknown_song PASSED
tests/test_ai_recommender.py::test_ai_rejects_invalid_k PASSED
tests/test_recommender.py::test_recommend_returns_songs_sorted_by_score PASSED
tests/test_recommender.py::test_explain_recommendation_returns_non_empty_string PASSED
tests/test_recommender.py::test_valid_preferences PASSED
tests/test_recommender.py::test_invalid_energy PASSED
tests/test_recommender.py::test_missing_genre PASSED
tests/test_recommender.py::test_invalid_energy_type PASSED

============================== 10 passed in 1.81s ==============================
These tests demonstrate correct behavior for the tested cases; they do not establish accuracy or fairness across a large real-world music catalog.
Experiments I Tried
In my original Module 3 project, I experimented with changing the rule-based scoring weights: I reduced the genre weight from 2 points to 1 and increased the energy-similarity weight from 1 point to 2, while leaving mood at 1 point.

The top recommendation stayed the same for all four profiles, but some lower rankings changed. For High-Energy Pop, Weekend Bounce moved from third to second, while Gym Hero dropped from second to fourth. For Conflicting Sad Energy, Desert Lights moved from fourth to third, while Quiet Thoughts dropped out of the top five. This showed me that scoring weights can change recommendations even when the top result stays the same. I restored the original weights after the experiment.

For VibeMatch 2.0, I added a separate nearest-neighbor model so that users can also explore songs with similar audio features. I have not yet conducted a user study showing that its suggestions are better than the original ranking.
Limitations and Risks
- The dataset contains only 20 fictional songs and cannot represent all genres, languages, cultures, or listening preferences.
- The original scoring algorithm gives genre the highest weight, which can favor genre matches over better energy matches.
- The similarity model considers four numerical features and does not account for lyrics, listening history, user feedback, or cultural context.
- Standardizing features makes their scales comparable but does not prove that all four features are equally important to listeners.
- Small datasets can produce recommendations that are mathematically similar without feeling musically similar to a person.
- Both methods may reinforce narrow recommendations instead of helping listeners discover unfamiliar styles.
Future improvements could include a larger and more diverse dataset, feedback from listeners, configurable scoring weights, and systematic evaluation of recommendation quality.
Reflection
This project helped me understand how recommendation systems use data and scoring rules to make personalized suggestions. The biggest surprise was that Blue Window ranked first for someone who wanted high-energy sad R&B, even though its energy was much lower than requested. This showed me that an algorithm can follow its rules correctly without producing the best recommendation for every user.

For my final project, I learned how to extend an existing Python application with a machine-learning similarity model, add input guardrails, and verify important behaviors with automated tests. I also learned that a successful test run does not automatically mean recommendations are useful to every listener. If I continued this project, I would add more songs and collect user feedback to make recommendations more personalized and evaluate their quality.
Additional Documentation
- [Model card](model_card.md): design choices, limitations, risks, and evaluation notes. This file should be reviewed and updated for the final submission.
- [Architecture diagram](diagrams/architecture.mmd): Mermaid source showing the main application components.
Submission note: This README documents observed behavior. Before submitting, confirm that the model card includes the required reflections and that all documentation and diagram files are committed and pushed to GitHub.