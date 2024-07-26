-- Create a stored procedure to compute the average weighted score for all users
DROP PROCEDURE IF EXISTS ComputeAverageWeightedScoreForUsers;

DELIMITER $$

CREATE PROCEDURE ComputeAverageWeightedScoreForUsers()
BEGIN
    -- Create a cursor for users
    DECLARE done INT DEFAULT 0;
    DECLARE user_id INT;
    DECLARE cur CURSOR FOR SELECT id FROM users;
    DECLARE CONTINUE HANDLER FOR NOT FOUND SET done = 1;

    OPEN cur;

    read_loop: LOOP
        FETCH cur INTO user_id;
        IF done THEN
            LEAVE read_loop;
        END IF;

        -- Call procedure to update average score for each user
        CALL ComputeAverageWeightedScoreForUser(user_id);
    END LOOP;

    CLOSE cur;
END$$

DELIMITER ;
