🩺 Dermo – AI-Powered Dermatology Assistant
An AI-based skin disease detection tool built with TensorFlow/Keras and a simple Tkinter GUI. The model can classify skin conditions such as Normal Skin, Acne, and Dermatophytosis, and provides quick reference links for more information.

Dermo is a desktop application that uses **deep learning** to assist in detecting common skin conditions such as:
- ✅ Normal Skin  
- ⚡ Acne  
- 🌱 Dermatophytosis

The project combines **TensorFlow/Keras** for AI-based image classification and a **Tkinter GUI** for user interaction.  
It allows users to upload a skin image, analyze it, and instantly receive predictions along with helpful resources.  

##

📌 Features
- 🖼️ Upload an image of skin for analysis.  
- 🤖 AI-powered classification using a pre-trained CNN model (`keras_model.h5`).  
- 🧾 Detects **Normal Skin**, **Acne**, and **Dermatophytosis**.  
- 🔗 Provides direct Wikipedia links for learning more about detected conditions.  
- 💻 Simple, interactive Tkinter-based GUI.  

##

📂 Project Structure

├── dermo.py # Main application with GUI + AI model integration </br>
├── keras_model.h5 # Pre-trained Keras model for skin condition detection </br>
├── Use of ai in dermatology.pptx # Project presentation </br>
├── README.md # Project documentation </br>

##

🚀 Installation & Usage

1. Clone the repository
git clone https://github.com/HimanshuChauragade/dermo.git

2. cd dermo

3. Install dependencies </br>
Make sure you have Python 3.8+ installed.  </br>
Then run:
pip install tensorflow opencv-python numpy

4. Run the application
python dermo.py

4. Usage
Click Browse... to select an image (.jpg, .jpeg, .png, .svg). </br> </br>
The AI model will classify the skin condition. </br>
The result will be shown in the GUI, and you can click on links to learn more.

##

## 🔮 Future Improvements

- Expand the dataset to include more skin conditions (e.g., Eczema, Psoriasis, Melanoma).  
- Improve model accuracy with advanced CNN architectures and transfer learning.  
- Add real-time camera input for instant skin analysis.  
- Enhance GUI design with modern frameworks (e.g., PyQt, Tkinter themes).  
- Provide multilingual support for global accessibility.  
- Integrate with cloud services for remote predictions and data storage.  

## 🤝 Contributing

Contributions are welcome! Here's how you can help:

1. **Fork the repository**
2. **Create a feature branch**: `git checkout -b feature/amazing-feature`
3. **Commit your changes**: `git commit -m 'Add amazing feature'`
4. **Push to the branch**: `git push origin feature/amazing-feature`
5. **Open a Pull Request**

## 👨‍💻 Development Guidelines

- Follow Python best practices for clean and maintainable code.  
- Use virtual environments to manage dependencies (`venv` or `conda`).  
- Keep commit messages clear, concise, and meaningful.  
- Test the application across different operating systems before merging.  
- Document new features or changes in the README.  
- Ensure the model file (`keras_model.h5`) is version-controlled separately or linked via release.  


## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- **TensorFlow/Keras** – for deep learning model development.  
- **OpenCV & NumPy** – for image processing and numerical computations.  
- **Tkinter** – for building the interactive desktop GUI.  
- **Wikipedia** – for providing open-access resources linked in the app.  
- Inspiration from real-world applications of AI in medical diagnostics.  

## 📞 Contact

- **GitHub**: [@HimanshuChauragade](https://github.com/HimanshuChauragade)
- **LinkedIn**: [Himanshu Chauragade](https://linkedin.com/in/himanshu-chauragade/)
- **Email**: 2024000129@mssu.ac.in

##

⭐ **Star this repository if you found it helpful!**
