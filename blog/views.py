from django.http import HttpResponse
from django.shortcuts import render
import random
def home(request):
    return HttpResponse("<p style='text-align:center;'>Urlga   <b>password/easy</b>    <b>password/medium</b>   <b>password/hard</b>larning birini tanlab kiriting! !</p>")

def generate_password(request, complexity):
    length = random.randint(8, 20)

    if complexity == 'easy':
        password = "".join(random.choice('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ') for _ in range(length))
        return render(request, 'blog/index.html', {'password': password})

    elif complexity == 'medium':
        length = int(length / 2)
        letters = "".join(random.choice('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ') for _ in range(length))
        numbers = "".join(random.choice('0123456789') for _ in range(length))
        password = "".join(random.sample(letters + numbers, len(letters + numbers)))
        return render(request, 'blog/index.html', {'password': password})

    else:
        leng = int(length // 3)
        lent2 = length - leng * 2
        letters = "".join(random.choice('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ') for _ in range(leng + 1))
        numbers = "".join(random.choice('0123456789') for _ in range(leng + 1))
        characters = "".join(random.choice('!@#$%^&*()') for _ in range(lent2 - 2))
        password = "".join(random.sample(letters + numbers + characters, len(letters + numbers + characters)))
        return render(request, 'blog/index.html', {'password': password})

