from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
fund_rank = '''
<table class="table table-hover">
  <thead>
    <tr>
      <th scope="col">#</th>
      <th scope="col">상품명</th>
      <th scope="col">수익률</th>
      <th scope="col">운영규모 (설정일)</th>
      <th scope="col">위험도</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th scope="row">1</th>
      <td><a href="http://www.samsungfund.com/retFundView.action?fundCd=KR5105924314">삼성WTI원유특별자산1(WTI원유-파생형)_A</a></td>
      <td>-</td>
      <td>899억 (2009.02.20)<td>
      <td>1 매우높은위험</td>
    </tr>
    <tr>
      <th scope="row">2</th>
      <td>미래에셋로저스Commodity인덱스특별자산자(파생)A</td>
      <td>-</td>
      <td>285억 (2006.08.16)<td>
      <td>2 높은위험</td>
    </tr>
    <tr>
      <th scope="row">3</th>
      <td>KB북미생산유전고배당특별자산(인프라-재간접형)_Ce</td>
      <td>-</td>
      <td>47억 (2015.04.20)<td>
      <td>1 매우높은위험</td>
    </tr>
  </tbody>
</table>
'''

irp_rank = '''
<table class="table table-hover">
  <thead>
    <tr>
      <th scope="col">#</th>
      <th scope="col">증권사</th>
      <th scope="col">수익률 (단위: %)</th>
      <th scope="col">적립금 (단위: 억원)</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th scope="row">1</th>
      <td><a href="https://www.kbsec.com/go.able?linkcd=m01010029">KB증권</a></td>
      <td>-0.57</td>
      <td>2,650<td>
    </tr>
    <tr>
      <th scope="row">2</th>
      <td>NH투자증권</td>
      <td>0.90</td>
      <td>4,548<td>
    </tr>
    <tr>
      <th scope="row">3</th>
      <td>대신증권</td>
      <td>0.48</td>
      <td>1,109<td>
    </tr>
  </tbody>
</table>
'''
tabs = [
    {'id': 'mypage', 'title': '마이페이지', 'body': '사용자 정보'},
    {'id': 'saving', 'title': '연금저축펀드', 'body': fund_rank},
    {'id': 'irp', 'title': '개인형 IRP', 'body': irp_rank} 
]

def index(articleTag):
    global tabs
    ul = ''
    for tab in tabs:
        ul += f'<li><a href="/{tab["id"]}">{tab["title"]}</a></li>'
    return f'''
    <html>
    <head>
        <meta charset="utf-8">
        <meta name="viewport" content="width=device-width, initial-scale=1">
        <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-1BmE4kWBq78iYhFldvKuhfTAU6auU8tT94WrHftjDbrCEXSU1oBoqyl2QvZ6jIW3" crossorigin="anonymous">
        <title>Silver Fund</title>
    </head>
    <body class="container">
        <br><br>
        <h1><a href="/">실버펀드</a></h1>
        <div class="row">
            <ul class="col-sm-3">
                {ul}
                <br>
            </ul>
            <article class="col-sm-9">
                {articleTag}
            </article>
        </div>
        <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/js/bootstrap.bundle.min.js" integrity="sha384-ka7Sk0Gln4gmtz2MlQnikT1wXgYsOg+OMhuP+IlRH9sENBO0LRn5q+8nbTov4+1p" crossorigin="anonymous"></script>
    </body>
    </html>
    '''

def home(request):
    article = '''
    <ul class="nav nav-tabs" id="myTab" role="tablist">
        <li class="nav-item" role="presentation">
            <button class="nav-link active" id="home-tab" data-bs-toggle="tab" data-bs-target="#intro" type="button" role="tab" aria-controls="intro" aria-selected="true">개인연금</button>
        </li>
        <li class="nav-item" role="presentation">
            <button class="nav-link" id="profile-tab" data-bs-toggle="tab" data-bs-target="#saving" type="button" role="tab" aria-controls="saving" aria-selected="false">연금저축</button>
        </li>
        <li class="nav-item" role="presentation">
            <button class="nav-link" id="contact-tab" data-bs-toggle="tab" data-bs-target="#irp" type="button" role="tab" aria-controls="irp" aria-selected="false">개인형 IRP</button>
        </li>
        <li class="nav-item" role="presentation">
            <button class="nav-link" id="contact-tab" data-bs-toggle="tab" data-bs-target="#comparison" type="button" role="tab" aria-controls="comparison" aria-selected="false">비교</button>
        </li>
    </ul>
    <div class="tab-content" id="myTabContent">
        <div class="tab-pane fade show active" id="intro" role="tabpanel" aria-labelledby="home-tab">
            <br><br>
            <p>국민연금 2057년 고갈?</p>
        </div>
        <div class="tab-pane fade" id="saving" role="tabpanel" aria-labelledby="profile-tab">
            <br><br>
            <p>연금저축이란...</p>
        </div>
        <div class="tab-pane fade" id="irp" role="tabpanel" aria-labelledby="contact-tab">
            <br><br>
            <p>개인형 IRP란...</p>
        </div>
        <div class="tab-pane fade" id="comparison" role="tabpanel" aria-labelledby="contact-tab">
            <br><br>
            <p>연금저축 vs. 개인형 IRP 비교</p>
        </div>
    </div>
    '''
    return HttpResponse(index(article))

def pages(request, id):
    global tabs
    article = ''
    for tab in tabs:
        if tab['id'] == id:
            article = f'<h2>{tab["title"]}</h2>{tab["body"]}'
    return HttpResponse(index(article))
