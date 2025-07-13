import re
import time
from typing import Dict, List, Tuple, Optional
from config import Config
import logging

logger = logging.getLogger(__name__)

class ResumeAnalyzer:
    def __init__(self):
        self.scoring_weights = Config.SCORING_WEIGHTS
        self.skill_categories = Config.SKILL_CATEGORIES
    
    def analyze_experience_level(self, resume_text: str, no_of_pages: int) -> Tuple[str, str]:
        """
        Analyze candidate experience level based on resume content
        Returns: (level, message)
        """
        try:
            if no_of_pages < 1:
                return "NA", "You are at Fresher level!"
            
            # Check for internship experience
            internship_keywords = ['INTERNSHIP', 'INTERNSHIPS', 'Internship', 'Internships']
            if any(keyword in resume_text for keyword in internship_keywords):
                return "Intermediate", "You are at intermediate level!"
            
            # Check for work experience
            experience_keywords = ['EXPERIENCE', 'WORK EXPERIENCE', 'Experience', 'Work Experience']
            if any(keyword in resume_text for keyword in experience_keywords):
                return "Experienced", "You are at experience level!"
            
            return "Fresher", "You are at Fresher level!"
            
        except Exception as e:
            logger.error(f"Error analyzing experience level: {str(e)}")
            return "Fresher", "Unable to determine experience level"
    
    def analyze_skills(self, skills: List[str]) -> Tuple[str, List[str], str]:
        """
        Analyze skills and recommend field and additional skills
        Returns: (field, recommended_skills, message)
        """
        try:
            for skill in skills:
                skill_lower = skill.lower()
                
                # Check each skill category
                for category, data in self.skill_categories.items():
                    if skill_lower in data['keywords']:
                        field_name = category.replace('_', ' ').title()
                        return field_name, data['recommended_skills'], f"Our analysis says you are looking for {field_name} Jobs."
            
            # No specific field found
            return "NA", ["No Recommendations"], "Currently our tool only predicts and recommends for Data Science, Web, Android, IOS and UI/UX Development"
            
        except Exception as e:
            logger.error(f"Error analyzing skills: {str(e)}")
            return "NA", ["Error in skill analysis"], "Error occurred during skill analysis"
    
    def calculate_resume_score(self, resume_text: str) -> Tuple[int, List[Dict]]:
        """
        Calculate resume score based on content analysis
        Returns: (total_score, score_details)
        """
        try:
            score = 0
            score_details = []
            
            # Check for Objective/Summary
            if any(keyword in resume_text for keyword in ['Objective', 'Summary']):
                score += self.scoring_weights['objective']
                score_details.append({
                    'component': 'Objective/Summary',
                    'score': self.scoring_weights['objective'],
                    'status': 'Present',
                    'message': 'Awesome! You have added Objective/Summary'
                })
            else:
                score_details.append({
                    'component': 'Objective/Summary',
                    'score': 0,
                    'status': 'Missing',
                    'message': 'Please add your career objective, it will give your career intention to the Recruiters.'
                })
            
            # Check for Education
            if any(keyword in resume_text for keyword in ['Education', 'School', 'College']):
                score += self.scoring_weights['education']
                score_details.append({
                    'component': 'Education',
                    'score': self.scoring_weights['education'],
                    'status': 'Present',
                    'message': 'Awesome! You have added Education Details'
                })
            else:
                score_details.append({
                    'component': 'Education',
                    'score': 0,
                    'status': 'Missing',
                    'message': 'Please add Education. It will give Your Qualification level to the recruiter'
                })
            
            # Check for Experience
            if any(keyword in resume_text for keyword in ['EXPERIENCE', 'Experience']):
                score += self.scoring_weights['experience']
                score_details.append({
                    'component': 'Experience',
                    'score': self.scoring_weights['experience'],
                    'status': 'Present',
                    'message': 'Awesome! You have added Experience'
                })
            else:
                score_details.append({
                    'component': 'Experience',
                    'score': 0,
                    'status': 'Missing',
                    'message': 'Please add Experience. It will help you to stand out from crowd'
                })
            
            # Check for Internships
            internship_keywords = ['INTERNSHIPS', 'INTERNSHIP', 'Internships', 'Internship']
            if any(keyword in resume_text for keyword in internship_keywords):
                score += self.scoring_weights['internships']
                score_details.append({
                    'component': 'Internships',
                    'score': self.scoring_weights['internships'],
                    'status': 'Present',
                    'message': 'Awesome! You have added Internships'
                })
            else:
                score_details.append({
                    'component': 'Internships',
                    'score': 0,
                    'status': 'Missing',
                    'message': 'Please add Internships. It will help you to stand out from crowd'
                })
            
            # Check for Skills
            skills_keywords = ['SKILLS', 'SKILL', 'Skills', 'Skill']
            if any(keyword in resume_text for keyword in skills_keywords):
                score += self.scoring_weights['skills']
                score_details.append({
                    'component': 'Skills',
                    'score': self.scoring_weights['skills'],
                    'status': 'Present',
                    'message': 'Awesome! You have added Skills'
                })
            else:
                score_details.append({
                    'component': 'Skills',
                    'score': 0,
                    'status': 'Missing',
                    'message': 'Please add Skills. It will help you a lot'
                })
            
            # Check for Hobbies
            if any(keyword in resume_text for keyword in ['HOBBIES', 'Hobbies']):
                score += self.scoring_weights['hobbies']
                score_details.append({
                    'component': 'Hobbies',
                    'score': self.scoring_weights['hobbies'],
                    'status': 'Present',
                    'message': 'Awesome! You have added your Hobbies'
                })
            else:
                score_details.append({
                    'component': 'Hobbies',
                    'score': 0,
                    'status': 'Missing',
                    'message': 'Please add Hobbies. It will show your personality to the Recruiters'
                })
            
            # Check for Interests
            if any(keyword in resume_text for keyword in ['INTERESTS', 'Interests']):
                score += self.scoring_weights['interests']
                score_details.append({
                    'component': 'Interests',
                    'score': self.scoring_weights['interests'],
                    'status': 'Present',
                    'message': 'Awesome! You have added your Interest'
                })
            else:
                score_details.append({
                    'component': 'Interests',
                    'score': 0,
                    'status': 'Missing',
                    'message': 'Please add Interest. It will show your interest other that job'
                })
            
            # Check for Achievements
            if any(keyword in resume_text for keyword in ['ACHIEVEMENTS', 'Achievements']):
                score += self.scoring_weights['achievements']
                score_details.append({
                    'component': 'Achievements',
                    'score': self.scoring_weights['achievements'],
                    'status': 'Present',
                    'message': 'Awesome! You have added your Achievements'
                })
            else:
                score_details.append({
                    'component': 'Achievements',
                    'score': 0,
                    'status': 'Missing',
                    'message': 'Please add Achievements. It will show that you are capable for the required position'
                })
            
            # Check for Certifications
            if any(keyword in resume_text for keyword in ['CERTIFICATIONS', 'Certifications', 'Certification']):
                score += self.scoring_weights['certifications']
                score_details.append({
                    'component': 'Certifications',
                    'score': self.scoring_weights['certifications'],
                    'status': 'Present',
                    'message': 'Awesome! You have added your Certifications'
                })
            else:
                score_details.append({
                    'component': 'Certifications',
                    'score': 0,
                    'status': 'Missing',
                    'message': 'Please add Certifications. It will show that you have done some specialization'
                })
            
            # Check for Projects
            if any(keyword in resume_text for keyword in ['PROJECTS', 'PROJECT', 'Projects', 'Project']):
                score += self.scoring_weights['projects']
                score_details.append({
                    'component': 'Projects',
                    'score': self.scoring_weights['projects'],
                    'status': 'Present',
                    'message': 'Awesome! You have added your Projects'
                })
            else:
                score_details.append({
                    'component': 'Projects',
                    'score': 0,
                    'status': 'Missing',
                    'message': 'Please add Projects. It will show that you have done work related the required position'
                })
            
            return score, score_details
            
        except Exception as e:
            logger.error(f"Error calculating resume score: {str(e)}")
            return 0, []
    
    def validate_file(self, uploaded_file) -> Tuple[bool, str]:
        """
        Validate uploaded file
        Returns: (is_valid, error_message)
        """
        try:
            if uploaded_file is None:
                return False, "Please upload a file"
            
            # Check file extension
            file_extension = uploaded_file.name.split('.')[-1].lower()
            if file_extension not in Config.ALLOWED_EXTENSIONS:
                return False, f"File type not supported. Please upload {', '.join(Config.ALLOWED_EXTENSIONS)} files"
            
            # Check file size
            if uploaded_file.size > Config.MAX_FILE_SIZE:
                return False, f"File size too large. Maximum size is {Config.MAX_FILE_SIZE // (1024*1024)}MB"
            
            return True, ""
            
        except Exception as e:
            logger.error(f"Error validating file: {str(e)}")
            return False, "Error validating file"

# Global analyzer instance
resume_analyzer = ResumeAnalyzer() 