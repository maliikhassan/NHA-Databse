create database NHA_Database;
use NHA_Database;

create table Tenders(
	PPRA_no varchar(20) primary key,
    title varchar(255),
    title_procurrement varchar(255),
    no_of_bids int,
    contract_no varchar(255),
    estimated_amount int,
    agencyName varchar(255),
    PPRA_No_publish_date date
);
CREATE INDEX idx_title ON Tenders(title);

create table tollTaxes(
	srNo int primary key,
	road_name varchar(255),
    road_distance int,
    PPRA_no varchar(20),
    Car int,
    Wagon int,
    MiniBus int,
    Bus int,
    TwoThreeAxleTruck int,
    articulatedTruck int,
	FOREIGN KEY (PPRA_no) REFERENCES Tenders(PPRA_no)
);

create table Projects(
	project_title varchar(255) primary key,
    PPRA_no varchar(20),
    project_length float(10,2),
    cost int,
    project_status varchar(50),
    project_type varchar(255),
    Completion_Date date, 
    Physical_Progress int,
    Financial_Progress int,
    PD_Name varchar(255),
    PD_Email varchar(255),
    FOREIGN KEY (PPRA_no) REFERENCES Tenders(PPRA_no)   
);

create table Remarks(
	contractOwner varchar(255),
    title_project varchar(255),
    reason varchar(255),
    constraint PK_Bkl_Contract primary key(contractOwner,title_project),
    FOREIGN KEY (contractOwner) REFERENCES Blacklist(contract_Owner),
    foreign key (title_project) references Projects(project_title)
);

create table Blacklist(
	contract_owner varchar(255) primary key,
    firm_name varchar(255),
    contractorCNIC varchar(100),
    contractorPhone varchar(100),
    adress varchar(255),
    statuses varchar(30)
);

select * from powerDuties;
create table PowerDuties(
    section varchar(255)primary key,
    sectionAllocation varchar(255),
    power_duty_name varchar(511),
    person_Responsible varchar(511)
);