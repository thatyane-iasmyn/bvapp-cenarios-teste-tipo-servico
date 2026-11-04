# UC004 - Consultar Tipos de Serviço com Paginação e Ordenação
#
# Autor: Thatyane Iasmyn Andrade Alves
#
# Objetivo:
# Permitir que um usuário autorizado consulte os tipos de serviço por meio de uma listagem paginada,
# navegue entre as páginas, altere a quantidade de registros exibidos e ordene os resultados por Nome ou Descrição.
#
# Requisitos relacionados:
# - US 25913 — Consulta de Tipos de Serviço.
# - US 25730 — Listagem de tipos de serviços.
# - Feature 25728 — Consulta de Tipo de Serviço.
# - Critérios de aceitação relacionados à paginação, navegação, indicadores e ordenação da Feature 25728.
#
# Ator:
# - Usuário autenticado com a permissão SERVICO_LISTAR.
#
# Pré-condições:
# - O usuário está autenticado no BVApp.
# - O usuário possui a permissão SERVICO_MENU para visualizar a opção no menu.
# - O usuário possui a permissão SERVICO_LISTAR para consultar a listagem.
# - Existem mais de 10 tipos de serviço não excluídos logicamente, para permitir a navegação entre páginas.
# - Existem registros com valores diferentes de Nome e Descrição, para permitir verificar a ordenação.
#
# 🟢 [FP] - CONSULTAR REGISTROS, NAVEGAR E ORDENAR
# ---------------------------------------------------------------
#
# 1. O ator acessa o sistema BVApp.
#
# 2. O sistema apresenta o menu lateral de navegação.
#
# 3. O ator seleciona a opção "Tipos de Serviço".
#
# 4. O sistema apresenta a listagem de tipos de serviço.
#
# 5. O sistema realiza a consulta paginada e apresenta inicialmente 10 registros por página.
#
# 6. O sistema apresenta a tabela com as colunas:
#    - Nome;
#    - Descrição;
#    - Status;
#    - Ações.
#
# 7. O sistema apresenta o indicador de paginação no formato "Página X de Y - Z tipo(s)",
#    informando a página atual, o total de páginas e a quantidade total de registros.
#
# 8. O ator verifica que os controles de navegação entre páginas estão disponíveis quando há páginas anteriores ou seguintes.
#
# 9. O ator seleciona a opção de avançar para a próxima página.
#
# 10. O sistema consulta a página seguinte e atualiza os registros apresentados na tabela.
#
# 11. O ator verifica que o indicador de paginação apresenta a nova página atual e que os registros exibidos pertencem à página consultada.
#
# 12. O ator seleciona a opção para retornar à página anterior.
#
# 13. O sistema apresenta novamente os registros da página anterior e atualiza o indicador de paginação.
#
# 14. O ator seleciona a opção de quantidade de registros por página e escolhe 20.
#
# 15. O sistema retorna à primeira página e apresenta até 20 registros, de acordo com a quantidade disponível.
#
# 16. O ator verifica que o indicador apresenta a primeira página e a quantidade total de registros continua correspondendo ao resultado da consulta.
#
# 17. O ator seleciona a opção de ordenação pela coluna "Nome".
#
# 18. O sistema atualiza a consulta ordenando os registros por Nome.
#
# 19. O ator alterna a ordenação entre crescente e decrescente.
#
# 20. O sistema atualiza a listagem de acordo com a direção selecionada.
#
# 21. O ator seleciona a ordenação pela coluna "Descrição".
#
# 22. O sistema atualiza a listagem considerando a Descrição e a direção de ordenação selecionada.
#
# 23. O ator verifica que os registros apresentados estão ordenados de acordo com o campo e a direção selecionados.
#
# 🟠 [A1] - CONSULTAR COM MENOS REGISTROS QUE O TAMANHO DA PÁGINA
# ---------------------------------------------------------------
#
# 1. O ator acessa a listagem quando existem menos de 10 tipos de serviço não excluídos logicamente.
#
# 2. O sistema apresenta somente os registros disponíveis.
#
# 3. O sistema informa a página atual, o total de páginas e a quantidade total de registros.
#
# 4. O ator verifica que não são apresentados registros inexistentes ou excluídos logicamente.
#
# 🟠 [A2] - ALTERAR A QUANTIDADE DE REGISTROS POR PÁGINA
# ---------------------------------------------------------------
#
# 1. O ator está em uma página diferente da primeira.
#
# 2. O ator seleciona outra quantidade de registros por página, escolhendo 10, 20, 30 ou 40.
#
# 3. O sistema retorna à primeira página e realiza novamente a consulta com a quantidade selecionada.
#
# 4. O ator verifica que o seletor apresenta a opção escolhida e que a listagem foi atualizada.
#
# 🟠 [A3] - NAVEGAR ATÉ OS LIMITES DA PAGINAÇÃO
# ---------------------------------------------------------------
#
# 1. O ator está na primeira página.
#
# 2. O ator verifica que o controle para retornar à página anterior está desabilitado.
#
# 3. O ator navega até a última página disponível.
#
# 4. O ator verifica que o controle para avançar à próxima página está desabilitado.
#
# 5. O sistema mantém os registros e o indicador de paginação correspondentes à página atual.
#
# 🟠 [A4] - CONSULTA SEM REGISTROS NA PÁGINA SOLICITADA
# ---------------------------------------------------------------
#
# 1. O ator realiza uma consulta paginada que não retorna registros para a página solicitada.
#
# 2. O sistema apresenta a tabela sem linhas de registros e exibe a mensagem "Nenhum tipo de serviço encontrado.".
#
# 3. O ator verifica que a interface não apresenta registros de outra página como se fossem da página consultada.
#
# 🟠 [A5] - FALHA NA CONSULTA PAGINADA
# ---------------------------------------------------------------
#
# 1. O ator acessa ou navega na listagem de tipos de serviço.
#
# 2. Durante a consulta, ocorre uma falha na comunicação ou no processamento da solicitação.
#
# 3. O sistema apresenta o feedback de erro da consulta.
#
# 4. O ator verifica que a falha não é apresentada como se fosse uma consulta sem resultados.
#
# 🟠 [A6] - ORDENAÇÃO INVÁLIDA RECEBIDA PELO BACKEND
# ---------------------------------------------------------------
#
# 1. Uma solicitação à consulta paginada é encaminhada ao backend com um campo de ordenação diferente de Nome ou Descrição,
#    ou com uma direção diferente de crescente ou decrescente.
#
# 2. O backend rejeita o parâmetro inválido e retorna HTTP 400, com mensagem indicando o valor inválido.
#
# 3. A solicitação não deve ser tratada como uma ordenação válida.
#
# Observação: este fluxo é uma verificação do comportamento da API; a interface disponibiliza as opções válidas ao usuário.
#
# 🟣 [RN1] - PERMISSÕES
# ---------------------------------------------------------------
#
# - O acesso ao menu "Tipos de Serviço" depende da permissão SERVICO_MENU.
# - A consulta paginada exige usuário autenticado e permissão SERVICO_LISTAR.
#
# 🟣 [RN2] - TAMANHO DA PÁGINA
# ---------------------------------------------------------------
#
# - O tamanho inicial apresentado pela interface é 10 registros por página.
# - O seletor disponibiliza as opções 10, 20, 30 e 40 registros por página.
# - Ao alterar o tamanho da página, a interface retorna à primeira página.
# - Não se presume neste cenário um limite máximo ou um valor padrão interno do backend além das opções confirmadas na interface.
#
# 🟣 [RN3] - INDICADORES E NAVEGAÇÃO
# ---------------------------------------------------------------
#
# - A interface apresenta página atual, total de páginas e quantidade total de registros.
# - A interface disponibiliza controles de página anterior, próxima e navegação pelos números de página.
# - Os controles anterior e próximo ficam desabilitados nos limites da navegação.
# - A integração utiliza o cabeçalho X-Pagination para obter informações de paginação.
#
# 🟣 [RN4] - ORDENAÇÃO
# ---------------------------------------------------------------
#
# - Os campos de ordenação aceitos pelo backend são Nome e Descrição.
# - As direções aceitas são crescente (asc) e decrescente (desc).
# - A ordenação padrão do backend é Nome em ordem crescente.
# - Campos ou direções de ordenação inválidos são rejeitados pelo backend com HTTP 400.
#
# 🟡 DADOS DE ENTRADA
# ---------------------------------------------------------------
#
# Dados de exemplo para a consulta:
# - Quantidade de registros não excluídos logicamente: 25.
# - Tamanho inicial da página: 10.
# - Opções de tamanho: 10, 20, 30 e 40.
# - Campos de ordenação: Nome e Descrição.
# - Direções de ordenação: crescente e decrescente.
#
# Exemplos de registros:
# - Nome: Calibração de Equipamentos; Descrição: Ajuste de equipamentos.
# - Nome: Inspeção Preventiva; Descrição: Verificação periódica.
# - Nome: Manutenção Corretiva; Descrição: Correção de falhas.
#
# ✅ RESULTADOS ESPERADOS
# ---------------------------------------------------------------
#
# - A consulta deve iniciar com 10 registros por página.
# - O seletor deve disponibilizar 10, 20, 30 e 40 registros por página.
# - A navegação deve atualizar os registros e o indicador de paginação.
# - A mudança do tamanho da página deve retornar à primeira página.
# - A ordenação deve considerar Nome ou Descrição, na direção selecionada.
# - A ordenação inicial deve ser Nome crescente.
# - Os controles de navegação devem respeitar os limites da paginação.
# - Uma página sem registros deve apresentar "Nenhum tipo de serviço encontrado.".
# - Uma falha de consulta deve ser apresentada como erro, não como ausência de registros.
# - Parâmetros de ordenação inválidos devem ser rejeitados pelo backend.
