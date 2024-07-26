-- Create a function to safely divide two numbers
DROP FUNCTION IF EXISTS SafeDiv;

DELIMITER $$

CREATE FUNCTION SafeDiv(a INT, b INT) RETURNS FLOAT
BEGIN
    RETURN IF(b = 0, 0, a / b);
END$$

DELIMITER ;
