import pandas as pd
import csv
import class_lp1 as lp1


robot = lp1.Robot(pd.read_csv('LP1j.csv'))   #csvファイルを読み込む

robot.firstg()

robot.recom()

robot.quest()

robot.lastg()

robot.data.to_csv('LP1j.csv',index=False)  #csvファイルに書き込む 

robot.data = pd.read_csv('LP1j.csv')

print(robot.data)                         #csvファイルのデータを出力する