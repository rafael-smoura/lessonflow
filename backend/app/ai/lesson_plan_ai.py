import os
import json

from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

client = OpenAI(
    api_key=os.getenv("GROQ_API_KEY"),
    base_url="https://api.groq.com/openai/v1"
)


def generate_lesson_plan_recommendations(
    title,
    discipline,
    summary
):

    prompt = f"""
    You are an educational assistant.

    Generate complementary lesson recommendations.

    Return ONLY valid JSON.

    Format:
    {{
        "contents": "...",
        "support_resources": "...",
        "tags": "tag1, tag2, tag3"
    }}

    Lesson title:
    {title}

    Discipline:
    {discipline}

    Summary:
    {summary}
    """

    response = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        response_format={"type": "json_object"},
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ]
    )

    text = response.choices[0].message.content

    cleaned_text = text.replace(
        "```json",
        ""
    ).replace(
        "```",
        ""
    ).strip()

    try:

        return json.loads(cleaned_text)

    except json.JSONDecodeError:

        return {
            "contents": "",
            "support_resources": "",
            "tags": ""
        }