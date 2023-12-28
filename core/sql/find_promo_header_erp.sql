select distinct
p.id,
p.periodovalidadeinicial, 
p.periodovalidadefinal, 
p.idvisibilidadepromocao 
from
promocaopersonalizada p
join
promocaopersonalizadaproduto pp ON pp.idpromocaopersonalizada = p.id
where
CURRENT_DATE between p.periodovalidadeinicial and p.periodovalidadefinal
and p.disponibilizado
and p.idvisibilidadepromocao = 2;