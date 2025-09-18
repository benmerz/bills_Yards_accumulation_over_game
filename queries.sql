select * from bills_stats
limit 10;






-- Bills and Opponents Combined with time, qtr, team_color, and team_logo columns
WITH plays AS (
    SELECT
        'Bills' AS team_type,
        play_id,
        week,
        posteam,
        yards_gained,
        time,
        qtr,
        SUM(yards_gained) OVER (PARTITION BY week ORDER BY play_id ASC) AS cumulative_yards
    FROM
        bills_stats
    WHERE
        posteam = 'BUF'

    UNION ALL

    SELECT
        'Opponent' AS team_type,
        play_id,
        week,
        posteam,
        yards_gained,
        time,
        qtr,
        SUM(yards_gained) OVER (PARTITION BY week ORDER BY play_id ASC) AS cumulative_yards
    FROM
        bills_stats
    WHERE
        posteam != 'BUF'
)
SELECT
    p.team_type,
    p.play_id,
    p.week,
    p.posteam,
    p.yards_gained,
    p.time,
    p.qtr,
    p.cumulative_yards,
    t.team_color,
    t.team_logo_wikipedia
FROM
    plays p
    LEFT JOIN teams t ON p.posteam = t.team_abbr
ORDER BY
    p.week ASC, p.play_id ASC, p.team_type;
