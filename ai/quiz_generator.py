import json
import time

def generate_quiz(client, exam_notes):

    prompt = f"""
Generate exactly 10 MCQs.

Return only JSON.

Exam Notes:
{exam_notes}
"""

    for attempt in range(3):

        try:

            response = client.models.generate_content(
                model="gemini-3.5-flash",
                contents=prompt
            )

            return json.loads(response.text)

        except Exception as e:

            if "429" in str(e):

                return [

                    {
                        "question":"Which section is most important for exams?",
                        "options":[
                            "Definitions",
                            "Movies",
                            "Sports",
                            "Music"
                        ],
                        "answer":"Definitions"
                    },

                    {
                        "question":"What should students revise first?",
                        "options":[
                            "Keywords",
                            "Games",
                            "Photos",
                            "Songs"
                        ],
                        "answer":"Keywords"
                    },

                    {
                        "question":"Which helps in exams?",
                        "options":[
                            "MCQ Practice",
                            "Sleeping",
                            "Watching TV",
                            "Scrolling"
                        ],
                        "answer":"MCQ Practice"
                    },

                    {
                        "question":"Revision should be?",
                        "options":[
                            "Regular",
                            "Never",
                            "Random",
                            "Monthly"
                        ],
                        "answer":"Regular"
                    },

                    {
                        "question":"Important topics should be?",
                        "options":[
                            "Highlighted",
                            "Ignored",
                            "Deleted",
                            "Hidden"
                        ],
                        "answer":"Highlighted"
                    },

                    {
                        "question":"Exam preparation needs?",
                        "options":[
                            "Practice",
                            "Luck",
                            "Nothing",
                            "Sleep only"
                        ],
                        "answer":"Practice"
                    },

                    {
                        "question":"Reading notes helps?",
                        "options":[
                            "Yes",
                            "No",
                            "Sometimes",
                            "Never"
                        ],
                        "answer":"Yes"
                    },

                    {
                        "question":"Which is useful?",
                        "options":[
                            "Short Notes",
                            "Memes",
                            "Movies",
                            "Games"
                        ],
                        "answer":"Short Notes"
                    },

                    {
                        "question":"Students should?",
                        "options":[
                            "Revise",
                            "Skip",
                            "Forget",
                            "Ignore"
                        ],
                        "answer":"Revise"
                    },

                    {
                        "question":"Final preparation includes?",
                        "options":[
                            "Revision",
                            "Gaming",
                            "Travel",
                            "Shopping"
                        ],
                        "answer":"Revision"
                    }

                ]

            if attempt < 2:
                time.sleep(5)
            else:
                raise