AUTOCOMPLETE = ''' <!DOCTYPE html>
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
    });
    </script>
</head>
<body>
    <input type="text" id="autocomplete" placeholder="Start typing...">
    <div id="suggestions"></div>
</body>
</html> '''
