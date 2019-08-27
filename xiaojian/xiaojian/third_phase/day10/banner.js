$(function (){
    //1.定义图片数组,保存路径
    var array1 = ["index_banner1.jpg",
                  "index_banner2.jpg",
                  "index_banner3.jpg",
                  "index_banner4.jpg",
                  "index_banner5.jpg"]

    //.定义索引
    var index = 0;
    //开启定时器
    var timer = setInterval(autoPlay,1500)
    function autoPlay(){
         $("#banner li").eq(index).css("background","gray");
        //更新索引
        index = ++index == array1.length ? 0 : index;
        //根据索引下标取元素
        $("#banner img").attr("src",array1[index]);
        //切换图片的索引样式
        $("#banner li").eq(index).css("background","red")


        }
    //鼠标的移入移出
    $("#banner").mouseover(function (){
        clearInterval(timer);
        }).mouseout(function (){
            timer = setInterval(autoPlay,1500);
            })

    //点击切图
    //上一张
    $(".prev").click(function (){
        $("#banner li").eq(index).css("background","gray");
        index = --index<0?array1.length-1:index;
        //根据索引下标取元素
        $("#banner img").attr("src",array1[index]);
        //切换图片的索引样式
        $("#banner li").eq(index).css("background","red");
        })
    //下一张
    $(".next").click(function (){
        autoPlay()
        })


})