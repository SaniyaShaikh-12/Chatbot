The chatbot/ directory contains a Python-based AI chatbot that helps users interact with the bookstore. It uses Flask for the backend and NLTK for natural language processing. A pre-trained model is saved to assist users with their queries.

📂 Folder Structure
chatbot/
├── app.py            # Flask server to host chatbot on web
├── chat.py           # Command-line chatbot interface
├── train.py          # Trains model based on intents.json
├── model.py          # Defines the neural network model
├── intents.json      # Contains training data/intents
├── data.pth          # Trained model (created after training)
├── templates/
│   └── index.html    # Frontend page (Flask)
└── static/           # Optional static files (e.g., CSS, JS)

⚙️ Installation Steps
🚨 Make sure Python (3.6+) is installed on your system.

✅ Step 1: Check Python Version
python --version

✅ Step 2: Create Virtual Environment
# Create a virtual environment named 'venv'
python -m venv venv

✅ Step 3: Activate Virtual Environment
# For Windows
venv\Scripts\activate

✅ Step 4: Verify Virtual Environment
python -c "import sys; print(sys.prefix)"
The printed path should point to your venv folder.

✅ Step 5: Install Required Libraries
pip install flask torch torchvision nltk

✅ Step 6: Download NLTK Data
Enter Python shell:
python
Then:
import nltk
nltk.download('punkt')
exit()

✅ Step 7: Train the Chatbot Model
python train.py
After training, a file named data.pth will be created automatically. It stores the trained model.  

✅ Step 8: Run the Chatbot 
python chat.py

✅ Step 9: Run the Chatbot 
python app.py
Then open http://127.0.0.1:5000/ in your browser to use the chatbot via UI.

