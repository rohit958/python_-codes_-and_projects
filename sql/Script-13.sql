-- Create the table
CREATE TABLE PolicyCoverages (
    PolicyNumber VARCHAR(10),
    CoverageNumber VARCHAR(10),
    Premium DECIMAL(10, 2)
);

-- Insert the data
INSERT INTO PolicyCoverages (PolicyNumber, CoverageNumber, Premium)
VALUES 
    ('P1', 'C1', 100.00),
    ('P1', 'C2', 100.00),
    ('P2', 'C1', 100.00);




SELECT 
    PolicyNumber,
    COUNT(CoverageNumber) AS NoOfCoverages,
    MAX(CASE WHEN CoverageNumber = 'C1' THEN 1 ELSE 0 END) AS C1,
    MAX(CASE WHEN CoverageNumber = 'C2' THEN 1 ELSE 0 END) AS C2,
    SUM(Premium) AS TotalPremium
FROM PolicyCoverages
GROUP BY PolicyNumber;



