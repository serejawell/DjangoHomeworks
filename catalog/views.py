from django.shortcuts import render


def home(request):
    return render(request, template_name='home.html')


def contacts(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        message = request.POST.get('message')
        # а также передается информация, которую заполнил пользователь
        print(f'''Пользователь: {name}\nНомер телефона: {phone}\nСообщение: "{message}"\n''')
    return render(request, template_name='contacts.html')
