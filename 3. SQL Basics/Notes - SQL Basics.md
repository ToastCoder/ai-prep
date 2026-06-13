### About SQL

SQL (Structured Query Language) is a language used to interact with relational databases.

SQL is used to
* Retrieve Data
* Insert Data
* Update Data
* Delete Data
* Create and modify database structures

Sample Table: `employees`

| id  | name    | salary |
| --- | ------- | ------ |
| 1   | John    | 50000  |
| 2   | Alice   | 70000  |
| 3   | Bob     | 60000  |
| 4   | Charlie | 45000  |
#### `SELECT` statement

The `SELECT` statement is used to retrieve data from the table.

Syntax:

```SQL
SELECT column_name
FROM table_name;
```

Example:

This below query selects all the columns from the table `employees`

```SQL
SELECT *
from employees;
```

#### Selecting specific columns

```SQL
SELECT name,salary
FROM employees;
```

#### `WHERE` clause

The `WHERE` clause is used to filter rows based on a condition.

Syntax:

```SQL
SELECT column_name
FROM table_name
WHERE condition;
```

For example, salary greater than 55000
Query:

```SQL
SELECT *
FROM employees
where salary > 55000;
```

Output:

| id  | name  | salary |
| --- | ----- | ------ |
| 2   | Alice | 70000  |
| 3   | Bob   | 60000  |

### Comparison Operators

|Operator|Meaning|
|---|---|
|=|Equal to|
|!=|Not equal to|
|>|Greater than|
|<|Less than|
|>=|Greater than or equal to|
|<=|Less than or equal to|

#### `ORDER BY` statement

The `ORDER BY` clause is used to sort query results.

Syntax:

```SQL
SELECT column_name
FROM table_name
ORDER BY column_name;
```

By default, it follows ascending order. 

Example:

```SQL
SELECT *
FROM employees
ORDER BY salary;
```

|id|name|salary|
|---|---|---|
|4|Charlie|45000|
|1|John|50000|
|3|Bob|60000|
|2|Alice|70000|
Rows are sorted from the smallest to largest salary.

**Descending Order**
Example

```SQL
SELECT *
FROM employees
ORDER BY salary DESC;
```

|id|name|salary|
|---|---|---|
|2|Alice|70000|
|3|Bob|60000|
|1|John|50000|
|4|Charlie|45000|
`DESC` sorts from largest to smallest. `ASC` can be used explicitly for sorting in ascending order.

#### `LIMIT` statement

The `LIMIT` clause restricts the number of rows returned. 

Syntax:

```SQL
SELECT *
FROM table_name
LIMIT n;
```

Example:

```SQL
SELECT *
FROM employees
LIMIT 2;
```

|id|name|salary|
|---|---|---|
|1|John|50000|
|2|Alice|70000|

**Top Highest Salary**
Query:

```SQL
SELECT *
FROM employees
ORDER BY salary DESC
LIMIT 1;
```

|id|name|salary|
|---|---|---|
|2|Alice|70000|
Explanation:
1. Sort salaries descending 
2. Return only the first row.

#### `DISTINCT` statement

The `DISTINCT` keyword removes duplicate values.

Sample Table:

|id|department|
|---|---|
|1|HR|
|2|IT|
|3|HR|
|4|Finance|
|5|IT|
#### Without `DISTINCT`:

```SQL
SELECT department
FROM employees;
```

Output:

```
HR
IT
HR
Finance
IT
```

#### With `DISTINCT`:

```SQL
SELECT DISTINCT department
FROM employees;
```

Output:

```
HR
IT
Finance
```

Duplicate values are removed.

#### SQL Query Execution Order

While reading queries, think in this order.

```SQL
SELECT *
FROM employees
WHERE salary >= 50000
ORDER BY salary DESC
LIMIT 3;
```

Execution Flow:

```
1. FROM employees
2. WHERE salary >= 50000
3. ORDER BY salary DESC
4. LIMIT 3
5. SELECT *
```
#### `COUNT()`

Returns the number of rows.

Example, for a table `employees`

|id|name|department|salary|
|---|---|---|---|
|1|John|IT|50000|
|2|Alice|HR|70000|
|3|Bob|IT|60000|
|4|Charlie|Finance|45000|
|5|David|IT|80000|

```SQL
SELECT COUNT(*)
FROM employees;
```

Output:

```
5
```

**Example: Count Employees in IT**

```SQL
SELECT COUNT(*)
FROM employees
WHERE department = 'IT';
```

Output

```
3
```

#### `SUM()`

Returns the total of a numeric column.

```SQL
SELECT SUM(salary)
FROM employees;
```

Output

```
305000
```

#### `AVG()`

Returns the average value.

```SQL
SELECT AVG(salary)
FROM employees;
```

Output

```
61000
```

#### `MIN()`

Returns the smallest value.

```SQL
SELECT MIN(salary)
FROM employees;
```

Output

```
45000
```

#### `MAX()`

Returns the largest value.

```SQL
SELECT MAX(salary)
FROM employees;
```

Output

```
80000
```

#### Using Multiple Aggregate Functions

```SQL
SELECT
	COUNT(*) AS total_employees,
	AVG(salary) AS avg_salary,
	MIN(salary) AS min_salary,
	MAX(salary) AS max_salary
FROM employees;
```

Output:

|total_employees|avg_salary|min_salary|max_salary|
|---|---|---|---|
|5|61000|45000|80000|

#### Aliases `AS`

Aliases rename columns in the output.

**Without Alias**

```SQL
SELECT AVG(salary)
FROM employees;
```

Output column: `AVG(salary)`

**With Alias**

```SQL
SELECT AVG(salary) as average_salary
FROM employees;
```

Output column: `average_salary`

#### `GROUP BY`

`GROUP BY` allows SQL to how to create seperate groups.

Syntax:

```SQL
SELECT column_name, aggregate_function(column_name)
FROM table_name
GROUP BY column_name;
```

For example for a table

|id|name|department|salary|
|---|---|---|---|
|1|John|IT|50000|
|2|Alice|HR|70000|
|3|Bob|IT|60000|
|4|Charlie|Finance|45000|
|5|David|IT|80000|
if we want an average salary per department,

```SQL
SELECT department, AVG(salary)
FROM employees
GROUP BY department;
```

How `GROUP BY` works

Step 1:

```
IT:
50000
60000
80000

HR:
70000

Finance:
45000
```

Step 2:

Apply `AVG(salary)`

Applies average function per department.

Step 3:

Return one row per group.

#### `HAVING`

`HAVING` filters groups after grouping has occured.

#### Execution Order

```
FROM
WHERE
GROUP BY
HAVING
SELECT
ORDER BY
LIMIT
```

`WHERE` - filters rows
`HAVING` - filters groups

Example:

Find departments whose average salary is greater than 60000

```SQL
SELECT department, AVG(salary)
FROM employees
GROUP BY department
HAVING AVG(salary) > 60000;
```

Output:

|department|AVG(salary)|
|---|---|
|IT|63333.33|
|HR|70000|

