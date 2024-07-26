-- Create a stored procedure to compute the average weighted score for a user
DROP PROCEDURE IF EXISTS ComputeAverageWeightedScoreForUser;

DELIMITER $$

CREATE PROCEDURE ComputeAverageWeightedScoreForUser(IN user_id INT)
BEGIN
    DECLARE avg_weighted_score FLOAT;

    -- Calculate average weighted score
    SELECT SUM(score * weight) / SUM(weight) INTO avg_weighted_score
    FROM corrections
    JOIN projects ON corrections.project_id = projects.id
    WHERE user_id = user_id;

    -- Update user's average score
    UPDATE users
    SET average_score = avg_weighted_score
    WHERE id = user_id;
END$$

DELIMITER ;
