🩺 Dermo – AI-Powered Dermatology Assistant
An AI-based skin disease detection tool built with TensorFlow/Keras and a simple Tkinter GUI. The model can classify skin conditions such as Normal Skin, Acne, and Dermatophytosis, and provides quick reference links for more information.

Dermo is a desktop application that uses **deep learning** to assist in detecting common skin conditions such as:
- ✅ Normal Skin  
- ⚡ Acne  
- 🌱 Dermatophytosis

The project combines **TensorFlow/Keras** for AI-based image classification and a **Tkinter GUI** for user interaction.  
It allows users to upload a skin image, analyze it, and instantly receive predictions along with helpful resources.  

---

📌 Features
- 🖼️ Upload an image of skin for analysis.  
- 🤖 AI-powered classification using a pre-trained CNN model (`keras_model.h5`).  
- 🧾 Detects **Normal Skin**, **Acne**, and **Dermatophytosis**.  
- 🔗 Provides direct Wikipedia links for learning more about detected conditions.  
- 💻 Simple, interactive Tkinter-based GUI.  

---

📂 Project Structure

├── dermo.py # Main application with GUI + AI model integration

├── keras_model.h5 # Pre-trained Keras model for skin condition detection

├── Use of ai in dermatology.pptx # Project presentation

├── README.md # Project documentation

---

🚀 Installation & Usage

1. Clone the repository
git clone https://github.com/HimanshuChauragade/dermo.git

2. cd dermo

3. Install dependencies

Make sure you have Python 3.8+ installed. Then run:
pip install tensorflow opencv-python numpy

4. Run the application
python dermo.py

4. Usage
Click Browse... to select an image (.jpg, .jpeg, .png, .svg).

The AI model will classify the skin condition.

The result will be shown in the GUI, and you can click on links to learn more.
