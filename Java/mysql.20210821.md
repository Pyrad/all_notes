### SQL99语法连接查询

#### 语法

```mysql
SELECT 查询列表
FROM 表 AS 别名 【连接类型（ INNER/LEFT OUTER/RIGHT OUTER ）】
JOIN 表1 AS 别名1 ON 连接条件1
JOIN 表2 AS 别名2 ON 连接条件2
...
【 WHERE 分组前筛选条件 】
【 GROUP BY 分组 】
【 HAVING 分组后筛选条件 】
【 ORDER BY 排序列表 】
```

#### SQL92 vs. SQL99

- 功能：**SQL99**支持较多
- 可读性：**SQL99**实现连接条件和筛选条件的分离，可读性较高

结论：推荐使用**SQL99**

#### 分类

- **内连接**：```INNER```
- **外连接**
  - 左外连接```LEFT OUTER```
  - 右外连接```RIGHT OUTER```
  - 全外连接```FULL OUTER```
- **交叉连接**：```CROSS```



#### 内连接

##### 语法

```mysql
SELECT 查询列表
FROM 表 AS 别名 INNER
JOIN 表1 AS 别名1 ON 连接条件1
JOIN 表2 AS 别名2 ON 连接条件2
JOIN 表3 AS 别名3 ON 连接条件3
【 WHERE 分组前筛选条件 】
【 GROUP BY 分组 】
【 HAVING 分组后筛选条件 】
【 ORDER BY 排序列表 】
```

##### 分类

- 等值连接
- 非等值连接
- 自连接

##### 特点

- 可添加排序、分组和筛选
- ```INNER```可以省略
- 筛选条件放在```WHERE```后面，连接条件放在```ON```后面，提高分离性，便于阅读
- ```INNER JOIN```连接和SQL92语法中的等值连接效果是一样的，都是查询多表的交集



##### 等值连接

- 查询员工名、部门名

```mysql
SELECT E.first_name, D.department_name
FROM employees AS E
INNER JOIN departments AS D
ON E.department_id = D.department_id;
```

- 查询名字中包含e的员工名和工种名（添加筛选）

```mysql
SELECT E.first_name, J.job_title
FROM employees AS E
INNER JOIN jobs AS J
ON E.job_id = J.job_id
WHERE E.first_name LIKE '%e%';
```

- 查询部门个数>3的城市名和部门个数，（添加分组+筛选）

```mysql
SELECT L.city, COUNT(*) AS DepNum
FROM departments AS D
INNER JOIN locations AS L
ON D.location_id = L.location_id
GROUP BY L.city
HAVING DepNum > 3;
```

- 查询哪个部门的员工个数>3的部门名和员工个数，并按个数降序（添加排序）

```mysql
SELECT D.department_id, D.department_name, COUNT(*) AS EmpNum
FROM employees AS E
INNER JOIN departments AS D
ON E.department_id = D.department_id
GROUP BY D.department_id
HAVING EmpNum > 3
ORDER BY EmpNum DESC;
```

- 查询员工名、部门名、工种名，并按部门名降序（添加三表连接）

```mysql
SELECT E.first_name, D.department_name, J.job_title
FROM employees AS E
INNER JOIN departments AS D ON E.department_id = D.department_id
INNER JOIN jobs AS J ON E.job_id = J.job_id
ORDER BY D.department_name DESC;
```



##### 非等值连接

- 查询员工的工资级别

```mysql
SELECT E.first_name, E.salary, JG.grade_level
FROM employees AS E
INNER JOIN job_grades AS JG
ON E.salary BETWEEN JG.lowest_sal AND JG.highest_sal;
```

- 查询工资级别的个数>20的个数，并且按工资级别降序

```mysql
SELECT E.job_id, JG.grade_level, COUNT(*) AS JobGradeNum
FROM employees AS E
INNER JOIN job_grades AS JG
ON E.salary BETWEEN JG.lowest_sal AND JG.highest_sal
GROUP BY JG.grade_level
HAVING JobGradeNum > 20;
```



##### 自连接

- 查询员工的名字、上级的名字

```mysql
SELECT E.first_name AS Ename, M.first_name AS Mname
FROM employees AS E
INNER JOIN employees AS M
ON E.manager_id = M.employee_id;
```

- 查询姓名中包含字符k的员工的名字、上级的名字

```mysql
SELECT E.first_name AS Ename, M.first_name AS Mname
FROM employees AS E
INNER JOIN employees AS M
ON E.manager_id = M.employee_id
WHERE E.first_name LIKE '%k%';
```



#### 外连接

##### 应用

查询一个表中有，另一个表没有的记录

##### 特点

- **外连接**查询结果 = **内连接**结果 + **主表**中有而**从表**没有的记录

  外连接的查询结果包括**主表**中的所有记录

  如果**从表**中有和它匹配的，则显示匹配的值

  如果**从表**中没有和它匹配的，则显示```NULL```

- **左外连接**：```LEFT JOIN```**左边**的是**主表**

  **右外连接**：```RIGHTJOIN```**右边**的是**主表**

- **左外**和**右外**交换两个表的顺序，可以实现**同样**的效果 

- **全外连接** = **内连接**的结果 + 表1中有但表2没有的 + 表2中有但表1没有的

  **注意：MySQL不支持全外连接**



##### 示例

- 查询男朋友 不在男神表的的女神名

```mysql
SELECT BE.name, BO.boyName
FROM beauty AS BE
LEFT OUTER JOIN boys AS BO
ON BE.boyfriend_id = BO.id
WHERE BO.boyName IS NULL;
```

- 查询哪个部门没有员工

```mysql
# With LEFT JOIN
SELECT D.department_id, D.department_name
FROM departments AS D
LEFT JOIN employees AS E
ON D.department_id = E.department_id
WHERE E.department_id IS NULL;

# With RIGHT JOIN
SELECT D.department_id, D.department_name
FROM employees AS E
RIGHT JOIN departments AS D
ON D.department_id = E.department_id
WHERE E.department_id IS NULL;
```

- 全外连接示例（**MySQL不支持全外连接**）

```mysql
SELECT BE.*, BO.*
FROM beauty AS BE
FULL OUTER JOIN boys AS BO
ON BE.boyfriend_id = BO.id
```

- 交叉连接示例（就是笛卡尔积）

```mysql
SELECT BE.*, BO.*
FROM beauty AS BE
CROSS JOIN boys AS BO;
```





### 分页查询

#### 应用场景

当要显示的数据，一页显示不全，需要**分页提交**SQL请求

#### 语法

```mysql
SELECT 查询列表
FROM 表 AS 别名 【连接类型（ INNER/LEFT OUTER/RIGHT OUTER ）】
JOIN 表1 AS 别名1 ON 连接条件1
JOIN 表2 AS 别名2 ON 连接条件2
...
【 WHERE 分组前筛选条件 】
【 GROUP BY 分组 】
【 HAVING 分组后筛选条件 】
【 ORDER BY 排序列表 】
【 LIMIT [offset, ] size 】
```

- **offset**：要显示条目的起始索引（起始索引从0开始）
- **size**：要显示的条目个数

#### 特点

- ```LIMIT```语句放在查询语句的最后

- 如果要显示的页数是 page，每页的条目数size

  ```mysql
  SELECT 查询列表
  FROM 表
  LIMIT (page-1)*size, size;
  ```

#### 示例

- 查询前五条员工信息

```mysql
SELECT *
FROM employees
LIMIT 0, 5;

# 如果起始索引是0，那么可以把这个offset省略，直接跟上后面的size（条目数）
SELECT *
FROM employees
LIMIT 5;
```

- 查询第11条至第25条

```mysql
SELECT *
FROM employees
LIMIT 11, 15;
```

- 有奖金的员工信息，并且工资较高的前10名显示出来

```mysql
SELECT *
FROM employees
WHERE commission_pct IS NOT NULL
ORDER BY salary DESC
LIMIT 10;
```



### 子查询

#### 含义

出现在其他语句中的```SELECT```语句，称为**子查询**或**内查询**

外部的查询语句，称为**主查询**或**外查询**

#### 分类

##### 按子查询出现的位置

- ```SELECT```后面：只支持**标量子查询**
- ```FROM```后面：支持**表子查询**
- ```WHERE```或```HAVING```后面：支持**标量子查询**（单行单列）、**列子查询**（多行）以及**行子查询**（多列）
- ```EXISTS```后面：支持**表子查询**

##### 按结果集的行列数不同

- **标量子查询**（结果集只有**一行一列**）
- **列子查询**（结果集只有**一列多行**）
- **行子查询**（结果集有**一行多列**）
- **表子查询**（结果集一般为**多行多列**）

#### ```WHERE```或```HAVING```后面

##### 支持三种子查询

- **标量子查询**（结果集只有**一行一列**）
- **列子查询**（结果集只有**一列多行**）
- **行子查询**（结果集有**一行多列**）

##### 特点

- 子查询放在小括号里

- 子查询一般放在条件的右侧

- 标量子查询一般搭配单行操作符使用```> < >= <= = <>```

  列子查询一般搭配多行操作符使用```IN ANY/SOME ALL```

- 子查询的执行优先于主查询而执行，主查询的条件用到了子查询的结果

##### 标量子查询示例

- 谁的工资比 Abel 高？

```mysql
SELECT EE.first_name, EE.salary
FROM employees AS EE
WHERE EE.salary > (
  SELECT salary
  FROM employees AS E 
  WHERE E.last_name = 'Abel'
);

/**
 * 注意，主查询里面的employees表也可以命名成同一个别名，
 * 但它和子查询里面的别名是不同的两个
 */
SELECT E.first_name, E.salary
FROM employees AS E
WHERE E.salary > (
  SELECT salary
  FROM employees AS E 
  WHERE E.last_name = 'Abel'
);
```

- 返回job_id与141号员工相同，salary比143号员工多的员工 姓名，job_id 和工资

```mysql
SELECT EE.first_name, EE.job_id, EE.salary
FROM employees AS EE
WHERE EE.job_id = (
  SELECT E.job_id
  FROM employees AS E
  WHERE E.employee_id = 141
) AND EE.salary > (
  SELECT E1.salary
  FROM employees AS E1
  WHERE E1.employee_id = 143
);
```

- 返回公司工资最少的员工的last_name，job_id和salary

```mysql
SELECT E.last_name, E.job_id, E.salary
FROM employees AS E
WHERE E.salary = (SELECT MIN(DISTINCT salary) FROM employees);

## 也可以用LIMIT语句，但是LIMIT只会保留最终一项，但最低工资的人可能有多个
SELECT E.last_name, E.job_id, E.salary
FROM employees AS E
ORDER BY E.salary ASC
LIMIT 1;
```

- 查询最低工资大于50号部门最低工资的部门id和其最低工资

```mysql
# 注意是求每个部门的最低工资 > 50号部门的最低工资
SELECT EE.department_id, MIN(EE.salary) AS MinSal
FROM employees AS EE
GROUP BY EE.department_id
HAVING MinSal > (
  SELECT MIN(E.salary)
  FROM employees AS E
  WHERE E.department_id = 50
)
ORDER BY MinSal ASC;
```



##### 列子查询（多行）示例

- 返回location_id是1400或1700的部门中的所有员工姓名

```mysql
SELECT E.first_name
FROM employees AS E
WHERE E.department_id IN (
  SELECT DISTINCT department_id
  FROM departments
  WHERE location_id IN (1400, 1700)
);

# 或者也可以使用连接查询
SELECT E.first_name, D.location_id
FROM employees AS E
INNER JOIN departments AS D
ON E.department_id = D.department_id
WHERE D.location_id = 1400 OR D.location_id = 1700
```

- 返回其它工种中比job_id为‘IT_PROG’工种任一工资低的员工的员工号、姓名、job_id 以及salary

```mysql
# 注意是ANY的考察，即只要低于其中之一即可
SELECT EE.first_name, EE.last_name, EE.employee_id, EE.job_id, EE.salary
FROM employees AS EE
WHERE EE.salary < ANY (
  SELECT E.salary
  FROM employees AS E
  WHERE E.job_id = 'IT_PROG'
) AND EE.job_id <> 'IT_PROG';
```

返回其它部门中比job_id为‘IT_PROG’部门所有工资都低的员工   的员工号、姓名、job_id 以及salary

```mysql
# 注意是ALL的考察，即只要低于所有的
SELECT EE.first_name, EE.last_name, EE.employee_id, EE.job_id, EE.salary
FROM employees AS EE
WHERE EE.salary < ALL (
  SELECT E.salary
  FROM employees AS E
  WHERE E.job_id = 'IT_PROG'
) AND EE.job_id <> 'IT_PROG';
```







```mysql

```























