AUTOCOMPLETE = '''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Autocomplete Demo</title>
    <script src="https://code.jquery.com/jquery-3.6.0.min.js"></script>
    <script src="{{ url_for('static', filename='autocomplete.js') }}"></script>
</head>
<body>
    <input type="text" id="autocomplete" placeholder="Start typing...">
    <button id="toggleAllWords">Toggle All Words</button>
    <div id="suggestions"></div>
    <hr id="separator" style="display:none;"> <!-- Изначально скрытая черта -->
    <div id="allWords" style="display:none;"></div> <!-- Изначально скрытый список -->
</body>
</html>
'''
