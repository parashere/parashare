from django.shortcuts import render
from django.http import HttpResponse
from .nfc_reader import read_nfc_tag


def page0(request):
    """ページ0 - 立ち上げ中画面"""
    return render(request, '0.html')

def page1(request):
    """ページ1 - スタンバイ画面"""
    return render(request, '1.html')

def page2(request):
    """ページ2 - ログイン成功画面"""
    student_id = request.GET.get('studentID', 't323')
    context = {
        'student_id': student_id
    }
    return render(request, '2.html', context)

def page3(request):
    """ページ3"""
    return render(request, '3.html')

def page4(request):
    """ページ4"""
    return render(request, '4.html')

def page5(request):
    """ページ5"""
    return render(request, '5.html')

def page6(request):
    """ページ6"""
    return render(request, '6.html')

def page7(request):
    """ページ7"""
    return render(request, '7.html')

def page8(request):
    """ページ8"""
    return render(request, '8.html')

def page9(request):
    """ページ9"""
    return render(request, '9.html')
