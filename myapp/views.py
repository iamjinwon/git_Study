from django.shortcuts import render, HttpResponse, redirect
import random
from django.views.decorators.csrf import csrf_exempt

nextId = 4
topics = [
    {'id' : 1, 'title':'routing', 'body':'Routing is ..'},
    {'id' : 2, 'title':'view', 'body':'View is ..'},
    {'id' : 3, 'title':'Model', 'body':'Model is ..'},
]

def HTMLTemplate(articleTag):
    global topics # 전역변수로 사용할 것임을 선언
    ol =''
    for topic in topics:
        ol += f'<li><a href="/read/{topic["id"]}">{topic["title"]}</a></li>'
    return (f'''
    <html>
    <body>
        <h1><a href="/">Django</a></h1>                    
        <ul>
            {ol}            
        </ul>
        {articleTag}
        <ul>
            <li><a href="/create/">create</a></li>      
        </ul>                                     
    </body>                     
    </html>                   
    ''') 

def index(request):
    article = '''
    <h2>Welcome</h2>
    Hello, Django    
'''
    return HttpResponse(HTMLTemplate(article))

def read(request, id):
    global topics
    article = ''
    for topic in topics:
        # print(type(topic['id']) , type(id)) 디버깅 해본 것
        if topic['id'] == int(id):
            article = f'<h2>{topic["title"]}</h2>{topic["body"]}'        
    return HttpResponse(HTMLTemplate(article))

@csrf_exempt
def create(request):
    global nextId
    if request.method == 'GET':
        article = '''
        <form action="/create/" method="post">
            <p><input type="text" name="title" placeholder="title"></p>
            <p><textarea name="body" placeholder="body"></textarea></p>
            <p><input type="submit"></p>
        </form>
        '''
        return HttpResponse(HTMLTemplate(article))
    elif request.method == 'POST':
        title = request.POST['title']
        body = request.POST['body']
        newTopic = {"id" : nextId, "title" : title, "body" : body}
        topics.append(newTopic)
        url = '/read/' + str(nextId)
        nextId += 1
        return redirect(url)
