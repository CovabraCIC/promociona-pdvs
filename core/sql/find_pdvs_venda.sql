select distinct
case
when nestab = 2 then 1
else nestab
end as nestab,
npdv::int
from
public.t_pdv tp
where
nestab not in (99, 13, 1, 0)
and npdv ~ '[0-9]'
and npdv::int < 30
order by
1,
2;