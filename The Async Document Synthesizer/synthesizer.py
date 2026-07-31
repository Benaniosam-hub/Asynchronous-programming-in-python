import asyncio
import aiohttp
import time 
import os

GROQ_API_KEY = os.getenv("GROQ_API_KEY", "GROQ_API_KEY")

# Coroutine 1:
async def fetch_wikipedia_summary(session, topic):

    url = f"https://en.wikipedia.org/api/rest_v1/page/summary/{topic.strip().replace(' ','_').capitalize()}"
    headers = {"User-Agent": "MyAsyncSynthesizerBot/1.0 (contact: Yourmailid@gmail.com)"}
    print(f"[Worker 1] Fetching verified history for '{topic}' from Wikipedia...")

    async with session.get(url, headers=headers) as response:
        if response.status == 200:
            data = await response.json()
            print("[Worker 1] Wikipedia data successfully retrieved.")
            return data.get("extract","No summary found.")
        print ("[Worker 1] Failed to fetch Wikipedia data.")
        return "Alternative background history unavailable."
    
# Coroutine 2:
async def generate_ai_insights(session, topic):
    print(f"[Worker 2] Prompting AI Engine for conceptual analysis on '{topic}...")

    if "YOUR_GROQ_KEY" in GROQ_API_KEY or GROQ_API_KEY.startswith("PASTE"):
        await asyncio.sleep(2.0)
        return f"AI Insight: {topic} represents a paradigm shift in human technological scaling."
    url = "https://api.groq.com/openai/v1/chat/completions"
    headers = {"Authorization": f"Bearer {GROQ_API_KEY}", "Content-Type": "application/json"}
    payload = {
        "model": "llama-3.3-70b-versatile",
        "messages": [{"role": "user", "content": f"Explain the core cultural or scientific significance of {topic} in two sentences."}]
    }

    async with session.post(url, json=payload, headers=headers) as response:
        result = await response.json()
        print("[Worker 2] AI analysis complete.")
        return result["choices"][0]["message"]["content"]
    
    # Main 
async def main():
        target_topic = "Artificial Intelligence"
        start_time = time.time()

        async with aiohttp.ClientSession() as session:
            print(f"--- Launching Async Document Pipeline for: {target_topic} ---")

            tasks = [
                fetch_wikipedia_summary(session, target_topic),
                generate_ai_insights(session,target_topic)
            ]

            wiki_text, ai_text = await asyncio.gather(*tasks)

        end_time = time.time()

        # Synthesize the final document structure
        markdown_document = f"""
    # Report: {target_topic}
    *Generated asynchronously in {end_time - start_time:.2f} seconds*

    ## Verified Background Context (Wikipedia)
    {wiki_text}

    ## Advanced AI Insight
    {ai_text}
    """
        print("\n=============== GENERATED DOCUMENT ==================")
        print(markdown_document)
        print("=======================================================")

# Initialize the async event loop
asyncio.run(main())
