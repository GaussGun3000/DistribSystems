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
