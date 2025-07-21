문의 : handbell@krihs.re.kr

폴더 내 확대본으로 보세요.
=============
Language : Python

1. 229개 시군구를 위치에 히트맵 채워 넣기
* DATA : 국토지리정보원 국토정보플랫폼 - 국토통계지도 - 국토지표 - 어린이집 서비스권역 내 영유아인구비율

 <img src="https://github.com/handbell-H/-visualization/blob/9646a63561caa58db25e3eb3d57d2783faf7409c/1.%20Grid_Viz/grid_visualization_sgg_299.png" width=70% height=70%/>

-------------

2. 229개 시군구 위치에 꺾은선 그래프 채워 넣기
* DATA : 통계청 - 시군구별 총인구
 <img src="https://github.com/handbell-H/-visualization/blob/main/2.%20Grid_Broken_line_graph/grid_broken_line_graph.png" width=70% height=70%/>

###### 격자 위치 생산 : 장혜식(서울대) 교수님, 손종혁 일부 수정

-------------

3-1. 17개 시도별 생활인프라 충족도 산출 후 바이올린 차트 그리기(가로)
* DATA : (국토지리정보원 국토정보플랫폼 - 국토통계지도 - 국토지표) & (국토교통부 국토정책과 국토모니터링 사업 내부자료)

 <img src="https://github.com/handbell-H/-visualization/blob/main/3.%20Violin%20plot%20by%20city/Violin%20plot%20by%20city_Horizontal.png" width=70% height=70%/>

3-2. 17개 시도별 생활인프라 충족도 산출 후 바이올린 차트 그리기(세로)
* DATA : (국토지리정보원 국토정보플랫폼 - 국토통계지도 - 국토지표) & (국토교통부 국토정책과 국토모니터링 사업 내부자료)

 <img src="https://github.com/handbell-H/-visualization/blob/main/3.%20Violin%20plot%20by%20city/Violin%20plot%20by%20city_vertical.png" width=70% height=70%/>

-------------

4. 생활인프라 충족도 산출 후 2분할 바이올린 차트그리기 (2019년 vs 2023년) 
* DATA : (국토지리정보원 국토정보플랫폼 - 국토통계지도 - 총인구 & 국토지표) 
** 초등학교, 어린이집, 도서관, 의원, 생활권공원, 종합사회복지관, 노인여가복지시설, 보건기관, 응급의료시설, 공공체육시설 500m 격자 접근성 및 총 인구
  
 <img src="https://github.com/handbell-H/-visualization/blob/main/4.%20Violin%20plot%20by%20city_2%20year%20comparison/Violin%20plot%20by%20city_2%20year%20comparison.png" width=70% height=70%/>

-------------

5. 21대 대선 지역별 개표 결과 그리기 (기호 1번,기호 2번, 그외)
* DATA : (나무위키 - 21대 대선 지역별 득표 결과로 자체 제작)
* 영남지역 행정구가 많구나. 몰려보일 수 있겠다.
  
 <img src="https://github.com/handbell-H/-visualization/blob/main/5.%20Ratio%20plot%20by%2021th%20presidential%20election%20results/5.%20Ratio%20plot%20by%2021th%20presidential%20election%20results_v2.png" width=70% height=70%/>

6. 시군구-월별 인구 스프링 모양으로 그려보기 (용어가 있나..?)
* DATA : (통계청 -  행정구역(시군구)별, 성별 인구수 (2011년 1월 ~ 2025년 5월))
* 패턴을 직관적으로 보기 좋은것 같다. 그려볼만한 월별 시계열 데이터 좋은게 있을까. 
  
 <img src="https://github.com/handbell-H/-visualization/blob/main/6.%203D%20spring%20plot%20-%20Monthly%20population%20by%20city/6.%203D%20spring%20plot%20-%20Monthly%20population%20by%20city.jpg" width=100% height=100%/>

7. 서울시 구별 아파트 거래금액 릿지플롯 그리기
* DATA : (서울특별시 -  열린데이터광장 - 서울시 부동산 실거래가 정보(2025년))
* 627 부동산 대책이 이슈다. 서울시 아파트가 이렇게 많이 오르다니, 내 고향 강동구도 선방 중이다.
* 강남, 서초, 성동, 용산에는 100억이 넘는 아파트들이.. 많아서 그래프가 ..
  
 <img src="https://github.com/handbell-H/-visualization/blob/main/7.%20ridgeplot%20by%20seoul%20apt%20price/7.%20ridgeplot%20by%20seoul%20apt%20price.png" width=100% height=100%/>

8. 서울시 구별 아파트 거래금액 릿지플롯 2개 겹쳐 그리기
* DATA : (서울특별시 -  열린데이터광장 - 서울시 부동산 실거래가 정보(2024, 2025년))
* 가독성을 위해 50억이 넘는 아파트는 필터링 했다. ㅠ
* 1년새 강남 평균 2.1억 증가 실화?
  
 <img src="https://github.com/handbell-H/-visualization/blob/main/8.%20ridgeplot%20by%20seoul%20apt%20price_2%20year%20comparison/8.%20ridgeplot%20by%20seoul%20apt%20price_2%20year%20comparison.png" width=100% height=100%/>

9. 생활인프라 양호지역 내 총인구 비율 vs 고령인구 비율
* DATA : (국토지리정보원 국토정보플랫폼 - 국토통계지도 - 국토지표) & (국토교통부 국토정책과 국토모니터링 사업 내부자료)
* 생활인프라 충족도 11점 이상인 지역에 사는 총인구 비율 vs 거주인구 비율
* 인구 규모별로 차이가 뚜렷하다.
  
 <img src="https://github.com/handbell-H/-visualization/blob/main/9.%20dumbbel%20plot%20by%202%20ratios/9.%20dumbbel%20plot%20by%202%20ratios.png" width=70% height=70%/>
