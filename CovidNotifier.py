from plyer import notification
from pandas.core.frame import DataFrame
import requests
import pandas as pd
import time

# function to notify 
def notifyme(title,message):
    notification.notify(
        title = title,
        message = message,
        app_icon = None,
        timeout = 30
    )

if __name__ == '__main__':     #__name == __main__ is used to notify only if the script is running
    while True:
        # function to get data and convert it into a dataframe
        def getdata():
            r = requests.get('https://www.mohfw.gov.in/data/datanew.json')
            data = r.json()                             #data is now retrieved in json format
            df = pd.DataFrame(data)
            df = df.drop(['sno','state_code'],axis = 1) #dropping unwanted columns
            return df

        df = getdata()
        states = ['Himachal Pradesh','Punjab','Tripura']        #states to be notified about
        for name in states:
            n_list= df.loc[df['state_name']==name].values.tolist()      #convert df to list
            n_list = sum(n_list, [])                                    #convert 2d list to 1d
            ntitle = f'Cases of covid-19\n{n_list[0]}'
            ntext = f'Active: {n_list[1]}\nPositive: {n_list[2]}\nCured: {n_list[3]}\nDeath: {n_list[4]}'
            notifyme(ntitle,ntext)
        time.sleep(60)                                        #time between next round of notifications