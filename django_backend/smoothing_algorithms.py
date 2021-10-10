import math
import pandas as pd
import numpy as np
# import matplotlib.pyplot as plt

# data =pd.read_csv('Rate.csv')
# theme = 'NOR' # YEN NewZ CAN
# mainLabel = "USD - "+theme

# print("full data\n",data)

# all_valueList = data[theme].tolist() #YEN  NewZ CAN NOR


# print("TIME ROW 30 ELEMENTS : "+mainLabel)
# TIMEROW = all_valueList[:-3]
# TIMEROW = [19.6, 50.5, 75.0, 79.8, 91.6, 93.1, 136.2, 173.4, 197.1, 217.9, 233.6, 253.8, 272.7, 283.4, 295.1, 307.4, 324.0, 307.0, 343.5, 357.2, 354.3, 344.0, 373.8, 324.6, 327.8, 291.2, 322.9]

# smoothing_data = pd.read_excel('./smoothing.xls')
# for column in smoothing_data:
#     TIMEROW = [i for i in smoothing_data[column]]

# timeline = np.arange(1,len(TIMEROW)+1)
# print(TIMEROW)


def average(array):
    return ( sum(array)/len(array) )

def d_pow2(array,average):
    summa = 0
    for i in range(len(array)):
        summa =summa + math.pow(array[i] - average,2)
    return ( summa/(len(array)-1) )

def sigma(D1,size1,D2,size2):
    return math.sqrt( ( (size1 - 1)*D1 + (size2 - 1)*D2 ) / (size1 + size2 - 2) )

def student(Y1,Y2):

    avg1 = average(Y1)
    avg2 = average(Y2)

    D1 = d_pow2(Y1,avg1)
    D2 = d_pow2(Y2,avg2)

    s = sigma(D1,len(Y1),D2,len(Y2))

    t = abs(avg1 - avg2)/(s*math.sqrt(1/len(Y1)+1/len(Y2)))
    print("t_emp за Критерієм Стюдента = ",t)
    return "Student "+str(t>2.05) 
    

def fisher(Y1,Y2):
    avg1 = average(Y1)
    avg2 = average(Y2)
    
    D1 = d_pow2(Y1,avg1)
    D2 = d_pow2(Y2,avg2)
    
    print("Середнє першого ряду: ",avg1)
    print("Середнє другого ряду: ",avg2)
    print("Варіанса першого рядку: ",D1)
    print("Варіанса другого рядку: ",D2)
    if D1>D2:
        res = D1/D2
        print("F_emp = ",D1/D2)
        return "Fisher "+str((res>3.15) or (res>2.45)) 
    else:
        res = D2/D1
        print("F_emp = ",D2/D1)
        return "Fisher "+str((res>3.15) or (res>2.45))

def smooth_avg(time_row,m):

    for column in time_row:
        time_row = [i for i in time_row[column]]

    smooth_row = []
    
    smooth_row = time_row[:int(m/2)]


    for i in range(0,len(time_row)-(m-1)):
        summ = 0
        for j in range(m):
            summ+=time_row[i+j]
        
        smooth_row.append(summ/m)

    temp = time_row[-int(m/2):]
    smooth_row = smooth_row+temp

    return {'data': time_row, 'result': smooth_row}

def getWeight(m):
    if m == 3:
        return [1/4,1/2,1/4]
    else:
        return [-3/35,12/35,17/35,12/35,-3/35]

def smooth_avg_weight(time_row,m):

    for column in time_row:
        time_row = [i for i in time_row[column]]

    weight = getWeight(m)

    smooth_row = []
    
    smooth_row = time_row[:int(m/2)]
    for i in range(0,len(time_row)-(m-1)):
        summ = 0
        for j in range(m):
            summ += time_row[i+j]*weight[j]
        smooth_row.append(summ)
    temp = time_row[-int(m/2):]
    smooth_row = smooth_row+temp

    return {'data': time_row, 'result': smooth_row}

# def smooth_exp(time_row):
#     predictNum = 3
    
#     q0 = sum(time_row[:5])/5
#     Q = []
#     Q.append(q0)
#     alpha = 0.2

#     for i in range(1,len(time_row)):
#         newY = alpha*time_row[i] + (1-alpha)*Q[i-1]
#         Q.append(newY)
#     '''
#     Y = []
#     Y += time_row
#     prediction = []
#     for j in range(len(time_row)-1,len(time_row)+predictNum-1):
#         #e = Y[j]-Q[j-1]
#         #predictY = Q[j-1] + alpha*e
#         predictY = ((2-alpha)*Y[j]-Q[j])/(1-alpha)
#         Y.append(predictY)

#         newQ = alpha*Y[j+1] + (1-alpha)*Q[j-1]
#         Q.append(newQ)
#     '''  
#     return Q

# def smooth_exp_pred(time_row):
#     predictNum = 1
    
#     q0 = sum(time_row[:5])/5
#     Q = []
#     Q.append(q0)
#     alpha = 0.2

#     for i in range(1,len(time_row)):
#         newY = alpha*time_row[i] + (1-alpha)*Q[i-1]
#         Q.append(newY)
    
#     Y = []
#     Y += time_row
#     prediction = []
#     for j in range(len(time_row)-1,len(time_row)+predictNum-1):
#         #e = Y[j]-Q[j-1]
#         #predictY = Q[j-1] + alpha*e
#         predictY = ((2-alpha)*Y[j]-Q[j])/(1-alpha)
#         Y.append(predictY)

#         newQ = alpha*Y[j+1] + (1-alpha)*Q[j-1]
#         Q.append(newQ)
      
#     return Q

def msr(time_row): #метод скінченних різниць - визначення степеню
    arrays = []
    origin = []
    origin = origin + time_row
    arrays.append(origin)

    for row in arrays:
        newRow =[]
        for i in range(1,len(row)):
            newRow.append(row[i]-row[i-1])
        arrays.append(newRow)
        if len(arrays) ==6:
            break
    deltas =[]
    
    for arr in range(1,len(arrays)):
        tempA =[]
        for i in range(len(arrays[arr])):
            tempA.append(abs(arrays[arr][i]))
        deltas.append(max(tempA))
    #print(deltas)
    
    delta = deltas.index(min(deltas))
    '''
    for arr in range(1,len(arrays)):
        tempA =[]
        maxi = max(arrays[arr])
        mini = min(arrays[arr])
        deltas.append(max(tempA))
    print(deltas)
    
    delta = deltas.index(min(deltas))
    '''
    #print(delta)
    
    return delta
    
def get_koef2(s0,s1,s2,t1,t2):
    Matrix = np.array([ [ s0,s1 ],[ s1,s2 ] ])
    Vector = np.array([ t1,t2 ])

    koefs = np.linalg.solve(Matrix,Vector)

    return koefs

def get_koef3(s0,s1,s2,s3,s4,t0,t1,t2):
    Matrix = np.array( [ [ s0,s1,s2 ],[ s1,s2,s3 ],[ s2,s3,s4 ] ] )
    Vector = np.array([t0,t1,t2])

    koefs = np.linalg.solve(Matrix,Vector)

    return koefs
    
def mnk(time_row,stepin):
    x = np.arange(1,len(time_row)+1)
    #x = np.array([2,3,4,5])
        
    s1 = sum(x)
    t0 = sum(time_row)
    x_2 = x*x
    s2 = sum(x_2)
    t1 = 0
    for i in range(1,len(time_row)+1):
        t1= t1+(x[i-1]*time_row[i-1])
    s0 = len(time_row)
    if stepin == 1:
        koefs = get_koef2(s0,s1,s2,t0,t1)
        return koefs
    else:
        x_3 = x_2*x
        x_4 = x_2*x_2
        s3 = sum(x_3)
        s4 = sum(x_4)
        t2 = 0
        for i in range(1,len(time_row)+1):
            t2= t2+(x_2[i-1]*time_row[i-1])
        koefs = get_koef3(s0,s1,s2,s3,s4,t0,t1,t2)
        return koefs

def polinom(koefs,x_time_value):
    if len(koefs)==2:
        #print(koefs[0] ," + ",koefs[1],"*X")
        return koefs[0] + koefs[1]*x_time_value
    else:
        #print(print(koefs[0] ," + ",koefs[1],"*X + ",koefs[2],"*X^2")
        return koefs[0] + koefs[1]*x_time_value + koefs[2]*(x_time_value**2)
    
def get_poly(time_row,stepin):

    koefs = mnk(time_row,stepin)
    #print(koefs)
    trend = []
    for i in range(1,len(time_row)+1):
        trend.append( polinom(koefs,i) )
    polinomLabel = "Mnogochlen"
    if len(koefs)==2:
        polinomLabel+=str(koefs[0]) +" + " + str(koefs[1]) +"*X"
    else:
        polinomLabel+=str(koefs[0]) +" + " + str(koefs[1]) +"*X + "+ str(koefs[2])+"*X^2"
    return trend,polinomLabel

def get_theoretical_y(b0, b1, x_es):
    y_thr = []
    for x in x_es:
        y_thr.append(b0+b1*x)
    return y_thr

# def expo(time_row):
#     ex = []
#     ex2 = []
#     exy=[]
#     for i in range(len(time_row)):
#         ex.append(np.exp(timeline[i]))
#         ex2.append(np.exp(timeline[i])**2)
#         exy.append(np.exp(timeline[i])*time_row[i])
#     x_sum = sum(ex)
#     x_mean = sum(ex)/len(ex)

#     x2_sum = sum(ex2)
#     x2_mean = sum(ex2)/len(ex2)

#     xy_sum = sum(exy)
#     xy_mean = sum(exy)/len(exy)

#     y_mean = sum(time_row)/len(time_row)
#     b1 = (xy_mean - x_mean*y_mean)/(x2_mean-x_mean**2)

#     print(f"b1 = {b1}")

#     b0 = y_mean-b1*x_mean

#     print(f"b0 = {b0}")
#     print("Equation:")
#     print(f"y* = {round(b0,2)} + {b1}*(e^x)")

#     y_pred = get_theoretical_y(b0,b1,ex)

#     print(y_pred)

#     return b0,b1,y_pred

# firstArr = TIMEROW[:-9] #1-21
# secondArr = TIMEROW[21:] #22-30

# print(len(firstArr),len(secondArr))

# print(fisher(firstArr,secondArr)) #YEN: F_table = 3.15 2.05
# print(student(firstArr,secondArr)) #YEN: t_table = 2.05

# #msr([2.68,2.67,2.78,2.85,3.72,2.94,3.57,3.86,4.21,3.98,4.29,4.35])
# #msr(TIMEROW)
# smooth_avg_3 = smooth_avg(TIMEROW,3)
# fig_avg_3 = plt.figure(1)
# plt.title("Згладження за ковзним середнім без ваг за трьома точками")
# plt.plot(timeline,TIMEROW,marker="D",color = 'green',label =mainLabel)
# plt.plot(timeline,smooth_avg_3,color = 'red',label ="згладжене")
# plt.legend()
# fig_avg_3.show()

# smooth_avg_5 = smooth_avg(TIMEROW,5)
# fig_avg_5 = plt.figure(2)
# plt.title("Згладження за ковзним середнім без ваг за 5-ма точками")
# plt.plot(timeline,TIMEROW,marker="D",color = 'green',label =mainLabel)
# plt.plot(timeline,smooth_avg_5,color = 'red',label ="згладжене")
# plt.legend()
# fig_avg_5.show()


# smooth_avg_w3 = smooth_avg_weight(TIMEROW,3)
# fig_avg_w3 = plt.figure(3)
# plt.title("Згладження за ковзним середнім з вагами за трьома точками")
# plt.plot(timeline,TIMEROW,marker="D",color = 'green',label =mainLabel)
# plt.plot(timeline,smooth_avg_w3,color = 'red',label ="згладжене")
# plt.legend()
# fig_avg_w3.show()

# smooth_avg_w5 = smooth_avg_weight(TIMEROW,5)
# fig_avg_w5 = plt.figure(4)
# plt.title("Згладження за ковзним середнім з вагами за 5-ма точками")
# plt.plot(timeline,TIMEROW,marker="D",color = 'green',label =mainLabel)
# plt.plot(timeline,smooth_avg_w5,color = 'red',label ="згладжене")
# plt.legend()
# fig_avg_w5.show()


# smooth_expL = smooth_exp(TIMEROW)
# fig_exp = plt.figure(5)
# plt.title("Експоненційне згладження")
# plt.plot(timeline,TIMEROW,marker="D",color = 'green',label =mainLabel)
# plt.plot(timeline,smooth_expL,color = 'red',label ="згладжене")
# plt.legend()
# fig_exp.show()

# # побудова многочлена
# delta = msr(TIMEROW)+1
              
# fig_poly = plt.figure(6)
# line,labelPOL = get_poly(TIMEROW,delta)
# print(labelPOL)
# plt.title("Тренд у вигляді многочлена")
# plt.scatter(np.arange(1,len(TIMEROW)+1),TIMEROW,label =mainLabel)
# plt.plot(np.arange(1,len(TIMEROW)+1),line,color='red',label = ("многочлен степеня"+str(delta)))
# plt.legend(loc='upper left', bbox_to_anchor=(1, 0.5))
# plt.tight_layout()
# plt.grid(True)
# fig_poly.show()

# #PREDICTION
# data = smooth_exp_pred(TIMEROW)

# print(len(data[:-1]))

# print("Передбачення на 31,32,33 :", data[-1])
# print("Реальні дані на 31,32,33 :",all_valueList[-3:])
# '''
# fig_pred = plt.figure(7)

# B0,B1,pred_line = expo(TIMEROW)
# plt.plot(np.arange(1,len(TIMEROW)+1),TIMEROW)
# plt.plot(np.arange(1,len(TIMEROW)+1),pred_line)
# fig_pred.show()

# predictionY = get_theoretical_y(B0,B1,np.exp([31,32,33]))
# print(predictionY)

# '''
# '''
# #-polynom by library-#
# f = np.polyfit(np.arange(0,30),TIMEROW,2)
# z = np.poly1d(f)
# newYY = []
# for i in range(len(TIMEROW)):
#     newYY.append(z(i+1))
# print(newYY)

# #plt.plot(newYY)
# '''
# plt.show()

