function mode(s){
    if(s=='Night'){
      document.querySelector('body').style.backgroundColor='#323232';
      document.querySelector('body').style.color='white';
      document.querySelector('nav ul').style.borderTopColor='white';
      document.querySelector('nav ul').style.borderBottomColor='white';
      var alist = document.querySelectorAll('a');
      var i = 0;
      while(i < alist.length){
        alist[i].style.color = 'white';
        i++;
      }
    }else if(s=='Day'){
      document.querySelector('body').style.backgroundColor='white';
      document.querySelector('body').style.color='black';
      document.querySelector('nav ul').style.borderTopColor='black';
      document.querySelector('nav ul').style.borderBottomColor='black';
      var alist = document.querySelectorAll('a');
      var i = 0;
      while(i < alist.length){
        alist[i].style.color = 'black';
        i++;
      }
    }
}

function getCookie(name) {
  let cookieValue = null;
  if (document.cookie && document.cookie !== '') {
      const cookies = document.cookie.split(';');
      for (let i = 0; i < cookies.length; i++) {
          const cookie = cookies[i].trim();
          if (cookie.substring(0, name.length + 1) === (name + '=')) {
              cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
              break;
          }
      }
  }
  return cookieValue;
}
const csrftoken = getCookie('csrftoken');

function csrfSafeMethod(method) {
  // these HTTP methods do not require CSRF protection
  return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
}
$.ajaxSetup({
  beforeSend: function(xhr, settings) {
      if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
          xhr.setRequestHeader("X-CSRFToken", csrftoken);
      }
  }
});

function sendQuestion(){
    userInputTag = document.getElementById('user_query');
    user_input = userInputTag.value;

    // if(user_input == "종료"){
    //     location.reload();
    // };

    user_text = '<div class="dialogbox user">' + user_input + '</div>';
    document.getElementById('botbox').innerHTML += user_text;
    
    let question = {
        "text": user_input,
        "user": true,
        "chatbot": false,
    };

    data = JSON.stringify(question);
    sendAnswer(data);

    $.ajax({
        url: "send/",
        type: 'POST',
        data: JSON.stringify(question),
        dataType: "json",
        success: function(data){sendAnswer(data);},
        error: function(){alert('오류가 발생하였습니다. 새로고침 후 다시 이용해 주세요.');}
    });

    userInputTag.value = "";

    var boxdiv = document.getElementById('botbox');
    boxdiv.scrollTop = document.getElementById('botbox').scrollHeight;
}

function sendAnswer(data){
    $.ajax({
      url: "back/",
      type: 'GET',
      data: data,
      dataType: "json",
      success: function(data){
        console.log(data['text']);
      },
      error: function(){alert('오류가 발생하였습니다. 새로고침 후 다시 이용해 주세요.')}
    });

    var boxdiv = document.getElementById('botbox');
    boxdiv.scrollTop = document.getElementById('botbox').scrollHeight;
}

function menu_selection(s){
      user_input = s;
      if(user_input == '관련 뉴스 검색'){
        bot_output = '검색어를 입력해 주세요.';
      }else if(user_input == '추가메뉴2'){
        bot_output = '서비스 예정입니다.';
      }else{
        bot_output = '함께 이야기할 수 있어서 즐거웠어요. 언제든 또 오세요 :-)';
      };
      // appendChat(user_input, bot_output);
    }

