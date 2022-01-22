# Write your MySQL query statement below
SELECT SUBQ.DNAME AS DEPARTMENT, EMPLOYEE.NAME AS EMPLOYEE, SUBQ.MAXSA AS SALARY FROM (SELECT DEPARTMENT.ID, DEPARTMENT.NAME AS DNAME, MAX(EMPLOYEE.SALARY) AS MAXSA FROM EMPLOYEE INNER JOIN DEPARTMENT ON EMPLOYEE.DEPARTMENTID=DEPARTMENT.ID GROUP BY EMPLOYEE.DEPARTMENTID) AS SUBQ INNER JOIN EMPLOYEE ON SUBQ.MAXSA=EMPLOYEE.SALARY AND SUBQ.ID=EMPLOYEE.DEPARTMENTID