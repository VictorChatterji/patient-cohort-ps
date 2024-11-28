import database
import sqlite3

# Objective: To assess the association between the use of specific medications (e.g., acetaminophen and lorazepam) and patient outcomes such as length of hospital stay and discharge location among patients diagnosed with sepsis and inflammatory conditions.

cohort1 = """
CREATE TABLE cohort_acetaminophen AS
SELECT subject_id, hadm_id, admittime, dischtime, drug, discharge_location, anchor_age, icd_code, long_title, gender
FROM patients_final
WHERE drug LIKE '%acetaminophen%'
"""

result1 = database.conn.execute(cohort1).fetchall()

cohort2 ="""
CREATE TABLE IF NOT EXISTS cohort_lorazepam AS
SELECT subject_id, hadm_id, admittime, dischtime, drug, discharge_location, anchor_age, icd_code, long_title, gender
FROM patients_final
WHERE drug LIKE '%Lorazepam%'
"""

result2 = database.conn.execute(cohort2).fetchall()

cohort3 ="""
CREATE TABLE IF NOT EXISTS cohort_atorvastatin AS
SELECT subject_id, hadm_id, admittime, dischtime, drug, discharge_location, anchor_age, icd_code, long_title, gender
FROM patients_final
WHERE drug LIKE '%Atorvastatin%'
"""

result3 = database.conn.execute(cohort3).fetchall()


los = """
CREATE TABLE IF NOT EXISTS cohort_length_of_stay AS
SELECT
    subject_id,
    hadm_id,
    admittime,
    dischtime,
    julianday(dischtime) - julianday(admittime) AS length_of_stay
FROM
    patients_final
WHERE
    hadm_id IN (SELECT hadm_id FROM cohort_acetaminophen
                UNION ALL
                SELECT hadm_id FROM cohort_lorazepam
                UNION ALL
                SELECT hadm_id FROM cohort_atorvastatin);

"""

result4 = database.conn.execute(los).fetchall()

discharge_location = """
CREATE TABLE IF NOT EXISTS cohort_discharge_location AS
SELECT
    subject_id,
    hadm_id,
    discharge_location
FROM
    patients_final
WHERE
    hadm_id IN (SELECT hadm_id FROM cohort_acetaminophen
                UNION ALL
                SELECT hadm_id FROM cohort_lorazepam
                UNION ALL
                SELECT hadm_id FROM cohort_atorvastatin);

"""

result5 = database.conn.execute(discharge_location).fetchall()


cohort_final = """
CREATE TABLE IF NOT EXISTS cohort_final AS
SELECT 
    m.subject_id,
    m.hadm_id,
    m.drug,
    m.anchor_age,
    m.icd_code,
    m.long_title,
    m.admittime,
    m.dischtime,
    m.gender,
    los.length_of_stay,
    dl.discharge_location
FROM 
    (SELECT * FROM cohort_acetaminophen
     UNION ALL
     SELECT * FROM cohort_lorazepam
     UNION ALL
     SELECT * FROM cohort_atorvastatin) m
JOIN cohort_length_of_stay los
    ON m.hadm_id = los.hadm_id
JOIN cohort_discharge_location dl
    ON m.hadm_id = dl.hadm_id;

"""

result6 = database.conn.execute(cohort_final).fetchall()


cohort_filtered = """
CREATE TABLE IF NOT EXISTS cohort_filtered AS
SELECT * 
FROM cohort_final
WHERE icd_code IN ('0389', 'L03115')
  AND length_of_stay >= 1; 
"""
result7 = database.conn.execute(cohort_filtered).fetchall()