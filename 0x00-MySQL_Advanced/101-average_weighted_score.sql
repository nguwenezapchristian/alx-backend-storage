-- Create a stored procedure to compute the average weighted score for all students
DELIMITER //

CREATE PROCEDURE ComputeAverageWeightedScoreForUsers()
BEGIN
    -- Temporary table to store the weighted scores for users
    CREATE TEMPORARY TABLE TempWeightedScores AS
    SELECT
        s.user_id,
        SUM(s.score * p.weight) AS total_weighted_score,
        SUM(p.weight) AS total_weight
    FROM
        Scores s
    JOIN
        Projects p ON s.project_id = p.id
    GROUP BY
        s.user_id;

    -- Update the Users table with the computed average weighted score
    UPDATE Users u
    JOIN TempWeightedScores t ON u.id = t.user_id
    SET u.average_score = CASE 
        WHEN t.total_weight = 0 THEN 0
        ELSE t.total_weighted_score / t.total_weight
    END;

    -- Clean up
    DROP TEMPORARY TABLE TempWeightedScores;
END //

DELIMITER ;
