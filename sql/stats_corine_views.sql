CREATE OR REPLACE VIEW corine.oc_level1 AS
SELECT 
count(*) AS anzahl, 
ROUND(count(*)*100/sum(count(*)) OVER(),2) AS prozent,
oc.clc_code,
label1 
FROM oc.dachli AS oc,
corine.classes_en AS corine
WHERE oc.clc_code = corine.clc_code::int
GROUP BY oc.clc_code, label1
ORDER BY anzahl DESC;

CREATE OR REPLACE VIEW corine.oc_level2 AS
SELECT 
count(*) AS anzahl, 
ROUND(count(*)*100/sum(count(*)) OVER(),2) AS prozent,
oc.clc_code,
label1,label2 
FROM oc.dachli AS oc,
corine.classes_en AS corine
WHERE oc.clc_code = corine.clc_code::int
GROUP BY oc.clc_code, label1, label2
ORDER BY anzahl DESC;


CREATE OR REPLACE VIEW corine.oc_level3 AS
SELECT 
count(*) AS anzahl, 
ROUND(count(*)*100/sum(count(*)) OVER(),2) AS prozent,
oc.clc_code,
label1,label2 
FROM oc.dachli AS oc,
corine.classes_en AS corine
WHERE oc.clc_code = corine.clc_code::int
GROUP BY oc.clc_code, label1, label2
ORDER BY anzahl DESC;
