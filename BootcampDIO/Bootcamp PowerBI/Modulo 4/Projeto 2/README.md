 # Projeto 2
 Criação de um relatóro financeiro usando sample no PBI Desktop.
 Foi criado como visto no star schema uma Tabela fato e cinco tabelas dimensões.
 ### Lista de Tabelas e suas descrições:
 
 - fVendas: Colunas: (SK_ID, IdProduct, Date, Profit, Sales, Unit Solds, Discount Brand, Discount, Product, Segment e Country)
 - dProduto: Colunas: (IdProduto, Product, Count, Média de Manufacturing, Média de Vendas, Mediana de Vendas, Valor Maximo de Vendas e Valor minimo de vendas)
 - dProdutoDetalhes: Colunas: (Discount band, IdProduto, Index, Manufacturing Price, Sale Price, Unit Solds)
 - dDescontos: Colunas: (Discount Band, Discounts, idProduto)
 - dCountry: Colunas: (Country)
 - dSegment: Colunas: (Segment)
 - dCalendario: Colunas: (Date, Mês Ano (Abr), Mês (Nome), Ano)

### Medidas criadas
- Unit Solds: SUM(fVendas[Units Sold])
- $ Sales: SUM(fVendas[ Sales])
- ! Max Sales: MAX(fVendas[ Sales])
- ! Min Sales: MIN(fVendas[ Sales])
- $ Ticket Médio: DIVIDE([$ Sales], [# Units Solds])
- $ Lucro: SUM(fVendas[Profit])
- $ Discount: SUM(fVendas[Discounts])
- $ Avg Sales Price: AVERAGE(fVendas[Sale Price])
- $ Discount Band = SUM(fVendas[Discount Band])
