-- Create the SafeDiv function
CREATE FUNCTION SafeDiv(a INT, b INT)
RETURNS INT
BEGIN
    DECLARE result INT;
    
    IF b <> 0 THEN
        SET result = a / b;
    ELSE
        SET result = 0;
    END IF;
    
    RETURN result;
END;
