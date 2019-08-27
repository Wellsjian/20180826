//获取元素
function fun1(tag,index){
    var elements = document.getElementsByTagName(tag)
    if(index){
        index = index
        }else{
        index = 0
        }
    return elements[0]
    }