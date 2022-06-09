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

let main = document.querySelector("#main");
let qna = document.querySelector("#qna");
let result = document.querySelector("#result");

const endPoint = 7;
let totalScore = 0;

function goSurvey() {
    main.style.display = "none";
    qna.style.display = "block";
    let qIdx = 0;
    goNext(qIdx);
}

function goNext(qIdx) {
    if(qIdx==endPoint){
        goResult();
    }else{
        var q = document.querySelector('.questionBox');
        q.innerHTML = qnaList[qIdx].q;
        for (let i in qnaList[qIdx].a){
            addAnswer(qnaList[qIdx].a[i].answer, qIdx, i);
        }
        var status = document.querySelector('.statusBar');
        status.style.width = (100 / endPoint) * (qIdx+1) + '%';
    
        document.getElementById("label").innerHTML = (qIdx+1) + '/' +  endPoint;
    };
}

function addAnswer(answerText, qIdx, idx) {
    var a = document.querySelector('.answerBox');
    var answer = document.createElement('button');
    answer.classList.add('answerList');
    answer.classList.add('btn');
    answer.classList.add('btn-light');
    answer.classList.add('btn-block');
    answer.setAttribute('value', qnaList[qIdx].a[idx].score);

    a.appendChild(answer)
    answer.innerHTML = answerText;

    answer.addEventListener("click", function(){
        var children = document.querySelectorAll('.answerList');

        var score = parseFloat(answer.value);
        totalScore += score;

        for(let i = 0; i < children.length; i++){
            children[i].style.display = 'none';
        }
        goNext(++qIdx);
    });
}

function goResult() {
    qna.style.display = 'none';
    result.style.display = 'block';

    let survey_data = {
        "score": totalScore,
        "result1": "",
        "result2": ""
    };
    $.ajax({
        url: "ranks/",
        type: "POST",
        data: JSON.stringify(survey_data),
        success: function(data){
            console.log(data);
            setResult(data);
        },
        error: function(){alert('오류가 발생하였습니다. 새로고침 후 다시 이용해 주세요.');}
    });
}

function setResult(data) {
    if(totalScore <= 20){
        level = levelList[0].name;
        desc = levelList[0].desc;
    }else if(totalScore <= 40){
        level = levelList[1].name;
        desc = levelList[1].desc;
    }else if(totalScore <= 60){
        level = levelList[2].name;
        desc = levelList[2].desc;
    }else if(totalScore <= 80){
        level = levelList[3].name;
        desc = levelList[3].desc;
    }else{
        level = levelList[4].name;
        desc = levelList[4].desc;
    };

    document.getElementById("desc").innerHTML += '<div class="intro">' +  level + '</div><br>'
                                                  + desc + '<br>추천 포트폴리오를 확인해 보세요.';                  

    result.innerHTML += '<div id="selection" class="row"><div class="col-sm-6"><div class="card"><div class="card-body"><h5 class="card-title">퇴직연금</h5>\
        <p class="card-text">세액공제 한도: 연 400만 원</p>\
        <input type=button id="result2-btn" class="btn btn-secondary btn-lg" value="확인" onclick=showResult2()></a></div></div></div>\
        <div class="col-sm-6"><div class="card"><div class="card-body"><h5 class="card-title">연금저축</h5>\
        <p class="card-text">세액공제 한도: 연 700만 원</p>\
        <input type=button id="result2-btn" class="btn btn-secondary btn-lg" value="확인" onclick=showResult2()></a></div></div></div></div>';

    result1 = data.result1;
    result2 = data.result2;

    r1 = document.getElementById("result1_body");
    r2 = document.getElementById("result2_body");

    r1.innerHTML += result1;
    r2.innerHTML += result2;

    r1.innerHTML += '<br><button type="button" class="btn btn-secondary" value="닫기" onclick="shutDown1()">닫기</button>';
    r2.innerHTML += '<br><button type="button" class="btn btn-secondary" value="닫기" onclick="shutDown2()">닫기</button>';
}

function showResult1() {
    document.getElementById("result1").style.display = 'block';
}

function showResult2() {
    document.getElementById("result2").style.display = 'block';

}

function shutDown1() {
    document.getElementById("result1").style.display = 'none';
}

function shutDown2() {
    document.getElementById("result2").style.display = 'none';
}