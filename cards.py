card_name = { 1: "The Easy 카드", 2: "다담 카드", 3: "골든 라이프 올림카드", 4: "골든 라이프 티타늄 카드", 5:"Easy Pick 카드" , 6:"나라사랑 체크카드" , 7: "청춘대로 싱글 레터링 체크카드 (긁으면)", 8: "펭수 노리 체크카드" , 9:"첵첵 체크카드",10:"골든대로 체크카드" }
adv = {
    1 : ['롯데슈퍼','이마트','홈플러스','GS25','CU','이마트24','세븐일레븐','미니스톱',
    '스타벅스','커피빈','이디야','파스쿠찌','할리스','탐앤탐스','엔제리너스','카페베네',
    '투썸','요거프레소','SK 주유소','GS 칼텍스','S-OIL','현대오일뱅크'],
    2: ['SK 주유소','롯데월드','에버랜드','캐리비안베이','백화점','스타벅스',
    '커피빈', '이디야커피', '파스쿠찌', '탐앤탐스', '할리스', '카페베네',
    '엔제리너스', '투썸','빽다방','아울렛','교보문고','알라딘','영풍문고','인터파크'],
    3 : ['병원','SK 주유소','GS 칼텍스','S-OIL','현대오일뱅크','이마트','홈플러스','롯데마트'],
    4 : ['이마트','홈플러스','롯데마트','SK 주유소','GS 칼텍스','교보문고','롯데 백화점','현대 백화점',
    '신세계 백화점','GS25','CU','스타벅스','커피빈'],
    5 : ['이마트','롯데마트','홈플러스','하나로마트','SK 주유소','GS 칼텍스','CU','GS25','스타벅스',
    '커피빈', '이디야커피', '파스쿠찌', '탐앤탐스', '할리스', '카페베네', '엔제리너스', '투썸','빽다방',
    '파리바게뜨','뚜레쥬르','던킨','설빙','베스킨','버거킹','맥도날드','롯데리아','도미노','서브웨이',
    '파파존스','피자헛','CGV','롯데 시네마','메가박스'],
    6 : ['GS25','CGV','스타벅스','아웃백','빕스','에버랜드','롯데월드','교보문고'],
    7 : ['GS25','세븐일레븐','다이소','올리브영','박승철','동물병원'],
    8 : ['CGV','아웃백','빕스','스타벅스','에버랜드','롯데월드','GS25','교보문고'],
    9 : ['CU','스타벅스','CGV','텐바이텐','올리브영'],
    10 : ['병원','약국','이마트','롯데마트','홈플러스','SK 주유소']
    }

recommend_credit = {
    "탄탄대로 Miz&Mr 티타늄카드" : ["2","n","y","n","n","n","y","n","n","n"],
    "탄탄대로 올쇼핑 티타늄카드" : ["2","n","y","n","y","n","n","n","n","n"],
    "청춘대로 톡톡카드" : ["1","n","y","n","n","n","n","y","n","n"],
    "탄탄대로 올쇼핑카드" : ["2","n","n","n","y","n","n","n","n","y"],
    "Easy all 티타늄카드" : ["3","n","n","n","n","n","n","n","n","n"],
    "The Easy카드" : ["1","n","n","n","n","n","n","n","n","n"],
    "굿데이 올림카드" : ["2","n","n","n","y","n","y","n","n","y"],
    "톡톡 Pay카드" : ["2","y","n","n","n","y","n","n","n","n"],
    "Easy on 카드" : ["3","n","y","n","n","n","n","y","y","n"],
    "청춘대로 1코노미 카드" : ["2","n","n","n","n","y","n","y","n","y"],
    "Easy ring 티타늄카드" : ["3","n","n","n","n","n","n","y","n","y"],
    "청춘대로 티타늄 카드" : ["2","n","y","n","n","n","n","n","n","n"],
    "Easy pick카드" : ["3","y","n","n","n","n","n","n","n","y"]
}

recommend_check = {
    "노리체크카드" : ["1","y","n","y","n","n","n","n","n","y"],
    "위글위글 첵첵 체크카드" : ["2","n","y","n","n","n","n","n","n","n"],
    "펭수 노리 체크카드(펭카)" : ["1","y","n","y","n","n","n","n","n","y"],
    "해피노리체크카드" : ["1","y","y","y","n","n","n","n","n","n"],
    "스타체크카드" : ["2","n","n","y","n","n","y","n","n","y"],
    "해피CU포인트 체크카드" : ["2","y","n","n","n","y","n","y","y","n"]
}

cards_url_priv = {
    "탄탄대로 Miz&Mr 티타늄카드" : [
        f"http://api6.card-gorilla.com:8080/storage/card/150/card_img/405/kb_tantan_miz%26mr_titanium_card.png",
        ["Trendy 서비스 : 미용/화장품, 스포츠/골프 결혼/가전업종 20% 할인","Trendy 서비스 : SPA 패션, 식품배송, 인테리어 20% 할인","Daily 서비스 : 커피/베이커리/아이스크림, 백화점/편의점 10% 할인","Daily 서비스 : 대중교통 10% 할인, 주유 100원/L 할인","티타늄 서비스 : 공항 라운지, 공항/호텔 발레파킹"],
        f"https://img2.kbcard.com/obj/card/download/09230__prdctOpmn_20200305.pdf"
    ],
    "탄탄대로 올쇼핑 티타늄카드" : [
        f"http://api6.card-gorilla.com:8080/storage/card/485/card_img/3814/KB%EA%B5%AD%EB%AF%BC_%ED%83%84%ED%83%84%EB%8C%80%EB%A1%9C_%EC%98%AC%EC%87%BC%ED%95%91_%ED%8B%B0%ED%83%80%EB%8A%84.png",
        ["쇼핑 영역 서비스 : 대형마트,홈쇼핑,온라인 쇼핑몰,면세점, 가전제품 10% 할인","자동납부 영역 서비스 : 통신요금, 아파트 관리비, 도시가스 10% 할인","생활영역 서비스 : 편의점, 커피 5% 할인, 주유 100원/L 할인","티타늄 서비스 : 공항 라운지, 공항/호텔 발레파킹"],
        f"https://img2.kbcard.com/obj/card/download/09233__prdctOpmn_20181004.pdf"
    ],
    "청춘대로 톡톡카드" : [
        f"http://api6.card-gorilla.com:8080/storage/card/129/card_img/281/km_cheongchuntocktock_card.png",
        ["Great 서비스 : 스타벅스 50% 청구할인","Enjoy 서비스 : 버거/패스트푸드 업종 20% 청구할인","Check 서비스 : 간편결제 10% 청구할인","Basic 서비스 : 대중교통/택시/이동통신 10% 청구할인"],
        f"https://img2.kbcard.com/obj/card/download/09174__prdctOpmn_20200213.pdf"
    ],
    "탄탄대로 올쇼핑카드" : [
        f"http://api6.card-gorilla.com:8080/storage/card/149/card_img/409/kb_tantan_allshopping_card.png",
        ["쇼핑 영역 서비스 : 대형마트,홈쇼핑,온라인 쇼핑몰,면세점 10% 할인","자동납부 영역 서비스 : 통신요금, 아파트 관리비 10% 할인","생활영역 서비스 : 편의점, 커피 5% 할인, 주유 80원/L 할인"],
        f"https://img2.kbcard.com/obj/card/download/09232__prdctOpmn_20181004.pdf"
    ],
    "Easy all 티타늄카드" : [
        f"http://api6.card-gorilla.com:8080/storage/card/634/card_img/8512/kb_Easy_all_Titanium.png",
        ["A 그룹 : 음식,교육,병원/약국,관리비/공과금 3% 할인","B 그룹 : 마트, 주유,이동통신, 온라인 쇼핑 5% 할인","C 그룹 : 스포츠, 대중교통, 패션, 뷰티, 편의점 7% 할인","D 그룹 : 택시, 커피, 제과/패스트푸드, 배달앱 10% 할인"],
        f"https://img2.kbcard.com/obj/card/download/09256__prdctOpmn_20200618.pdf"
    ],
    "The Easy카드" : [
        f"http://api6.card-gorilla.com:8080/storage/card/146/card_img/433/kb_theeasy_card.png",
        ["기본 적립/할인 : 전 가맹점 0.7% 적립/할인","추가 적립 : 자주 가는 곳 3% 추가 적립","추가 할인 : 많이 쓰는 곳 5% 추가 할인"],
        f"https://img2.kbcard.com/obj/card/download/09250__prdctOpmn_20181001.pdf?_ga=2.266869451.451842090.1599544774-1779415638.1598350109&_gac=1.257057657.1599546064.CjwKCAjwtNf6BRAwEiwAkt6UQlA4geml1MsNRRxR1d6l-acQwKnXP2F1kLY99-zbPhKBGq5PlA8thhoCeegQAvD_BwE"
    ],
    "굿데이 올림카드" : [
        f"http://api6.card-gorilla.com:8080/storage/card/115/card_img/354/KB_gooddayup_CARD.png",
        ["기본 할인 : 주유소, 충전소 업종 리터당 60원 청구할인","기본 할인 : 통신, 대중교통 업종 10% 청구할인","기본 할인 : 이마트,홈플러스,롯데마트 10% 청구할인","추가 할인 : 음식점, 커피 전문점, 편의점, 약국 업종 10% 추가 청구할인","추가 할인 : 학원, 휘트니스센터 업종 10% 추가 청구할인"],
        f"https://img2.kbcard.com/obj/card/download/09063__prdctOpmn_20200213.pdf?_ga=2.190699118.451842090.1599544774-1779415638.1598350109&_gac=1.247752181.1599546408.CjwKCAjwtNf6BRAwEiwAkt6UQlpsxJErcsfQk4isc_5vsyCPNN78rMKUh-R_p_7ZId5BlWJcqRl-GxoC5bYQAvD_BwE"
    ],
    "톡톡 Pay카드" : [
        f"http://api6.card-gorilla.com:8080/storage/card/142/card_img/365/kb_toktokpay_card.png",
        ["간편결제 : 간편결제 20/40% 청구할인","대중교통 : 버스/지하철 10% 청구할인","편의점 : GS25, CU 10% 청구할인"],
        f"https://img2.kbcard.com/obj/card/download/09231__prdctOpmn_20200213.pdf"
    ],
    "Easy on 카드" : [
        f"http://api6.card-gorilla.com:8080/storage/card/470/card_img/2905/KB_EasyOn.PNG",
        ["Easy on 특화서비스 : 푸드, 인터넷 쇼핑몰/소셜커머스/배달앱/백화점, 커피/편의점/제과 5% 할인","Easy on Plus 서비스 : 대중교통/이동통신, 온라인 음원/숙박앱 5% 할인"],
        f"https://img2.kbcard.com/obj/card/download/09244__prdctOpmn_20200221.pdf?_ga=2.93838296.451842090.1599544774-1779415638.1598350109&_gac=1.186712922.1599546535.CjwKCAjwtNf6BRAwEiwAkt6UQoGhIMwJ_OKUCuP9tj13forfjMHe0urcgMAFMEKMS95cUMdFZedxhRoCQb8QAvD_BwE"
    ],
    "청춘대로 1코노미 카드" : [
        f"http://api6.card-gorilla.com:8080/storage/card/132/card_img/337/kb_1conomy_card.png",
        ["Daily 서비스 : 편의점/음식점/택시 5~20% 적립","Monthly 서비스 : 이동통신/인터넷 쇼핑몰 등 5% 적립","Someday 서비스 : 캐릭터샵/배달앱 등 5% 적립"],
        f"https://img2.kbcard.com/obj/card/download/09175__prdctOpmn_20200904.pdf"
    ],
    "Easy ring 티타늄카드" : [
        f"http://api6.card-gorilla.com:8080/storage/card/615/card_img/8082/%EC%9D%B4%EC%A7%80%EB%A7%81%ED%8B%B0%ED%83%80%EB%8A%84.png",
        ["Easy ring 통신 할인 : 1만원 당 1,500원 청구 할인","Easy ring 플러스 : 영화, 음원/영상, 배달앱 등 1~4천원 청구할인","Easy ring 리워드 : 전월 이용실적 150만원초과 이용금액의 0.3% 포인트리 적립"],
        f"https://img2.kbcard.com/obj/card/download/09253__prdctOpmn_20200421.pdf?_ga=2.31349114.451842090.1599544774-1779415638.1598350109&_gac=1.20074058.1599546535.CjwKCAjwtNf6BRAwEiwAkt6UQoGhIMwJ_OKUCuP9tj13forfjMHe0urcgMAFMEKMS95cUMdFZedxhRoCQb8QAvD_BwE"
    ],
    "청춘대로 티타늄 카드" : [
        f"http://api6.card-gorilla.com:8080/storage/card/117/card_img/291/km_cheongchuntitanum_card.png",
        ["쇼핑 홀릭 : 인터넷 쇼핑, 소셜 커머스 10% 청구할인","푸드 홀릭 : 음식업종 5% 청구할인","커피 홀릭 : 커피, 제과 5~10% 청구할인","데이 홀릭 : 버스/지하철, 택시 10% 청구할인"],
        f"https://img2.kbcard.com/obj/card/download/09171__prdctOpmn_20200421.pdf?_ga=2.4585846.451842090.1599544774-1779415638.1598350109&_gac=1.222047722.1599546535.CjwKCAjwtNf6BRAwEiwAkt6UQoGhIMwJ_OKUCuP9tj13forfjMHe0urcgMAFMEKMS95cUMdFZedxhRoCQb8QAvD_BwE"
    ],
    "Easy pick카드" : [
        f"http://api6.card-gorilla.com:8080/storage/card/469/card_img/2751/kb_easypick.PNG",
        ["Easy 서비스 : 인터넷 쇼핑몰/배달앱 5% 적립","Easy 서비스 : 대형마트, 주유소/충전소 5% 적립","Basic 서비스 : 교통/통신 5% 적립"],
        f"https://img2.kbcard.com/obj/card/download/09243__prdctOpmn_20190627.pdf"
    ],
    "노리체크카드" : [
        f"http://api6.card-gorilla.com:8080/storage/card/348/card_img/547/kb_noricheck_card.png",
        ["대중교통 : 버스/지하철 10% 청구할인","이동통신 : 이동통신요금 2,500원 환급할인","영화 : CGV 35% 환급할인","커피 : 스타벅스 20% 환급할인","편의점 : GS25 5% 환급할인","금융 : 금융수수료 면제 서비스"],
        f"https://img2.kbcard.com/obj/card/download/01664__prdctOpmn_20181005.pdf?_ga=2.98440794.451842090.1599544774-1779415638.1598350109&_gac=1.221374954.1599546535.CjwKCAjwtNf6BRAwEiwAkt6UQoGhIMwJ_OKUCuP9tj13forfjMHe0urcgMAFMEKMS95cUMdFZedxhRoCQb8QAvD_BwE"
    ],
    "위글위글 첵첵 체크카드" : [
        f"http://api6.card-gorilla.com:8080/storage/card/614/card_img/7976/KB_wigglecheck.png",
        ["대중교통 : 버스/지하철 2~4천원 청구할인","편의점 : CU 편의점 2~4천원 환급할인","커피 : 스타벅스 2~4천원 환급할인","영화 : CGV 2~4천원 환급할인","쇼핑 : 텐바이텐 2~4천원 환급할인"],
        f"https://img2.kbcard.com/obj/card/download/_01914__prdctOpmn_20200608.pdf?_ga=2.34478692.451842090.1599544774-1779415638.1598350109&_gac=1.255060730.1599546535.CjwKCAjwtNf6BRAwEiwAkt6UQoGhIMwJ_OKUCuP9tj13forfjMHe0urcgMAFMEKMS95cUMdFZedxhRoCQb8QAvD_BwE"
    ],
    "펭수 노리 체크카드(펭카)" : [
        f"http://api6.card-gorilla.com:8080/storage/card/559/card_img/6125/%ED%8E%AD%EC%88%98%EB%85%B8%EB%A6%AC%EC%B2%B4%ED%81%AC%EC%B9%B4%EB%93%9C.png",
        ["대중교통 : 버스/지하철 : 10% 청구할인","이동통신 : 이동통신 요금 2,500원 환급할인","영화 : CGV 35% 환급할인","커피 : 스타벅스 20% 환급할인","편의점 : GS25 5% 환급 할인"],
        f"https://img2.kbcard.com/obj/card/download/01664__prdctOpmn_20181005.pdf?_ga=2.193517160.451842090.1599544774-1779415638.1598350109&_gac=1.249644916.1599546535.CjwKCAjwtNf6BRAwEiwAkt6UQoGhIMwJ_OKUCuP9tj13forfjMHe0urcgMAFMEKMS95cUMdFZedxhRoCQb8QAvD_BwE"
    ],
    "해피노리체크카드" : [
        f"http://api6.card-gorilla.com:8080/storage/card/342/card_img/640/kb_happynori_checkcard.png",
        ["대중교통 : 버스/지하철 10% 청구할인","통신 : 이동통신 요금 2,500원 환급할인","영화 : CGV 35% 환급할인","커피 : 스타벅스 20% 환급할인","편의점 : GS25 5% 환급할인"],
        f"https://img2.kbcard.com/obj/card/download/01670__prdctOpmn_20181004.pdf?_ga=2.93385304.451842090.1599544774-1779415638.1598350109&_gac=1.250285940.1599546535.CjwKCAjwtNf6BRAwEiwAkt6UQoGhIMwJ_OKUCuP9tj13forfjMHe0urcgMAFMEKMS95cUMdFZedxhRoCQb8QAvD_BwE"
    ],
    "스타체크카드" : [
        f"http://api6.card-gorilla.com:8080/storage/card/351/card_img/624/kb_star_checkcard.png",
        ["주유 : GS칼텍스 리터당 50~60원 환급할인","영화 : CGV 3000원 환급 할인","대중 교통 : 버스/지하철 5% 청구할인","통신 : 이동통신요금 2,500원 환급할인"],
        f"https://img2.kbcard.com/obj/card/download/01552__prdctOpmn_20181004.pdf?_ga=2.102291012.451842090.1599544774-1779415638.1598350109&_gac=1.253446651.1599546535.CjwKCAjwtNf6BRAwEiwAkt6UQoGhIMwJ_OKUCuP9tj13forfjMHe0urcgMAFMEKMS95cUMdFZedxhRoCQb8QAvD_BwE"
    ],
    "해피CU포인트 체크카드" : [
        f"http://api6.card-gorilla.com:8080/storage/card/353/card_img/637/kb_happycu_checkcard.png",
        ["제휴 포인트 : CU 편의점 2% 적립","포인트리 : 대중교통, 택시 1% 적립"],
        f"https://img2.kbcard.com/obj/card/download/01754__prdctOpmn_20181004.pdf?_ga=2.90109662.451842090.1599544774-1779415638.1598350109&_gac=1.183181908.1599546535.CjwKCAjwtNf6BRAwEiwAkt6UQoGhIMwJ_OKUCuP9tj13forfjMHe0urcgMAFMEKMS95cUMdFZedxhRoCQb8QAvD_BwE"
    ]
}

def card_recommend(post_data):
    overall_data = [
        post_data['spent'],post_data['vehicle'],
        post_data['coffee'],post_data['movie'],post_data['mart'],post_data['conv'],post_data['car'],
        post_data['outdoor'],post_data['trip'],post_data['tele']
    ]
    score = 0
    prop_card = ''
    if post_data['card_type'] == "check":
        for card in recommend_check:
            temp_score = 0
            for item1, item2 in zip(recommend_check[card], overall_data):
                if item1 == item2:
                    temp_score += 1
            print(card, str(temp_score))
            if temp_score >= score:
                score = temp_score
                prop_card = card
        print()
        print(prop_card,str(score))
        return cards_url_priv[prop_card], prop_card
    else :
        for card in recommend_credit:
            temp_score = 0
            for item1, item2 in zip(recommend_credit[card], overall_data):
                if item1 == item2:
                    temp_score += 1
            print(card, str(temp_score))
            if temp_score >= score:
                score = temp_score
                prop_card = card
        print()
        print(prop_card,str(score))
        return cards_url_priv[prop_card], prop_card
   