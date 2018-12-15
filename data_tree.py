from constants import *

class DataTree:
    VERF_JOBS = {
        VERF_J: {
            'items_issued': NORMAL_EQ_PACKET,
            'allowance': 800,
        },
        VERF_S: {
            'items_issued': NORMAL_EQ_PACKET,
            'allowance': 800,
        },
        VERF_SM: {
            'items_issued': MANAGER_EQ_PACKET,
            'allowance': 1500,
        },
        VERF_JM: {
            'items_issued': MANAGER_EQ_PACKET,
            'allowance': 2000,
        }
    }

    VREF_DEP = {
        'job_title': VERF_JOBS,
        'manager': ['John Travolta']
    }

    RD_JOBS = {
        SW_J: {
            'items_issued': NORMAL_EQ_PACKET,
            'allowance': 800,
        },
        SW_JM: {
            'items_issued': MANAGER_EQ_PACKET,
            'allowance': 2000,
        },
        SW_S: {
            'items_issued': NORMAL_EQ_PACKET,
            'allowance': 800,
        },
        SW_SM: {
            'items_issued': MANAGER_EQ_PACKET,
            'allowance': 1500,
        },
        SW99: {
            'items_issued': NORMAL_EQ_PACKET,
            'allowance': 200,
        }
    }

    RD_DEP = {
        'job_title': RD_JOBS,
        'manager': ['John Travolta']
    }

    QA_JOBS = {
        QA_M: {
            'items_issued': MANAGER_EQ_PACKET,
            'allowance': 1000,
        },
        QA99: {
            'items_issued': NORMAL_EQ_PACKET,
            'allowance': 200,
        }
    }

    QA_DEP = {
        'job_title': QA_JOBS,
        'manager': ['Jimmy Page']
    }

    HR_JOBS = {
        HR_R: {
            'items_issued': HR_EQ_PACKET,  # -> [LAPTOP, TAG]
            'allowance': -1,
        },
        HR_M: {
            'items_issued': HR_EQ_PACKET,  # -> [LAPTOP, TAG]
            'allowance': 1000,
        }
    }

    HR_DEP = {
        'job_title': HR_JOBS,
        'manager': ['Stevie Wonders']
    }

    MRKT_JOBS = {
        MRKT_M: {
            'items_issued': [LAPTOP, TABLET, TAG],
            'allowance': 1000,
        },
        MRKT_TW: {
            'items_issued': [LAPTOP, HEADPHONES, TAG],
            'allowance': -1,
        },
        MRKT_CS: {
            'items_issued': [LAPTOP, HEADPHONES, TAG],
            'allowance': -1,
        }
    }

    MRKT_DEP = {
        'job_title': MRKT_JOBS,
        'manager': ['Stevie Wonders']
    }

    USA_SEA = {'office_loc': [SEA]}
    USA_SITE = {
        'dep': {
            VERF: {**VREF_DEP, **USA_SEA},
            RD: {**RD_DEP, **USA_SEA},
            QA: {**QA_DEP, **USA_SEA},
            HR: {**HR_DEP, **USA_SEA},
            FDW: [FDW]
        },
        'bank_no': {
            JPM: JPM_SEC
        }
    }

    IL_HFA = {'office_loc': [HFA]}
    IL_TLV = {'office_loc': [TLV]}
    IL_SITE = {
        'dep': {
            VERF: {**VREF_DEP, **IL_HFA},
            RD  : {**RD_DEP, **IL_HFA},
            QA  : {**QA_DEP, **IL_HFA},
            HR  : {**HR_DEP, **IL_TLV},
            MRKT: {**MRKT_DEP, **IL_TLV},
            FDL : [FDL]
        },
        'bank_no': {
            HAPOALIM: HAPOALIM_SEC,
            LEUMI: LEUMI_SEC
        }
    }

    ENG_LCY = {'office_loc': [LCY]}
    ENG_SITE = {
        'dep': {
            HR  : {**HR_DEP, **ENG_LCY},
            MRKT: {**MRKT_DEP, **ENG_LCY},
            FDW : [FDW]
        },
        'bank_no': {
            NATWEST: NATWEST_SEC
        }
    }

    company = {
        USA: USA_SITE,
        IL: IL_SITE,
        ENG: ENG_SITE
    }