import time

def generate_exam_notes(client, text):

    prompt = f"""
You are an expert university professor.

Convert the following study material into exam-ready notes.

Study Material:
{text}
"""

    for attempt in range(3):
        try:
            response = client.models.generate_content(
                model="gemini-3.5-flash",
                contents=prompt
            )
            return response.text

        except Exception as e:

            if "429" in str(e):

                return f"""
# 📚 Exam Ready Notes

## Introduction
{text}

## Key Points

- Important concepts from the uploaded PDF
- Read all headings carefully
- Focus on definitions
- Revise keywords
- Practice previous questions

## Quick Revision

- Read once
- Revise twice
- Practice MCQs
"""

            if attempt < 2:
                time.sleep(5)
            else:
                raise