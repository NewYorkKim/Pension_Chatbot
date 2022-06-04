const main = document.querySelector("#main");
const qna = document.querySelector("#qna");
const result = document.querySelector("#result");

const endPoint = 7;
let totalScore = 0;

function goSurvey() {
    main.style.display = "none";
    qna.style.display = "block";
    let qIdx = 0;
    goNext(qIdx)
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
}