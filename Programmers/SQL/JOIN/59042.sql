-- 코드를 입력하세요
SELECT OUTS.ANIMAL_ID, OUTS.NAME
FROM ANIMAL_OUTS OUTS LEFT JOIN ANIMAL_INS INS
    ON OUTS.ANIMAL_ID = INS.ANIMAL_ID
WHERE 1=1
AND IFNULL(INS.ANIMAL_ID,'') = ''
ORDER BY OUTS.ANIMAL_ID