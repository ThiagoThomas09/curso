from django.shortcuts import render

def home(request):
    speakers = [
        {'name': 'Michael Scott', 'photo': 'https://miro.medium.com/v2/resize:fit:1396/1*njwXqsShWvK81ANQCMBevw.jpeg'},
        {'name': 'Jim Halpert', 'photo': 'https://www.denofgeek.com/wp-content/uploads/2021/10/Jim-The-Office-John-Krasinski.jpg?fit=1200%2C675'}
    ]
    return render(request, 'index.html', {'speakers': speakers})