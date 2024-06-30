use nha_database;

-- (JOIN on 3 Tables: tenders, project, remarks of banned firms):
select t.PPRA_No,p.project_title,r.contractOwner,r.reason as Banned_Reason
	from tenders t
	join projects p on t.PPRA_No = p.PPRA_No
   	join remarks r on p.project_title = r.title_project;

-- (Compaies Black listed for 3 years for which project):
select p.PPRA_No,p.project_title,b.firm_name,r.reason as Banned_Reason,b.statuses
	from projects p
    join remarks r on p.project_title = r.title_project
   	join blacklist b on b.contract_owner = r.contractOwner
	where b.statuses = "3 Years";

-- (Using group by and Having Clause [No of Duties > 5]):
select sectionAllocation,count(section) as No_of_Duties_Assigned 
	from powerduties 
	group by sectionAllocation
    having No_of_Duties_Assigned > 5;

-- (Average Toll Taxes of Vehicles on Pakistani Roads):
select avg(car) as AVG_CAR_TAX,avg(wagon) as AVG_Wagon_TAX,
    avg(miniBus) as AVG_MINIBus_TAX,
    avg(bus) as AVG_Bus_TAX,
    avg(twothreeaxletruck) as AVG_Truck_TAX,
    avg(articulatedTruck) as AVG_ArticulatedTruck_TAX
    from tolltaxes;

-- (Most Expensive(Toll Tax) Road in Pakistan for Trucks):
select road_name,twothreeAxleTruck as HighestTax_for_Trucks
	from tolltaxes
   	where twothreeAxleTruck = (select max(twothreeAxleTruck) from tolltaxes);

-- (5 most Expensive Projects by NHA):
select p.ppra_no, project_title,project_length,cost,t.agencyname
	from projects p,tenders t
	where p.ppra_no = t.ppra_no and agencyname = "national highway authority"
    order by cost desc limit 5;

-- (Create a function to calculate the AVG total toll tax):
DELIMITER //
CREATE FUNCTION TotalTollTaxForRoad()
RETURNS DECIMAL(10, 2)
DETERMINISTIC
BEGIN
    DECLARE totalTollTax DECIMAL(10, 2);
    SELECT avg(car + wagon + MiniBus + Bus + twothreeAxleTruck + ArticulatedTruck) INTO totalTollTax
    FROM TollTaxes;
    RETURN totalTollTax;
END //
DELIMITER ;

select TotalTollTaxForRoad();

 -- Find the projects that have more bids than the average number of bids across all tenders.
SELECT project_title, P.PPRA_No, no_of_Bids
FROM Projects P
JOIN Tenders T ON P.PPRA_No = T.PPRA_No
WHERE T.no_of_Bids > (select avg(no_of_bids) from tenders);

 -- List the names of contractors who have been blacklisted and are also associated with remarks.
SELECT firm_Name FROM BlackList WHERE contract_Owner in (SELECT contractOwner FROM Remarks);

 -- Find the average estimated amount of tenders for each agency.
SELECT agencyName, AVG(estimated_Amount) AS average_estimated_amount FROM Tenders GROUP BY agencyName HAVING AVG(estimated_Amount) > 100000;
