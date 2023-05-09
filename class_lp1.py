import torch
import pandas as pd


class Robot:

    def __init__(self,data): 
        self.data = data       #pandas データ
        self.i_name = 'none'   #相手の名前
        self.count = -1        #カウント recom()で用いる 
    

    def firstg(self):          #挨拶と名前を聞く関数
        print("こんにちは私はロボット受付です。あなたの名前は?")
        self.i_name = input()


    def recom(self):           #登録されている店を順に聞き、カウントを増やすか決める関数
         for index in self.data.iterrows():  #データが終わるまで,行ごとに読み込む                          
             
             self.count = self.count + 1
             sh_name = self.data.iloc[self.count,0] #登録されている店の名前参照　

             print(self.i_name +"さん。"+ sh_name +"がおすすめです")
             print(self.i_name +"さんは好きですか  [はい/いいえ]") 
             check1 = input()

             if check1 == 'はい':            #「はい」なら参照している店のカウントを1増やす
                 self.data.iloc[self.count,1] = self.data.iloc[self.count,1] + 1
                 check1 = 'none'
    

    def quest(self): #好きなレストランを聞き、それを登録するか決める関数
        print(self.i_name+"さん。どこのレストランが好きですか")
        nsh_name = input()
        check = self.data[self.data['NAME'] == nsh_name]  #既に登録されてないか確認する
                                                          #されていれば checkはデータが入った状態に　されていなければ空の状態になる
        
        if check.empty == True:                           #登録されていなければ新たにデータを追加する
            self.data = self.data.append({'NAME': nsh_name,'COUNT': 1},ignore_index=True)
           
            

    def lastg(self):  #挨拶とデータを並び替える関数
        print(self.i_name + "さん、良い一日を") 
        self.data = self.data.sort_values('COUNT',ascending=False)  #データを並び替える
                                                                    
