-- a SQL script that creates a stored procedure ComputeAverageScoreForUser that
-- computes and store the average score for a student.An average score can be a decimal
DELIMITER //

CREATE PROCEDURE ComputeAverageScoreForUser(
    IN user_id INT
)
BEGIN
    DECLARE total_score FLOAT;
    DECLARE total_projects INT;
    DECLARE avg_score FLOAT;

    -- Compute total score for the user
    SELECT SUM(score) INTO total_score FROM corrections WHERE user_id = user_id;

    -- Compute total number of projects for the user
    SELECT COUNT(DISTINCT project_id) INTO total_projects FROM corrections WHERE user_id = user_id;

    -- Compute average score
    IF total_projects > 0 THEN
        SET avg_score = total_score / total_projects;
    ELSE
        SET avg_score = 0;
    END IF;

    -- Update average score for the user
    UPDATE users SET average_score = avg_score WHERE id = user_id;

END//

DELIMITER ;
