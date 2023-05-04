-- 코드를 입력하세요
SELECT CATEGORY, sum(SALES) as TOTAL_SALES from BOOK as book 
inner join BOOK_SALES as sales on book.BOOK_ID = sales.BOOK_ID
where date_format(sales.SALES_DATE, '%Y%m') = '202201'
group by book.CATEGORY
order by book.CATEGORY ASC