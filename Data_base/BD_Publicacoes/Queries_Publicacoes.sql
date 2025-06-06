-- Livros que possuam preços superiores a R$ 50,00.
SELECT * FROM livro WHERE preco>50.0;
-- Livros que possuam preços entre R$ 100,00 e R$ 200,00.
SELECT * FROM livro WHERE preco>100 AND preco<200;
-- Livros cujos títulos possuam a palavra ‘Banco’.
SELECT * FROM livro WHERE titulo LIKE '%Banco%';
-- Livros cujos títulos iniciam com a palavra ‘Banco’.
SELECT * FROM livro WHERE titulo LIKE 'Banco%';
-- Livros cujos títulos terminam com a palavra ‘Dados’.
SELECT * FROM livro WHERE TITULO LIKE '%Dados';
-- Livros cujos títulos possuem a expressão ‘Banco de Dados’ ou ‘Bancos de Dados’.
SELECT * FROM livro WHERE titulo LIKE 'Banco de Dados' OR titulo LIKE 'Bancos de Dados';
-- Livros que foram lançados há mais de 5 anos.
SELECT * FROM livro WHERE data_lancamento<NOW()-INTERVAL 5 YEAR;
-- Livros que ainda não foram lançados, ou seja, com a data de lançamento nula.
SELECT * FROM livro WHERE data_lancamento IS NULL;
-- Livros cujo assunto seja ‘Estruturas de Dados’.
SELECT * FROM livro WHERE assunto_codigo=2;
-- Livros cujo assunto tenha código 1, 2 ou 3.
SELECT * FROM livro WHERE assunto_codigo IN (1, 2, 3);
-- Quantidade de livros.
SELECT COUNT(*) FROM publicacoes.livro;
-- Quantidade de livros que ainda não foram lançados, ou seja, com a data de lançamento nula.
SELECT COUNT(*) AS "NÃO LANÇADOS"
FROM livro 
WHERE data_lancamento < now() OR data_lancamento IS NULL;
-- Soma dos preços dos livros.
SELECT SUM(preco) FROM livro;
-- Média de preços dos livros.
SELECT AVG(preco) FROM livro;
-- Maior preço dos livros.
SELECT MAX(preco) FROM livro;
-- Menor preço dos livros.
SELECT MIN(preco) FROM livro;
-- O preço médio dos livros para cada assunto.
SELECT AVG(preco), assunto_codigo 
FROM livro
GROUP BY assunto_codigo; 
-- Quantidade de livros para cada assunto.
SELECT a.descricao AS assunto, COUNT(a.codigo) AS qtd_livros
FROM publicacoes.livro l
JOIN publicacoes.assunto a ON l.assunto_codigo = a.codigo
GROUP BY a.descricao
ORDER BY a.descricao;
 
