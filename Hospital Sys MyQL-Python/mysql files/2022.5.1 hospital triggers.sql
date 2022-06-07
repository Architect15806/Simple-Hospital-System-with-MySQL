# 触发器：限制doctor的部门和职称在合适的范围内
DROP TRIGGER IF EXISTS tg_doctor;
DELIMITER //
CREATE TRIGGER tg_doctor BEFORE INSERT ON doctors
FOR EACH ROW
BEGIN
	IF NEW.ddept NOT IN (SELECT mdname FROM medic_departments) THEN
		SIGNAL SQLSTATE '45000'
		SET MESSAGE_TEXT = 'Doctor department illegal';
	ELSEIF NEW.dlevel NOT IN (SELECT dlname FROM doctor_level) THEN
		SIGNAL SQLSTATE '45000'
		SET MESSAGE_TEXT = 'Doctor level illegal';
	END IF;

END;//
DELIMITER ;

# INSERT INTO doctors VALUES ('D2100', 'AAA', '男', 1999, 'aaa', '主治医师');
# SELECT * FROM doctors;

# 触发器：限制nurse的部门和职称在合适的范围内
DROP TRIGGER IF EXISTS tg_nurse;
DELIMITER //
CREATE TRIGGER tg_nurse BEFORE INSERT ON nurses
FOR EACH ROW
BEGIN
	IF NEW.ndept NOT IN (SELECT mdname FROM medic_departments) THEN
		SIGNAL SQLSTATE '45000'
		SET MESSAGE_TEXT = 'Nurse department illegal';
	ELSEIF NEW.nlevel NOT IN (SELECT nlname FROM nurse_level) THEN
		SIGNAL SQLSTATE '45000'
		SET MESSAGE_TEXT = 'Nurse level illegal';
	END IF;

END;//
DELIMITER ;

# INSERT INTO nurses VALUES ('N2100', 'AAA', '男', 1999, '内科', '主治医师');
# SELECT * FROM nurses;

