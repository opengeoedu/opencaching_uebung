ALTER TABLE results.regional_stats
ADD COLUMN IF NOT EXISTS clc_1_bebaut int DEFAULT 0,
ADD COLUMN IF NOT EXISTS clc_2_landw int DEFAULT 0,
ADD COLUMN IF NOT EXISTS clc_3_waldnat int DEFAULT 0,
ADD COLUMN IF NOT EXISTS clc_4_feucht int DEFAULT 0,
ADD COLUMN IF NOT EXISTS clc_5_wasser int DEFAULT 0;

WITH temp AS (
	SELECT
		count(oc.*),
		nuts.id
	FROM oc.dachli AS oc,
	     eurostat.nuts_regionen AS nuts
	WHERE st_contains(nuts.geom,st_transform(oc.location::geometry,3035))
		AND oc.clc_code / 100 = 1
	GROUP BY nuts.id
)
UPDATE results.regional_stats
SET clc_1_bebaut = count
FROM temp
WHERE regional_stats.id = temp.id;


WITH temp AS (
	SELECT
		count(oc.*),
		nuts.id
	FROM oc.dachli AS oc,
	     eurostat.nuts_regionen AS nuts
	WHERE st_contains(nuts.geom,st_transform(oc.location::geometry,3035))
		AND oc.clc_code / 100 = 2
	GROUP BY nuts.id
)
UPDATE results.regional_stats
SET clc_2_landw = count
FROM temp
WHERE regional_stats.id = temp.id;


WITH temp AS (
	SELECT
		count(oc.*),
		nuts.id
	FROM oc.dachli AS oc,
	     eurostat.nuts_regionen AS nuts
	WHERE st_contains(nuts.geom,st_transform(oc.location::geometry,3035))
		AND oc.clc_code / 100 = 3
	GROUP BY nuts.id
)
UPDATE results.regional_stats
SET clc_3_waldnat = count
FROM temp
WHERE regional_stats.id = temp.id;



WITH temp AS (
	SELECT
		count(oc.*),
		nuts.id
	FROM oc.dachli AS oc,
	     eurostat.nuts_regionen AS nuts
	WHERE st_contains(nuts.geom,st_transform(oc.location::geometry,3035))
		AND oc.clc_code / 100 = 4
	GROUP BY nuts.id
)
UPDATE results.regional_stats
SET clc_4_feucht = count
FROM temp
WHERE regional_stats.id = temp.id;



WITH temp AS (
	SELECT
		count(oc.*),
		nuts.id
	FROM oc.dachli AS oc,
	     eurostat.nuts_regionen AS nuts
	WHERE st_contains(nuts.geom,st_transform(oc.location::geometry,3035))
		AND oc.clc_code / 100 = 5
	GROUP BY nuts.id
)
UPDATE results.regional_stats
SET clc_5_wasser = count
FROM temp
WHERE regional_stats.id = temp.id;
