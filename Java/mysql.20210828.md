## 联合查询

### 语法定义

```UNION```也叫联合、合并，就是将多条查询语句合并成一个结果

```mysql
查询语句1
UNION
查询语句2
UNION
查询语句3
UNION
...
```

### 应用场景

要查询的结果来自多个表，且多个表没有直接的连接关系，但查询的信息一致的时候

### 特点

- 要求多条查询语句的查询**列数是一致**的
- 要求多条查询语句的查询列的**类型和顺序最好一致**
- ```UNION```关键字默认是去重复的（即把结果中重复的行去掉），如果不想去掉重复的行，可以使用```UNION ALL```

### 示例

- 查询部门编号>90或邮箱包含a的员工信息

```mysql
SELECT * FROM employees AS E
WHERE E.email LIKE '%a%'
UNION
SELECT * FROM employees AS E
WHERE E.department_id > 90;
```

- 查询中国用户中男性的信息以及外国用户中年男性的用户信息

```mysql
SELECT id,cname FROM t_ca WHERE csex='男'
UNION ALL
SELECT t_id,tname FROM t_ua WHERE tGender='male';
```



# DML 数据管理（操作）语言

DML = Data Management Language



## 三大类：增、删、改

- **插入语句**
- **修改语句**
- **删除语句**

注意：操作的对象都是表里面的**一行**或者**多行**



## 插入语句 ```INSERT```

**注意：就是插入一行或者多行的记录**

### 第一种插入方式

```mysql
INSERT INTO 表名(列名1, 列名2, ...) VALUES(值1, 值2, ...)
```

#### 几个要点

- **插入的值的类型要和列的类型一致或者兼容**

```mysql
INSERT INTO beauty(id, NAME, sex, borndate, phone, photo, boyfriend_id)
VALUES(13, 'Aragaki Yui', '女', '1992-05-02', 15210560360, NULL, 3);
```

- **不可为```NULL```的列必须插入值，可以为```NULL```的列有两种办法插入值。**
  - 对于可以为NULL的列，值可以写NULL插入NULL值
  - 对可以为NULL的列，可以省略列名和对应的值NULL，这样默认插入的值就是NULL

```mysql
# 对于可以为NULL的列，值可以写NULL插入NULL值
INSERT INTO beauty(id, NAME, sex, borndate, phone, photo, boyfriend_id)
VALUES(14, '唐艺昕', '女', '1990-4-23', '1898888888', NULL, 2);

# 对可以为NULL的列，可以省略列名和对应的值NULL，这样默认插入的值就是NULL
INSERT INTO beauty(id, NAME, sex, phone)
VALUES(15, '娜扎', '女', '1388888888');
```

- **列的顺序可以调换**

```mysql
INSERT INTO beauty(NAME, sex, id, phone)
VALUES('蒋欣', '女', 16, '15210560360');
```

- **列的个数和值的个数必须一致**

```mysql
INSERT INTO beauty(NAME, sex, id, phone)
VALUES('关晓彤', '女', 17, '110');
```

- **如果插入的时候不写列名，默认就是所有的列名，而且顺序和表中的顺序一致，后面的值也必须都写**

```mysql
INSERT INTO beauty
VALUES(18, 'Riho Yoshioka', '女', '1992-05-07', '15210560360', NULL, 1);
```

- **可以一次插入多行**
  - 注意，```VALUES```只写一次

```mysql
INSERT INTO beauty
VALUES(19, 'Satomi', '女', '1992-05-07', '15210560360', NULL, 2)
, (20, 'TingLiu', '女', '1992-05-07', '15210560360', NULL, 2)
, (21, 'Liudi', '女', '1992-05-07', '15210560360', NULL, 3);
```

- 可以利用子查询来插入子查询的结果

```mysql
INSERT INTO beauty(id, NAME, phone)
SELECT 23,'宋茜','11809866';

INSERT INTO beauty(id,NAME,phone)
SELECT id, boyname, '1234567'
FROM boys WHERE id<3;
```



### 第二种插入方式

```mysql
INSERT INTO 表名 SET 列名1=值1, 列名2=值2, ...
```

例子

```mysql
INSERT INTO beauty
SET id=22, NAME='刘涛', phone='999';
```



### 两种插入方式比较

- 第一种插入方式支持一次插入多行，第二种插入方式不支持
- 第一种插入方式支持子查询，第二种不支持





## 修改语句 ```UPDATE```

**注意：就是更新一行或者多行的记录**

### 语法

- 修改单表的记录

```mysql
UPDATE 表名
SET 列名1 = 值1, 列名2 = 值2, ...
WHERE 筛选条件
```

- 修改多表的记录

```mysql
# SQL99
UPDATE 表名1 AS 别名1
[INNER | LEFT | RIGHT JOIN] 表2 AS 别名2
ON 连接条件
SET 列名1 = 值1, 列名2 = 值2, ...
WHERE 筛选条件

# SQL92
UPDATE 表1 AS 别名1, 表2 AS 别名2
SET 列名1 = 值1, 列名2 = 值2, ...
WHERE 连接条件
AND 筛选条件
```



### 示例 - 修改单表

- 修改beauty表中姓唐的女神的电话为13899888899

```mysql
UPDATE beauty AS B
SET phone='13899888899'
WHERE B.name LIKE '唐%';
```

- 修改boys表中id号为2的名称为张飞，魅力值 10

```mysql
UPDATE boys
SET boyName = '张飞', userCP = 10
WHERE id = 2;
```



### 示例 - 修改多表

- 修改张无忌的女朋友的手机号为114，张无忌的魅力值为1000

```mysql
UPDATE beauty AS BE
INNER JOIN boys AS BO
ON BE.boyfriend_id = BO.id
SET BE.phone = '114', BO.userCP = 1000
WHERE BO.boyName = '张无忌';
```

- 修改没有男朋友的女神的男朋友编号都为2号

```mysql
UPDATE beauty AS BE
LEFT OUTER JOIN boys AS BO
ON BE.boyfriend_id = BO.id
SET BE.boyfriend_id = 2
WHERE BO.id IS NULL;
```



## 删除语句 ```DELETE```

**注意：就是删除一行或者多行的记录**



### 语法

#### 方式一：```DELETE```

- 单表中记录的删除

```mysql
DELETE FROM 表名 WHERE 筛选条件
```

- 多表中记录的删除

```mysql
DELETE 别名1, 别名2, 别名3, ...
FROM 表1 AS 别名1
[INNER | LEFT | RIGHT JOIN] 表2 AS 别名2 ON 连接条件
[INNER | LEFT | RIGHT JOIN] 表3 AS 别名3 ON 连接条件
WHERE 筛选条件
```

##### 示例

- 删除单表中的记录：删除手机号以9结尾的女神信息

```mysql
DELETE FROM beauty
WHERE phone LIKE '%9';
```

- 删除多表中的记录：删除张无忌的女朋友的信息





#### 方式二：```TRUNCATE```

```mysql
TRUNCATE TABLE 表名;
```



#### 示例



































# DDL 数据定义语言

DDL = Data Definition Language



# TCL 事务控制语言

TCL = Transaction Control Language
