import sample_database_config

# Example query: Filter patients aged 50 and above (assuming a table 'patients')
# query = """
# SELECT subject_id
# FROM patients
# WHERE gender = 'F';
# """


# We often need to specify more than one condition. For instance, the following
# query lists the subject_ids whose first or last care unit was a coronary care unit
# (CCU)


# query = """
# SELECT subject_id
# FROM icustays
# WHERE first_careunit = 'Coronary Care Unit (CCU)' OR last_careunit = 'Coronary Care Unit (CCU)';
# """



# Since a patient may have been in several ICUs, the same patient ID sometimes
# appears several times in the result of the previous query. To return only distinct
# rows, use the DISTINCT keyword

# query = """
# SELECT DISTINCT subject_id
# FROM icustays
# WHERE first_careunit = 'Coronary Care Unit (CCU)' OR last_careunit = 'Coronary Care Unit (CCU)';
# """


# To count how many patients there are in the icustays table, combine DISTINCT
# with the COUNT keyword. As you can see, if there is no condition, we simply
# don’t use the keyword WHERE

# query = """
# SELECT COUNT(DISTINCT subject_id) as icu_patients_count
# FROM icustays
# """

# Total number of patients in the dataset
# query="""
# SELECT COUNT(subject_id) as total_patients
# from patients;
# """

# Taking a similar approach, we can count how many patients went through the
# CCU using the query


# query = """
# SELECT COUNT(DISTINCT subject_id) as patients_count
# FROM icustays
# WHERE first_careunit like '%CCU%' OR last_careunit like '%CCU%'
# """

# How many adult patients have gone through CCU

# query="""
# SELECT COUNT(DISTINCT p.subject_id) as adult_patients_ccu
# FROM patients p
# INNER JOIN icustays i
# ON p.subject_id = i.subject_id
# WHERE (i.first_careunit LIKE '%CCU%' OR i.last_careunit LIKE '%CCU%')
# AND p.anchor_age >= 18
# """

# Ranking across rows using a window function

# query="""
# SELECT subject_id, stay_id, intime,
#     RANK() OVER (PARTITION BY subject_id ORDER BY intime ASC) as rank
# FROM icustays;
# """

# query = """
# SELECT pe.itemid, di.label
# FROM procedureevents pe
# INNER JOIN d_items di
# ON pe.itemid = di.itemid
# GROUP BY pe.itemid, di.label
# """

query="""
SELECT *
FROM patients_final
LIMIT 5
"""



result = sample_database_config.conn.execute(query).fetchall()
columns = [desc[0] for desc in sample_database_config.conn.execute(query).description]
print("Query Result:")
for row in result:
    print(dict(zip(columns,row)))

