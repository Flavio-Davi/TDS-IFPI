-- 1. Encontrar o nome e valor de todos os produtos com preço superior a 10.0.
SELECT
	pr.nome,
    pr.preco
FROM
	produtos pr
WHERE
	pr.preco > 10;

-- Listar a data de todos os pedidos feitos por um cliente específico, identificado pelo cliente com id = 2.
SELECT
	pd.data_pedido
FROM
	pedidos pd
WHERE
	pd.id_cliente = 2;

-- Listar a quantidade de pedidos realizados pelo cliente com id = 3.
SELECT
	COUNT(pd.id_pedido)
FROM
	pedidos pd
WHERE
	pd.id_cliente = 3;

-- Listar o nome, quantidade e preço unitário dos produtos que foram comprados em um pedido 
-- específico (id_pedido = 1), com quantidade e preço unitário.
SELECT
	pr.nome, 
    pp.quantidade, 
    pp.preco_unitario
FROM
	produtos pr
JOIN
	pedidos_produtos pp ON pp.id_produto=pr.id_produto
WHERE
	pp.id_pedido = 1;

-- Listar a quantidade de pedidos realizados pelo cliente com nome = ‘Beltrano’.
SELECT
	COUNT(pd.id_pedido)
FROM
	clientes cl
JOIN
	pedidos pd ON pd.id_cliente=cl.id_cliente
WHERE
	cl.nome='Beltrano';

-- Calcular o valor total do pedido com id = 2.
SELECT
	SUM(pp.preco_unitario * pp.quantidade)
FROM
	pedidos_produtos pp	
WHERE
	id_pedido = 2;
    
-- Calcular o valor total de todos os pedidos do cliente com id = 1.
SELECT
	SUM(pp.quantidade * pp.preco_unitario)
FROM
	pedidos pd
JOIN
	pedidos_produtos pp ON pp.id_pedido=pd.id_pedido
WHERE
	pd.id_cliente = 1;
