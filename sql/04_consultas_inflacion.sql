-- ============================================================
-- HITO 2: MONITOR DE COYUNTURA E INFLACIÓN EN CHILE
-- Ciencia de Datos para Economia
--

-- Consulta 01: Últimas observaciones de las series de precios
SELECT
    s.nombre AS indicador,
    t.tema AS categoria,
    o.fecha,
    o.valor,
    s.unidad
FROM observaciones o
JOIN series s
    ON o.id_serie = s.id_serie
JOIN temas t
    ON s.id_tema = t.id_tema
WHERE t.tema = 'Precios'
    AND o.fecha = (
        SELECT MAX(o2.fecha)
        FROM observaciones o2
        WHERE o2.id_serie = o.id_serie)
ORDER BY s.nombre;



-- Consulta 02: Promedio anual de la inflación interanual en Chile
SELECT
    strftime('%Y', o.fecha) AS anio,
    ROUND(AVG(o.valor), 2) AS inflacion_promedio,
    COUNT(*) AS meses_observados
FROM observaciones o
JOIN series s
    ON o.id_serie = s.id_serie
WHERE s.id_serie = 'F074.IPC.V12.Z.EP23.C.M'
GROUP BY strftime('%Y', o.fecha)
ORDER BY anio;



-- Consulta 03: Inflación interanual transable y no transable
WITH variaciones AS (
    SELECT
        s.nombre AS indicador,
        o.fecha,
        o.valor AS indice,
        LAG(o.valor, 12) OVER (
            PARTITION BY o.id_serie
            ORDER BY o.fecha
        ) AS indice_12m_atras
    FROM observaciones o
    JOIN series s
        ON o.id_serie = s.id_serie
    WHERE s.id_serie IN (
        'F074.IPCT.IND.Z.EP23.Z.M',
        'F074.IPCN.IND.Z.EP23.Z.M'))
SELECT
    indicador,
    fecha,
    ROUND(
        (indice / NULLIF(indice_12m_atras, 0) - 1) * 100, 2) AS inflacion_interanual
FROM variaciones
WHERE indice_12m_atras IS NOT NULL
ORDER BY fecha, indicador;



-- Consulta 04: Tipo de cambio y precio del petróleo
-- Calculamos el promedio mensual y la variación interanual

WITH datos_mensuales AS (
    SELECT o.id_serie, date(o.fecha, 'start of month') AS fecha, AVG(o.valor) AS valor_mensual
    FROM observaciones o
    WHERE o.id_serie IN (
        'F073.TCO.PRE.Z.D',
        'F019.PPB.PRE.41AB.M')
    GROUP BY o.id_serie, date(o.fecha, 'start of month')),

variaciones AS (
    SELECT id_serie, fecha, valor_mensual,
        LAG(valor_mensual, 12) OVER (
            PARTITION BY id_serie
            ORDER BY fecha) AS valor_12m_atras
    FROM datos_mensuales)

SELECT id_serie, fecha, 100.0 * (valor_mensual / NULLIF(valor_12m_atras, 0) - 1) AS variacion_anual
FROM variaciones
WHERE valor_12m_atras IS NOT NULL
ORDER BY fecha, id_serie;