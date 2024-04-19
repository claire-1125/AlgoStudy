-- 보호 시작일: ANIMAL_INS.DATETIME
-- 입양일: ANIMAL_OUTS.DATETIME
-- 입양일 < 보호 시작일

SELECT INS.ANIMAL_ID, INS.NAME
FROM ANIMAL_INS INS INNER JOIN ANIMAL_OUTS OUTS
    ON INS.ANIMAL_ID = OUTS.ANIMAL_ID
WHERE 1=1
AND OUTS.DATETIME < INS.DATETIME
ORDER BY INS.DATETIME ASC