# Countries
USA = 'USA'
IL  = 'IL'
ENG = 'ENG'
COUNTRIES = [USA, IL, ENG]

# Departments
QA  = 'QA'
RD  = 'R&D'
HR  = 'HR'
VERF  = 'Verification'
MRKT  = 'Marketing'
ADMN  = 'Administration'

# Jobs
# HR Dep.
HR_R = 'HR Recruiter'
HR_M = 'HR Manager'
# QA Dep.
QA99 = 'QA Student'
QA_M = 'QA Manager'
# R&D Dep.
SW99  = 'SW Student'
SW_J  = 'Junior SW Engineer'
SW_S  = 'Senior SW Engineer'
SW_JM = 'Junior SW Manager'
SW_SM = 'Senior SW Manager'
# Verification Dep.
VERF_J  = 'Junior SW Engineer'
VERF_S  = 'Senior SW Engineer'
VERF_JM = 'Junior SW Manager'
VERF_SM = 'Senior SW Manager'
# Marketing Dep.
MRKT_M  = 'Manager'
MRKT_TW = 'Technical Writer'
MRKT_CS = 'Customer Support'

# Jobs By Title
SENIOR_MANAGERS = [SW_SM, VERF_SM]
JUNIOR_MANAGERS = [SW_JM, VERF_JM]
MANAGER         = [HR_M, QA_M, MRKT_M]
ENDINEERS       = [SW_S, SW_J, VERF_S, VERF_J]
STUDENTS        = [SW99, QA99]
# Items
LAPTOP = 'Laptop'
CELL = 'Cell Phone'
MOUSE = 'Remote Mouse'
TABLET = 'iPad'
TAG = 'Employee Tag'
HEADPHONES = 'Headphones'

MANAGER_EQ_PACKET = [LAPTOP, MOUSE, CELL, TABLET, TAG]
NORMAL_EQ_PACKET  = [LAPTOP, MOUSE, TAG]
HR_EQ_PACKET      = [LAPTOP, TAG]
# Finance Dep.
FDW = 'FDW'
FDL = 'FDL'

# BANKS
# bank name | bank no. | ----------- sections ------------
HAPOALIM    = '12'
LEUMI       = '18'
JPM         = '21'
NATWEST     = '14'

HAPOALIM_SEC = ['726', '710', '706']
LEUMI_SEC    = ['102', '120']
NATWEST_SEC  = ['712-L']
JPM_SEC      = ['200', '603']

# country   | banks name
IL_BANKS    = [HAPOALIM, LEUMI]
USA_BANKS   = [JPM]
ENG_BANKS   = [NATWEST]
