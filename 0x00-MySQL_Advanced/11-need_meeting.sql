-- Create a view that lists students with scores under 80 and no meeting or meetings more than a month ago
CREATE VIEW need_meeting AS
SELECT name
FROM students
WHERE score < 80 AND (last_meeting IS NULL OR last_meeting < CURDATE() - INTERVAL 1 MONTH);
