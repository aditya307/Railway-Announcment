import os
import pandas as pd
from pydub import AudioSegment
from gtts import gTTS 


def textToSpeech(text, filename):
    mytext=str(text)
    language='hi'
    myobj=gTTS(text=mytext,lang=language,slow=False)
    myobj.save(filename)

def mergeAudios(audios):
    combined=AudioSegment.empty()
    for audio in audios:
        combined+=AudioSegment.from_mp3(audio)
    
    return combined

def generateSkeleton():
    
    
    audio=AudioSegment.from_mp3('railways.mp3')
    
    #1-yatrigan kripya dhyaan de
    start=0
    finish=4000
    audioProcessed=audio[start:finish]
    audioProcessed.export("1_hindi.mp3",format="mp3")
    
    #2-gaadi no.
    start=4000
    finish=5000
    audioProcessed=audio[start:finish]
    audioProcessed.export("2_hindi.mp3",format="mp3")

   
    #3 is train no. and name

    #4 from city

    #5- se
    start=7200
    finish=7900
    audioProcessed=audio[start:finish]
    audioProcessed.export("5_hindi.mp3",format="mp3")

    
    #6 to city
    
    #7 apne nirdharit samay
    start=9500
    finish=11300
    audioProcessed=audio[start:finish]
    audioProcessed.export("7_hindi.mp3",format="mp3")

    #8time

    # 9 platform no.
    start=14000
    finish=15500
    audioProcessed=audio[start:finish]
    audioProcessed.export("9_hindi.mp3",format="mp3")
    
    # 10 no.


    # 11 ravana 
    start=15800
    finish=20000
    audioProcessed=audio[start:finish]
    audioProcessed.export("11_hindi.mp3",format="mp3")





def generateAnnouncement(filename):
    df=pd.read_excel(filename)
    print(df)
    for index,item in df.iterrows():
        #3 is train no. and name]
        textToSpeech(item['Train_no'], '3_hindi.mp3')
        #4 from city]
        textToSpeech(item['from'],'4_hindi.mp3')
        #6 to city]
        textToSpeech(item['to'],'6_hindi.mp3')
        #8 time]
        textToSpeech(item['time'],'8_hindi.mp3')
        #10 no.
        textToSpeech(item['platform'],'10_hindi.mp3')

        audios=[f"{i}_hindi.mp3" for i in range(1,12)] 

        announcement=mergeAudios(audios)
        announcement.export(f"announcement_{item['Train_no']}_{index+1}.mp3", format="mp3")   



if __name__ == '__main__':
    print("Generating Skeleton....")
    generateSkeleton()
    print("NOw Generatng Announcement...")
    generateAnnouncement("announcment.xlsx")