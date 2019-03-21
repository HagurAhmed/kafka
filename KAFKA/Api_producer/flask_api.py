from flask import Flask, render_template, request, send_from_directory
from prod import *
import random

cont = True
index = 0

app = Flask(__name__)

@app.route('/')
def ss():
    return render_template('api_1.html')

@app.route('/start',methods = ['POST', 'GET'])
def start():
    if request.method == 'POST':
       l_range = []  
       for i in range(5):
           l_range.append((int(request.form['min'+'_v'+str(i+1)]),int(request.form['max'+'_v'+str(i+1)]))) 
       
       global cont
       global index
       cont = True
       
       while cont is True :
           print("yeeeeeeeeeeeeeeeeeeees"+str(index))
           
           data1 = random.randint(l_range[0][0],l_range[0][1])
           data2 = random.randint(l_range[1][0],l_range[1][1])
           data3 = random.randint(l_range[2][0],l_range[2][1])
           data4 = random.randint(l_range[3][0],l_range[3][1])
           data5 = random.randint(l_range[4][0],l_range[4][1])
           
           producer.send('NUMS', value=(data1,data2,data3,data4,data5))
           sleep(1)
           index +=1
           if index % 40 == 0:
               cont = False
    return render_template('api_1.html')   




@app.route('/stop',methods = ['POST', 'GET'])
def stop():
    global cont
    cont = False
    return 'stped'            

if __name__ == '__main__':
   app.run(debug = True)