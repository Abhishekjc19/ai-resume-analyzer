# 🤖 AI Resume Analyzer

[![Python](https://img.shields.io/badge/Python-3.9+-blue.svg)](https://www.python.org/downloads/)
[![Streamlit](https://img.shields.io/badge/Streamlit-1.12+-red.svg)](https://streamlit.io/)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![Last Commit](https://img.shields.io/github/last-commit/yourusername/smart-resume-analyzer)](https://github.com/yourusername/smart-resume-analyzer)

> **Enhanced AI-powered resume analysis tool** that extracts insights, provides skill recommendations, and scores resumes using NLP and machine learning. Built with Streamlit and Python with improved security, modular architecture, and better user experience.

## ✨ Features

### 🔍 **Resume Analysis**
- **Smart Parsing**: Extract information from PDF resumes using advanced NLP
- **Skill Detection**: Automatically identify and categorize skills
- **Experience Level**: Determine candidate experience level (Fresher/Intermediate/Experienced)
- **Resume Scoring**: Comprehensive scoring system with detailed feedback

### 🎯 **Recommendations**
- **Skill Recommendations**: Get personalized skill suggestions based on your profile
- **Course Recommendations**: Curated learning resources for skill development
- **Job Role Prediction**: AI-powered field prediction (Data Science, Web Development, etc.)
- **Resume Tips**: Actionable advice to improve your resume

### 📊 **Analytics Dashboard**
- **User Analytics**: Track usage patterns and demographics
- **Performance Metrics**: Resume score distributions and trends
- **Geographic Insights**: Usage analytics by location
- **Export Capabilities**: Download data in CSV format

### 🔒 **Enhanced Security**
- **Environment Variables**: Secure configuration management
- **File Validation**: Comprehensive file type and size validation
- **Error Handling**: Robust error handling and logging
- **Database Security**: Secure database connections with proper authentication

## 🏗️ Architecture

### **Modular Design**
```
App/
├── config.py              # Configuration management
├── database.py            # Database operations
├── resume_analyzer.py     # Resume analysis logic
├── App.py                 # Main Streamlit application
├── Courses.py             # Course recommendations
└── requirements.txt       # Dependencies
```

### **Key Improvements**
- ✅ **Modular Architecture**: Separated concerns for better maintainability
- ✅ **Security Enhancements**: Environment variables and file validation
- ✅ **Error Handling**: Comprehensive logging and error management
- ✅ **Type Safety**: Type hints throughout the codebase
- ✅ **Configuration Management**: Centralized settings

## 🚀 Quick Start

### **Prerequisites**
- Python 3.9+
- MySQL Database
- Git

### **Installation**

1. **Clone the repository**
   ```bash
   git clone https://github.com/yourusername/smart-resume-analyzer.git
   cd smart-resume-analyzer/App
   ```

2. **Create virtual environment**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   python -m spacy download en_core_web_sm
   ```

4. **Setup environment variables**
   ```bash
   cp env_example.txt .env
   # Edit .env with your database credentials
   ```

5. **Setup database**
   ```sql
   CREATE DATABASE cv;
   ```

6. **Run the application**
   ```bash
   streamlit run App.py
   ```

## 🔧 Configuration

### **Environment Variables**
Create a `.env` file in the `App` directory:

```env
# Database Configuration
DB_HOST=localhost
DB_USER=root
DB_PASSWORD=your_password
DB_NAME=cv

# Admin Configuration
ADMIN_USERNAME=admin
ADMIN_PASSWORD=your_admin_password

# Application Configuration
UPLOAD_FOLDER=./Uploaded_Resumes/
MAX_FILE_SIZE=10485760
```

### **Customization**
- **Scoring Weights**: Modify scoring criteria in `config.py`
- **Skill Categories**: Add new skill categories and keywords
- **File Types**: Configure supported file formats

## 📊 Usage

### **For Users**
1. Navigate to the **User** section
2. Fill in your basic information
3. Upload your resume (PDF format)
4. Get instant analysis and recommendations
5. View your resume score and improvement tips

### **For Admins**
1. Navigate to the **Admin** section
2. Login with admin credentials
3. View user analytics and data
4. Export reports and insights
5. Monitor system performance

## 🛠️ Technology Stack

### **Frontend**
- [Streamlit](https://streamlit.io/) - Web application framework
- [Plotly](https://plotly.com/) - Interactive visualizations
- [HTML/CSS/JavaScript] - Custom styling and interactions

### **Backend**
- [Python](https://www.python.org/) - Core programming language
- [Streamlit](https://streamlit.io/) - Backend framework
- [PyMySQL](https://pymysql.readthedocs.io/) - Database connectivity

### **AI/ML**
- [spaCy](https://spacy.io/) - Natural language processing
- [NLTK](https://www.nltk.org/) - Text processing
- [pyresparser](https://github.com/OmkarPathak/pyresparser) - Resume parsing

### **Database**
- [MySQL](https://www.mysql.com/) - Relational database

## 📈 Features in Detail

### **Resume Scoring System**
- **Objective/Summary**: 6 points
- **Education**: 12 points
- **Experience**: 16 points
- **Internships**: 6 points
- **Skills**: 7 points
- **Hobbies**: 4 points
- **Interests**: 5 points
- **Achievements**: 13 points
- **Certifications**: 12 points
- **Projects**: 19 points

### **Supported Job Fields**
- **Data Science**: ML, Deep Learning, Analytics
- **Web Development**: Frontend, Backend, Full Stack
- **Android Development**: Mobile app development
- **iOS Development**: Apple ecosystem development
- **UI/UX Development**: Design and user experience

## 🔒 Security Features

- **Environment Variables**: Secure credential management
- **File Validation**: Type and size restrictions
- **Input Sanitization**: Protection against malicious inputs
- **Database Security**: Prepared statements and connection pooling
- **Error Logging**: Comprehensive audit trail

## 📝 API Documentation

### **Database Schema**

#### **user_data Table**
```sql
CREATE TABLE user_data (
    ID INT AUTO_INCREMENT PRIMARY KEY,
    sec_token VARCHAR(20) NOT NULL,
    ip_add VARCHAR(50),
    host_name VARCHAR(50),
    dev_user VARCHAR(50),
    os_name_ver VARCHAR(50),
    latlong VARCHAR(50),
    city VARCHAR(50),
    state VARCHAR(50),
    country VARCHAR(50),
    act_name VARCHAR(50) NOT NULL,
    act_mail VARCHAR(50) NOT NULL,
    act_mob VARCHAR(20) NOT NULL,
    Name VARCHAR(500) NOT NULL,
    Email_ID VARCHAR(500) NOT NULL,
    resume_score VARCHAR(8) NOT NULL,
    Timestamp VARCHAR(50) NOT NULL,
    Page_no VARCHAR(5) NOT NULL,
    Predicted_Field BLOB NOT NULL,
    User_level BLOB NOT NULL,
    Actual_skills BLOB NOT NULL,
    Recommended_skills BLOB NOT NULL,
    Recommended_courses BLOB NOT NULL,
    pdf_name VARCHAR(50) NOT NULL
);
```

## 🤝 Contributing

We welcome contributions! Please see our [Contributing Guidelines](CONTRIBUTING.md) for details.

### **How to Contribute**
1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.



## 📞 Support

- **Email**: [abhishekjc679@gmail.com.com]
- **Issues**: [GitHub Issues](https://github.com/yourusername/smart-resume-analyzer/issues)
- **Documentation**: [Wiki](https://github.com/yourusername/smart-resume-analyzer/wiki)

## 🚀 Roadmap

- [ ] **Enhanced File Support**: DOCX and other formats
- [ ] **API Development**: REST API for integration
- [ ] **Mobile App**: React Native mobile application
- [ ] **Advanced Analytics**: Machine learning insights
- [ ] **Multi-language Support**: Internationalization
- [ ] **Cloud Deployment**: AWS/Azure integration

---

<div align="center">
  <p>Made with ❤️ by <a href="https://github.com/Abhishekjc19">Abhishekjc</a></p>
  <p>⭐ Star this repository if you found it helpful!</p>
</div>
