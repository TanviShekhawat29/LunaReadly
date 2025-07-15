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
