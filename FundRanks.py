from selenium import webdriver
import time
import os
from datetime import datetime
# import pyexcel as px
import pandas as pd
import glob
import schedule

class FundRanker:
    def delete_all_files(self, filePath): # 파일이 저장될 디렉토리에 기존 파일이 존재한다면 삭제해주는 함수
        if os.path.exists(filePath):
            for file in os.scandir(filePath):
                os.remove(file.path)
            return 'Remove All File'
        else:
            return 'Directory Not Found'
    
    def update_data(self):
        current_time = datetime.now()
        Year = str(current_time.year)
        Month = str(current_time.month)
        if len(Month) == 1:
            Month = str(0) + Month
        Day = str(current_time.day)
        if len(Day) == 1:
            Day = str(0) + Day
        Today= Year + Month + Day #오늘날짜를 8자리 숫자로 표현, 다운받을시 파일명에 포함됨
        
        file_path1 = './data/8분류'
        abs_path1 = os.path.abspath(file_path1)
        self.delete_all_files(file_path1)
        
        options = webdriver.ChromeOptions()
        
        user_agent = "Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0; rv:11.0) like Gecko"
        options.add_argument('user-agent=' + user_agent)
        
        options.add_argument('headless') #headless모드 브라우저가 뜨지 않고 실행됩니다.
        
        options.add_experimental_option("prefs", {'download.default_directory':rf'{abs_path1}'})#파일저장 경로 설정
        
        chromedriver = './data/chromedriver.exe'
        driver = webdriver.Chrome(chromedriver, options=options)
        
        driver.get('https://dis.kofia.or.kr/websquare/index.jsp?w2xPath=/wq/cmpann/DISPensionProfit.xml&divisionId=MDIS01010003000000&serviceId=SDIS01010003000#!')
        time.sleep(5)
        
        #주식 국내 연금저축, Xpath를 활용한 클릭 방식으로 필요한 자료 다운로드
        driver.find_element_by_xpath('/html/body/div/div[2]/div/div[2]/div[2]/form/div/table/tbody/tr[2]/td/ul/li[2]/input').click()
        driver.find_element_by_xpath('//*[@id="fundTyp_input_0"]/option[2]').click()
        driver.find_element_by_xpath('/html/body/div/div[2]/div/div[2]/div[2]/form/div/table/tbody/tr[5]/td/ul/li[2]/input').click()
        driver.find_element_by_xpath('//*[@id="brcGb_input_3"]').click()
        driver.find_element_by_xpath('/html/body/div[1]/div[2]/div/div[2]/div[2]/form/div/table/tbody/tr[8]/td/div/a[1]/img').click()
        time.sleep(40) # 조건에 맞게 검색되는 시간 30초
        
        driver.find_element_by_xpath('/html/body/div[1]/div[2]/div/div[2]/div[3]/div/div[1]/div[2]/a[1]/img').click()
        time.sleep(3)
        
        file_oldname = os.path.join(file_path1, f"연금상품상세수익률_{Today}.xlsx")# 다운받은 파일명 변경작업
        file_newname_newfile = os.path.join(file_path1, "연금저축국내주식.xlsx")
        os.rename(file_oldname, file_newname_newfile)
        
        #주식 해외 연금저축
        driver.find_element_by_xpath('/html/body/div[1]/div[2]/div/div[2]/div[2]/form/div/table/tbody/tr[5]/td/ul/li[3]/input').click()
        driver.find_element_by_xpath('/html/body/div[1]/div[2]/div/div[2]/div[2]/form/div/table/tbody/tr[8]/td/div/a[1]/img').click()
        time.sleep(40)
        
        driver.find_element_by_xpath('/html/body/div[1]/div[2]/div/div[2]/div[3]/div/div[1]/div[2]/a[1]/img').click()
        time.sleep(3)
        
        file_oldname = os.path.join(file_path1, f"연금상품상세수익률_{Today}.xlsx")
        file_newname_newfile = os.path.join(file_path1, "연금저축해외주식.xlsx")
        os.rename(file_oldname, file_newname_newfile)
        
        #채권 해외 연금저축
        driver.find_element_by_xpath('/html/body/div[1]/div[2]/div/div[2]/div[2]/form/div/table/tbody/tr[4]/td[1]/div/div/select/option[5]').click()
        driver.find_element_by_xpath('/html/body/div[1]/div[2]/div/div[2]/div[2]/form/div/table/tbody/tr[8]/td/div/a[1]/img').click()
        time.sleep(40)
        
        driver.find_element_by_xpath('/html/body/div[1]/div[2]/div/div[2]/div[3]/div/div[1]/div[2]/a[1]/img').click()
        time.sleep(3)
        
        file_oldname = os.path.join(file_path1, f"연금상품상세수익률_{Today}.xlsx")
        file_newname_newfile = os.path.join(file_path1, "연금저축해외채권.xlsx")
        os.rename(file_oldname, file_newname_newfile)
        
        
        #채권 국내 연금저축
        driver.find_element_by_xpath('/html/body/div[1]/div[2]/div/div[2]/div[2]/form/div/table/tbody/tr[5]/td/ul/li[2]/input').click()
        driver.find_element_by_xpath('/html/body/div[1]/div[2]/div/div[2]/div[2]/form/div/table/tbody/tr[8]/td/div/a[1]/img').click()
        time.sleep(30)
        
        driver.find_element_by_xpath('/html/body/div[1]/div[2]/div/div[2]/div[3]/div/div[1]/div[2]/a[1]/img').click()
        time.sleep(3)
        
        file_oldname = os.path.join(file_path1, f"연금상품상세수익률_{Today}.xlsx")
        file_newname_newfile = os.path.join(file_path1, "연금저축국내채권.xlsx")
        os.rename(file_oldname, file_newname_newfile)
        
        
        #채권 국내 퇴직연금
        driver.find_element_by_xpath('/html/body/div[1]/div[2]/div/div[2]/div[2]/form/div/table/tbody/tr[6]/td/ul/li[5]/input').click()
        driver.find_element_by_xpath('/html/body/div[1]/div[2]/div/div[2]/div[2]/form/div/table/tbody/tr[8]/td/div/a[1]/img').click()
        time.sleep(40)
        
        driver.find_element_by_xpath('/html/body/div[1]/div[2]/div/div[2]/div[3]/div/div[1]/div[2]/a[1]/img').click()
        time.sleep(3)
        
        file_oldname = os.path.join(file_path1, f"연금상품상세수익률_{Today}.xlsx")
        file_newname_newfile = os.path.join(file_path1, "퇴직연금국내채권.xlsx")
        os.rename(file_oldname, file_newname_newfile)
        
        
        #채권 해외 퇴직연금
        driver.find_element_by_xpath('/html/body/div[1]/div[2]/div/div[2]/div[2]/form/div/table/tbody/tr[5]/td/ul/li[3]/input').click()
        driver.find_element_by_xpath('/html/body/div[1]/div[2]/div/div[2]/div[2]/form/div/table/tbody/tr[8]/td/div/a[1]/img').click()
        time.sleep(40)
        
        driver.find_element_by_xpath('/html/body/div[1]/div[2]/div/div[2]/div[3]/div/div[1]/div[2]/a[1]/img').click()
        time.sleep(3)
        
        file_oldname = os.path.join(file_path1, f"연금상품상세수익률_{Today}.xlsx")
        file_newname_newfile = os.path.join(file_path1, "퇴직연금해외채권.xlsx")
        os.rename(file_oldname, file_newname_newfile)
        
        
        #주식 해외 퇴직연금
        driver.find_element_by_xpath('/html/body/div[1]/div[2]/div/div[2]/div[2]/form/div/table/tbody/tr[4]/td[1]/div/div/select/option[2]').click()
        driver.find_element_by_xpath('/html/body/div[1]/div[2]/div/div[2]/div[2]/form/div/table/tbody/tr[8]/td/div/a[1]/img').click()
        time.sleep(40)
        
        driver.find_element_by_xpath('/html/body/div[1]/div[2]/div/div[2]/div[3]/div/div[1]/div[2]/a[1]/img').click()
        time.sleep(3)
        
        file_oldname = os.path.join(file_path1, f"연금상품상세수익률_{Today}.xlsx")
        file_newname_newfile = os.path.join(file_path1, "퇴직연금해외주식.xlsx")
        os.rename(file_oldname, file_newname_newfile)
        
        
        #주식 국내 퇴직연금
        driver.find_element_by_xpath('/html/body/div[1]/div[2]/div/div[2]/div[2]/form/div/table/tbody/tr[5]/td/ul/li[2]/input').click()
        driver.find_element_by_xpath('/html/body/div[1]/div[2]/div/div[2]/div[2]/form/div/table/tbody/tr[8]/td/div/a[1]/img').click()
        time.sleep(40)
        
        driver.find_element_by_xpath('/html/body/div[1]/div[2]/div/div[2]/div[3]/div/div[1]/div[2]/a[1]/img').click()
        time.sleep(3)
        
        file_oldname = os.path.join(file_path1, f"연금상품상세수익률_{Today}.xlsx")
        file_newname_newfile = os.path.join(file_path1, "퇴직연금국내주식.xlsx")
        os.rename(file_oldname, file_newname_newfile)
        
        driver.quit()
    
        #통합 위험등급 데이터 수집
    
        file_path2 = './data/통합'
        abs_path2 = os.path.abspath(file_path2)

        self.delete_all_files(file_path2) # 1번셀 자료도 지우므로 사용에 유의
        
        options = webdriver.ChromeOptions()
        
        user_agent = "Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0; rv:11.0) like Gecko"
        options.add_argument('user-agent=' + user_agent)
        
        options.add_argument('headless') #headless모드 브라우저가 뜨지 않고 실행됩니다.
        
        options.add_experimental_option("prefs", {'download.default_directory':rf'{abs_path2}'})#파일저장 경로 설정
        
        chromedriver = './static/chromedriver.exe'
        driver = webdriver.Chrome(chromedriver, options=options)
        
        #통합.xls 만들기/ 통합파일은 월별 갱신
        driver.get('https://dis.kofia.or.kr/websquare/index.jsp?w2xPath=/wq/fundann/DISFundSalRtn.xml&divisionId=MDIS01013004000000&serviceId=SDIS01013004000')
        time.sleep(10)
        
        # KB증권 /1.선택탭 클릭, 2.증권사선택, 3.검색
        driver.find_element_by_xpath('/html/body/div[1]/div[2]/div/div[2]/div[2]/form/div/table/tbody/tr[2]/td/div/div/select').click()
        driver.find_element_by_xpath('/html/body/div/div[2]/div/div[2]/div[2]/form/div/table/tbody/tr[2]/td/div/div/select/option[21]').click()#이것만 수정
        driver.find_element_by_xpath('/html/body/div[1]/div[2]/div/div[2]/div[2]/form/div/table/tbody/tr[4]/td/div/a[1]/img').click()
        time.sleep(15)
        
        driver.find_element_by_xpath('/html/body/div[1]/div[2]/div/div[2]/div[3]/div/div[1]/div[2]/a[1]/img').click()# 다운로드
        time.sleep(8)
        
        file_oldname = os.path.join(file_path2, f"펀드판매회사 펀드 수익률 공시_{Today}.xlsx")
        file_newname_newfile = os.path.join(file_path2, "KB증권.xlsx")
        os.rename(file_oldname, file_newname_newfile)
        
        #KEB하나은행
        driver.find_element_by_xpath('/html/body/div[1]/div[2]/div/div[2]/div[2]/form/div/table/tbody/tr[2]/td/div/div/select').click()
        driver.find_element_by_xpath('/html/body/div[1]/div[2]/div/div[2]/div[2]/form/div/table/tbody/tr[2]/td/div/div/select/option[2]').click()
        driver.find_element_by_xpath('/html/body/div[1]/div[2]/div/div[2]/div[2]/form/div/table/tbody/tr[4]/td/div/a[1]/img').click()
        time.sleep(15)
        
        driver.find_element_by_xpath('/html/body/div[1]/div[2]/div/div[2]/div[3]/div/div[1]/div[2]/a[1]/img').click()
        time.sleep(8)
        
        file_oldname = os.path.join(file_path2, f"펀드판매회사 펀드 수익률 공시_{Today}.xlsx")
        file_newname_newfile = os.path.join(file_path2, "KEB하나은행.xlsx")
        os.rename(file_oldname, file_newname_newfile)
        
        #NH투자증권
        driver.find_element_by_xpath('/html/body/div[1]/div[2]/div/div[2]/div[2]/form/div/table/tbody/tr[2]/td/div/div/select').click()
        driver.find_element_by_xpath('/html/body/div[1]/div[2]/div/div[2]/div[2]/form/div/table/tbody/tr[2]/td/div/div/select/option[22]').click()
        driver.find_element_by_xpath('/html/body/div[1]/div[2]/div/div[2]/div[2]/form/div/table/tbody/tr[4]/td/div/a[1]/img').click()
        time.sleep(15)
        
        driver.find_element_by_xpath('/html/body/div[1]/div[2]/div/div[2]/div[3]/div/div[1]/div[2]/a[1]/img').click()
        time.sleep(8)
        
        file_oldname = os.path.join(file_path2, f"펀드판매회사 펀드 수익률 공시_{Today}.xlsx")
        file_newname_newfile = os.path.join(file_path2, "NH투자증권.xlsx")
        os.rename(file_oldname, file_newname_newfile)
        
        #대신증권
        driver.find_element_by_xpath('/html/body/div[1]/div[2]/div/div[2]/div[2]/form/div/table/tbody/tr[2]/td/div/div/select').click()
        driver.find_element_by_xpath('/html/body/div[1]/div[2]/div/div[2]/div[2]/form/div/table/tbody/tr[2]/td/div/div/select/option[26]').click()
        driver.find_element_by_xpath('/html/body/div[1]/div[2]/div/div[2]/div[2]/form/div/table/tbody/tr[4]/td/div/a[1]/img').click()
        time.sleep(15)
        
        driver.find_element_by_xpath('/html/body/div[1]/div[2]/div/div[2]/div[3]/div/div[1]/div[2]/a[1]/img').click()
        time.sleep(8)
        
        file_oldname = os.path.join(file_path2, f"펀드판매회사 펀드 수익률 공시_{Today}.xlsx")
        file_newname_newfile = os.path.join(file_path2, "대신증권.xlsx")
        os.rename(file_oldname, file_newname_newfile)
        
        #미래에셋증권
        driver.find_element_by_xpath('/html/body/div[1]/div[2]/div/div[2]/div[2]/form/div/table/tbody/tr[2]/td/div/div/select').click()
        driver.find_element_by_xpath('/html/body/div[1]/div[2]/div/div[2]/div[2]/form/div/table/tbody/tr[2]/td/div/div/select/option[29]').click()
        driver.find_element_by_xpath('/html/body/div[1]/div[2]/div/div[2]/div[2]/form/div/table/tbody/tr[4]/td/div/a[1]/img').click()
        time.sleep(15)
        
        driver.find_element_by_xpath('/html/body/div[1]/div[2]/div/div[2]/div[3]/div/div[1]/div[2]/a[1]/img').click()
        time.sleep(8)
        
        file_oldname = os.path.join(file_path2, f"펀드판매회사 펀드 수익률 공시_{Today}.xlsx")
        file_newname_newfile = os.path.join(file_path2, "미래에셋증권.xlsx")
        os.rename(file_oldname, file_newname_newfile)
        
        #삼성증권
        driver.find_element_by_xpath('/html/body/div[1]/div[2]/div/div[2]/div[2]/form/div/table/tbody/tr[2]/td/div/div/select').click()
        driver.find_element_by_xpath('/html/body/div[1]/div[2]/div/div[2]/div[2]/form/div/table/tbody/tr[2]/td/div/div/select/option[32]').click()
        driver.find_element_by_xpath('/html/body/div[1]/div[2]/div/div[2]/div[2]/form/div/table/tbody/tr[4]/td/div/a[1]/img').click()
        time.sleep(15)
        
        driver.find_element_by_xpath('/html/body/div[1]/div[2]/div/div[2]/div[3]/div/div[1]/div[2]/a[1]/img').click()
        time.sleep(8)
        
        file_oldname = os.path.join(file_path2, f"펀드판매회사 펀드 수익률 공시_{Today}.xlsx")
        file_newname_newfile = os.path.join(file_path2, "삼성증권.xlsx")
        os.rename(file_oldname, file_newname_newfile)
        
        #신영증권
        driver.find_element_by_xpath('/html/body/div[1]/div[2]/div/div[2]/div[2]/form/div/table/tbody/tr[2]/td/div/div/select').click()
        driver.find_element_by_xpath('/html/body/div[1]/div[2]/div/div[2]/div[2]/form/div/table/tbody/tr[2]/td/div/div/select/option[34]').click()
        driver.find_element_by_xpath('/html/body/div[1]/div[2]/div/div[2]/div[2]/form/div/table/tbody/tr[4]/td/div/a[1]/img').click()
        time.sleep(15)
        
        driver.find_element_by_xpath('/html/body/div[1]/div[2]/div/div[2]/div[3]/div/div[1]/div[2]/a[1]/img').click()
        time.sleep(8)
        
        file_oldname = os.path.join(file_path2, f"펀드판매회사 펀드 수익률 공시_{Today}.xlsx")
        file_newname_newfile = os.path.join(file_path2, "신영증권.xlsx")
        os.rename(file_oldname, file_newname_newfile)
        
        #신한금융투자
        driver.find_element_by_xpath('/html/body/div[1]/div[2]/div/div[2]/div[2]/form/div/table/tbody/tr[2]/td/div/div/select').click()
        driver.find_element_by_xpath('/html/body/div[1]/div[2]/div/div[2]/div[2]/form/div/table/tbody/tr[2]/td/div/div/select/option[35]').click()
        driver.find_element_by_xpath('/html/body/div[1]/div[2]/div/div[2]/div[2]/form/div/table/tbody/tr[4]/td/div/a[1]/img').click()
        time.sleep(15)
        
        driver.find_element_by_xpath('/html/body/div[1]/div[2]/div/div[2]/div[3]/div/div[1]/div[2]/a[1]/img').click()
        time.sleep(8)
        
        file_oldname = os.path.join(file_path2, f"펀드판매회사 펀드 수익률 공시_{Today}.xlsx")
        file_newname_newfile = os.path.join(file_path2, "신한금융투자.xlsx")
        os.rename(file_oldname, file_newname_newfile)
        
        #신한은행
        driver.find_element_by_xpath('/html/body/div[1]/div[2]/div/div[2]/div[2]/form/div/table/tbody/tr[2]/td/div/div/select').click()
        driver.find_element_by_xpath('/html/body/div[1]/div[2]/div/div[2]/div[2]/form/div/table/tbody/tr[2]/td/div/div/select/option[12]').click()
        driver.find_element_by_xpath('/html/body/div[1]/div[2]/div/div[2]/div[2]/form/div/table/tbody/tr[4]/td/div/a[1]/img').click()
        time.sleep(15)
        
        driver.find_element_by_xpath('/html/body/div[1]/div[2]/div/div[2]/div[3]/div/div[1]/div[2]/a[1]/img').click()
        time.sleep(8)
        
        file_oldname = os.path.join(file_path2, f"펀드판매회사 펀드 수익률 공시_{Today}.xlsx")
        file_newname_newfile = os.path.join(file_path2, "신한은행.xlsx")
        os.rename(file_oldname, file_newname_newfile)
        
        #유안타증권
        driver.find_element_by_xpath('/html/body/div[1]/div[2]/div/div[2]/div[2]/form/div/table/tbody/tr[2]/td/div/div/select').click()
        driver.find_element_by_xpath('/html/body/div[1]/div[2]/div/div[2]/div[2]/form/div/table/tbody/tr[2]/td/div/div/select/option[36]').click()
        driver.find_element_by_xpath('/html/body/div[1]/div[2]/div/div[2]/div[2]/form/div/table/tbody/tr[4]/td/div/a[1]/img').click()
        time.sleep(15)
        
        driver.find_element_by_xpath('/html/body/div[1]/div[2]/div/div[2]/div[3]/div/div[1]/div[2]/a[1]/img').click()
        time.sleep(8)
        
        file_oldname = os.path.join(file_path2, f"펀드판매회사 펀드 수익률 공시_{Today}.xlsx")
        file_newname_newfile = os.path.join(file_path2, "유안타증권.xlsx")
        os.rename(file_oldname, file_newname_newfile)
        
        #키움증권
        driver.find_element_by_xpath('/html/body/div[1]/div[2]/div/div[2]/div[2]/form/div/table/tbody/tr[2]/td/div/div/select').click()
        driver.find_element_by_xpath('/html/body/div[1]/div[2]/div/div[2]/div[2]/form/div/table/tbody/tr[2]/td/div/div/select/option[43]').click()
        driver.find_element_by_xpath('/html/body/div[1]/div[2]/div/div[2]/div[2]/form/div/table/tbody/tr[4]/td/div/a[1]/img').click()
        time.sleep(15)
        
        driver.find_element_by_xpath('/html/body/div[1]/div[2]/div/div[2]/div[3]/div/div[1]/div[2]/a[1]/img').click()
        time.sleep(8)
        
        file_oldname = os.path.join(file_path2, f"펀드판매회사 펀드 수익률 공시_{Today}.xlsx")
        file_newname_newfile = os.path.join(file_path2, "키움증권.xlsx")
        os.rename(file_oldname, file_newname_newfile)
        
        #하나금융투자
        driver.find_element_by_xpath('/html/body/div[1]/div[2]/div/div[2]/div[2]/form/div/table/tbody/tr[2]/td/div/div/select').click()
        driver.find_element_by_xpath('/html/body/div[1]/div[2]/div/div[2]/div[2]/form/div/table/tbody/tr[2]/td/div/div/select/option[44]').click()
        driver.find_element_by_xpath('/html/body/div[1]/div[2]/div/div[2]/div[2]/form/div/table/tbody/tr[4]/td/div/a[1]/img').click()
        time.sleep(15)
        
        driver.find_element_by_xpath('/html/body/div[1]/div[2]/div/div[2]/div[3]/div/div[1]/div[2]/a[1]/img').click()
        time.sleep(8)
        
        file_oldname = os.path.join(file_path2, f"펀드판매회사 펀드 수익률 공시_{Today}.xlsx")
        file_newname_newfile = os.path.join(file_path2, "하나금융투자.xlsx")
        os.rename(file_oldname, file_newname_newfile)
        
        #하이투자증권
        driver.find_element_by_xpath('/html/body/div[1]/div[2]/div/div[2]/div[2]/form/div/table/tbody/tr[2]/td/div/div/select').click()
        driver.find_element_by_xpath('/html/body/div[1]/div[2]/div/div[2]/div[2]/form/div/table/tbody/tr[2]/td/div/div/select/option[45]').click()
        driver.find_element_by_xpath('/html/body/div[1]/div[2]/div/div[2]/div[2]/form/div/table/tbody/tr[4]/td/div/a[1]/img').click()
        time.sleep(15)
        
        driver.find_element_by_xpath('/html/body/div[1]/div[2]/div/div[2]/div[3]/div/div[1]/div[2]/a[1]/img').click()
        time.sleep(8)
        
        file_oldname = os.path.join(file_path2, f"펀드판매회사 펀드 수익률 공시_{Today}.xlsx")
        file_newname_newfile = os.path.join(file_path2, "하이투자증권.xlsx")
        os.rename(file_oldname, file_newname_newfile)
        
        #한국투자증권
        driver.find_element_by_xpath('/html/body/div[1]/div[2]/div/div[2]/div[2]/form/div/table/tbody/tr[2]/td/div/div/select').click()
        driver.find_element_by_xpath('/html/body/div[1]/div[2]/div/div[2]/div[2]/form/div/table/tbody/tr[2]/td/div/div/select/option[46]').click()
        driver.find_element_by_xpath('/html/body/div[1]/div[2]/div/div[2]/div[2]/form/div/table/tbody/tr[4]/td/div/a[1]/img').click()
        time.sleep(15)
        
        driver.find_element_by_xpath('/html/body/div[1]/div[2]/div/div[2]/div[3]/div/div[1]/div[2]/a[1]/img').click()
        time.sleep(8)
        
        file_oldname = os.path.join(file_path2, f"펀드판매회사 펀드 수익률 공시_{Today}.xlsx")
        file_newname_newfile = os.path.join(file_path2, "한국투자증권.xlsx")
        os.rename(file_oldname, file_newname_newfile)
        
        #한국포스증권
        driver.find_element_by_xpath('/html/body/div[1]/div[2]/div/div[2]/div[2]/form/div/table/tbody/tr[2]/td/div/div/select').click()
        driver.find_element_by_xpath('/html/body/div[1]/div[2]/div/div[2]/div[2]/form/div/table/tbody/tr[2]/td/div/div/select/option[47]').click()
        driver.find_element_by_xpath('/html/body/div[1]/div[2]/div/div[2]/div[2]/form/div/table/tbody/tr[4]/td/div/a[1]/img').click()
        time.sleep(15)
        
        driver.find_element_by_xpath('/html/body/div[1]/div[2]/div/div[2]/div[3]/div/div[1]/div[2]/a[1]/img').click()
        time.sleep(8)
        
        file_oldname = os.path.join(file_path2, f"펀드판매회사 펀드 수익률 공시_{Today}.xlsx")
        file_newname_newfile = os.path.join(file_path2, "한국포스증권.xlsx")
        os.rename(file_oldname, file_newname_newfile)
        
        driver.quit()
        
        #통합.xls로 파일처리하기/ 디렉토리 내부의 모든 xls파일 통합하는 방식, 활용에 융의할 필요 있음
        
        print("Process start")
        start_time = time.time()
        
        ## 폴더명 지정
        directory = f"{file_path2}"
        
        ## 결과 파일명 지정
        outfile_name = f"{file_path2}/통합.xlsx"
        
        input_files=os.listdir(directory)
        
        CONTENTS = []
        
        for filename in input_files:
            if ".xls" not in filename:
                continue
        
            data_array=px.get_array(file_name=directory + "/" + filename)
        
            header = data_array[0]
            data_array = data_array[1:]
        
            if len(CONTENTS) == 0:
                CONTENTS.append(header)
        
            CONTENTS += data_array
        
            px.save_as(array=CONTENTS, dest_file_name=outfile_name)
        
        print("process done")
        
        end_time = time.time()
        
        print("the job took " + str(end_time - start_time) + "seconds.")
        
        
        #통합.xls로 파일처리하기/ 디렉토리 내부의 모든 xls파일 통합하는 방식, 활용에 융의할 필요 있음
        
        print("Process start")
        start_time = time.time()
        
        ## 폴더명 지정
        directory = f"{file_path2}"
        
        ## 결과 파일명 지정
        outfile_name = f"{file_path2}/통합.xlsx"
        
        input_files = os.listdir(directory)
        
        CONTENTS = []
        
        for filename in input_files:
            if ".xlsx" not in filename:
                continue
        
            data_array=px.get_array(file_name=directory + "/" + filename)
        
            header = data_array[0]
            data_array = data_array[1:]
        
            if len(CONTENTS) == 0:
                CONTENTS.append(header)
        
            CONTENTS += data_array
        
            px.save_as(array=CONTENTS, dest_file_name=outfile_name)
        
        print("process done")
        
        end_time = time.time()
        
        print("the job took " + str(end_time - start_time) + "seconds.")
        
        
        #데이터 통합과정    
        File_List = glob.glob(r'.\data\8분류\*.xlsx')
        
        for i in range(8,0,-1):
            data = pd.read_excel(File_List[8-i])
            name = []
        
            for k in range(len(data)):
                name.append(data['펀드명'][k])
            
            names=name[1:]
        
            result = ['위험등급']
            risk_data = pd.read_excel('./data/통합/통합.xls')
        
            for name in names:
                if name in list(risk_data['펀드명']):
                    index=risk_data[risk_data['펀드명'] == name].index[0]
                    result.append(risk_data['위험등급'][index])
                else:
                    result.append('NA')
        
            data['위험등급']=result
            data.columns=['회사','펀드유형','상품종류','펀드명','설정일','기준가격','설정원본','순자산','이익1개월','이익3개월','이익6개월','이익1년','이익2년','이익3년','이익4년','이익5년','위험등급']
            data=data[1:]
            data.to_excel(f'./data/funds{i}.xlsx', index=False)
    
    ####10개의 결과화면 만들기
        for i in range(1,9):
            globals()['R_Data'+str(i)] = pd.read_excel(f'./data/funds{i}.xlsx').sort_values('이익1년').drop(['상품종류'], axis=1)
    ###문제없이 작동
    ####퇴직연금 안정형
        result1 = pd.concat([R_Data4.head(2), R_Data3.head(6), R_Data1.head(2)])
        result1.to_excel('./result/result1.xlsx')
    ####퇴직연금 안정추구형
        result2 = pd.concat([R_Data4.head(3), R_Data3.head(4), R_Data1.head(3)])
        result2.to_excel('./result/result2.xlsx')
    ####퇴직연금 위험중립형
        result3 = pd.concat([R_Data4.head(3), R_Data2.head(2), R_Data3.head(3), R_Data1.head(2)])
        result3.to_excel('./result/result3.xlsx')
    ####퇴직연금 적극투자형
        result4 = pd.concat([R_Data4.head(3), R_Data2.head(3), R_Data3.head(2), R_Data1.head(2)])
        result4.to_excel('./result/result4.xlsx')
    ####퇴직연금 공격투자형
        result5 = pd.concat([R_Data4.head(4), R_Data2.head(4), R_Data3.head(1), R_Data1.head(1)])
        result5.to_excel('./result/result5.xlsx')
    ####연금저축 안정형
        result6 = pd.concat([R_Data8.head(2), R_Data7.head(6), R_Data5.head(2)])
        result6.to_excel('./result/result6.xlsx')
    ####연금저축 안정추구형
        result7 = pd.concat([R_Data8.head(3), R_Data7.head(4), R_Data5.head(3)])
        result7.to_excel('./result/result7.xlsx')
    ####연금저축 위험중립형
        result8 = pd.concat([R_Data8.head(3), R_Data6.head(2), R_Data7.head(3), R_Data5.head(2)])
        result8.to_excel('./result/result8.xlsx')
    ####연금저축 적극투자형
        result9 = pd.concat([R_Data8.head(3), R_Data6.head(3), R_Data7.head(2), R_Data5.head(2)])
        result9.to_excel('./result/result9.xlsx')
    ####연금저축 공격투자형
        result10 = pd.concat([R_Data8.head(4), R_Data6.head(4), R_Data7.head(1), R_Data5.head(1)])
        result10.to_excel('./result/result10.xlsx')
        
        print('finish')
    
    def data_call(self, score):
        if score <= 20 : 
            result1 = pd.read_excel('./result/result1.xlsx', usecols="B:Q")
            result2 = pd.read_excel('./result/result6.xlsx', usecols="B:Q")
        elif score <= 40 :
            result1 = pd.read_excel('./result/result2.xlsx', usecols="B:Q")
            result2 = pd.read_excel('./result/result7.xlsx', usecols="B:Q")
        elif score <= 60 :
            result1 = pd.read_excel('./result/result3.xlsx', usecols="B:Q")
            result2 = pd.read_excel('./result/result8.xlsx', usecols="B:Q")
        elif score <= 80 :
            result1 = pd.read_excel('./result/result4.xlsx', usecols="B:Q")
            result2 = pd.read_excel('./result/result9.xlsx', usecols="B:Q")
        else:
            result1 = pd.read_excel('./result/result5.xlsx', usecols="B:Q")
            result2 = pd.read_excel('./result/result10.xlsx', usecols="B:Q")
        
        return result1, result2

    def execute_daily(self):
        schedule.every().sunday.at("04:00").do(self.update_data)

