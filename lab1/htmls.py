# HTML форма для ввода данных
form_html = \
'''
<body>
    <form method="post">
        Имя: <input type="text" name="name"><br>
        Фамилия: <input type="text" name="surname"><br>
        E-mail: <input type="email" name="email"><br>
        <input type="submit" value="Отправить">
    </form>
</body>
'''

# HTML шаблон для вывода введенных данных
result_html = \
'''
    <h1>Введенные данные:</h1>
    Имя: {{ name }}<br>
    Фамилия: {{ surname }}<br>
    E-mail: {{ email }}
'''

# Страница с ссылкой на форму
index_html = \
'''
    <h1>Добро пожаловать!</h1>
    <a href="/input">Перейти к форме ввода</a>
'''