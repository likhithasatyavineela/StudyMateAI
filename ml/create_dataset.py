import pandas as pd
import random

random.seed(42)

data = []

for _ in range(500):

    pages = random.randint(5, 50)

    words = pages * random.randint(180, 280)

    topics = max(2, pages // 4 + random.randint(-1, 2))

    difficulty = random.randint(1, 3)

    # Base study time according to pages
    study_time = pages * 0.08

    # Add extra time for more words
    study_time += words / 12000

    # Add extra time for more topics
    study_time += topics * 0.05

    # Difficulty adjustment
    if difficulty == 1:
        study_time += 0.3
    elif difficulty == 2:
        study_time += 0.7
    else:
        study_time += 1.2

    # Small random variation
    study_time += random.uniform(-0.2, 0.2)

    study_time = round(study_time, 2)

    data.append([
        pages,
        words,
        topics,
        difficulty,
        study_time
    ])

df = pd.DataFrame(
    data,
    columns=[
        "pages",
        "words",
        "topics",
        "difficulty",
        "study_time_hours"
    ]
)

df.to_csv("data/study_time_dataset.csv", index=False)

print("✅ New realistic dataset created successfully!")
print(df.head())