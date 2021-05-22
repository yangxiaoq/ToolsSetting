$(function(){
            $(".checktable li,input[name='shopcontent']:checkbox").click(function () {
                 var sel_shop = '';

                if(window.event.srcElement.tagName == "INPUT"){
                    $("input[name='shopcontent']:checkbox").each(function () {
                        if ($(this).is(":checked")) {
                            sel_shop += $(this).val() + '|';
                        }
                    });
                }else{
                    var index =$(this).index();
                    if($(".checktable").find('input:checkbox').eq(index).is(':checked')){
                        $(".checktable").find('input:checkbox').eq(index).prop("checked",false);
                    }else{
                        $(".checktable").find('input:checkbox').eq(index).prop("checked",true);
                    }
                    $("input[name='shopcontent']:checkbox").each(function (i,v) {
                        if ($(".checktable").find('input:checkbox').eq(i).is(":checked")) {
                            sel_shop += $(".checktable").find('input:checkbox').eq(i).val() + '|';
                        }
                    });
                }

                 sel_shop = sel_shop.substring(0,sel_shop.length-1);
//                 sel_shop = '[' +sel_shop +']'

                 $( "#sel_shop" ).val(sel_shop);

             });
		});