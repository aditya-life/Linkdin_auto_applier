"""
LinkedIn Auto Applier
Developed by Aditya Kumar
GitHub: https://github.com/aditya-life/Linkdin_auto_applier
"""



###################################################### APPLICATION INPUTS ######################################################


# >>>>>>>>>>> Easy Apply Questions & Inputs <<<<<<<<<<<

# Give an relative path of your default resume to be uploaded. If file in not found, will continue using your previously uploaded resume in LinkedIn.
default_resume_path = ""      # (In Development)

# What do you want to answer for questions that ask about years of experience you have, this is different from current_experience? 
years_of_experience = "1"          # A number in quotes Eg: "0","1","2","3","4", etc.

# Do you need visa sponsorship now or in future?
require_visa = "No"               # "Yes" or "No"

# What is the link to your portfolio website, leave it empty as "", if you want to leave this question unanswered
website = ""                        # "www.example.bio" or "" and so on....

# Please provide the link to your LinkedIn profile.
linkedIn = "https://www.linkedin.com/in/aditya-kumar-552232259/"       # "https://www.linkedin.com/in/example" or "" and so on...

# What is the status of your citizenship? # If left empty as "", tool will not answer the question. However, note that some companies make it compulsory to be answered
# Valid options are: "U.S. Citizen/Permanent Resident", "Non-citizen allowed to work for any employer", "Non-citizen allowed to work for current employer", "Non-citizen seeking work authorization", "Canadian Citizen/Permanent Resident" or "Other"
us_citizenship = "Other"



## SOME ANNOYING QUESTIONS BY COMPANIES 🫠 ##

# What to enter in your desired salary question (American and European), What is your expected CTC (South Asian and others)?, only enter in numbers as some companies only allow numbers,
desired_salary = 300000          # 80000, 90000, 100000 or 120000 and so on... Do NOT use quotes
'''
Note: If question has the word "lakhs" in it (Example: What is your expected CTC in lakhs), 
then it will add '.' before last 5 digits and answer. Examples: 
* 2400000 will be answered as "24.00"
* 850000 will be answered as "8.50"
And if asked in months, then it will divide by 12 and answer. Examples:
* 2400000 will be answered as "200000"
* 850000 will be answered as "70833"
'''

# What is your current CTC? Some companies make it compulsory to be answered in numbers...
current_ctc = 180000            # 800000, 900000, 1000000 or 1200000 and so on... Do NOT use quotes
'''
Note: If question has the word "lakhs" in it (Example: What is your current CTC in lakhs), 
then it will add '.' before last 5 digits and answer. Examples: 
* 2400000 will be answered as "24.00"
* 850000 will be answered as "8.50"
# And if asked in months, then it will divide by 12 and answer. Examples:
# * 2400000 will be answered as "200000"
# * 850000 will be answered as "70833"
'''

# (In Development) # Currency of salaries you mentioned. Companies that allow string inputs will add this tag to the end of numbers. Eg: 
# currency = "INR"                 # "USD", "INR", "EUR", etc.

# What is your notice period in days?
notice_period = 0                   # Any number >= 0 without quotes. Eg: 0, 7, 15, 30, 45, etc.
'''
Note: If question has 'month' or 'week' in it (Example: What is your notice period in months), 
then it will divide by 30 or 7 and answer respectively. Examples:
* For notice_period = 66:
  - "66" OR "2" if asked in months OR "9" if asked in weeks
* For notice_period = 15:"
  - "15" OR "0" if asked in months OR "2" if asked in weeks
* For notice_period = 0:
  - "0" OR "0" if asked in months OR "0" if asked in weeks
'''

# Your LinkedIn headline in quotes Eg: "Software Engineer @ Google, Masters in Computer Science", "Recent Grad Student @ MIT, Computer Science"
linkedin_headline = "Full Stack Developer with Masters in Computer Applications and 1+ years of experience" # "Headline" or "" to leave this question unanswered

# Your summary in quotes, use \n to add line breaks if using single quotes "Summary".You can skip \n if using triple quotes """Summary"""
linkedin_summary = """
Full Stack Developer with a Master of Computer Applications (MCA) and hands-on experience building production-grade web applications using the MERN stack (MongoDB, Express.js, React.js, Node.js), PHP/Laravel, and mobile solutions (React Native). Experienced in REST API design, database management (MySQL, MongoDB), cloud/VPS deployment, Nginx, and CI/CD pipelines.
"""

'''
Note: If left empty as "", the tool will not answer the question. However, note that some companies make it compulsory to be answered. Use \n to add line breaks.
''' 

# Your cover letter in quotes, use \n to add line breaks if using single quotes "Cover Letter".You can skip \n if using triple quotes """Cover Letter""" (This question makes sense though)
cover_letter = """
Dear Hiring Manager,

I am writing to express my strong interest in the Full Stack Developer position. With a Master of Computer Applications (MCA) and practical experience developing production-grade web and mobile applications using React.js, Node.js, PHP/Laravel, and React Native, I am confident in my ability to contribute effectively to your development team.

During my tenure at SRJ Global Technologies and my internship at NCA IT Solution, I designed and maintained RESTful APIs, optimized database queries, built responsive user interfaces, and configured VPS/Nginx servers. I am highly proficient in modern JavaScript/ES6+, Tailwind CSS, Git, and automated deployment pipelines (CI/CD).

I am eager to bring my skills in full-stack development, database modeling, and performance optimization to your organization. Thank you for your time and consideration.

Sincerely,
Aditya Kumar
aditya12186@gmail.com | +91 9504022167
Noida, Sector-70, UP, India
"""

# Your user_information_all letter in quotes, use \n to add line breaks if using single quotes "user_information_all".You can skip \n if using triple quotes """user_information_all""" (This question makes sense though)
# We use this to pass to AI to generate answer from information , Assuing Information contians eg: resume  all the information like name, experience, skills, Country, any illness etc. 
user_information_all ="""
Name: Aditya Kumar
Email: aditya12186@gmail.com
Phone: +91 9504022167
Location: Noida, Sector-70, UP - 201301, India
Role: Full Stack Developer (React.js, Node.js, MySQL, MERN Stack, PHP/Laravel, React Native)
LinkedIn: https://www.linkedin.com/in/aditya-kumar-552232259/

Professional Summary:
Results-driven Full Stack Developer with hands-on experience building production-grade web applications using the MERN stack, and PHP/Laravel. Completed a 6-month MERN Stack internship at NCA IT Solution, followed by nearly a year of professional experience at SRJ Global Technologies developing and deploying full-stack and cross-platform mobile solutions. Proficient in REST API design, database management (MySQL, MongoDB), cloud/VPS deployment, and CI/CD pipelines.

Professional Experience:
1. SRJ Global Technologies (June 2025 – May 2026)
Role: Full Stack Developer | Mayur Vihar-III, New Delhi
- Built and shipped production-grade full-stack web apps using React.js, Node.js, and MySQL.
- Designed and maintained RESTful APIs with Node.js/Express.js; handled end-to-end feature development from requirement gathering to deployment.
- Optimised frontend performance (lazy loading, code splitting) and backend query efficiency.
- Collaborated via Git/GitHub; managed branches, pull requests, and code reviews.
- Supported VPS deployment, Nginx configuration, and production server stability.
- Worked with ASP.NET Core (.NET 8) and PHP/Laravel.

2. NCA IT Solution (Jan 2025 – June 2025)
Role: MERN Stack Developer — Internship | Noida
- Completed structured 6-month internship focused on MongoDB, Express.js, React.js, Node.js.
- Developed dynamic, responsive frontend components using React.js and integrated with Node/Express APIs.
- Worked with MongoDB for data modelling and performed CRUD operations.
- Gained experience in authentication flows (JWT), state management, and REST API consumption.

Projects:
1. Lookbook — Ride-Hailing Platform (Rapido-style Clone)
Tech Stack: Laravel 10, React Native, NativeWind, Firebase Realtime DB, MySQL, Nginx, Google Maps API, FCM, GitHub Actions CI/CD.
Details: Contributed to a full-featured ride-hailing clone with React Native Driver & User apps and a Laravel 10 REST API backend. Implemented booking flow, driver assignment, real-time tracking, digital wallet, Nginx VPS deployment.

2. JobNest — Job Portal Platform
Tech Stack: PHP, Laravel, Blade Templating, MySQL, REST API.
Details: Built job portal with job posting, employer dashboard, candidate management, authentication, role-based access control.

Technical Skills:
- Mobile: React Native, NativeWind, Firebase, FCM, Google Maps API
- Frontend: React.js, Next.js, Vue.js, HTML5, CSS3, JavaScript (ES6+), Bootstrap, Tailwind CSS
- Backend: Node.js, Express.js, PHP, Laravel, ASP.NET Core (.NET 8)
- Database: MySQL, MongoDB, SQL Server
- DevOps / Tools: Git, GitHub, GitHub Actions CI/CD, VPS Hosting, Nginx, Postman, Linux CLI, Cloudinary

Education:
- Master of Computer Applications (MCA) from Lovely Professional University, Punjab (2023 - 2025, CGPA 7.4)
- Bachelor of Commerce (B.Com) from Deen Dayal Upadhyaya University, Gorakhpur (2019 - 2022, 53.6%)
- Class XII (Science) from Bihar School Examination Board, Patna (2017 - 2019, 62.8%)
- Class X from Bihar School Examination Board, Patna (2015, 52.8%)

Certifications:
- MERN Stack Developer Internship Certificate (NCA IT Solution, ID: 2025NCA170)
- Adv. Diploma in Computer Applications (ADCA) from BN Computers, Nautan (2016-2017)
"""
'''
Note: If left empty as "", the tool will not answer the question. However, note that some companies make it compulsory to be answered. Use \n to add line breaks.
''' 

# Name of your most recent employer
recent_employer = "SRJ Global Technologies" # "", "Lala Company", "Google", "Snowflake", "Databricks"

# Example question: "On a scale of 1-10 how much experience do you have building web or mobile applications? 1 being very little or only in school, 10 being that you have built and launched applications to real users"
confidence_level = "8"             # Any number between "1" to "10" including 1 and 10, put it in quotes ""
##



# >>>>>>>>>>> RELATED SETTINGS <<<<<<<<<<<

## Allow Manual Inputs
# Should the tool pause before every submit application during easy apply to let you check the information?
pause_before_submit = False         # True or False, Note: True or False are case-sensitive
'''
Note: Will be treated as False if `run_in_background = True`
'''

# Should the tool pause if it needs help in answering questions during easy apply?
# Note: If set as False will answer randomly...
pause_at_failed_question = False    # True or False, Note: True or False are case-sensitive
'''
Note: Will be treated as False if `run_in_background = True`
'''
##

# Do you want to overwrite previous answers?
overwrite_previous_answers = False # True or False, Note: True or False are case-sensitive







############################################################################################################
"""
LinkedIn Auto Applier - Developed by Aditya Kumar
Good luck with your job search!
"""
############################################################################################################