-- Liste os clientes que já fizeram mais de 2 pedidos com status 'Concluído'.
SELECT
	COUNT(p.cliente_id) AS NUM_PEDIDO,
	c.nome AS NOME
FROM
	pedidos AS p
INNER JOIN
	clientes AS c ON p.cliente_id = c.id
WHERE
	p.status = "Concluído"
GROUP BY
	p.cliente_id
HAVING
	COUNT(p.cliente_id)>2;
    
-- Para cada produto, exiba: id, nome, estoque, e uma coluna chamada situacao_estoque com as seguintes regras:
-- "Crítico" se o estoque for 10 ou menos
-- "Baixo" se estiver entre 11 e 30
-- "OK" se estiver acima de 30
-- Use a cláusula CASE para gerar a coluna situacao_estoque.
SELECT
	p.id, p.nome, p.estoque,
    CASE 
		WHEN estoque > 30 THEN "OK"
        WHEN estoque BETWEEN 11 AND 30 THEN "Baixo"
        WHEN estoque <=10 THEN "Crítico"
        END AS situacao_estoque
FROM
	produtos AS p
ORDER BY
	p.estoque;

-- Liste os clientes que fizeram pedidos, mas todos eles foram cancelados. 
-- Exiba: id do cliente, nome, total_pedidos, pedidos_cancelados
-- e uma coluna todos_cancelados com "Sim" ou "Não"
-- Use COUNT, IF, HAVING e subconsulta se precisar.
SELECT
	c.id AS ID_Cliente,
	c.nome as Nome,
    COUNT(p.cliente_id) AS total_pedidos
FROM
	clientes AS c
INNER JOIN
	pedidos as p ON p.cliente_id = c.id
GROUP BY
	p.cliente_id,
    c.nome;
