CREATE DATABASE edulab;
CREATE TABLE dataanalyst_ncr
(job_title VARCHAR(255),
experience_required VARCHAR(255),
company_name VARCHAR(255),
link_job_description VARCHAR(255),
keyskills VARCHAR(255),
job_description VARCHAR(255),
salary VARCHAR(255),
Job_Id INT AUTO_INCREMENT PRIMARY KEY,
last_updated_on DATETIME);

CREATE TABLE location_jobs(
  Job_Id INT,
  locn_id INT AUTO_INCREMENT PRIMARY KEY,
  location VARCHAR(255),
  FOREIGN KEY(Job_Id) REFERENCES dataanalyst_ncr(Job_Id));
