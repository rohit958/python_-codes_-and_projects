with combined_result as (
    -- Perspective of Team 1
    select 
        team_1 as team, 
        case when team_1 = result then 1 else 0 end as won,
        case when result is null then 1 else 0 end as draw,
        case when team_2 = result then 1 else 0 end as lost 
    from Match_Result 

    union all

    -- Perspective of Team 2
    select 
        team_2 as team, 
        case when team_2 = result then 1 else 0 end as won, -- Corrected: team_2 wins if result = team_2
        case when result is null then 1 else 0 end as draw,
        case when team_1 = result then 1 else 0 end as lost  -- Corrected: team_2 loses if result = team_1
    from Match_Result 
)

select 
    team, 
    count(*) as total_match_played,
    sum(won) as total_won, 
    sum(lost) as total_lost,
    sum(draw) as total_draw
from combined_result
group by team;