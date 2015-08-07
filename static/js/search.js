/**
 * Created by zavier on 6/08/15.
 */

$('#search-form').submit(function(e){
    $.post('/search/', $(this).serialize(), function(data){
        $('.tweets'.html(data));
    });
    e.preventDefault();
});