-- 코드를 입력하세요
SELECT WAREHOUSE_ID, WAREHOUSE_NAME, ADDRESS, if(WAREHOUSE_ID in (select WAREHOUSE_ID 
                                                                  from FOOD_WAREHOUSE 
                                                                  where FREEZER_YN is null or FREEZER_YN = 'N'),'N','Y') 
                                                                  as FREEZER_YN from FOOD_WAREHOUSE 
where WAREHOUSE_NAME like '%_경기%'
order by WAREHOUSE_ID