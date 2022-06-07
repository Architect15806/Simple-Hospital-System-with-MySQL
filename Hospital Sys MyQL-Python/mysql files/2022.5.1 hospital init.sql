USE hospital;

CALL hospital_table_init()

# 医生表
DROP TABLE IF EXISTS doctors;
CREATE TABLE doctors(
dno VARCHAR(16) PRIMARY KEY,	# 医生编号
dname VARCHAR(16) NOT NULL,		# 医生姓名
dsex VARCHAR(2),							# 医生性别
dbirth INT,										# 医生出生年份
ddept VARCHAR(16),						# 医生科室
dlevel VARCHAR(16)						# 医生职称（住院医师、主治医师、副主任医师、主任医师）
)DEFAULT CHARSET=utf8;

# 护士表
DROP TABLE IF EXISTS nurses;
CREATE TABLE nurses(
nno VARCHAR(16) PRIMARY KEY,	# 护士编号
nname VARCHAR(16) NOT NULL,		# 护士姓名
nsex VARCHAR(2),							# 护士性别
nbirth INT,										# 护士出生年份
ndept VARCHAR(16),						# 护士科室
nlevel VARCHAR(16)						# 护士职称（护士、护师、主管护师、副主任护师、主任护师）
)DEFAULT CHARSET=utf8;

# 科室表（只读）
DROP TABLE IF EXISTS medic_departments;
CREATE TABLE medic_departments(
mdno INT PRIMARY KEY,	# 科室编号
mdname VARCHAR(16) NOT NULL		# 科室名称
)DEFAULT CHARSET=utf8;


# 医生职称表（只读）
DROP TABLE IF EXISTS doctor_level;
CREATE TABLE doctor_level(
dlno INT PRIMARY KEY,	# 医生职称编号
dlname VARCHAR(16) NOT NULL		# 医生职称名称
)DEFAULT CHARSET=utf8;

# 护士职称表（只读）
DROP TABLE IF EXISTS nurse_level;
CREATE TABLE nurse_level(
nlno INT PRIMARY KEY,					# 护士职称编号
nlname VARCHAR(16) NOT NULL,		# 护士职称名称
nlprice DOUBLE
)DEFAULT CHARSET=utf8;

# 行政级别表（只读）
DROP TABLE IF EXISTS admin_level;
CREATE TABLE admin_level(
alno INT PRIMARY KEY,	# 医生职称编号
alname VARCHAR(16) NOT NULL		# 医生职称名称
)DEFAULT CHARSET=utf8;


# 病患表
DROP TABLE IF EXISTS patients;
CREATE TABLE patients(
pno VARCHAR(16) PRIMARY KEY,	# 病患编号
pname VARCHAR(16) NOT NULL,		# 病患姓名
psex VARCHAR(2),							# 病患性别
pbirth INT,										# 病患出生年份
paddress VARCHAR(64),					# 病患住址
pdate DATE										# 病患入院时间
)DEFAULT CHARSET=utf8;

-- INSERT INTO patients VALUES
-- ('11223', '刘干', '男', 1979, '华中科技大学', STR_TO_DATE('12-3-1999','%m-%d-%Y'));


# 医患关系表
DROP TABLE IF EXISTS dp_rel;
CREATE TABLE dp_rel(
dpno VARCHAR(16) PRIMARY KEY,		# 诊断编号
dno VARCHAR(16) NOT NULL,				# 医生编号（外键）
pno VARCHAR(16) NOT NULL,				# 病患编号（外键）
illness VARCHAR(16),						# 诊断结果
dcost DOUBLE,										# 药品费用（计算）
dpcost DOUBLE										# 诊断费用
)DEFAULT CHARSET=utf8;

# 药品表
DROP TABLE IF EXISTS drugs;
CREATE TABLE drugs(
dno VARCHAR(16) PRIMARY KEY,	# 药品编号
dname VARCHAR(16) NOT NULL,		# 药品名称
dprice DOUBLE,								# 药品价格
dstorage INT
)DEFAULT CHARSET=utf8;

# 开药表
DROP TABLE IF EXISTS drug_sell;
CREATE TABLE drug_sell(
dsno VARCHAR(16) PRIMARY KEY,	# 开药单号
dno VARCHAR(16),							# 药品编号
dnum int,											# 药品数量
dpno VARCHAR(16)							# 诊断编号（外键）
)DEFAULT CHARSET=utf8;

# 住院关系表
DROP TABLE IF EXISTS host_rel;									#注：本表里的均未出院
CREATE TABLE dp_rel(
hno VARCHAR(16) PRIMARY KEY,		# 住院编号
nno VARCHAR(16) NOT NULL,				# 护士编号（外键）
pno VARCHAR(16) NOT NULL,				# 病患编号（外键）
bno VARCHAR(16) NOT NULL,				# 病床编号（外键）
hdate DATE											# 住院起始时间
)DEFAULT CHARSET=utf8;

# 病床表
DROP TABLE IF EXISTS beds;
CREATE TABLE beds(
bno VARCHAR(16) PRIMARY KEY,	# 病床编号
bprice DOUBLE									# 病床价格
)DEFAULT CHARSET=utf8;


/* 废案

# 行政表
DROP TABLE IF EXISTS administrators;
CREATE TABLE administrators(
ano VARCHAR(16) PRIMARY KEY,	# 行政编号
aname VARCHAR(16) NOT NULL,		# 行政姓名
asex VARCHAR(2),							# 行政性别
abirth INT,										# 行政出生年份
adept VARCHAR(16),						# 行政单位（院务处，政治处，医务处，财务处，人事科，医保科，老干科）
alevel VARCHAR(16)						# 行政级别（处级正职、处级副职、科级正职、科级副职）
)DEFAULT CHARSET=utf8;

# 费用结算表
DROP TABLE IF EXISTS charges;
CREATE TABLE charges(
pno VARCHAR(16) PRIMARY KEY,	# 病患编号
cdate DATE, 									# 查询日期
charge DOUBLE									# 总价格（诊断费用、药品费用）
)DEFAULT CHARSET=utf8;

# 行政单位表（只读）
DROP TABLE IF EXISTS admin_departments;
CREATE TABLE admin_departments(
adno INT PRIMARY KEY,	# 行政单位编号
adname VARCHAR(16) NOT NULL		# 行政单位名称
)DEFAULT CHARSET=utf8;
*/