from data_tree import *


class DataBase:
    tree = DataTree.company

    # departments_table = {
    # # country | departemnts available
    #     USA   : [VERF, QA, RD, HR],
    #     IL    : [VERF, QA, RD, HR, MRKT, ADMN, FDL],
    #     ENG   : [MRKT, HR, FDW]
    # }
    #
    # jobs_table = {
    # # department | jobs available
    #     HR       : [HR_M, HR_R],
    #     QA       : [QA_M, QA99],
    #     RD       : [SW_J, SW_JM, SW_S, SW_SM, SW99],
    #     VERF     : [VERF_J, VERF_S, VERF_SM, VERF_JM],
    #     MRKT     : [MRKT_M, MRKT_TW, MRKT_CS]
    # }
    #
    #
    #
    # equipments_table = {
    # #   dep.| job title | items
    #     HR: {
    #             HR_R    : HR_EQ_PACKET,       # -> [LAPTOP, TAG]
    #             HR_M    : HR_EQ_PACKET },
    #     RD: {
    #             SW_SM   : MANAGER_EQ_PACKET,  # -> [LAPTOP, MOUSE, CELL, TABLET, TAG]
    #             SW_JM   : MANAGER_EQ_PACKET,
    #             SW_S    : NORMAL_EQ_PACKET,   # -> [LAPTOP, MOUSE, TAG]
    #             SW_J    : NORMAL_EQ_PACKET,
    #             SW99    : NORMAL_EQ_PACKET },
    #     QA: {
    #             QA_M    : MANAGER_EQ_PACKET,
    #             QA99    : NORMAL_EQ_PACKET },
    #     VERF: {
    #             VERF_SM : MANAGER_EQ_PACKET,
    #             VERF_JM : MANAGER_EQ_PACKET,
    #             VERF_S  : NORMAL_EQ_PACKET,
    #             VERF_J  : NORMAL_EQ_PACKET },
    #
    #     MRKT: {
    #             MRKT_M  : [LAPTOP, TABLET,TAG],
    #             MRKT_TW : [LAPTOP, HEADPHONES, TAG],
    #             MRKT_CS : [LAPTOP, HEADPHONES, TAG] }
    # }
    #
    # allowance_table = {
    # # allowance | job title
    #     2000    : JUNIOR_MANAGERS,
    #     1500    : SENIOR_MANAGERS,
    #     1000    : MANAGER,
    #     800     : ENDINEERS,
    #     200     : STUDENTS
    # }
    #
    # banks_table = {
    # # country | bank_no | sections
    #     USA: {
    #             JPM     : ['200', '603'] },
    #     IL : {
    #             HAPOALIM: ['726', '710', '706'],
    #             LEUMI   : ['102', '120'] },
    #     ENG: {
    #             NATWEST : ['712-L'] }
    # }
    #
    # tabels = {
    #     'job_title'     : jobs_table,
    #     'dep'           : departments_table,
    #     'manager'       : managers_table,
    #     'items_issued'  : equipments_table,
    #     'allowance'     : allowance_table,
    #     'bank_no'       : banks_table,
    #     'country'       : COUNTRIES
    # }

    def query(self, keys):
        select = self.tree
        for k in keys:
            select = select[k]
            #print(select)

        return list(select)



db = DataBase()
print(db.query([USA, 'dep', VERF, 'job_title']))
