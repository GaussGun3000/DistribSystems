TEMPLATE = '''
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Converter Client</title>
</head>
<body>
    <h2>Conversion Result: {{ result }}</h2>
    <form action="/convert-client" method="get">
        <input type="number" name="amount" placeholder="Amount" required>
        <input type="number" step="any" name="rate" placeholder="Rate" required>
        <input type="submit" value="Convert">
    </form>
</body>
</html>
'''
# Страница с ссылкой на форму
index_html = '''
    <h1>Добро пожаловать!</h1>
    <a href="/convert-client">страница конвертации</a>
'''