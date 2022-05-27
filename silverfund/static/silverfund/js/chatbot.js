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

function appendChat(user, bot){
    console.log('Trying to append')
    console.log(user, bot)
    $('#botbox')(`<div class="dialogbox user">${user}</div>
                         <div class="dialogbox bot">${bot}</div>`);

    const $element = document.getElementById('botbox');
    $element.scrollTop = $element.scrollHeight;
}

document.getElementById('chatForm').addEventListener('submit', function(e){
        e.preventDefault();
        userInputTag = document.getElementById('user_query');
        user_input = userInputTag.value;
        if(user_input == '안녕'){
          bot_output = '만나서 반가워요.'
        }else if(user_input == '잘가'){
          bot_output = '함께 이야기할 수 있어서 즐거웠어요. 언제든 또 오세요 :-)'
        }else{
          bot_output = '죄송합니다. 잘 모르겠어요 :('
        }

        fetch('{% url "silverfund:chatbot" %}', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({name: user_input}),
        }).then(response => response.json()).then(some => appendChat(user_input, some))
        userInputTag.value = "";
    });

function menu_selection(s){
      user_input = s;
      if(user_input == '관련 뉴스 검색'){
        bot_output = '검색어를 입력해 주세요.'
      }else if(user_input == '추가메뉴2'){
        bot_output = '서비스 예정입니다.'
      }else{
        bot_output = '함께 이야기할 수 있어서 즐거웠어요. 언제든 또 오세요 :-)'
      }
      appendChat(user_input, bot_output)
    }
