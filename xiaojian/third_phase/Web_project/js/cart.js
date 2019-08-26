$(function (){
    //1.全选和取消全选
    var isCheck = false//全选元素的状态
    $(".checkAll").click(function (){
        isCheck = !isCheck;
        if(isCheck){
            $(".checkAll").attr("src","../images/cart/product_true.png")
            $(".checkItem").attr("src","../images/cart/product_true.png")
            .attr("checked",true)
            }else{
                $(".checkAll").attr("src","../images/cart/product_normal.png")
                $(".checkItem").attr("src","../images/cart/product_normal.png")
                .attr("checked",false)
            }
        //console.log($(this).prop("checked"))
        /*
        //自定义标签属性或属性值
        $(this).prop("a","b").attr("aa","bb")8i=ii
        console.log($(this).prop("a")
        */
        sum()
    })
    //2.反选
    $(".checkItem").click(function (){
        if($(this).attr("checked")){
            //移除标记
            $(this).attr("checked",false).attr("src","../images/cart/product_normal.png")

            //$(".checkAll").attr("src","../images/cart/product_normal.png")
            }else{
                $(this).attr("checked",true).attr("src","../images/cart/product_true.png")
                //$(".checkAll").attr("src","../images/cart/product_true.png")
                }
        //反选
        //console.log($(".checkItem[checked=checked]").length)
        //获取被选中的商品数量
        if($(".checkItem[checked=checked]").length==$(".checkItem").length){
            $(".checkAll").attr("src","../images/cart/product_true.png");
            isCheck = true;
            }else{
                $(".checkAll").attr("src","../images/cart/product_normal.png")
                isCheck = false;
                }
        sum()
        })
    //3数量增加
    $(".add").click(function (){
        var value = $(this).prev().val();
        value ++;
        $(this).prev().val(value);
        //价格联动
        //获取单价

        changeSum(this,value)
        sum()
        })
    $(".minus").click(function (){
        var value = $(this).next().val();
        if(value > 1){
            value --;
            }
        $(this).next().val(value);
        //价格联动
        //获取单价
        changeSum($(this),value)
        sum()
        })
    //4.价格联动
    function changeSum(that,number){
        //获取单价
//        var s1 = $(that).parent().prev().find("p").html();
        var price =$(that).parents(".item").find(".price p").html()
        //去掉符号
        var each_price = price.substring(1)
        //获取总额
        var total_price = (each_price * number).toFixed(2)
        //显示界面
        $(that).parents(".item").find(".sum").html("¥"+total_price)

        }


    //5.移除商品
    $(".item .action ").click(function(){
        $(this).parent().remove()
        sum()
        })

    //6获取被选中商品的数量和总价
    function sum(){
        var num = 0
        var price = 0
        $(".checkItem[checked=checked]").each(function (){
            num += Number($(this).parents(".item").find(".count input").val())
            var str = $(this).parents(".item").find(".sum p").html()
            var s = Number(str.substring(1))
            price += s

            })
        //显示在界面
        $(".total_count").html(num)
        price = price.toFixed(2)
        $(".total_price").html(price+"元")

        }








})