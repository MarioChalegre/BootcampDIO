use company;
show tables;

-- Número de empregados por departamento e localidade 
create view Qtd_employee_dept_view as
	select count(e.ssn) as Qtde_employee, Dname from employee as e
		left join departament as d on e.Dno = d.Dnumber
        group by Dname
        order by Qtde_employee asc;
        
select * from Qtd_employee_dept_view;

-- Lista de departamentos e seus gerentes
create view List_dept_mgr_view as
	select Dname, concat(Fname,' ', Minit,' ', Lname) as Mgr_name from employee as e
		inner join departament as d on e.ssn = d.Mgr_ssn
		order by Dname;

select * from List_dept_mgr_view;

-- Projetos com maior número de empregados (ex: por ordenação desc) 
create view Qtde_employee_project_view as
	select p.Pname, Dname, count(e.ssn) as Qtde_employee from employee as e
		inner join departament as d on e.Dno = d.Dnumber
        inner join project as p on d.Dnumber = p.Dnum
        group by Pname 
        order by Qtde_employee desc;

select * from Qtde_employee_project_view;

-- Lista de projetos, departamentos e gerentes 
create view List_project_dept_mgr as
	select p.Pname, Dname, concat(Fname,' ', Minit,' ', Lname) as Mgr_Name from employee as e
		inner join departament as d on e.Ssn = d.Mgr_ssn
        inner join project as p on d.Dnumber = p.Dnum;
    
select * from List_project_dept_mgr;
    
    
 -- Quais empregados possuem dependentes e se são gerentes 
create view List_employee_dependent_dept_view as 
	select dp.dependent_name, dp.Relationship, concat(Fname,' ', Minit,' ', Lname) as Employee_name, CASE WHEN e.Ssn = d.Mgr_ssn THEN 'TRUE' ELSE 'FALSE' END AS Mgr from employee as e
		left join departament as d on e.Ssn = d.Mgr_ssn
        inner join dependent as dp on e.Ssn = dp.Essn;

select * from List_employee_dependent_dept_view;
        
