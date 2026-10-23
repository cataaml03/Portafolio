
SELECT COUNT(*) AS total_series
FROM series;

SELECT COUNT(*) AS total_observaciones
FROM observaciones;

SELECT id_serie, fecha, COUNT(*) AS repeticiones
FROM observaciones
GROUP BY id_serie, fecha
HAVING COUNT(*) > 1;

SELECT o.id_serie, o.fecha
FROM observaciones AS o
LEFT JOIN series AS s
    ON o.id_serie = s.id_serie
WHERE s.id_serie IS NULL;

SELECT s.id_serie
FROM series AS s
LEFT JOIN temas AS t
    ON s.id_tema = t.id_tema
WHERE t.id_tema IS NULL;

PRAGMA foreign_key_check;
