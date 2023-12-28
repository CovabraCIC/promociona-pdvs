SELECT DISTINCT
    pp.idpromocaopersonalizada,
    pp.valorminimo,
    pp.idproduto,
    pp.descricaoproduto,
    pp.codigobarrasproduto,
    pp.idsubcodigoproduto,
    pp.unidadeproduto,
    pp.preco4,
    pp.limiteprodutos
FROM
    promocaopersonalizada p
    JOIN promocaopersonalizadaproduto pp ON pp.idpromocaopersonalizada = p.id
WHERE
    CURRENT_DATE BETWEEN p.periodovalidadeinicial
    AND p.periodovalidadefinal
    AND p.disponibilizado
    AND p.idvisibilidadepromocao = 2;