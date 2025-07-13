import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

class Config:
    # Database Configuration
    DB_HOST = os.getenv('DB_HOST', 'localhost')
    DB_USER = os.getenv('DB_USER', 'root')
    DB_PASSWORD = os.getenv('DB_PASSWORD', 'root@MySQL4admin')
    DB_NAME = os.getenv('DB_NAME', 'cv')
    
    # Admin Configuration
    ADMIN_USERNAME = os.getenv('ADMIN_USERNAME', 'admin')
    ADMIN_PASSWORD = os.getenv('ADMIN_PASSWORD', 'admin@resume-analyzer')
    
    # Application Configuration
    UPLOAD_FOLDER = os.getenv('UPLOAD_FOLDER', './Uploaded_Resumes/')
    MAX_FILE_SIZE = int(os.getenv('MAX_FILE_SIZE', 10 * 1024 * 1024))  # 10MB
    ALLOWED_EXTENSIONS = {'pdf', 'docx', 'doc'}
    
    # Resume Scoring Weights
    SCORING_WEIGHTS = {
        'objective': 6,
        'education': 12,
        'experience': 16,
        'internships': 6,
        'skills': 7,
        'hobbies': 4,
        'interests': 5,
        'achievements': 13,
        'certifications': 12,
        'projects': 19
    }
    
    # Skill Categories
    SKILL_CATEGORIES = {
        'data_science': {
            'keywords': ['tensorflow', 'keras', 'pytorch', 'machine learning', 'deep learning', 'flask', 'streamlit'],
            'recommended_skills': ['Data Visualization', 'Predictive Analysis', 'Statistical Modeling', 'Data Mining', 'Clustering & Classification', 'Data Analytics', 'Quantitative Analysis', 'Web Scraping', 'ML Algorithms', 'Keras', 'Pytorch', 'Probability', 'Scikit-learn', 'Tensorflow', 'Flask', 'Streamlit']
        },
        'web_development': {
            'keywords': ['react', 'django', 'node js', 'react js', 'php', 'laravel', 'magento', 'wordpress', 'javascript', 'angular js', 'c#', 'asp.net', 'flask'],
            'recommended_skills': ['React', 'Django', 'Node JS', 'React JS', 'php', 'laravel', 'Magento', 'wordpress', 'Javascript', 'Angular JS', 'c#', 'Flask', 'SDK']
        },
        'android_development': {
            'keywords': ['android', 'android development', 'flutter', 'kotlin', 'xml', 'kivy'],
            'recommended_skills': ['Android', 'Android development', 'Flutter', 'Kotlin', 'XML', 'Java', 'Kivy', 'GIT', 'SDK', 'SQLite']
        },
        'ios_development': {
            'keywords': ['ios', 'ios development', 'swift', 'cocoa', 'cocoa touch', 'xcode'],
            'recommended_skills': ['IOS', 'IOS Development', 'Swift', 'Cocoa', 'Cocoa Touch', 'Xcode', 'Objective-C', 'SQLite', 'Plist', 'StoreKit', 'UI-Kit', 'AV Foundation', 'Auto-Layout']
        },
        'uiux_development': {
            'keywords': ['ux', 'adobe xd', 'figma', 'zeplin', 'balsamiq', 'ui', 'prototyping', 'wireframes', 'storyframes', 'adobe photoshop', 'photoshop', 'editing', 'adobe illustrator', 'illustrator', 'adobe after effects', 'after effects', 'adobe premier pro', 'premier pro', 'adobe indesign', 'indesign', 'wireframe', 'solid', 'grasp', 'user research', 'user experience'],
            'recommended_skills': ['UI', 'User Experience', 'Adobe XD', 'Figma', 'Zeplin', 'Balsamiq', 'Prototyping', 'Wireframes', 'Storyframes', 'Adobe Photoshop', 'Editing', 'Illustrator', 'After Effects', 'Premier Pro', 'Indesign', 'Wireframe', 'Solid', 'Grasp', 'User Research']
        }
    } 