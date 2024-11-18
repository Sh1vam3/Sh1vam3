# HealthPredict - AI-Powered Heart Disease Prediction Platform

![Model Accuracy](https://img.shields.io/badge/Model%20Accuracy-92.5%25-brightgreen)
![License](https://img.shields.io/badge/license-MIT-blue)

HealthPredict is a modern web-based platform that uses artificial intelligence to assess heart disease risk factors. Built with a focus on accuracy and user experience, it provides instant health risk assessments based on clinical parameters.

## 🌟 Features

- **AI-Powered Analysis**: Advanced machine learning model with 92.5% accuracy
- **Real-time Assessment**: Instant heart disease risk prediction
- **Modern UI/UX**: Clean, responsive design optimized for all devices
- **Secure**: Built with security and privacy in mind
- **Interactive Dashboard**: User-friendly interface for inputting health data
- **Professional Reports**: Clear presentation of assessment results

## 🚀 Tech Stack

- **Frontend**:
  - HTML5
  - CSS3 (with Tailwind CSS)
  - JavaScript (Vanilla JS)
  - Custom SVG icons
  - Responsive design patterns

- **Backend** (Required for full functionality):
  - Python Flask server
  - Machine Learning model (Scikit-learn)
  - RESTful API endpoints

## 📋 Prerequisites

- Modern web browser (Chrome, Firefox, Safari, Edge)
- Python 3.8+ (for backend)
- Node.js and npm (for development)

## 💻 Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/yourusername/healthpredict.git
   cd healthpredict
   ```

2. **Set up the frontend**
   ```bash
   # If you're using a development server
   npm install -g live-server
   live-server
   ```

3. **Set up the backend**
   ```bash
   # Create a virtual environment
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   
   # Install dependencies
   pip install -r requirements.txt
   
   # Start the Flask server
   python app.py
   ```

## 🔧 Configuration

The application connects to a Flask backend server by default at `http://127.0.0.1:5000`. To modify this:

1. Open `index.html`
2. Locate the fetch request URL in the JavaScript section
3. Update the URL to match your backend server address

## 📊 API Endpoints

### Prediction Endpoint
- **URL**: `/predict`
- **Method**: `POST`
- **Data Parameters**:
  ```json
  {
    "age": number,
    "cp": number,
    "thalach": number
  }
  ```
- **Success Response**:
  ```json
  {
    "prediction": "string"
  }
  ```

## 🎯 Usage

1. Open the application in your web browser
2. Enter the required health parameters:
   - Age
   - Chest Pain Type (0-3)
   - Maximum Heart Rate
3. Click "Get Assessment" to receive your results
4. Review the detailed analysis provided

## 🛠️ Development

### File Structure
```
healthpredict/
├── index.html          # Main application file
├── styles/             # CSS styles
├── scripts/            # JavaScript files
├── assets/            # Images and icons
├── backend/           # Python Flask server
│   ├── app.py        # Server implementation
│   └── model/        # ML model files
└── README.md         # This file
```

### Contributing
1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📜 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 👥 Team

- **Shivam** - *Lead Developer*
- **Shagun** - *UI/UX Designer*

## 🙏 Acknowledgments

- Modern UI inspiration from current healthcare platforms
- Tailwind CSS for the styling framework
- Medical professionals for their input on risk factors

## 📞 Support

For support, email support@healthpredict.com or open an issue in the repository.

## 🔮 Future Enhancements

- [ ] Additional health parameters for more accurate predictions
- [ ] User accounts and history tracking
- [ ] Detailed health reports with recommendations
- [ ] Integration with wearable devices
- [ ] Multi-language support
- [ ] Mobile application

## ⚠️ Disclaimer

This tool is for educational and informational purposes only. It should not be used as a substitute for professional medical advice, diagnosis, or treatment. Always seek the advice of your physician or other qualified health provider with any questions you may have regarding a medical condition.

<!---
Sh1vam3/Sh1vam3 is a ✨ special ✨ repository because its `README.md` (this file) appears on your GitHub profile.
You can click the Preview link to take a look at your changes.
--->
