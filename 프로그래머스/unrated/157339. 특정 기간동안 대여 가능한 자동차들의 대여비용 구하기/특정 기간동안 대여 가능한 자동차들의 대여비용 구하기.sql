# SELECT info.*, plan.*, floor(info.DAILY_FEE * (100 - plan.DISCOUNT_RATE) / 100 * 30) as FEE
SELECT info.CAR_ID, info.CAR_TYPE, floor(info.DAILY_FEE * (100 - plan.DISCOUNT_RATE) / 100 * 30) as FEE
from CAR_RENTAL_COMPANY_CAR as info 
inner join CAR_RENTAL_COMPANY_DISCOUNT_PLAN as plan on info.CAR_TYPE = plan.CAR_TYPE and DURATION_TYPE = '30일 이상'
where (info.CAR_TYPE = '세단' or info.CAR_TYPE = 'SUV')
    and info.CAR_ID not in (select CAR_ID from CAR_RENTAL_COMPANY_RENTAL_HISTORY as history
                        where   (history.START_DATE < '2022-11-01' and '2022-11-30' < history.END_DATE) or
                                (history.START_DATE between '2022-11-01' and '2022-11-30') or
                                (history.END_DATE between '2022-11-01' and '2022-11-30'))
HAVING FEE >= 500000 AND FEE < 2000000
order by FEE DESC, info.CAR_TYPE ASC, info.CAR_ID desc;