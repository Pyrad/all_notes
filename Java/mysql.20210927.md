# 存储过程

含义：一组预先编译好的SQL语句的集合

优点：

1. 提高代码重用率
2. 简化操作
3. 减少编译次数，减少和服务器的连接次数，提高效率



## 语法

### 定义

```mysql
CREATE PROCEDURE 存储过程名字 (参数列表)
BEGIN
  存储过程体
END
```

### 调用

```mysql
CALL 存储过程名称(实参列表)
```

### 查看

```mysql
SHOW CREATE PROCEDURE 存储过程名称
```

### 删除

```mysql
DROP PROCEDURE 存储过程名称
```



## 注意事项

### 参数列表结构

参数列表包含三部分：**参数模式 + 参数名称 + 参数类型**

例如，

```mysql
IN StuName VARCHAR(20)
```

### 参数模式

| 参数模式关键字 | 含义                                                         |
| -------------- | ------------------------------------------------------------ |
| `IN`           | 参数作为输入（即该参数需要调用方法传入值）                   |
| `OUT`          | 参数作为输出（即该参数可以作为返回值）                       |
| `INOUT`        | 参数既作为输入又作为输出（既该参数既需要传入值，又可以赋予返回值） |

### `BEGIN...END`

- 如果存储过程体中只有一句话，`BEGIN...END`可以省略

- 存储过程中每条`SQL`语句都要加分号

- 存储过程的结尾可以使用`DELIMITER`来设置结束符号，比如

  ```mysql
  # 把'$'符号设置为存储过程的结束符号
  DELIMITER $
  ```



## 使用案例

### 空参列表

- 插入到admin表中5条记录

```mysql
# 定义
DELIMITER $
CREATE PROCEDURE MyP()
BEGIN
  INSERT INTO admin(username, `password`)
  VALUES('john', '00'), ('kevin', '01'), ('rose', '02'), ('jack', '03'), ('tom', '04')
END $

# 调用
CALL MyP()$
```



### 带`IN`模式参数的存储过程

- 创建存储过程，实现根据女神名，查询对应的男神信息

```mysql
# 定义
CREATE PROCEDURE MyP(IN beautyName VARCHAR(20))
BEGIN
  SELECT BO.*
  FROM boys AS BO
  RIGHT OUTER JOIN beauty AS BE
  ON BE.boyfriend_id = BO.id;
END $

# 调用
CALL MyP('柳岩')$
```

- 创建存储过程，实现检查用户是否登录成功

```mysql
# 定义
CREATE PROCEDURE MyP(IN userName VARCHAR(20), IN passwd VARCHAR(20))
BEGIN
  DECLARE res INT DEFAULT 0;
  SELECT COUNT(*) INTO res
  FROM admin
  WHERE admin.username = userName
  AND admin.password = passwd;
  
  SELECT IF ( res > 0, 'Success' : 'Fail');
END $

# 调用
CALL MyP('张飞', '888')$
```



### 带`OUT`模式参数的存储过程

- 根据输入的女神名，返回对应的男神名

```mysql
# 定义
CREATE PROCEDURE MyP(IN beautyName VARCHAR(20), OUT boyName VARCHAR(20))
BEGIN
  SELECT 
  FROM boys AS BO
  RIGHT JOIN beauty AS BE
  ON BO.id = BE.boyfriend_id
  WHERE BE.name = beautyName;
END $

# 调用
SET @BNAME = ''$
CALL MyP('赵敏', BNAME)$
```

- 根据输入的女神名，返回对应的男神名和魅力值

```mysql
# 定义
CREATE PROCEDURE MyP(IN beautyName VARCHAR(20), OUT boyName VARCHAR(20), OUT usercp INT)
BEGIN
  SELECT BO.boyname, BO.usercp INTO boyName, usercp
  FROM boys AS BO
  RIGHT OUTER JOIN beauty AS BE
  ON BE.boyfriend_id = BO.id
  WHERE BE.name = beautyName ;
END $

# 调用
SET @BNAME = ''$
SET @UCP = ''$
CALL MyP('赵敏', @BNAME, @UCP)$
SELECT @BNAME, @UCP $
```



### 带`INOUT`模式参数的存储过程

- 传入`a`和`b`两个值，最终`a`和`b`都翻倍并返回

```mysql
# 定义
CREATE PROCEDURE MyP(INOUT a INT, INOUT b INT)
BEGIN
  SET a = a * 2;
  SEt b = b * 2;
END $

# 调用
SET @m = 10 $
SET @n = 20 $
CALL MyP(@m, @n)$
SELECT @m, @n $
```





# 函数

含义：一组预先编译好的SQL语句的集合

优点：

1. 提高代码重用率
2. 简化操作
3. 减少编译次数，减少和服务器的连接次数，提高效率

函数和存储过程的区别：

|          | 返回值          | 适用场景               |
| -------- | --------------- | ---------------------- |
| 存储过程 | 可以有0个或多个 | 批量插入、批量更新     |
| 函数     | 有且仅有1个     | 处理数据后返回一个结果 |

## 语法

### 创建

```mysql
CREATE FUNCTION 函数名称(参数列表) RETURNS 返回类型
BEGIN
  函数体
END
```

### 调用

```mysql
SELECT 函数名称(实参列表);
```

### 查看

```mysql
SHOW CREATE FUNCTION 函数名称;
```

### 删除

```mysql
DROP FUNCTION 函数名称;
```



## 注意事项

### 参数列表

参数列表包含两部分：**参数名 + 参数类型**

### 函数体

- 必须有`RETURN`语句，如果没有就会报错
- `RETURN`语句如果没有放在函数体的最后也不会报错，但不建议这么做

### `BEGIN...END`

- 如果函数体中只有一句话，`BEGIN...END`可以省略
- 函数体中每条`SQL`语句都要加分号
- 函数体的结尾可以使用`DELIMITER`来设置结束符号（类似存储过程）



## 使用案例

### 无参有返回

- 返回公司的员工个数

```mysql
# 定义
CREATE FUNCTION MyF() RETURNS INT
BEGIN
  DECLARE c INT DEFAULT INT;
  SELECT COUNT(*)
  FROM empolyees;
  RETURN c;
END $

# 返回
SELECT MyF()$
```



### 有参有返回

- 根据员工名，返回对应的工资

```mysql
# 定义
CREATE FUNCTION MyF(empName VARCHAR(20)) RETURNS DOUBLE
BEGIN
  SET @sal = 0;
  SELECT E.salary INTO @sal
  FROM employees AS E
  WHERE E.last_name = empName;
  RETURN @sal;
END $

# 调用
SELECT MyF('k_ing') $
```

- 根据部门名，返回部门的平均工资

```mysql
# 定义
CREATE FUNCTION MyF(deptName VARCHAR(20)) RETURNS DOUBLE
BEGIN
  DECLARE avg_sal DOUBLE DEFAULT 0;
  SELECT AVG(E.salary) INTO avg_sal
  FROM employees AS E
  INNER JOIN departments AS D
  ON D.department_id = E.department_id
  WHERE d.department_name = deptName;
  RETURN avg_sal;
END $
```

- 创建函数，传入两个`FLOAT`，返回二者之和

```mysql
# 定义
CREATE FUNCTION MyF(m FLOAT, n FLOAT) RETURNS FLOAT
BEGIN
  DELCARE res FLOAT DEFAULT 0;
  SET res = m + n;
  RETURN res;
END $

# 调用
SELECT MyF(1, 2)$
```
