-- Create the SafeDiv function
CREATE FUNCTION SafeDiv(a INT, b INT)
RETURNS INT
BEGIN
    IF b <> 0 THEN
        RETURN a / b;
    ELSE
        RETURN 0;
    END IF;
END;
