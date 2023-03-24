-- 코드를 입력하세요
SELECT U.USER_ID,
        # COUNT(B.BOARD_ID) AS CNT,
        U.NICKNAME,
        CONCAT(U.CITY, " ", U.STREET_ADDRESS1, " ", U.STREET_ADDRESS2)
        AS '전체주소',
        # LEFT(칼럼,왼쪽부터몇개), MID(칼럼,몇번째부터,몇개), RIGHT(칼럼,몇개)
        CONCAT(LEFT(U.TLNO, 3), "-", MID(U.TLNO, 4, 4), "-", RIGHT(U.TLNO, 4))
        AS '전화번호'
    FROM USED_GOODS_BOARD B
    INNER JOIN USED_GOODS_USER U ON B.WRITER_ID = U.USER_ID
    GROUP BY U.USER_ID
    HAVING COUNT(B.BOARD_ID) >= 3
    ORDER BY U.USER_ID DESC