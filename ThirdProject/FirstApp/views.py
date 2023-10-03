from django.shortcuts import render
import datetime;
def wishes3(request):
    date1=datetime.datetime.now()
    msg1='Hello User/Client...GOOD';
    hr=int(date1.strftime('%H'));
    imgs='image1.jpg';
    if hr<12:
        msg1+=' Morning!!'
        imgs = 'images.jpeg';
    elif hr<16:
        msg1+=' Afternoon!!'
        imgs = 'images1.jpeg';
    elif hr<20:
        msg1+=' Evening!!'
        imgs = 'images2.jpg';
    else:
        msg1='Hello User/Client...Very Good Night!!'
        imgs = 'images3.jpg';
    dict1={'date1':date1,'msg1':msg1,'imgs':imgs}
    return render(request,'FirstApp/wishes3.html',context=dict1);
def imgsgalley(request):
        date1=datetime.datetime.now();
        msg1='HELLO USER.....!!!CLINT GOOD MORNING';
        hr=int(date1.strftime('%H'));
        dict1 = {'date1': date1, 'msg1': msg1}
        return render(request, 'FirstApp/imgsgallery.html', context=dict1);
def imgsgallery(request):
    date1=datetime.datetime.now()
    msg1='HELLO USER ...!!CLINT  GOOD MORNING';
    hr=int(date1.strftime('%H'))
    dict1={'date1':date1,'msg1':msg1}
    return render(request, "FirstApp/imgsgallery2.html",context=dict1);
def sample(request):
    return render(request, 'FirstApp/sample.html');
def hyperlinks(request):
    date1=datetime.datetime.now()
    msg1='***Django Hyprerlinks**';
    dict1={'date1':date1,'msg1':msg1}
    return render(request, 'FirstApp/hyperlinks.html',context=dict1);




# Create your views here.
