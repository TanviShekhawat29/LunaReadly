from flask import Flask, request, jsonify
from flask_cors import CORS
from ibm_watson import AssistantV2
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
import requests
import random
import os
from dotenv import load_dotenv
import traceback

load_dotenv()

app = Flask(__name__)
CORS(app)

# IBM Watson Setup
WATSON_API_KEY = os.getenv("WATSON_API_KEY")
WATSON_URL = os.getenv("WATSON_URL")
ASSISTANT_ID = os.getenv("WATSON_ASSISTANT_ID")

authenticator = IAMAuthenticator(WATSON_API_KEY)
assistant = AssistantV2(
    version='2021-11-27',
    authenticator=authenticator
)
assistant.set_service_url(WATSON_URL)

# Session setup
session_id = assistant.create_session(assistant_id=ASSISTANT_ID).get_result()['session_id']

# Greeting/help/goodbye replies
GREETING_REPLIES = ["Hi!", "Hey reader!", "Hello! Ready for a good book?", "Hi there 📚"]
HELP_REPLIES = ["I can recommend books by mood, genre, author...", "Need a thriller or a romantic classic? Just ask!", "Tell me your mood or favorite author 💡"]
GOODBYE_REPLIES = ["Thanks for visiting LunaReadly 💖", "See you again soon!", "Goodbye! Happy reading 📚"]

# Mapping moods to genres
MOOD_GENRE_MAP = {
    "happy": "comedy",
    "sad": "inspiring",
    "romantic": "romance",
    "dark": "thriller",
    "relaxed": "drama",
    "angry": "action",
    "inspiring": "biography",
    "adventurous": "adventure"
}

@app.route('/chat', methods=['POST'])
def chat():
    user_input = request.json.get('message')
    print("📥 User Message:", user_input)

    try:
        response = assistant.message(
            assistant_id=ASSISTANT_ID,
            session_id=session_id,
            input={'message_type': 'text', 'text': user_input}
        ).get_result()

        print("🧠 Watson Full Response:")
        print(response)

        intent = response['output']['intents'][0]['intent'] if response['output']['intents'] else None
        entities = response['output'].get('entities', [])

        entity_dict = {e['entity']: e['value'] for e in entities}

        genre = entity_dict.get("genre")
        mood = entity_dict.get("mood")
        age = entity_dict.get("age")
        rating = entity_dict.get("rating")
        author = entity_dict.get("author")

        # Author alias cleanup
        if author:
            author = author.lower().replace(".", "").replace(" ", "+")
            author_aliases = {
                "j+k+rowling": "jk+rowling",
                "paulo+coelho": "paulo+coelho",
                "chetan+bhagat": "chetan+bhagat",
                "stephen+king": "stephen+king",
                "agatha+christie": "agatha+christie",
                "george+orwell": "george+orwell",
                "dan+brown": "dan+brown",
                "neil+gaiman": "neil+gaiman",
                "colleen+hoover": "colleen+hoover"
            }
            author = author_aliases.get(author, author)

        # Fallback genre if mood is present
        if mood and not genre:
            genre = MOOD_GENRE_MAP.get(mood.lower())

        # Handle special replies
        if intent == "greeting":
            return jsonify({"reply": random.choice(GREETING_REPLIES)})
        elif intent == "help":
            return jsonify({"reply": random.choice(HELP_REPLIES)})
        elif intent == "goodbye":
            return jsonify({"reply": random.choice(GOODBYE_REPLIES)})

        # For book recommendation intents
        if intent and "recommend" in intent:
            query_parts = []

            if genre:
                query_parts.append(f"subject:{genre}")
            if author:
                query_parts.append(f"inauthor:{author}")
            if age:
                if "child" in age:
                    query_parts.append("subject:children")
                elif "teen" in age:
                    query_parts.append("subject:teen")
                elif "adult" in age:
                    query_parts.append("subject:adult")

            query = "+".join(query_parts) or "bestsellers"

            url = f"https://www.googleapis.com/books/v1/volumes?q={query}&key={os.getenv('GOOGLE_BOOKS_API_KEY')}&maxResults=10"
            result = requests.get(url)

            if result.status_code == 200:
                data = result.json()
                books = data.get("items", [])

                # Optional: Filter for 4+ rating
                if rating == "high":
                    books = [b for b in books if b.get("volumeInfo", {}).get("averageRating", 0) >= 4]

                if books:
                    selected_books = random.sample(books, min(len(books), 2))
                    reply_texts = []

                    for book in selected_books:
                        info = book['volumeInfo']
                        title = info.get("title", "Untitled")
                        authors = ", ".join(info.get("authors", ["Unknown Author"]))
                        reply_texts.append(f"📚 *{title}* by {authors}")

                    return jsonify({"reply": "\n".join(reply_texts)})

                else:
                    return jsonify({"reply": "Hmm, I couldn’t find anything matching that. Want to try a different genre or author?"})
            else:
                print("❌ Google Books API failed:", result.status_code)
                return jsonify({"reply": "Oops! I couldn’t fetch books right now. Try again later!"})

        # Fallback
        fallback_text = response['output']['generic'][0]['text']
        return jsonify({"reply": fallback_text})

    except Exception as e:
        print("❌ Error:", str(e))
        traceback.print_exc()
        return jsonify({"reply": "Luna: Sorry, something went wrong 😓"})

if __name__ == '__main__':
    app.run(debug=True)
