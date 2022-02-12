from codecs import ignore_errors
from unicodedata import name
import pandas as pd
def analyze(phone_list,user_pref):
    #creating a dataframe to store phone values and aggregate 
    pagg=pd.DataFrame(columns=['gaming','batt','disp','cam','name','price','agg','sup']) 
    agg_list=[]
    #phone_list=[    #Sample phone database. temp solution, should replace with actual db
    #    {'gaming':4,
    #     'batt':9,
    #     'disp':6,
    #     'cam':4,
    #     'name':'a'
    #    },
    #    {'gaming':9,
    #     'batt':6,
    #     'disp':9,
    #     'cam':8,
    #     'name':'b'
    #    },
    #    {'gaming':6,
    #     'batt':8,
    #     'disp':7,
    #     'cam':8,
    #     'name':'c'
    #    },
    #    {'gaming':1,
    #     'batt':2,
    #     'disp':10,
    #     'cam':5,
    #     'name':'d'
    #    },
    #    {'gaming':6,
    #     'batt':8,
    #     'disp':7,
    #     'cam':4,
    #     'name':'e'
    #    },
    #]
    #user_pref={'gaming':6,  #user preferences
    #            'batt':7,
    #            'disp':8,
    #            'cam':9,
    #            
    #            'name':''}
    for item in range(len(phone_list)):
        sup=0
        disp,gaming,batt,cam=0,0,0,0
        #comparing user and sample phone data and subtracting 
        phone_data=phone_list[item]
        if (user_pref['disp']>phone_data['disp']):
            disp=abs(user_pref['disp']-phone_data['disp'])
            sup=0
        else:
            disp=0
            sup+=phone_data['disp']-user_pref['disp']       #supplementary value
            
        if (user_pref['gaming']>phone_data['gaming']):
            gaming=abs(user_pref['gaming']-phone_data['gaming'])
        else:
            gaming=0
            sup+= phone_data['gaming']-user_pref['gaming']
            
        if (user_pref['batt']>phone_data['batt']):
            batt=abs(phone_data['batt']-user_pref['batt'])
        else:
            batt=0
            sup+= phone_data['batt']-user_pref['batt']
        
        if (user_pref['cam']>phone_data['cam']):
            cam=abs(user_pref['cam']-phone_data['cam'])
        else:
            cam=0
            sup= phone_data['cam']-user_pref['cam']
        
        agg=disp+gaming+batt+cam            #adding the all values to get aggregate
       # print(batt,agg,phone_data['name'])
        pagg=pagg.append({        #adding values to the dataframe
            'gaming':phone_data['gaming'],
            'batt':phone_data['batt'],
            'disp':phone_data['disp'],
            'cam':phone_data['cam'],
            'name':phone_data['name'],
            'price':phone_data['price'],
            'agg':agg,
            'sup':sup
            },ignore_index=True)
    
    pagg=pagg.sort_values(by=['agg'],ascending=True)
    if(len(pagg.loc[pagg['agg']==pagg['agg'].iloc[0]])==1):
        print("hello")
        winner=pagg.iloc[0].to_dict()
    else:
        pf=pagg.loc[pagg['agg']==pagg['agg'].iloc[0]]
        pf=pf.sort_values(by=['sup'],ascending=False)
        winner=pf.iloc[0].to_dict()
   # print(winner)
    return winner