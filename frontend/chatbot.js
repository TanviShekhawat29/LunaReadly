// Elements
const chatButton = document.getElementById('chatbot-button');
const chatWindow = document.getElementById('chatbot-window');
const minimizeBtn = document.getElementById('minimize-btn');
const chatForm = document.getElementById('chatbot-form');
const chatInput = document.getElementById('chatbot-input');
const chatMessages = document.getElementById('chatbot-messages');

// Toggle chatbot window
chatButton.addEventListener('click', () => {
  chatWindow.classList.toggle('hidden');
});

// Minimize button
minimizeBtn.addEventListener('click', () => {
  chatWindow.classList.add('hidden');
});

// Handle message sending
chatForm.addEventListener('submit', async (e) => {
  e.preventDefault();
  const userMessage = chatInput.value.trim();
  if (!userMessage) return;

  appendMessage(userMessage, 'user-message');
  chatInput.value = '';

  try {
    const backendURL = window.location.hostname.includes("localhost")
  ? "http://127.0.0.1:5000/chat"
  : "https://lunareadly-2.onrender.com/chat";

    const res = await fetch(backendURL, {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ message: userMessage })
    });
    const data = await res.json();
    appendMessage(data.reply, 'bot-message');
  } catch (err) {
    appendMessage("Oops! Something went wrong 😓", 'bot-message');
  }
});

// Add message to DOM
function appendMessage(text, className) {
  const msg = document.createElement('div');
  msg.className = className;
  msg.textContent = text;
  chatMessages.appendChild(msg);
  chatMessages.scrollTop = chatMessages.scrollHeight;
}

// Dragging behavior
let isDragging = false, offsetX, offsetY;

chatWindow.addEventListener('mousedown', (e) => {
  if (e.target.closest('#chatbot-header')) {
    isDragging = true;
    offsetX = e.clientX - chatWindow.getBoundingClientRect().left;
    offsetY = e.clientY - chatWindow.getBoundingClientRect().top;
  }
});

document.addEventListener('mousemove', (e) => {
  if (isDragging) {
    chatWindow.style.left = `${e.clientX - offsetX}px`;
    chatWindow.style.top = `${e.clientY - offsetY}px`;
    chatWindow.style.right = 'auto';
    chatWindow.style.bottom = 'auto';
    chatWindow.style.position = 'fixed';
  }
});

document.addEventListener('mouseup', () => {
  isDragging = false;
});
