"""
LinkedIn Auto Applier
Developed by Aditya Kumar
GitHub: https://github.com/aditya-life/Linkdin_auto_applier
"""



###################################################### CONFIGURE YOUR BOT HERE ######################################################

# >>>>>>>>>>> LinkedIn Settings <<<<<<<<<<<

# Keep browser tabs open after applying
close_tabs = True                  # True or False, Note: True or False are case-sensitive
'''
Note: RECOMMENDED TO LEAVE IT AS `True`, if you set it `False`, be sure to CLOSE ALL TABS BEFORE CLOSING THE BROWSER!!!
'''

# Automatically follow applied companies
follow_companies = False            # True or False, Note: True or False are case-sensitive

## Upcoming features (In Development)
# # Send connection requests to HR's 
# connect_hr = True                  # True or False, Note: True or False are case-sensitive

# # What message do you want to send during connection request? (Max. 200 Characters)
# connect_request_message = ""       # Leave Empty to send connection request without personalized invitation (recommended to leave it empty, since you only get 10 per month without LinkedIn Premium*)

# Loop job search continuously (Beta)
run_non_stop = False                # True or False, Note: True or False are case-sensitive
'''
Note: Will be treated as False if `run_in_background = True`
'''
alternate_sortby = True             # True or False, Note: True or False are case-sensitive
cycle_date_posted = True            # True or False, Note: True or False are case-sensitive
stop_date_cycle_at_24hr = True      # True or False, Note: True or False are case-sensitive





# >>>>>>>>>>> RESUME GENERATOR (Experimental & In Development) <<<<<<<<<<<

# Give the path to the folder where all the generated resumes are to be stored
generated_resume_path = "all resumes/" # (In Development)





# >>>>>>>>>>> Global Settings <<<<<<<<<<<

# File path configurations for logging history (Sentence after the last "/" will be considered as the file name).
file_name = "all excels/all_applied_applications_history.csv"
failed_file_name = "all excels/all_failed_applications_history.csv"
logs_folder_path = "logs/"

# Maximum delay duration between click events
click_gap = 1                       # Enter max allowed secs to wait approximately. (Only Non Negative Integers Eg: 0,1,2,3,....)

# Run browser headlessly (in background) (May reduce performance). 
run_in_background = False           # True or False, Note: True or False are case-sensitive ,   If True, this will make pause_at_failed_question, pause_before_submit and run_in_background as False

# Disable Chrome extensions for performance (Better for performance)
disable_extensions = False          # True or False, Note: True or False are case-sensitive

# Safe mode - opens Chrome using guest profile or if you have multiple profiles in browser. This will open chrome in guest profile!
safe_mode = False                    # True or False, Note: True or False are case-sensitive

# Smooth scrolling enablement (Can reduce performance if True)
smooth_scroll = False               # True or False, Note: True or False are case-sensitive

# Prevent computer from sleeping during execution and prevent PC from sleeping. Instead you could disable this feature (set it to false) and adjust your PC sleep settings to Never Sleep or a preferred time. 
keep_screen_awake = True            # True or False, Note: True or False are case-sensitive (Note: Will temporarily deactivate when any application dialog boxes are present (Eg: Pause before submit, Help needed for a question..))

# Bypass anti-bot mechanisms using undetected mode (Preview Feature, UNSTABLE. Recommended to leave it as False)
stealth_mode = True                # True or False, Note: True or False are case-sensitive

# Alert on AI connection errors
showAiErrorAlerts = False            # True or False, Note: True or False are case-sensitive

# Use AI model for dynamic resume generation (Experimental Feature can break the application. Recommended to leave it as False) 
# use_resume_generator = False       # True or False, Note: True or False are case-sensitive ,   This feature may only work with 'stealth_mode = True'. As ChatGPT website is hosted by CloudFlare which is protected by Anti-bot protections!











############################################################################################################
"""
LinkedIn Auto Applier - Developed by Aditya Kumar
Good luck with your job search!
"""
############################################################################################################