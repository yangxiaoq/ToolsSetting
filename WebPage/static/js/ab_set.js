$(function(){
            $(document).ready(function() {
                $('#date').daterangepicker();
                $('#time').daterangepicker({
                    "timePicker": true,
                    'clanderPicker':false,
                    "timePicker24Hour": true,
                    "linkedCalendars": false,
                    "autoUpdateInput": false, //自动更新默认日期
    //                "locale": {
    //                    format: 'YYYY-MM-DD',
    //                    separator: ' ~ ',
    //                    applyLabel: "应用",
    //                    cancelLabel: "取消",
    //                    resetLabel: "重置",
    //                }
                }, function(start, end, label) {
                    if(!this.startDate){
                        this.element.val('');
                    }else{
                        this.element.val(this.startDate.format(this.locale.formatmin) + this.locale.separator + this.endDate.format(this.locale.formatmin));
                    }
                });
            });

            $(".checktable li,input[name='tablecontent']:checkbox").click(function () {
                 var sel_table = '';

                if(window.event.srcElement.tagName == "INPUT"){
                    $("input[name='tablecontent']:checkbox").each(function () {
                        if ($(this).is(":checked")) {
                            sel_table += $(this).val() + '|';
                        }
                    });
                }else{
                    var index =$(this).index();
                    if($(".checktable").find('input:checkbox').eq(index).is(':checked')){
                        $(".checktable").find('input:checkbox').eq(index).prop("checked",false);
                    }else{
                        $(".checktable").find('input:checkbox').eq(index).prop("checked",true);
                    }
                    $("input[name='tablecontent']:checkbox").each(function (i,v) {
                        if ($(".checktable").find('input:checkbox').eq(i).is(":checked")) {
                            sel_table += $(".checktable").find('input:checkbox').eq(i).val() + '|';
                        }
                    });
                }

                 sel_table = sel_table.substring(0,sel_table.length-1);
//                 sel_table = '[' +sel_table +']'

                 $( "#sel_table" ).val(sel_table);

             });

            $(".checkpayment li,input[name='pwcontent']:checkbox").click(function () {
                var sel_pw = '';
		        if(window.event.srcElement.tagName == "INPUT"){
                    $("input[name='pwcontent']:checkbox").each(function () {
                        if ($(this).is(":checked")) {
                            sel_pw += $(this).val() + '|';
                        }
                    });
                }else {
                    var index =$(this).index();
                    if ($(".checkpayment").find('input:checkbox').eq(index).is(':checked')) {
                        $(".checkpayment").find('input:checkbox').eq(index).prop("checked", false);
                    } else {
                        $(".checkpayment").find('input:checkbox').eq(index).prop("checked", true);
                    }


                    $("input[name='pwcontent']:checkbox").each(function (i, v) {
                        if ($(".checkpayment").find('input:checkbox').eq(i).is(":checked")) {
                            sel_pw += $(".checkpayment").find('input:checkbox').eq(i).val() + '|';
                        }
                    });
                }
                 sel_pw = sel_pw.substring(0,sel_pw.length-1);
//                 sel_pw = '[' +sel_pw +']'
                 $( "#sel_pw" ).val(sel_pw);

             });
		});