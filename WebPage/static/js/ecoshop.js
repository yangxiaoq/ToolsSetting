$(function(){
    var selectsid = "";
    var invoice = "";
    var free_delivery = "";
    var delivery_markup = "";
    var sel_value = "";
    var sel_length = "{{sel_week|length}}";

     // 初始化
    $('#sel_opt_week').multiSelect({
        selectableHeader: "<div class='custom-header'>周期列表</div>",
        selectionHeader: "<div class='custom-header'>已选周期</div>",
        selectableOptgroup: true
    });

    $(".ms-selectable .ms-list li").click(function () {
        var index = $(this).index();
        if(index == 0){
            for(var i=1;i<sel_length;i++){
                $(".ms-selectable .ms-list").find('li').eq(i).css({'pointer-events':'none'});
            }
        } else {
            $(".ms-selectable .ms-list").find('li').eq(0).css({'pointer-events':'none'});
        }

     });

    $(".ms-selection .ms-list li").click(function () {
        var index = $(this).index();
        if(index == 0){
            for(var i=1;i<sel_length;i++){
                $(".ms-selectable .ms-list").find('li').eq(i).css({'pointer-events':''});
            }
        } else {
            if(sel_value.split(",").length -1 <= 1) {
                $(".ms-selectable .ms-list").find('li').eq(0).css({'pointer-events':''});
            }
        }
     });

    $("#clearselect").click(function(){
        $('.sel_week').empty();
    });

    $('.sel_week').change(function () {
        var value = $(this).val().toString();
        document.getElementById('week_text').value = value;
    });


     function getshopParam() {
            $.ajax({
                type: "POST",
                dataType: "json",
                url: "/getshopparam" ,
                data: {sid : selectsid},
                success: function (result) {
                    console.log(result);//打印服务端返回的数据(调试用)
                    if (result.success == "1") {
                        if(result.data.auto_receive_order == "1"){ //1 营业  2非营业
                            $("#invoiceRadio8").removeAttr("checked");
                            $("#invoiceRadio7").attr("checked","checked");
                        } else {
                            $("#invoiceRadio7").removeAttr("checked");
                            $("#invoiceRadio8").attr("checked","checked");
                        }
                        if(result.data.dinrule == "1"){ //1:固定餐点，2：用户时间顺延
                            $("#invoiceRadio10").removeAttr("checked");
                            $("#invoiceRadio9").attr("checked","checked");
                        } else {
                            $("#invoiceRadio9").removeAttr("checked");
                            $("#invoiceRadio10").attr("checked","checked");
                        }

                        $( "#sel_buss" ).val(result.data.business_type);

                        if(result.data.business_type.indexOf("2") != -1){
                            $("#buscheckzt").prop("checked", true);
                        }else{
                            $("#buscheckzt").prop("checked", false);
                        }

                        if(result.data.business_type.indexOf("1") != -1){
                            $("#buscheckwm").prop("checked", true);
                        } else {
                            $("#buscheckwm").prop("checked", false);
                        }

                        document.getElementsByName("devtime")[0].value=result.data.intervaltime;

                        if(result.data.dinrange != ""){
                            // let clear = document.getElementById("clearselect");
                            // clear.click();
                            var dinlist = result.data.dinrange.split(",");
                            for(var i=0;i<dinlist.length;i++){
                                var inde = parseInt(dinlist[i]) + 48 + "-selectable";
                                let dinli = document.getElementById(inde);
                                dinli.click();
                            }

                        }
                    } else {
                        alert(result.msg);
                    }
                    ;
                },
                error : function() {
                    alert("异常！");
                }
            });
        }


    $(document).ready(function() {
    });

    $(".checkshop li,input[name='shopcontent']:checkbox").click(function () {

        selectsid = $(this).val().match(/sid': '(\S*)', 'sname':/)[1];

        var sel_shop = '';

        $("input[name='shopcontent']:checkbox").each(function () {
            if ($(this).is(":checked")) {
                sel_shop += $(this).val() + '|';
            }
        });
         sel_shop = sel_shop.substring(0,sel_shop.length-1);
//                 sel_shop = '[' +sel_shop +']'

         $( "#sel_shop" ).val(sel_shop);

        if ($(this).is(":checked")) {
            invoice = $(this).val().match(/isinvoice': '(\S*)',/)[1];
            free_delivery = $(this).val().match(/free_delivery': '(\S*)',/)[1];
            delivery_markup = $(this).val().match(/delivery_markup': '(\S*)',/)[1];
            if(invoice == "1"){
                $("#invoiceRadio6").removeAttr("checked");
                $("#invoiceRadio5").attr("checked","checked");
            } else {
                $("#invoiceRadio6").removeAttr("checked");
                $("#invoiceRadio5").attr("checked","checked");
            }
            $( "#free_delivery" ).val(free_delivery);
            $( "#delivery_markup" ).val(delivery_markup);
            getshopParam();
        }


     });


    $(".lineofbuss,input[name='lineofbuss']:checkbox").click(function () {

        var sel_buss = '';

        $("input[name='lineofbuss']:checkbox").each(function () {
            if ($(this).is(":checked")) {
                sel_buss += $(this).val() + ',';
            }
        });
         sel_buss = sel_buss.substring(0,sel_buss.length-1);
//                 sel_shop = '[' +sel_shop +']'

        $( "#sel_buss" ).val(sel_buss);


     });




});