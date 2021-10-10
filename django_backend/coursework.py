# import pandas as pd
import numpy as np
# import matplotlib.pyplot as plt
# import seaborn

# user_data = pd.read_excel('./data.xls')

def linear_time_trend(user_data):

    preprocessed_data = {}
    for column in user_data:
        preprocessed_data['data'] = [i for i in user_data[column]]
        preprocessed_data['t'] = [i+1 for i in range(len(user_data[column]))]
        preprocessed_data['t*t'] = [(i+1)**2 for i in range(len(user_data[column]))]
        preprocessed_data['y*t'] = [round(preprocessed_data['data'][i]*preprocessed_data['t'][i], 1) 
            for i in range(len(user_data[column]))]

        preprocessed_data['average_data'] = sum(preprocessed_data['data'])/len(preprocessed_data['data'])
        preprocessed_data['average_t'] = sum(preprocessed_data['t'])/len(preprocessed_data['t'])
        preprocessed_data['average_t*t'] = sum(preprocessed_data['t*t'])/len(preprocessed_data['t*t'])
        preprocessed_data['average_y*t'] = sum(preprocessed_data['y*t'])/len(preprocessed_data['y*t'])

        preprocessed_data['b1'] = (preprocessed_data['average_y*t'] 
            - preprocessed_data['average_data']*preprocessed_data['average_t'])/(preprocessed_data['average_t*t'] 
            - preprocessed_data['average_t']**2)
        preprocessed_data['b2'] = preprocessed_data['average_data'] - preprocessed_data['b1']*preprocessed_data['average_t']

        preprocessed_data['linear'] = [preprocessed_data['b2'] + preprocessed_data['b1']*t for t in preprocessed_data['t']]

        preprocessed_data['prediction'] = preprocessed_data['b2'] + preprocessed_data['b1'] * (preprocessed_data['t'][-1] + 1)

        preprocessed_data['correlation'] = (len(preprocessed_data['data'])
            *sum([preprocessed_data['data'][i]*preprocessed_data['linear'][i] for i in range(len(preprocessed_data['data']))]) 
            - sum(preprocessed_data['data'])*sum(preprocessed_data['linear'])) / (
             (len(preprocessed_data['data'])*sum([i**2 for i in preprocessed_data['data']]) 
            - (sum(preprocessed_data['data']))**2)*(len(preprocessed_data['linear'])
            *sum([i**2 for i in preprocessed_data['linear']]) 
            - (sum(preprocessed_data['linear']))**2))**0.5

    return preprocessed_data


#######################################################################################################


def logarithmic_time_trend(user_data):

    preprocessed_data = {}
    for column in user_data:
        preprocessed_data['data'] = [i for i in user_data[column]]
        preprocessed_data['t'] = [i+1 for i in range(len(user_data[column]))]
        preprocessed_data['ln(t)'] = [np.log(t) for t in preprocessed_data['t']]
        preprocessed_data['ln(t)*ln(t)'] = [np.log(t)**2 for t in preprocessed_data['t']]
        preprocessed_data['y*ln(t)'] = [round(preprocessed_data['data'][i]*preprocessed_data['ln(t)'][i], 1) 
            for i in range(len(user_data[column]))]

        preprocessed_data['average_data'] = sum(preprocessed_data['data'])/len(preprocessed_data['data'])
        preprocessed_data['average_ln(t)'] = sum(preprocessed_data['ln(t)'])/len(preprocessed_data['ln(t)'])
        preprocessed_data['average_ln(t)*ln(t)'] = sum(preprocessed_data['ln(t)*ln(t)'])/len(preprocessed_data['ln(t)*ln(t)'])
        preprocessed_data['average_y*ln(t)'] = sum(preprocessed_data['y*ln(t)'])/len(preprocessed_data['y*ln(t)'])

        preprocessed_data['b1'] = (preprocessed_data['average_y*ln(t)'] 
            - preprocessed_data['average_data']*preprocessed_data['average_ln(t)'])/(preprocessed_data['average_ln(t)*ln(t)'] 
            - preprocessed_data['average_ln(t)']**2)
        preprocessed_data['b2'] = preprocessed_data['average_data'] - preprocessed_data['b1']*preprocessed_data['average_ln(t)']

        preprocessed_data['logarithmic'] = [preprocessed_data['b2'] + preprocessed_data['b1']*t for t in preprocessed_data['ln(t)']]
        preprocessed_data['prediction'] = preprocessed_data['b2'] + preprocessed_data['b1'] * np.log((preprocessed_data['t'][-1] + 1))

        preprocessed_data['correlation'] = (len(preprocessed_data['data'])
            *sum([preprocessed_data['data'][i]*preprocessed_data['logarithmic'][i] for i in range(len(preprocessed_data['data']))]) 
            - sum(preprocessed_data['data'])*sum(preprocessed_data['logarithmic'])) / (
            (len(preprocessed_data['data'])*sum([i**2 for i in preprocessed_data['data']]) 
            - (sum(preprocessed_data['data']))**2)*(len(preprocessed_data['logarithmic'])
            *sum([i**2 for i in preprocessed_data['logarithmic']]) 
            - (sum(preprocessed_data['logarithmic']))**2))**0.5

    return preprocessed_data


#######################################################################################################


def hyperbolic_time_trend(user_data):


    preprocessed_data = {}
    for column in user_data:
        preprocessed_data['data'] = [i for i in user_data[column]]
        preprocessed_data['t'] = [i+1 for i in range(len(user_data[column]))]
        preprocessed_data['1/t'] = [1/t for t in preprocessed_data['t']]
        preprocessed_data['1/t*1/t'] = [(1/t)**2 for t in preprocessed_data['t']]
        preprocessed_data['y*1/t'] = [round(preprocessed_data['data'][i]*preprocessed_data['1/t'][i], 1) 
            for i in range(len(user_data[column]))]

        preprocessed_data['average_data'] = sum(preprocessed_data['data'])/len(preprocessed_data['data'])
        preprocessed_data['average_1/t'] = sum(preprocessed_data['1/t'])/len(preprocessed_data['1/t'])
        preprocessed_data['average_1/t*1/t'] = sum(preprocessed_data['1/t*1/t'])/len(preprocessed_data['1/t*1/t'])
        preprocessed_data['average_y*1/t'] = sum(preprocessed_data['y*1/t'])/len(preprocessed_data['y*1/t'])

        preprocessed_data['b1'] = (preprocessed_data['average_y*1/t']  
            - preprocessed_data['average_data']*preprocessed_data['average_1/t'])/(preprocessed_data['average_1/t*1/t'] 
            - preprocessed_data['average_1/t']**2)
        preprocessed_data['b2'] = preprocessed_data['average_data'] - preprocessed_data['b1']*preprocessed_data['average_1/t']

        preprocessed_data['hyperbolic'] = [preprocessed_data['b2'] + preprocessed_data['b1']*t for t in preprocessed_data['1/t']]
        preprocessed_data['prediction'] = preprocessed_data['b2'] + preprocessed_data['b1'] * (1/(preprocessed_data['t'][-1] + 1))

        preprocessed_data['correlation'] = (len(preprocessed_data['data'])
            *sum([preprocessed_data['data'][i]*preprocessed_data['hyperbolic'][i] for i in range(len(preprocessed_data['data']))]) 
            - sum(preprocessed_data['data'])*sum(preprocessed_data['hyperbolic'])) / (
            (len(preprocessed_data['data'])*sum([i**2 for i in preprocessed_data['data']]) 
            - (sum(preprocessed_data['data']))**2)*(len(preprocessed_data['hyperbolic'])
            *sum([i**2 for i in preprocessed_data['hyperbolic']]) 
            - (sum(preprocessed_data['hyperbolic']))**2))**0.5

    return preprocessed_data


#######################################################################################################

# smoothing_data = pd.read_excel('./smoothing.xls')


def smoothing(smoothing_data):
    preprocessed_data = {}
    parameters = linear_time_trend(smoothing_data)

    amountOfPredicts = 1

    for column in smoothing_data:
        preprocessed_data['data'] = [i for i in smoothing_data[column]]
        preprocessed_data['t'] = [i + 1 for i in range(len(smoothing_data[column]))]

        preprocessed_data['b1'] = parameters['b1']
        preprocessed_data['b2'] = parameters['b2']
        preprocessed_data['alpha'] = 2/3
        preprocessed_data['m'] = 1

        preprocessed_data['s11'] = preprocessed_data['b2'] - ((1-preprocessed_data['alpha'])/preprocessed_data['alpha'])*preprocessed_data['b1']
        preprocessed_data['s21'] = preprocessed_data['b2'] - (2*(1-preprocessed_data['alpha'])/preprocessed_data['alpha'])*preprocessed_data['b1']

        prev_s1 = preprocessed_data['s11']
        s1 = [preprocessed_data['s11']]

        for i in range(len(preprocessed_data['data']) - 1):
            s1.append(preprocessed_data['alpha']*preprocessed_data['data'][i+1] + (1-preprocessed_data['alpha'])*prev_s1)
            prev_s1 = preprocessed_data['alpha']*preprocessed_data['data'][i+1] + (1-preprocessed_data['alpha'])*prev_s1
        preprocessed_data['s1'] = s1

        prev_s2 = preprocessed_data['s21']
        s2 = [preprocessed_data['s21']]

        for i in range(len(preprocessed_data['data']) - 1):
            s2.append(preprocessed_data['alpha']*preprocessed_data['s1'][i+1] + (1-preprocessed_data['alpha'])*prev_s2)
            prev_s2 = preprocessed_data['alpha']*preprocessed_data['s1'][i+1] + (1-preprocessed_data['alpha'])*prev_s2
        preprocessed_data['s2'] = s2

        preprocessed_data['^b1'] = [2*preprocessed_data['s1'][i] 
            - preprocessed_data['s2'][i] for i in range(len(preprocessed_data['s1']))]
        preprocessed_data['^b2'] = [(preprocessed_data['alpha']/(1-preprocessed_data['alpha']))*(preprocessed_data['s1'][i] 
            - preprocessed_data['s2'][i]) for i in range(len(preprocessed_data['s1']))]

        preprocessed_data['smoothing'] = [preprocessed_data['^b1'][i] + preprocessed_data['^b2'][i] 
            * preprocessed_data['m'] for i in range(len(preprocessed_data['^b1']))]
        preprocessed_data['prediction'] = preprocessed_data['^b1'][-1] + preprocessed_data['^b2'][-1]*amountOfPredicts

        preprocessed_data['correlation'] = (len(preprocessed_data['data'])
            *sum([preprocessed_data['data'][i]*preprocessed_data['smoothing'][i] for i in range(len(preprocessed_data['data']))]) 
            - sum(preprocessed_data['data'])*sum(preprocessed_data['smoothing'])) / (
            (len(preprocessed_data['data'])*sum([i**2 for i in preprocessed_data['data']]) 
            - (sum(preprocessed_data['data']))**2)*(len(preprocessed_data['smoothing'])
            *sum([i**2 for i in preprocessed_data['smoothing']]) - (sum(preprocessed_data['smoothing']))**2))**0.5
    return preprocessed_data


# data = smoothing(smoothing_data)

# for key in data:
#     print(key, data[key])

# plt.plot(data['t'], data['data'])
# plt.plot(data['t'], data['smoothed'])
# plt.show()

#######################################################################################################
#######################################################################################################
#######################################################################################################


# def linear_time_trend(user_data):

#     preprocessed_data = {}
#     for column in user_data:
#         preprocessed_data['data'] = [i for i in user_data]
#         preprocessed_data['t'] = [i+1 for i in range(len(user_data))]
#         preprocessed_data['t*t'] = [(i+1)**2 for i in range(len(user_data))]
#         preprocessed_data['y*t'] = [round(preprocessed_data['data'][i]*preprocessed_data['t'][i], 1) for i in range(len(user_data))]

#         preprocessed_data['average_data'] = sum(preprocessed_data['data'])/len(preprocessed_data['data'])
#         preprocessed_data['average_t'] = sum(preprocessed_data['t'])/len(preprocessed_data['t'])
#         preprocessed_data['average_t*t'] = sum(preprocessed_data['t*t'])/len(preprocessed_data['t*t'])
#         preprocessed_data['average_y*t'] = sum(preprocessed_data['y*t'])/len(preprocessed_data['y*t'])

#         preprocessed_data['b1'] = (preprocessed_data['average_y*t'] - preprocessed_data['average_data']*preprocessed_data['average_t'])/(preprocessed_data['average_t*t'] - preprocessed_data['average_t']**2)
#         preprocessed_data['b2'] = preprocessed_data['average_data'] - preprocessed_data['b1']*preprocessed_data['average_t']
#         preprocessed_data['linear'] = [preprocessed_data['b2'] + preprocessed_data['b1']*t for t in preprocessed_data['t']]
#         preprocessed_data['correlation'] = (len(preprocessed_data['data'])*sum([preprocessed_data['data'][i]*preprocessed_data['linear'][i] for i in range(len(preprocessed_data['data']))]) - sum(preprocessed_data['data'])*sum(preprocessed_data['linear'])) / (
#             (len(preprocessed_data['data'])*sum([i**2 for i in preprocessed_data['data']]) - (sum(preprocessed_data['data']))**2)*(len(preprocessed_data['linear'])*sum([i**2 for i in preprocessed_data['linear']]) - (sum(preprocessed_data['linear']))**2))**0.5

#     return preprocessed_data

# def logarithmic_time_trend(user_data):

#     preprocessed_data = {}
#     for column in user_data:
#         preprocessed_data['data'] = [i for i in user_data]
#         preprocessed_data['t'] = [i+1 for i in range(len(user_data))]
#         preprocessed_data['ln(t)'] = [np.log(t) for t in preprocessed_data['t']]
#         preprocessed_data['ln(t)*ln(t)'] = [np.log(t)**2 for t in preprocessed_data['t']]
#         preprocessed_data['y*ln(t)'] = [round(preprocessed_data['data'][i]*preprocessed_data['ln(t)'][i], 1) for i in range(len(user_data))]

#         preprocessed_data['average_data'] = sum(preprocessed_data['data'])/len(preprocessed_data['data'])
#         preprocessed_data['average_ln(t)'] = sum(preprocessed_data['ln(t)'])/len(preprocessed_data['ln(t)'])
#         preprocessed_data['average_ln(t)*ln(t)'] = sum(preprocessed_data['ln(t)*ln(t)'])/len(preprocessed_data['ln(t)*ln(t)'])
#         preprocessed_data['average_y*ln(t)'] = sum(preprocessed_data['y*ln(t)'])/len(preprocessed_data['y*ln(t)'])

#         preprocessed_data['b1'] = (preprocessed_data['average_y*ln(t)'] - preprocessed_data['average_data']*preprocessed_data['average_ln(t)'])/(preprocessed_data['average_ln(t)*ln(t)'] - preprocessed_data['average_ln(t)']**2)
#         preprocessed_data['b2'] = preprocessed_data['average_data'] - preprocessed_data['b1']*preprocessed_data['average_ln(t)']
#         preprocessed_data['logarithmic'] = [preprocessed_data['b2'] + preprocessed_data['b1']*t for t in preprocessed_data['ln(t)']]
#         preprocessed_data['correlation'] = (len(preprocessed_data['data'])*sum([preprocessed_data['data'][i]*preprocessed_data['logarithmic'][i] for i in range(len(preprocessed_data['data']))]) - sum(preprocessed_data['data'])*sum(preprocessed_data['logarithmic'])) / (
#             (len(preprocessed_data['data'])*sum([i**2 for i in preprocessed_data['data']]) - (sum(preprocessed_data['data']))**2)*(len(preprocessed_data['logarithmic'])*sum([i**2 for i in preprocessed_data['logarithmic']]) - (sum(preprocessed_data['logarithmic']))**2))**0.5

#     return preprocessed_data


# #######################################################################################################


# def hyperbolic_time_trend(user_data):

#     preprocessed_data = {}
#     for column in user_data:
#         preprocessed_data['data'] = [i for i in user_data]
#         preprocessed_data['t'] = [i+1 for i in range(len(user_data))]
#         preprocessed_data['1/t'] = [1/t for t in preprocessed_data['t']]
#         preprocessed_data['1/t*1/t'] = [(1/t)**2 for t in preprocessed_data['t']]
#         preprocessed_data['y*1/t'] = [round(preprocessed_data['data'][i]*preprocessed_data['1/t'][i], 1) for i in range(len(user_data))]

#         preprocessed_data['average_data'] = sum(preprocessed_data['data'])/len(preprocessed_data['data'])
#         preprocessed_data['average_1/t'] = sum(preprocessed_data['1/t'])/len(preprocessed_data['1/t'])
#         preprocessed_data['average_1/t*1/t'] = sum(preprocessed_data['1/t*1/t'])/len(preprocessed_data['1/t*1/t'])
#         preprocessed_data['average_y*1/t'] = sum(preprocessed_data['y*1/t'])/len(preprocessed_data['y*1/t'])

#         preprocessed_data['b1'] = (preprocessed_data['average_y*1/t'] - preprocessed_data['average_data']*preprocessed_data['average_1/t'])/(preprocessed_data['average_1/t*1/t'] - preprocessed_data['average_1/t']**2)
#         preprocessed_data['b2'] = preprocessed_data['average_data'] - preprocessed_data['b1']*preprocessed_data['average_1/t']
#         preprocessed_data['hyperbolic'] = [preprocessed_data['b2'] + preprocessed_data['b1']*t for t in preprocessed_data['1/t']]
#         preprocessed_data['correlation'] = (len(preprocessed_data['data'])*sum([preprocessed_data['data'][i]*preprocessed_data['hyperbolic'][i] for i in range(len(preprocessed_data['data']))]) - sum(preprocessed_data['data'])*sum(preprocessed_data['hyperbolic'])) / (
#             (len(preprocessed_data['data'])*sum([i**2 for i in preprocessed_data['data']]) - (sum(preprocessed_data['data']))**2)*(len(preprocessed_data['hyperbolic'])*sum([i**2 for i in preprocessed_data['hyperbolic']]) - (sum(preprocessed_data['hyperbolic']))**2))**0.5

#     return preprocessed_data


# #######################################################################################################

# # smoothing_data = pd.read_excel('./smoothing.xls')


# def smoothing(smoothing_data):
#     preprocessed_data = {}
#     parameters = linear_time_trend(smoothing_data)

#     for column in smoothing_data:
#         preprocessed_data['data'] = [i for i in smoothing_data]
#         preprocessed_data['t'] = [i + 1 for i in range(len(smoothing_data))]
#         preprocessed_data['b1'] = parameters['b1']
#         preprocessed_data['b2'] = parameters['b2']
#         preprocessed_data['alpha'] = 2/3
#         preprocessed_data['m'] = 1
#         preprocessed_data['s11'] = preprocessed_data['b2'] - ((1-preprocessed_data['alpha'])/preprocessed_data['alpha'])*preprocessed_data['b1']
#         preprocessed_data['s21'] = preprocessed_data['b2'] - (2*(1-preprocessed_data['alpha'])/preprocessed_data['alpha'])*preprocessed_data['b1']

#         prev_s1 = preprocessed_data['s11']
#         s1 = [preprocessed_data['s11']]

#         for i in range(len(preprocessed_data['data']) - 1):
#             s1.append(preprocessed_data['alpha']*preprocessed_data['data'][i+1] + (1-preprocessed_data['alpha'])*prev_s1)
#             prev_s1 = preprocessed_data['alpha']*preprocessed_data['data'][i+1] + (1-preprocessed_data['alpha'])*prev_s1
#         preprocessed_data['s1'] = s1

#         prev_s2 = preprocessed_data['s21']
#         s2 = [preprocessed_data['s21']]

#         for i in range(len(preprocessed_data['data']) - 1):
#             s2.append(preprocessed_data['alpha']*preprocessed_data['s1'][i+1] + (1-preprocessed_data['alpha'])*prev_s2)
#             prev_s2 = preprocessed_data['alpha']*preprocessed_data['s1'][i+1] + (1-preprocessed_data['alpha'])*prev_s2
#         preprocessed_data['s2'] = s2

#         preprocessed_data['^b2'] = [2*preprocessed_data['s1'][i] - preprocessed_data['s2'][i] for i in range(len(preprocessed_data['s1']))]
#         preprocessed_data['^b1'] = [(preprocessed_data['alpha']/(1-preprocessed_data['alpha']))*(preprocessed_data['s1'][i] - preprocessed_data['s2'][i]) for i in range(len(preprocessed_data['s1']))]
#         preprocessed_data['smoothed'] = [preprocessed_data['^b2'][i] + preprocessed_data['^b1'][i] * preprocessed_data['m'] for i in range(len(preprocessed_data['^b2']))]
#         preprocessed_data['correlation'] = (len(preprocessed_data['data'])*sum([preprocessed_data['data'][i]*preprocessed_data['smoothed'][i] for i in range(len(preprocessed_data['data']))]) - sum(preprocessed_data['data'])*sum(preprocessed_data['smoothed'])) / (
#             (len(preprocessed_data['data'])*sum([i**2 for i in preprocessed_data['data']]) - (sum(preprocessed_data['data']))**2)*(len(preprocessed_data['smoothed'])*sum([i**2 for i in preprocessed_data['smoothed']]) - (sum(preprocessed_data['smoothed']))**2))**0.5
#     return preprocessed_data