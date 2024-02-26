AUTOCOMPLETE = '''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Autocomplete Demo</title>
    <script src="https://code.jquery.com/jquery-3.6.0.min.js"></script>
    <script>
    $(document).ready(function(){
        $("#autocomplete").keyup(function(){
            var searchText = $(this).val();
            if(searchText.length > 1){
                $.getJSON("/autocomplete?term=" + searchText, function(data){
                    $('#suggestions').empty();
                    $.each(data, function(key, value){
                        $('#suggestions').append('<div>' + value + '</div>');
                    });
                });
            } else {
                $('#suggestions').empty();
            }
        });

        $("#toggleAllWords").click(function(){
            var allWordsDiv = $("#allWords");
            if(allWordsDiv.is(":visible")){
                allWordsDiv.hide();
                $("#separator").hide(); // Скрываем разделительную черту
            } else {
                allWordsDiv.empty(); // Очищаем текущий список
                $.getJSON("/allwords", function(data){
                    $.each(data, function(key, value){
                        allWordsDiv.append('<div>' + value + '</div>');
                    });
                });
                allWordsDiv.show();
                $("#separator").show(); // Показываем разделительную черту
            }
        });
    });
    </script>
</head>
<body>
    <input type="text" id="autocomplete" placeholder="Start typing...">
    <button id="toggleAllWords">Toggle All Words</button>
    <div id="suggestions"></div>
    <hr id="separator" style="display:none;"> <!-- Изначально скрытая черта -->
    <div id="allWords" style="display:none;"></div> <!-- Изначально скрытый список -->
</body>
</html> '''
