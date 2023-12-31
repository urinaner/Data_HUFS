from flask import Flask
from flask import request
from flask import redirect

app=Flask(__name__)

nextId = 4
topics=[
    {'id':1, 'title':'html','body': 'html is ...'},
    {'id':2, 'title':'css','body': 'css is ...'},
    {'id':3, 'title':'javascript','body': 'javascript is ...'},
]


def template(contents, content):   # 중복된 코드 하나로 묶기
     return f'''<!doctype html>
    <html>
        <body>
            <h1><a href="/">WEB</a></h1>
            <ol>
                {contents}
            </ol>
            {content}
            <ul>
                <li><a href='/create/'>create</a></li>        
            </ul>   
        </body>
    </html>
    '''


def getContents():   # 중복된 코드 하나로 묶기
    liTags = ''
    for topic in topics:
        liTags = liTags + f'<li><a href="/read/{topic["id"]}/">{topic["title"]}</a></li>'
    return liTags



@app.route('/')
def indenx():
    return template(getContents(), '<h2>Welcome</h2>Hello, Web')


@app.route('/read/<int:id>/')
def read(id):
    title = ''
    body = ''
    for topic in topics:
        if id == topic['id']:
            title = topic['title']
            body = topic['body']
            break
    return template(getContents(), f'<h2>{title}</h2>{body}')


@app.route('/create/', methods=['GET', 'POST']) ## Get: url 통해서 data 전송, 즉 url 안에 데이터 정보가 담겨있음. 반면에, POST: url 주소 변동 없음. 은밀하게 데이터 전송함.
def create():
    if request.method == 'GET':
        content= '''
            <form action="/create/" method="POST">  
                <p><input type="text" name="title" placeholder="title"></p>
                <p><textarea name="body" placeholder="body"></textarea></p>
                <p><input type="submit" value="create"></p>
            </form>
        '''
        return template(getContents(), content)
    elif request.method == 'POST' :
        global nextId
        title = request.form['title']
        body = request.form['body']
        newTopic = {'id': nextId, 'title': title, 'body': body}
        topics.append(newTopic)
        url = '/read/' + str(nextId) + '/'
        nextId = nextId + 1
        return redirect(url)


app.run(debug=True)
