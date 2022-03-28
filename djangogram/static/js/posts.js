
//A부분 토큰 불러오는 코드를 위해 붙여 넣은 것
function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}


const handleLikeClick = (buttonId) => {
    console.log(buttonId);

    const likeButton = document.getElementById(buttonId);
    const likeIcon = likeButton.querySelector("i");//태그, #아이디, .클래스 다 가능
    
    const csrftoken = getCookie('csrftoken');  // 위의 코드로 토큰을 생성할 수 있음.
    console.log(csrftoken);
    
    //서버로 좋아요 api호출 위해 패치 사용 패치를 사용하고 아래 then(data)에 변경하고 싶은 것을 넣음
    const postId = buttonId.split("-").pop();
    const url = "/post/" + postId + "/post_like";
    fetch(url, {
        method: "POST",
        mode: "same-origin",
        headers: {
            'X-CSRFToken': csrftoken
          },
    })
    .then(response => response.json())
    .then(data => {
        if(data.result === "like"){
            likeIcon.classList.replace("fa-heart-o", "fa-heart");
        } else {
            likeIcon.classList.replace("fa-heart", "fa-heart-o");
        }
    });

  
    //likeIcon.innerText = "good";  //텍스트 넣기
   

}