USE hospital;

# 医生表
INSERT INTO doctors VALUES
('D0001', '章北海', '男', 1997, '内科', '主任医师')
SELECT * FROM doctors


内科、外科、妇科、儿科

DROP TABLE IF EXISTS doctors;
CREATE TABLE doctors(
dno VARCHAR(16) PRIMARY KEY,	# 医生编号
dname VARCHAR(16) NOT NULL,		# 医生姓名
dsex VARCHAR(2),							# 医生性别
dbirth INT,										# 医生出生年份
ddept VARCHAR(16),						# 医生科室
dlevel VARCHAR(16)						# 医生职称（住院医师、主治医师、副主任医师、主任医师）
)DEFAULT CHARSET=utf8;