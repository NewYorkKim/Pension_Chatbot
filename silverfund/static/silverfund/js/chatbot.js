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

function endChatbot(){
    bot_output = '함께 이야기할 수 있어서 즐거웠어요. 언제든 또 오세요 :-)';
    bot_text = '<div class="dialogbox bot">' + bot_output + '</div>';
    document.getElementById('botbox').innerHTML += bot_text;

    displayScroll()
    
    setTimeout(function(){
        location.reload();
    }, 1500);
}

function displayScroll(){
  var boxdiv = document.getElementById('botbox');
  boxdiv.scrollTop = document.getElementById('botbox').scrollHeight;
}

function sendQuestion(s){
    userInputTag = document.getElementById('user_query');
    user_input = userInputTag.value;

    user_text = '<div class="dialogbox user">' + user_input + '</div>';
    document.getElementById('botbox').innerHTML += user_text;

    if(user_input == "종료"){
      endChatbot();
    };

    userInputTag.value = "";

    displayScroll()

    if(s=='QA'){
        questionAnswer(user_input);
    }else if(s=='News'){
        newsSearch(user_input);
    };
}

function questionAnswer(user){
    let question = {
        "text": user,
        "user": true,
        "chatbot": false,
    };
    $.ajax({
        url: "qna/",
        type: 'POST',
        data: JSON.stringify(question),
        success: function(data){
          console.log(data);
          sendAnswer(data);},
        error: function(){alert('오류가 발생하였습니다. 새로고침 후 다시 이용해 주세요.');}
    });
}

function sendAnswer(data){
    var qna_output = data.text;

    qna_text = qna_output

    document.getElementById('botbox').innerHTML += '<div class="dialogbox bot">' + qna_text + '</div>';

    var boxdiv = document.getElementById('botbox');
    boxdiv.scrollTop = document.getElementById('botbox').scrollHeight;
  
    displayScroll()
}

function newsSearch(user){
    let question = {
        "text": user,
        "user": true,
        "chatbot": false,
    };
    $.ajax({
        url: "news/",
        type: 'POST',
        data: JSON.stringify(question),
        success: function(data){
          console.log(data);
          loading();
          sendNews(data);
        },
        error: function(){alert('오류가 발생하였습니다. 새로고침 후 다시 이용해 주세요.');}
    });
}

function sendNews(data){
    var news_output = data.text;

    news_text = ''
    for(var idx in news_output){
        news_text +=  news_output[idx] + '<br><br>';
    };

    news_header = '검색 결과입니다: <br><br>';
    document.getElementById('botbox').innerHTML += '<div class="dialogbox bot">' + news_header + news_text + '</div>';

    var boxdiv = document.getElementById('botbox');
    boxdiv.scrollTop = document.getElementById('botbox').scrollHeight;

    defaultbox = document.getElementById('defaultbox');
    document.getElementById('botbox').innerHTML += defaultbox.innerHTML;
    
    displayScroll()

    document.getElementById("submit").setAttribute("onclick", "sendQuestion('QA')");
}

function menu_selection(s){
      user_input = s;
      user_text = '<div class="dialogbox user">' + user_input + '</div>';
      document.getElementById('botbox').innerHTML += user_text;

      if(user_input == '관련 뉴스 검색'){
        bot_output = '검색어를 입력해 주세요.';
        bot_text = '<div class="dialogbox bot">' + bot_output + '</div>';
        document.getElementById('botbox').innerHTML += bot_text;
        document.getElementById("submit").setAttribute("onclick", "sendQuestion('News')");

        displayScroll()
      }else if(user_input == '추가메뉴2'){
        bot_output = '서비스 예정입니다.';
        bot_text = '<div class="dialogbox bot">' + bot_output + '</div>';
        document.getElementById('botbox').innerHTML += bot_text;

        displayScroll()
      }else{
        endChatbot();
      };
    }

function loading(){
      loading_bubble = '<div id="loader">\
        <div class="bubble"></div>\
        <div class="bubble"></div>\
        <div class="bubble"></div>\
      </div></div>';

      document.getElementById('botbox').innerHTML += loading_bubble;
}

