import requests
from bs4 import BeautifulSoup
import telebot
import pandas
import numpy as np
import matplotlib.pyplot as plt
plt.switch_backend('agg')
from keras.models import load_model
import random
import openpyxl
import datetime
from threading import Thread
import time


model90141 = load_model('model90141.h5')
model = load_model('lstm_model.h5')

headers = {
  'authority': 'www.coingecko.com',
  'accept': '*/*',
  'accept-language': 'ru-UA,ru-RU;q=0.9,ru;q=0.8,en-US;q=0.7,en;q=0.6,uk;q=0.5',
  'cookie': '__cf_bm=waLgAZEa7AnrY.6nXl.JmEEIDOty5txa.hEUCjra1YI-1652378436-0-Ac1T4xhBZ7kam3sGvVQyUIEc/xrEV37Ij7jcZpmPnXjo7Oybb2pljVOKc8QJ2EtF4PHdQntOJ6pKgWnqHnJZnx8=; _gid=GA1.2.1363290745.1652378441; _session_id=6a1ef15723159570f417eb96ff33c260; cookie_notice_accept=1; _ga=GA1.2.2146667781.1652378441; _gat_gtag_UA_49392197_1=1; _ga_LJR3232ZPB=GS1.1.1652378438.1.1.1652379130.0; __cf_bm=x7aWKZqJZvmOCzpQz486SLERekHTkHAJIWVqNetqoKI-1652380385-0-AWHAludnDUoBnQ2jj8CUMhGk7KxVFaH/bmWcaX+WLR4eKR4y6aUQ80p1mAVQkydHOEGTcY8vVGEGhMH517/FqVk=',
  'referer': 'https://www.coingecko.com/ru/%D0%9A%D1%80%D0%B8%D0%BF%D1%82%D0%BE%D0%B2%D0%B0%D0%BB%D1%8E%D1%82%D1%8B/solana/usd',
  'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="101", "Google Chrome";v="101"',
  'sec-ch-ua-mobile': '?0',
  'sec-ch-ua-platform': '"Windows"',
  'sec-fetch-dest': 'empty',
  'sec-fetch-mode': 'cors',
  'sec-fetch-site': 'same-origin',
  'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.54 Safari/537.36'
}

token = "1136116062:AAGt_NttQfJfCEoV_eHZ_ecQQm94gAyWwGo"

URL_GST = "https://www.coingecko.com/ru/%D0%9A%D1%80%D0%B8%D0%BF%D1%82%D0%BE%D0%B2%D0%B0%D0%BB%D1%8E%D1%82%D1%8B/green-satoshi-token/usd"
URL_SOL = "https://www.coingecko.com/ru/%D0%9A%D1%80%D0%B8%D0%BF%D1%82%D0%BE%D0%B2%D0%B0%D0%BB%D1%8E%D1%82%D1%8B/solana/usd"
URL_BTC = "https://www.coingecko.com/uk/coins/bitcoin"
URL_USDC = "https://www.coingecko.com/ru/%D0%9A%D1%80%D0%B8%D0%BF%D1%82%D0%BE%D0%B2%D0%B0%D0%BB%D1%8E%D1%82%D1%8B/usd-coin"
URL_USDT ="https://www.coingecko.com/ru/%D0%9A%D1%80%D0%B8%D0%BF%D1%82%D0%BE%D0%B2%D0%B0%D0%BB%D1%8E%D1%82%D1%8B/tether"
URL_GMT="https://www.coingecko.com/uk/coins/stepn"
URL_BNB="https://www.coingecko.com/uk/coins/bnb"

GST_id=21841
SOL_id=4128
BTC_id=1
USDC_id=6319
USDT_id=325
GMT_id=23597
BNB_id=825

STEPN_groud_id='-751942882'
my_id='563523358'
savula_id='274643320'
Meka_id='226677264'
Zoja_id='1163976300'
"1211904051"
bot = telebot.TeleBot(token)

token_GST24h_url='https://www.coingecko.com/price_charts/21841/usd/24_hours.json'

from telebot import types
#import config


    
@bot.message_handler(commands=['start'])
def start(message):
    if message.chat.id==563523358 or message.chat.id==-751942882 or message.chat.id==274643320 or message.chat.id==226677264:
        print(message.chat.id, message.from_user.first_name, message.from_user.last_name, message.from_user.username)
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("???????????? ????????????, ?????? ?????????")
        btn2 = types.KeyboardButton("?? ?????? ?????? ???????? ????????!")
        markup.add(btn1, btn2)
        bot.send_message(message.chat.id, text="???????????? ".format(message.from_user), reply_markup=markup)
    else:
        print('____ DEFENSE _____')
        print(message.chat.id, message.from_user.first_name, message.from_user.last_name, message.from_user.username)       




@bot.message_handler(content_types=['text'])
def func(message):
    if (message.text == "???????????? ????????????, ?????? ?????????"):
        if message.chat.id==563523358 or message.chat.id==-751942882 or message.chat.id==274643320 or message.chat.id==226677264:
            print(message.chat.id, message.from_user.first_name, message.from_user.last_name, message.from_user.username)
            ans1_list=['???????? ???????????????????? ???????? ?????????? ???? ??????????????????. ???? ???? ???????????????????????',
                       '?????? ?????? ?????????????? ?????????? ?????????????????? ?? ?????????????????? ??????????????. ???? ?????????????? ????????????.',
                       '??????????? ???? ???????????????? ?????? ?? ??????????...',
                       '?? ???????? ?????????????? ????????, ???? ?????? ?????? ?????????? ?? ???????????????????? ????????????.',
                       '?? ?????? ???????????? ????????????????.',
                       '???? ??????????????????????, ?????? ???????????? ???? ???????? ????????????????????. ?? ????????, ???? ???????? ?????????????? ???? ????????????.',
                       '?? ?????????????????? ?? ????????????????????????? ???? ???????? ??????????????????.',
                       '????????????????????, ???? ?????????? ???????????? ???? ?????? ????????????.',
                       '?? ??????????, ?????? ?????????????? ??????????, ?????? ?? ?? ???????????????? ??????????????????',
                       '?????? ?? ??????????? ?? ?????? ?????????? ?????????? ??????????????????????????? ?????????????????? ???? ??????-???????????? ?? ?????????????????????? ????????????????, ???????? ?? ???? ?????????? ???? ?????????????',
                       '????????????????????, ????-??????????, ???? ?????????????????? ???????? ??????????????, ???????? ?? ?????????? ?? ?????? ?????????? ????????????.']
            bot.send_message(message.chat.id, text=random.choice(ans1_list))
        else:
            print('____ DEFENSE _____')
            print(message.chat.id, message.from_user.first_name, message.from_user.last_name, message.from_user.username)       


    elif (message.text == "?? ?????? ?????? ???????? ????????!"):
        if message.chat.id==563523358 or message.chat.id==-751942882 or message.chat.id==274643320 or message.chat.id==226677264:
            print(message.chat.id, message.from_user.first_name, message.from_user.last_name, message.from_user.username)
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            btn1 = types.KeyboardButton("???? ?????? ?? GST?")
            btn2 = types.KeyboardButton("???? ?????? SOL?")
            btn3 = types.KeyboardButton("???? ?????? ???????????")
            back = types.KeyboardButton("??????????...")
            markup.add(btn1, btn2, btn3, back)
            ans2_list=['???????????? ?????? ???????????? ??????????????????, ?????? ???????? ?????????? ?????????? ???? ??????????, ?????? ?????????? ???? ???????????????????? ?????????',
                '????????????, ?????? ?????? ???? ????????????????????.',
                '?? ???? ?????? ?????? ????????????????, ???? ?????? ??????????? ???????? ?????????????? ???? ??????????????.',
                '???????? ???? ?????? ???????????????????? ?????? ????????????.',
                '???? ??????????????, ?? ?????? ???????? ????????????????? ?????? ?? ???????????????? ???????????? ???? ????, ???????? ???? ???? ???????? ?????????????? ?? ??????????????????????-???????????????????????? ????????????????? ??????, ???? ?????????????????? ????????????????, ?? ?? ?????????????????? ?????????? ?????? ??????????, ?? ???? ???? ???????? ????????????. ?? ???????? ?????????? ????????????, ???????? ?????????? ?? ???????????? ?????????????? ???????????? ???? ?????????? ????????????.',
                '??, ?????????? ?????? ??? ????????????????, ???????????????? ???? ?????????????????? ????????!']
            bot.send_message(message.chat.id, text=random.choice(ans2_list), reply_markup=markup)
        else:
            print('____ DEFENSE _____')
            print(message.chat.id, message.from_user.first_name, message.from_user.last_name, message.from_user.username)       
           
        
    
    elif (message.text == "???? ?????? ?? GST?"):
        if message.chat.id==563523358 or message.chat.id==-751942882 or message.chat.id==274643320 or message.chat.id==226677264:
            print(message.chat.id, message.from_user.first_name, message.from_user.last_name, message.from_user.username)
            results=get_currect_coin_price(URL_GST,GST_id)
            mean_coin_price=mean_price(GST_id)
            predcit=predict_price_orig(results)[[0]]
            predcit2=predict_price_fake(results)[[0]]
            ots=((float(results.replace('$','').replace(' ','').replace(',','.'))/float(mean_coin_price))-1)*100
            if ots>0.1:
                ans_ots=f'???????? ???????????? ???????? ???????????????? ???? 30 ???????? ???? '+str(abs(round(ots, 4)))+'%... ???????? ??????????...'
            elif ots<0.1:
                ans_ots=f'???????? ???????????? ???????? ???????????????? ???? 30 ???????? ???? '+str(abs(round(ots, 4)))+'%... ???????? ????????????????, ???????? ?????? ??...'
            else:
                ans_ots=f'???????? ???????????? ???? ???????????? ???????????????????? ???? ???????????????? ???? 30 ???????? ???? {ots}%... ???????? ??????????????, ???? ?????? ?????? ????????????????????????...'
            bot.send_message(message.chat.id,f"GST ???? = {results} \nMean 30 days = {mean_coin_price}\nPredict GST= {predcit2}\n{ans_ots}\n...\n?? ???????????????? ???????? ????????????????. ?????? ?????????????????? ???????????? ????????????: ???????? ?????????????? ?? ???????? ?????? ???????????????????? ?????????? ???? ???????????")
            save_fig(predcit,predcit2)
            try:
                bot.send_photo(message.chat.id, open('__results___2_3.png', 'rb'))
            except:
                print("An exception occurred")
        else:
            print('____ DEFENSE _____')
            print(message.chat.id, message.from_user.first_name, message.from_user.last_name, message.from_user.username)       
            
        
        
    elif (message.text == "???? ?????? SOL?"):
        if message.chat.id==563523358 or message.chat.id==-751942882 or message.chat.id==274643320 or message.chat.id==226677264:
            print(message.chat.id, message.from_user.first_name, message.from_user.last_name, message.from_user.username)
            results=get_currect_coin_price(URL_SOL,SOL_id)
            bot.send_message(message.chat.id,"SOL ???? = "+results+'\n...\n?? ???????????????? ???????? ????????????????. ?????? ?????????????????? ???????????? ????????????: ???????? ?????????????? ?? ???????? ?????? ???????????????????? ?????????? ???? ???????????')
        else:
            print('____ DEFENSE _____')
            print(message.chat.id, message.from_user.first_name, message.from_user.last_name, message.from_user.username)       
            
         
        
    elif (message.text == "???? ?????? ???????????"):
        if message.chat.id==563523358 or message.chat.id==-751942882 or message.chat.id==274643320 or message.chat.id==226677264:
            print(message.chat.id, message.from_user.first_name, message.from_user.last_name, message.from_user.username)
            resultsBTC=get_currect_coin_price(URL_BTC,BTC_id)
            resultsUSDC=get_currect_coin_price(URL_USDC,USDC_id)
            resultsUSDT=get_currect_coin_price(URL_USDT,USDT_id)
            resultsSOL=get_currect_coin_price(URL_SOL,SOL_id)
            resultsGST=get_currect_coin_price(URL_GST,GST_id)
            resultsGMT=get_currect_coin_price(URL_GMT,GMT_id)
            resultsBNB=get_currect_coin_price(URL_BNB,BNB_id)
            bot.send_message(message.chat.id,"BTC ???? = "+resultsBTC+"\n"+
                             "USDC ???? = "+resultsUSDC+"\n"+
                             "USDT ???? = "+resultsUSDT+"\n"+
                             "SOL ???? = "+resultsSOL+"\n"+
                             "GST ???? = "+resultsGST+"\n"+
                             "GMT ???? = "+resultsGMT+"\n"+
                             "BNB ???? = "+resultsBNB+'\n...\n?? ???????????????? ???????? ????????????????. ?????? ?????????????????? ???????????? ????????????: ???????? ?????????????? ?? ???????? ?????? ???????????????????? ?????????? ???? ???????????')
           
     
        else:
            print('____ DEFENSE _____')
            print(message.chat.id, message.from_user.first_name, message.from_user.last_name, message.from_user.username)       
            
        
    elif (message.text == "??????????..."):
        if message.chat.id==563523358 or message.chat.id==-751942882 or message.chat.id==274643320 or message.chat.id==226677264:
            print(message.chat.id, message.from_user.first_name, message.from_user.last_name, message.from_user.username)
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            button1 = types.KeyboardButton("???????????? ????????????, ?????? ?????????")
            button2 = types.KeyboardButton("?? ?????? ?????? ???????? ????????!")
            markup.add(button1, button2)
            bot.send_message(message.chat.id, text="???? ?????????????? ?????? ?????????? ????????????????????... ???? ????... ?? ???????? ?????? ?????? ?????????? ??????????...", reply_markup=markup)

        else:
            print('____ DEFENSE _____')
            print(message.chat.id, message.from_user.first_name, message.from_user.last_name, message.from_user.username)       
    else:
        bot.send_message(message.chat.id, text="???? ?????????? ???????????????? ?? ???? ????????????????????????????????...")


      
def get_currect_coin_price(coin_url,coin_id):
    page = requests.get(coin_url)
    soup = BeautifulSoup(page.content, "html.parser")
    results = soup.find("span", {"class": "no-wrap" , "data-coin-id":coin_id})  
    return results.string
     

@bot.message_handler(commands=['like'])
def like(message):   
    cid = message.chat.id
    bot.send_message(cid, "Do you like it?")

@bot.message_handler(commands=['mean_shift_GST'])
def get_last_token_data(message):
    cid = message.chat.id
    print(cid)
    token_data=requests.get(token_GST24h_url,headers=headers).json()
    token_data= pandas.DataFrame(token_data['stats'], columns=['time', 'value'])
    mean_shift=token_data['value'].iloc[-6:-1].rolling(5).mean()
    bot.send_message(cid,"mean_shift_GST rolling (5) = "+str(mean_shift.iloc[-1]))
    mean_shift=token_data['value'].iloc[-11:-1].rolling(10).mean()
    bot.send_message(cid,"mean_shift_GST rolling (10) = "+str(mean_shift.iloc[-1]))
    mean_shift=token_data['value'].iloc[-51:-1].rolling(50).mean()
    bot.send_message(cid,"mean_shift_GST rolling (50) = "+str(mean_shift.iloc[-1]))

def mean_price(Coin_id):
    token_data=requests.get(f"https://www.coingecko.com/price_charts/{Coin_id}/usd/30_days.json",headers=headers).json()
    token_data=pandas.DataFrame(token_data['stats'], columns=['time', 'value'])
    mean_price=token_data['value'].mean()
    return mean_price

def predict_price_orig(resultsGST):
    resultsBTC=get_currect_coin_price(URL_BTC,BTC_id).replace('$','').replace(' ','').replace(',','.')
    resultsGST=resultsGST.replace('$','').replace(' ','').replace(',','.')
    token_data=requests.get(f"https://www.coingecko.com/price_charts/1/usd/30_days.json",headers=headers).json()
    token_data=pandas.DataFrame(token_data['stats'], columns=['time', 'value'])
    prev_price=token_data['value'].iloc[-2]
    yhat = model.predict(np.array([[((float(resultsBTC)-40000)/4057), ((float(resultsGST)-4.91)/0.848)]]), verbose=0)
    #yhat=(yhat[[0]]+4.9)/0.858
    yhat=(yhat[[0]]*0.858+4.9)
    return yhat[[0]]

def predict_price_fake(resultsGST):
    resultsBTC=get_currect_coin_price(URL_BTC,BTC_id).replace('$','').replace(' ','').replace(',','.')
    resultsGST=resultsGST.replace('$','').replace(' ','').replace(',','.')
    token_data=requests.get(f"https://www.coingecko.com/price_charts/1/usd/30_days.json",headers=headers).json()
    token_data=pandas.DataFrame(token_data['stats'], columns=['time', 'value'])
    prev_price=token_data['value'].iloc[-2]
    #print(((float(resultsBTC)-prev_price)+6.18)/476)
    yhat = model.predict(np.array([[((float(resultsBTC)-35880)/5229), ((float(resultsGST)-4.43)/1.19)]]), verbose=0)
    yhat=(yhat[[0]]*1.19+4.43)
    return yhat[[0]]

def save_fig(predict,predict2):
    token_data=requests.get('https://www.coingecko.com/price_charts/21841/usd/24_hours.json',headers=headers).json()
    token_data=pandas.DataFrame(token_data['stats'], columns=['time', 'value'])
    y1=np.array(token_data['value'][-50:-1])
    x1 = np.arange(1, 50)
    x2 = np.arange(1, 51)
    x3 = np.arange(1, 51)
    y2=np.concatenate((y1, predict[0]))
    y3=np.concatenate((y1, predict2[0]))
    plt.plot(x3,y3,x1,y1) 
    plt.title("Matplotlib PLot NumPy Array") 
    plt.xlabel("x axis") 
    plt.ylabel("y axis") 
    plt.savefig("__results___2_3.png")
    plt.close()

def write_file():
    while True:
        results=get_currect_coin_price(URL_GST,GST_id)
        resultsWRITE=results.replace('$','').replace(' ','').replace(',','.')
        predcit=predict_price_orig(results)[[0]]
        predcit2=predict_price_fake(results)[[0]]

            

        excel_file = openpyxl.load_workbook('model_test.xlsx')
        excel_sheet = excel_file['data']
        holiday_rows = (str(resultsWRITE), str(predcit[0][0]), str(predcit2[0][0]))
        excel_sheet.append(holiday_rows)

        excel_file.save(filename="model_test.xlsx")

        time.sleep(180)
        print('___write file___')


                
  
#print(get_last_token_data(token_GST24h_url))

#th = Thread(target=write_file, daemon=True)
#th.start()                   

bot.polling(none_stop=True)

