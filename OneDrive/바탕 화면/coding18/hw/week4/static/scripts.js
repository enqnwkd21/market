$(document).ready(function (){
    $(".list-group-item-action").click(function() {
        // list-group-item-action class 속성을 가진 태그를 클릭
        let product_title = $(this).attr('id');
        // 그럴때 id속성값 즉 list에서의 product.title로 되어있는 값을 가져와야함
        // 이때 this는 자기 자신을 의미
        $.get("/detail?title=" + product_title)
        // 그 제목을 가지고 (product.title) ajax를 요청
            .then(function (result){
                //then아래에서 가지고 온 결과로 modal을 만들어내기
                $("#detailModalLabel").text(result.title);
                $("#detailModalContent").text(result.content);
                $('#detailModal').modal('show')
            })
    })
})