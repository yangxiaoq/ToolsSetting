$(function(){
    $(document).ready(function() {
        text_foled('.p1', 180);
    });
});

function text_foled(clas, num) {
    var num = num;
    var a = $("<a></a>").on('click', showText).addClass('a-text').text("【展开】");
    var b = $("<a></a>").on('click', showText).addClass('a-text').text("【折叠】");
    var p = $("<p></p>").addClass('p2');
    var str = $(clas).text();
    $(clas).after(p);
    if (str.length > num) {
        var text = str.substring(0, num) + "...";
        $(clas).html(text).append(a);
    }
    $('.p2').html(str).append(b);
    function showText() {
        $(this).parent().hide().siblings().show();
    }
}