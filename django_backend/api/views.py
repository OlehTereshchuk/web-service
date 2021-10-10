from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response

import pandas as pd

from coursework import linear_time_trend, logarithmic_time_trend, hyperbolic_time_trend, smoothing
from smoothing_algorithms import smooth_avg, smooth_avg_weight

from django.http import HttpResponse
# Create your views here.
# data = [float(i.replace(',', '.')) for i in [j for j in request.data][0].split(' ')]


@api_view(['GET'])
def index(request):
    data="hello"
    return Response(data)


@api_view(['POST'])
def linearTrend(request):
    if '.xls' in str(request.FILES['file']):
        user_data = pd.read_excel(request.FILES['file'])
        data = linear_time_trend(user_data)
        return Response(data)
    error_message = 'Please, choose the correct file format'
    return Response({'error': error_message})
    


@api_view(['POST'])
def logarithmicTrend(request):
    if '.xls' in str(request.FILES['file']):
        user_data = pd.read_excel(request.FILES['file'])
        data = logarithmic_time_trend(user_data)
        return Response(data)
    error_message = 'Please, choose the correct file format'
    return Response({'error': error_message})
    

@api_view(['POST'])
def hyperbolicTrend(request):
    if '.xls' in str(request.FILES['file']):
        user_data = pd.read_excel(request.FILES['file'])
        data = hyperbolic_time_trend(user_data)
        return Response(data)
    error_message = 'Please, choose the correct file format'
    return Response({'error': error_message})

    
@api_view(['POST'])
def dataSmoothing(request):
    if '.xls' in str(request.FILES['file']):
        user_data = pd.read_excel(request.FILES['file'])
        data = smoothing(user_data)
        return Response(data)
    error_message = 'Please, choose the correct file format'
    return Response({'error': error_message})


@api_view(['POST'])
def movingAveragesWithoutWeightsThree(request):
    if '.xls' in str(request.FILES['file']):
        user_data = pd.read_excel(request.FILES['file'])
        data = smooth_avg(user_data, 3)
        return Response(data)
    error_message = 'Please, choose the correct file format'
    return Response({'error': error_message})
    

@api_view(['POST'])
def movingAveragesWithoutWeightsFive(request):
    if '.xls' in str(request.FILES['file']):
        user_data = pd.read_excel(request.FILES['file'])
        data = smooth_avg(user_data, 5)
        return Response(data)
    error_message = 'Please, choose the correct file format'
    return Response({'error': error_message})
    

@api_view(['POST'])
def movingAveragesWithWeightsThree(request):
    if '.xls' in str(request.FILES['file']):
        user_data = pd.read_excel(request.FILES['file'])
        data = smooth_avg_weight(user_data, 3)
        return Response(data)
    error_message = 'Please, choose the correct file format'
    return Response({'error': error_message})
    
    
@api_view(['POST'])
def movingAveragesWithWeightsFive(request):
    if '.xls' in str(request.FILES['file']):
        user_data = pd.read_excel(request.FILES['file'])
        data = smooth_avg_weight(user_data, 5)
        return Response(data)
    error_message = 'Please, choose the correct file format'
    return Response({'error': error_message})
    