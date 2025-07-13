import pymysql
from config import Config
import logging

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class DatabaseManager:
    def __init__(self):
        self.connection = None
        self.cursor = None
        
    def connect(self):
        """Establish database connection with error handling"""
        try:
            self.connection = pymysql.connect(
                host=Config.DB_HOST,
                user=Config.DB_USER,
                password=Config.DB_PASSWORD,
                db=Config.DB_NAME,
                charset='utf8mb4',
                cursorclass=pymysql.cursors.DictCursor
            )
            self.cursor = self.connection.cursor()
            logger.info("Database connection established successfully")
            return True
        except Exception as e:
            logger.error(f"Database connection failed: {str(e)}")
            return False
    
    def disconnect(self):
        """Close database connection"""
        if self.cursor:
            self.cursor.close()
        if self.connection:
            self.connection.close()
            logger.info("Database connection closed")
    
    def create_tables(self):
        """Create necessary database tables if they don't exist"""
        try:
            # Create user_data table
            user_data_sql = """
            CREATE TABLE IF NOT EXISTS user_data (
                ID INT NOT NULL AUTO_INCREMENT,
                sec_token VARCHAR(20) NOT NULL,
                ip_add VARCHAR(50) NULL,
                host_name VARCHAR(50) NULL,
                dev_user VARCHAR(50) NULL,
                os_name_ver VARCHAR(50) NULL,
                latlong VARCHAR(50) NULL,
                city VARCHAR(50) NULL,
                state VARCHAR(50) NULL,
                country VARCHAR(50) NULL,
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
                pdf_name VARCHAR(50) NOT NULL,
                PRIMARY KEY (ID)
            )
            """
            self.cursor.execute(user_data_sql)
            
            # Create user_feedback table
            feedback_sql = """
            CREATE TABLE IF NOT EXISTS user_feedback (
                ID INT NOT NULL AUTO_INCREMENT,
                feed_name VARCHAR(50) NOT NULL,
                feed_email VARCHAR(50) NOT NULL,
                feed_score VARCHAR(5) NOT NULL,
                comments VARCHAR(100) NULL,
                Timestamp VARCHAR(50) NOT NULL,
                PRIMARY KEY (ID)
            )
            """
            self.cursor.execute(feedback_sql)
            
            self.connection.commit()
            logger.info("Database tables created successfully")
            return True
            
        except Exception as e:
            logger.error(f"Error creating tables: {str(e)}")
            return False
    
    def insert_user_data(self, data_dict):
        """Insert user data with error handling"""
        try:
            sql = """
            INSERT INTO user_data (
                sec_token, ip_add, host_name, dev_user, os_name_ver, latlong, 
                city, state, country, act_name, act_mail, act_mob, Name, 
                Email_ID, resume_score, Timestamp, Page_no, Predicted_Field, 
                User_level, Actual_skills, Recommended_skills, Recommended_courses, pdf_name
            ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
            """
            
            values = (
                data_dict['sec_token'], data_dict['ip_add'], data_dict['host_name'],
                data_dict['dev_user'], data_dict['os_name_ver'], data_dict['latlong'],
                data_dict['city'], data_dict['state'], data_dict['country'],
                data_dict['act_name'], data_dict['act_mail'], data_dict['act_mob'],
                data_dict['name'], data_dict['email'], data_dict['resume_score'],
                data_dict['timestamp'], data_dict['no_of_pages'], data_dict['reco_field'],
                data_dict['cand_level'], data_dict['skills'], data_dict['recommended_skills'],
                data_dict['courses'], data_dict['pdf_name']
            )
            
            self.cursor.execute(sql, values)
            self.connection.commit()
            logger.info("User data inserted successfully")
            return True
            
        except Exception as e:
            logger.error(f"Error inserting user data: {str(e)}")
            return False
    
    def insert_feedback(self, feedback_dict):
        """Insert feedback data with error handling"""
        try:
            sql = """
            INSERT INTO user_feedback (feed_name, feed_email, feed_score, comments, Timestamp)
            VALUES (%s, %s, %s, %s, %s)
            """
            
            values = (
                feedback_dict['feed_name'], feedback_dict['feed_email'],
                feedback_dict['feed_score'], feedback_dict['comments'],
                feedback_dict['timestamp']
            )
            
            self.cursor.execute(sql, values)
            self.connection.commit()
            logger.info("Feedback data inserted successfully")
            return True
            
        except Exception as e:
            logger.error(f"Error inserting feedback: {str(e)}")
            return False
    
    def get_user_data(self):
        """Fetch all user data for admin panel"""
        try:
            sql = """
            SELECT ID, sec_token, ip_add, act_name, act_mail, act_mob, 
                   convert(Predicted_Field using utf8) as Predicted_Field, 
                   Timestamp, Name, Email_ID, resume_score, Page_no, pdf_name, 
                   convert(User_level using utf8) as User_level, 
                   convert(Actual_skills using utf8) as Actual_skills, 
                   convert(Recommended_skills using utf8) as Recommended_skills, 
                   convert(Recommended_courses using utf8) as Recommended_courses, 
                   city, state, country, latlong, os_name_ver, host_name, dev_user 
            FROM user_data
            """
            self.cursor.execute(sql)
            return self.cursor.fetchall()
            
        except Exception as e:
            logger.error(f"Error fetching user data: {str(e)}")
            return []
    
    def get_feedback_data(self):
        """Fetch all feedback data"""
        try:
            sql = "SELECT * FROM user_feedback"
            self.cursor.execute(sql)
            return self.cursor.fetchall()
            
        except Exception as e:
            logger.error(f"Error fetching feedback data: {str(e)}")
            return []
    
    def get_analytics_data(self):
        """Fetch data for analytics charts"""
        try:
            sql = """
            SELECT ID, ip_add, resume_score, 
                   convert(Predicted_Field using utf8) as Predicted_Field, 
                   convert(User_level using utf8) as User_level, 
                   city, state, country 
            FROM user_data
            """
            self.cursor.execute(sql)
            return self.cursor.fetchall()
            
        except Exception as e:
            logger.error(f"Error fetching analytics data: {str(e)}")
            return []

# Global database manager instance
db_manager = DatabaseManager() 