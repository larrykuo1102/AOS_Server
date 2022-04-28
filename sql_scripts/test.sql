-- INSERT INTO awan_project.symptoms (symptom_name)
-- VALUES ("痛風");

INSERT INTO awan_project.departments (symptoms_id, department)
VALUES (485, "風濕免疫科"), (485, "新陳代謝科"), (485, "家醫科"), (485, "骨科");

-- SELECT * FROM awan_project.symptoms
-- INNER JOIN awan_project.departments
-- ON awan_project.symptoms.id = awan_project.departments.symptoms_id 
-- WHERE symptom_name = "頭痛";