-- Livros que possuam preços superiores a R$ 50,00.
SELECT * FROM livro WHERE preco>50.0;
-- Livros que possuam preços entre R$ 100,00 e R$ 200,00.
SELECT * FROM livro WHERE preco>100 AND preco<200;
-- Livros cujos títulos possuam a palavra ‘Banco’.
SELECT * FROM livro WHERE titulo LIKE '%Banco%';
-- Livros cujos títulos iniciam com a palavra ‘Banco’.
SELECT * FROM livro WHERE titulo LIKE 'Banco%';
-- Livros cujos títulos terminam com a palavra ‘Dados’.
SELECT * FROM livro WHERE titulo LIKE '%Dados';
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
