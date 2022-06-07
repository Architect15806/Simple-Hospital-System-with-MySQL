SELECT max(pno) FROM `patients`

SELECT drugs.dprice AS P, drug_sell.dnum AS N, drugs.dprice * drug_sell.dnum AS TOTAL FROM patients 
LEFT JOIN dp_rel ON patients.pno = dp_rel.pno
LEFT JOIN drug_sell ON	dp_rel.dpno = drug_sell.dpno
LEFT JOIN drugs ON drugs.dno = drug_sell.dno
WHERE patients.pno = 'P0001';

DROP VIEW IF EXISTS drugs_pay_view;
CREATE VIEW drugs_pay_view AS 
SELECT drugs.dprice AS drug_price, 
drug_sell.dnum AS drug_number, 
drugs.dprice * drug_sell.dnum AS total_price, 
patients.pno AS patient_no,
patients.pname AS patient_name
FROM patients
LEFT JOIN dp_rel ON patients.pno = dp_rel.pno
LEFT JOIN drug_sell ON	dp_rel.dpno = drug_sell.dpno
LEFT JOIN drugs ON drugs.dno = drug_sell.dno;

SELECT drug_name, drug_price, drug_number, total_price FROM drugs_pay_view WHERE patient_no = 'P0001'

SELECT sum(total_price) FROM drugs_pay_view WHERE patient_no = 'P0001'

SHOW TABLES