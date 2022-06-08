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

const main = document.querySelector("#main");
const qna = document.querySelector("#qna");
const result = document.querySelector("#result");

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
        status.style.width = (100 / endPoint) * (qIdx) + '%';
    
        document.getElementById("label").innerHTML = qIdx + '/' +  endPoint;
    }
}

function addAnswer(answerText, qIdx, idx) {
    var a = document.querySelector('.answerBox');
    var answer = document.createElement('button');
    answer.classList.add('answerList');
    answer.classList.add('btn');
    answer.classList.add('btn-light');
    answer.classList.add('btn-block');
    // answer.classList.add('mx-auto');
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

    setResult();
}

function setResult() {
    if(totalScore <= 20){
        level = levelList[0].name;
        desc = levelList[0].desc;
        file1 = levelList[0].file[0];
        file2 = levelList[0].file[1];
    }else if(totalScore <= 40){
        level = levelList[1].name;
        desc = levelList[1].desc;
        file1 = levelList[1].file[0];
        file2 = levelList[1].file[1];
    }else if(totalScore <= 60){
        level = levelList[2].name;
        desc = levelList[2].desc;
        file1 = levelList[2].file[0];
        file2 = levelList[2].file[1];
    }else if(totalScore <= 80){
        level = levelList[3].name;
        desc = levelList[3].desc;
        file1 = levelList[3].file[0];
        file2 = levelList[3].file[1];
    }else{
        level = levelList[4].name;
        desc = levelList[4].desc;
        file1 = levelList[4].file[0];
        file2 = levelList[4].file[1];
    };
    let survey_data = {
        "score": totalScore,
        "result1": file1,
        "result2": file2
    };
    $.ajax({
        url: "ranks/",
        type: "POST",
        data: JSON.stringify(survey_data),
        success: function(data){
            console.log(data);
        },
        error: function(){alert('오류가 발생하였습니다. 새로고침 후 다시 이용해 주세요.');}
    });

    document.getElementById("desc").innerHTML += '<div class="intro">당신의 투자 성향은 ' +  level + '입니다.</div><br>'
                                                  + desc + '<br>추천 포트폴리오는 아래와 같습니다.';                  
    
    result.innerHTML += "<input type=button id='result1-btn' class='btn btn-secondary' value='퇴직연금' onclick='showResult1()'><br><br>";
    result.innerHTML += "<input type=button id='result2-btn' class='btn btn-secondary' value='연금저축' onclick='showResult2()'>";

    // const result1 = data.result1;
    // const result2 = data.result2;

    // r1 = document.getElementById("result1");
    // r2 = document.getElementById("result2");

    // r1.innerHTML += result1;
    // r2.innerHTML += result2;
}

function showResult1() {
    window.open("result1/", "퇴직연금", "width=400, height=300, left=100, top=50");
}

function showResult2() {
    window.open("result2/", "연금저축", "width=400, height=300, left=100, top=50");
}