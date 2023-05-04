-- 코드를 입력하세요
SELECT book.BOOK_ID, author.AUTHOR_NAME, date_format(book.PUBLISHED_DATE, '%Y-%m-%d') from BOOK as book
inner join AUTHOR as author on book.AUTHOR_ID = author.AUTHOR_ID
where book.CATEGORY = '경제'
order by book.PUBLISHED_DATE ASC