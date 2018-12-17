#
# DB Query SQL 도움말
# - https://www.tutorialspoint.com/sql/sql-insert-query.htm
# - https://www.tutorialspoint.com/sql/sql-update-query.htm
import sqlite3

conn = sqlite3.connect('data.db')
c = conn.cursor()

## 테이블 PICK
try:
  c.execute('''CREATE TABLE pick
                 (title text, name text, info text, url text, address text, time text)''')
  c.execute("INSERT INTO pick VALUES ('갬성 충만한 카페', '을지빈', '카페 내부에 보면 여기저기서 모아 놓은 빈티지한 소품들이 가득하다. "
            "카페 인테리어도 빈티지한 모습이고, 조용한 음악이 어우러진 공간!.', 'https://www.instagram.com/cafe_euljibean/', "
            "'서울 중구 을지로 14길 21', '11:30~22:00')")
  c.execute("INSERT INTO pick VALUES ('갬성 충만한 카페', '제주 책다방', '입장료 6000원으로 가능한 음료 무엇이든 주문 가능한 북카페."
            "제주도 혼행하는 여행자에게 추천하고 싶은 조용한 카페', 'http://blog.naver.com/jo_1218', '제주특별자치도 제주시 구좌읍"
            "월정1길 70-1', '11:00~19:00(월요일 휴무)')")
  c.execute("INSERT INTO pick VALUES ('갬성 충만한 카페', '돌창고프로젝트', '바로 옆 건물이 음료와 디저트를 즐길 수 있는 카페인데,"
            "들어가자마자 보였던 대박적인 논뷰! 다들 오션뷰가 짱이라고 하지만, 가끔 논뷰에도 눈길이 간다.', 'http://dolchanggo.com/',"
            "'경상남도 남해군 삼동면 봉화로 538-1', '10:00~18:00(목요일 휴무)')")
  c.execute("INSERT INTO pick VALUES ('갬성 충만한 카페', '커피한약방', '허준 선생님이 환자를 돌봤던 혜민서가 있었던 곳! 커피에 한약은 없다.', "
            "'https://store.naver.com/restaurants/detail?entry=plt&id=1614417324&query=%EC%BB%A4%ED%94%BC%ED%95%9C%EC%95%BD%EB%B0%A9',"
            "'서울 중구 삼일대로12길 16-6', '평일 08:00~22:30 토요일 11:00~22:00 일요일 11:00~21:30')")

  c.execute("INSERT INTO pick VALUES ('속이 확 풀리는 해장국집', '24시 철원양평신내해장국', '해장국의 양이 부족하다 느끼는 사람은 이곳으로!"
            "선지가 무한리필인 곳이다.', 'https://store.naver.com/restaurants/detail?id=18355637', '경기 고양시 일산동구 장항로 367',"
            "'00:00~24:00')")
  c.execute("INSERT INTO pick VALUES ('속이 확 풀리는 해장국집', '중앙식당', '순대국이 야무지게 들어가 있어 항상 손님이 붐비는 집."
            "양도 맛도 다 만족스러운 식당이다.', 'https://store.naver.com/restaurants/detail?entry=plt&id=18391668&query=%EC%A4%91%EC%95%99%EC%8B%9D%EB%8B%B9',"
            "'경기 고양시 일산서구 일청로12번길 9', '10:00~22:00(매월 14일 정기휴무)')")
  c.execute("INSERT INTO pick VALUES ('속이 확 풀리는 해장국집', '소담반상', '칼칼하고 진한 국물에 속이 화끈히게 풀리는 맛이다. 자극적인"
            "맛을 좋아하는 사람에게 강추', 'https://store.naver.com/restaurants/detail?id=1935684763', '서울 강서구 하늘길 112',"
            "'06:00~20:30')")
  c.execute("INSERT INTO pick VALUES ('속이 확 풀리는 해장국집', '대풍식당', '순대와 고기가 서비스로 나오는 해장국을 맛볼 수 있다. 국밥안에 들어가는"
            "콩나물은 그야말로 최고!', '', '광주광역시 동구 동계천로 56-4', '8:00~20:00')")

  conn.commit()
  print('Created PICK')
except:
  print('Skip PICK')
  pass
