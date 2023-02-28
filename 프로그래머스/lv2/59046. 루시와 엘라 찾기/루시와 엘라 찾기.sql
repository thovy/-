-- 코드를 입력하세요
SELECT AI.ANIMAL_ID, AI.NAME, AI.SEX_UPON_INTAKE
    FROM ANIMAL_INS AS AI
    WHERE AI.NAME LIKE "Lucy"
        OR AI.NAME LIKE "Ella"
        OR AI.NAME LIKE "Pickle"
        OR AI.NAME LIKE "Rogan"
        OR AI.NAME LIKE "Sabrina"
        OR AI.NAME LIKE "Mitty"
    ORDER BY AI.ANIMAL_ID