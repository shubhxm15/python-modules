CREATE DATABASE IF NOT EXISTS basketball_tournament;
USE basketball_tournament;

CREATE TABLE eligibility_proforma (
    sr_no INT PRIMARY KEY,
    name VARCHAR(50),
    fathers_name VARCHAR(50),
    mothers_name VARCHAR(50),
    pu_reg_pupin_number VARCHAR(20),
    date_of_birth DATE,
    board_name VARCHAR(50),
    roll_no VARCHAR(20),
    passing_year INT,
    compartment_in_10_2 ENUM('YES', 'NO'),
    year_1st_admission_after_10_2 INT,
    present_course VARCHAR(100),
    aadhar_card VARCHAR(20)
);

INSERT INTO eligibility_proforma (sr_no, name, fathers_name, mothers_name, pu_reg_pupin_number, date_of_birth, board_name, roll_no, passing_year, compartment_in_10_2, year_1st_admission_after_10_2, present_course, aadhar_card)
VALUES
(1, 'ADITYA YADAV', 'JASWANT SINGH', 'RAMAN YADAV', '37021000085', '2002-12-19', 'CBSE', '13682155', 2021, 'NO', 2021, 'BE, 4 Year', '548281505033'),
(2, 'SUKHJOT SINGH', 'DEVINDER SINGH', 'RANJIT KAUR', '37021000168', '2004-10-25', 'CBSE', '13698177', 2021, 'NO', 2021, 'BE, 4 Year', '372298820537'),
(3, 'ISHTVEER SINGH BILLING', 'SUKHWINDER SINGH BILLING', 'GURDISH KAUR', '37021000037', '2003-08-19', 'CBSE', '13700176', 2021, 'NO', 2021, 'BE, 4 Year', '397493385762'),
(4, 'MOHD ASHAD', 'MOHD SHAMSAD KHAN', 'AMINA KHATOON', '37022000053', '2004-11-04', 'CBSE', '13619248', 2022, 'NO', 2022, 'BE, 3 Year', '957947509656'),
(5, 'DEEPINDER SINGH', 'HARDEEP SINGH', 'PALVINDER KAUR', '37022001682', '2000-02-08', 'Diploma', NULL, NULL, 'NO', 2022, 'BE, 4 Year', '454632660111'),
(6, 'SHUBHAM SHARMA', 'SAT PAL', 'EISHYA DEVI', '37023000066', '2005-07-15', 'CBSE', '13614182', 2023, 'NO', 2023, 'BE, 4 Year', '536946004547'),
(7, 'SAKSHAM KOHLI', 'SANJEEV KOHLI', 'MADHURI KOHLI', '37022000145', '2004-07-20', 'CBSE', '13502942', 2022, 'NO', 2022, 'BE, 4 Year', '624692907090'),
(8, 'SAMRATH SINGH HANSRAO', 'AMARPREET SINGH', 'SARAVJOT KAUR HANSRAO', '37021000214', '2003-07-02', 'CBSE', '13700221', 2021, 'NO', 2021, 'BE, 4 Year', '541812266762'),
(9, 'RANVIR SEHGAL', 'RAJESH SEHGAL', 'VASUDHA', '37022001185', '2003-04-17', 'AICTE DIPLOMA', '2019-028', 2022, 'NO', 2022, 'BE, 4 Year', '233018836641'),
(10, 'SAHIL MEHMI', 'SARANJIT RAM', 'ANURADHA', '37023000236', '2005-08-17', 'CBSE', NULL, 2023, 'NO', 2023, 'BE, 4 Year', '888508498634'),
(11, 'MANAV BARWAL', 'VIPIN KUMAR BARWAL', 'SONU BARWAL', '37023000222', '2006-03-07', 'CBSE', '13604980', 2023, 'NO', 2023, 'BE, 4 Year', '960591605597'),
(12, 'ROHAN PRATAP SINGH', 'TARSEM SINGH', 'REKHA', '37023000235', '2003-12-19', 'CBSE', '13617623', 2023, 'NO', 2023, 'BE, 4 Year', '720850015256');