const qnaList =[
    {
        q: '당신의 연령대는 어떻게 됩니까?',
        a: [
            { answer: '19세 이하', score: 12.5},
            { answer: '20세 ~ 40세', score: 12.5},
            { answer: '41세 ~ 50세', score: 9.3},
            { answer: '51세 ~ 60세', score: 6.2},
            { answer: '61세 이상', score: 3.1}
        ]
    },
    {
        q: '투자하고자 하는 자금의 투자 가능 기간은 얼마나 됩니까?',
        a: [
            { answer: '6개월 이내', score: 3.1},
            { answer: '6개월 이상 ~ 1년 이내', score: 6.2},
            { answer: '1년 이상 ~ 2년 이내', score: 9.3},
            { answer: '2년 이상 ~ 3년 이내', score: 12.5},
            { answer: '3년 이상', score: 15.6}
        ]
    },
    {
        q: '다음 중 투자경험과 가장 가까운 것은 어느 것입니까?',
        a: [
            { answer: '은행의 예·적금, 국채, 지방채, 보증채, MMF, CMA 등', score: 3.1},
            { answer: '금융채, 신용도가 높은 회사채, 채권형펀드, 원금보존추구형ELS 등', score: 6.2},
            { answer: '신용도 중간 등급의 회사채, 원금의 일부만 보장되는 ELS, 혼합형펀드 등', score: 9.3},
            { answer: '신용도가 낮은 회사채, 주식, 원금이 보장되지 않는 ELS, 시장수익률 수준의 수익을 추구하는 주식형펀드 등', score: 12.5},
            { answer: 'ELW, 선물옵션, 시장수익률 이상의 수익을 추구하는 주식형펀드, 파생상품에 투자하는 펀드, 주식 신용거래 등', score: 15.6}
        ]
    },
    {
        q: '금융상품 투자에 대한 본인의 지식수준은 어느 정도라고 생각하십니까?',
        a: [
            { answer: '［매우 낮은 수준］투자의사 결정을 스스로 내려본 경험이 없는 정도', score: 3.1},
            { answer: '［낮은 수준］주식과 채권의 차이를 구별할 수 있는 정도', score: 6.2},
            { answer: '［높은 수준］투자할 수 있는 대부분의 금융상품의 차이를 구별할수 있는 정도', score: 9.3},
            { answer: '［매우 높은 수준］금융상품을 비롯하여 모든 투자대상 상품의 차이를 이해할 수 있는 정도', score: 12.5}
        ]
    },
    {
        q: '현재 투자하고자 하는 자금은 전체 금융자산(부동산 등을 제외) 중 어느 정도의 비중을 차지합니까?',
        a: [
            { answer: '10% 이내', score: 15.6},
            { answer: '10% 이상 ~ 20% 이내', score: 12.5},
            { answer: '20% 이상 ~ 30% 이내', score: 9.3},
            { answer: '30% 이상 ~ 40% 이내', score: 6.2},
            { answer: '40%이상', score: 3.1}
        ]
    },
    {
        q: '다음 중 당신의 수입원을 가장 잘 나타내고 있는 것은 어느 것입니까?',
        a: [
            { answer: '현재 일정한 수입이 발생하고 있으며, 향후 현재 수준을 유지하거나 증가할 것으로 예상된다.', score: 9.3},
            { answer: '현재 일정한 수입이 발생하고 있으나, 향후 감소하거나 불안정할 것으로 예상된다.', score: 6.2},
            { answer: '현재 일정한 수입이 없으며, 연금이 주수입원이다.', score: 3.1}
        ]
    },
    {
        q: '만약 투자원금에 손실이 발생할 경우 다음 중 감수할 수 있는 손실 수준은 어느 것입니까?',
        a: [
            { answer: '무슨 일이 있어도 투자원금은 보전되어야 한다.', score: 6.2},
            { answer: '10% 미만까지는 손실을 감수할 수 있을 것 같다.', score: 6.2},
            { answer: '20% 미만까지는 손실을 감수할 수 있을 것 같다.', score: 12.5},
            { answer: '기대수익이 높다면 위험이 높아도 상관하지 않겠다.', score: 18.7},
        ]
    }
]