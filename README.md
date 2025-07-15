# LunaReadly
LunaReadly is a smart, elegant, and conversational book recommendation platform designed to make reading discovery delightful, meaningful, and personalized. Powered by IBM Watson Assistant and the Google Books API, LunaReadly helps users find books that match their mood, genre preferences, age group, favorite authors, or desired popularity rating — all through natural, friendly conversation.
Whether you're a child looking for adventure, a teen in the mood for drama, or an adult seeking something inspiring — LunaReadly understands your context and curates live book suggestions that match your needs in real time.

<img width="421" height="522" alt="image" src="https://github.com/user-attachments/assets/6f6d711a-3015-4ca6-92a8-6a3e397b4830" />

## Why LunaReadly?

•	Modern readers are overwhelmed with choices. Most platforms rely on static reviews or basic search filters. LunaReadly reimagines this experience by:

•	Using live data from Google Books API to fetch only the freshest, trending, and top-rated books

•	Providing an AI-powered conversational interface using IBM Watson Assistant with rich intents and entity recognition

•	Understanding user context such as “I’m feeling sad, suggest a book” or “Any books by Dan Brown?”

•	Offering a delightfully aesthetic interface with a soft pastel theme, draggable floating chatbot, and smooth transitions

•	Supporting multi-intent understanding and offering multiple or single book suggestions, depending on the query

•	Being fully deployable on platforms like Replit, Render, or local servers — ready for professional use or presentations

## Key Features

1.	Natural Language Book Recommendations

•	Supports queries like:

	“Suggest a light-hearted book for teens”

	“I want something romantic and dramatic”

	“Books by J.K. Rowling please”

	“I’m angry. Recommend something intense”

2.	Real-time Suggestions

•	Live integration with Google Books API

•	Dynamic filtering based on genre, mood, age, author, and rating

3.	Watson-Powered Chatbot

•	IBM Watson Assistant (Classic Experience)

•	Intents + Entities trained via CSV import

•	Handles greetings, help, goodbye, and 7+ book recommendation contexts

4.	Intelligent Frontend

•	Floating, draggable chat widget

•	Luna avatar image with chat bubbles

•	Soft fonts, rounded corners, classy and clean layout

5.	Custom Dialog + Random Responses

•	Watson Assistant dialog nodes return random replies for:

•	Greeting: "Hi there! Ready to read something new?"

•	Help: "You can ask me for books by mood, author, or genre!"

•	Goodbye: "Take care! Come back soon for another story."

6.	Fully Functional Backend

•	Flask + Python backend handles chat requests

•	Watson API + Google Books API logic

•	Filters based on entities using fuzzy matching

## IBM Watson Setup

<img width="1226" height="293" alt="image" src="https://github.com/user-attachments/assets/0a978683-e2a8-4a1f-84cf-420cfdc3d437" />

LunaReadly uses IBM Watson Assistant (Classic Experience) with:

•	Intents including:

o	recommend_by_genre

o	recommend_by_author

o	recommend_by_age

o	recommend_by_mood

o	recommend_by_rating

o	greeting, help, goodbye

<img width="1827" height="734" alt="image" src="https://github.com/user-attachments/assets/8ec4513d-c680-4d67-b355-1ec02aa7f14c" />

•	Entities including:

o	genre: fantasy, thriller, romance, horror, sci-fi, etc.

o	mood: happy, sad, light-hearted, angry, romantic, etc.

o	age: kids, teens, adult

o	rating: high, medium, low

<img width="1865" height="807" alt="image" src="https://github.com/user-attachments/assets/88281a2b-5d85-468f-bb61-0fd9b4694291" />

Dialog Nodes are designed to return intelligent replies, fallback handling, and personalized prompts to guide users.

<img width="1919" height="795" alt="image" src="https://github.com/user-attachments/assets/18641522-4b69-4fac-82a8-c7f2fdc43dcd" />

## AI Logic in Backend

•	Extracts entities from Watson response

•	Maps genre, mood, age_group, rating, or author to Google Books search parameters

•	Fuzzy matches if exact results aren’t found (e.g., "thriller" ≈ "suspense")

•	Filters and sorts results based on real-time data

•	Responds with one or multiple books with title, author, and description

## UI/UX & Aesthetics

•	Built using HTML, CSS, JS with bubbly, clean, pastel aesthetic

•	Sections: Home, Features, Genres, How it Works, About

•	Floating chatbot with Luna avatar, drag + close/open, smooth transitions

•	Mobile-responsive and lightweight for all browsers

<img width="1919" height="1022" alt="image" src="https://github.com/user-attachments/assets/073ed311-ecf1-4fc9-889f-0a79cdc78a4d" />

## Complete Website with Chatbot


## Conclusion

LunaReadly isn’t just a chatbot — it’s a smart literary companion.

Built with care and technology, it brings personality to reading recommendations and delivers an internship-grade user experience with real-time intelligence. Whether deployed in a hackathon, internship showcase, or portfolio, LunaReadly is designed to stand out.
