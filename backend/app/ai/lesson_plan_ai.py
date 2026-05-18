import os
import json
import time 

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
    You are an educational assistant. [cite: 176]

    Generate complementary lesson recommendations based on the summary provided. [cite: 115, 118]
    
    CRITICAL: The values for "contents", "support_resources", and "tags" MUST be plain text strings. Do not use nested arrays or nested objects.

    Return ONLY valid JSON. [cite: 145]

    Format:
    {{
        "contents": "Line-separated list of topics to teach",
        "support_resources": "Line-separated list of materials or links",
        "tags": "tag1, tag2, tag3"
    }}

    Lesson title:
    {title}

    Discipline:
    {discipline}

    Summary:
    {summary}
    """

    start_time = time.time()

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

    latency = round(time.time() - start_time, 2)

    token_usage = response.usage.total_tokens if response.usage else 0

    print(f'[INFO] AI Request: Title="{title}", Discipline="{discipline}", Token Usage={token_usage}, Latency={latency}s.', flush=True)

    text = response.choices[0].message.content

    cleaned_text = text.replace(
        "```json",
        ""
    ).replace(
        "```",
        ""
    ).strip()

    try:
        raw_data = json.loads(cleaned_text)
        
        contents = raw_data.get("contents", "")
        if isinstance(contents, list):
            contents = "\n".join([str(item.get("topic", item)) if isinstance(item, dict) else str(item) for item in contents])
        elif isinstance(contents, dict):
            contents = json.dumps(contents)

        resources = raw_data.get("support_resources", "")
        if isinstance(resources, list):
            resources = "\n".join([str(item.get("resource", item)) if isinstance(item, dict) else str(item) for item in resources])
        elif isinstance(resources, dict):
            resources = json.dumps(resources)

        tags = raw_data.get("tags", "")
        if isinstance(tags, list):
            tags = ", ".join([str(t) for t in tags])
        elif isinstance(tags, dict):
            tags = ", ".join([str(v) for v in tags.values()])

        return {
            "contents": str(contents).strip(),
            "support_resources": str(resources).strip(),
            "tags": str(tags).strip()
        }

    except json.JSONDecodeError:
        return {
            "contents": "",
            "support_resources": "",
            "tags": ""
        }