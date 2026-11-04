# UC003 - Listar Tipos de Serviço
#
# Autor: Thatyane Iasmyn Andrade Alves
#
# Objetivo:
# Permitir que um usuário autorizado consulte a listagem de tipos de serviço cadastrados, visualizando os dados principais dos registros que não foram excluídos logicamente.
#
# Requisitos relacionados:
# - US 25730 — Listagem de tipos de serviços.
# - Critérios de aceitação relacionados: 25732, 25733 e 25734.
#
# Ator:
# - Usuário autenticado com a permissão SERVICO_LISTAR.
#
# Pré-condições:
# - O usuário está autenticado no BVApp.
# - O usuário possui a permissão SERVICO_MENU para visualizar a opção no menu.
# - O usuário possui a permissão SERVICO_LISTAR para consultar os registros.
# - Existem tipos de serviço cadastrados, incluindo registros ativos e inativos.
# - Para verificar a exclusão lógica, existe um registro previamente marcado como excluído.
#
# 🟢 [FP] - ACESSAR E VISUALIZAR A LISTAGEM
# ---------------------------------------------------------------
#
# 1. O ator acessa o sistema BVApp.
# 2. O sistema apresenta o menu lateral de navegação.
# 3. O ator seleciona a opção "Tipos de Serviço".
# 4. O sistema acessa a tela de listagem de tipos de serviço.
# 5. Enquanto os dados são consultados, o sistema apresenta o estado de carregamento da listagem.
# 6. O sistema solicita os registros ao backend por meio da consulta paginada.
# 7. O backend retorna os tipos de serviço que não foram excluídos logicamente.
# 8. O sistema apresenta uma tabela com as colunas:
#    - Nome;
#    - Descrição;
#    - Status;
#    - Ações.
# 9. O ator observa os registros apresentados na tabela.
# 10. O ator verifica que cada linha apresenta os dados correspondentes ao respectivo tipo de serviço.
# 11. O ator verifica que os registros estão ordenados inicialmente pelo Nome em ordem crescente.
# 12. O ator verifica que os tipos de serviço ativos e inativos permanecem disponíveis na listagem, desde que não tenham sido excluídos logicamente.
# 13. O ator verifica que um tipo de serviço excluído logicamente não aparece na listagem.
#
# 🟠 [A1] - LISTAGEM SEM REGISTROS
# ---------------------------------------------------------------
#
# 1. O ator acessa a tela de Tipos de Serviço quando não existem registros não excluídos logicamente para apresentar.
# 2. O backend retorna uma lista vazia para a consulta.
# 3. O sistema apresenta a mensagem "Nenhum tipo de serviço encontrado.".
# 4. O ator verifica que a interface não apresenta registros inexistentes ou já excluídos logicamente.
#
# 🟠 [A2] - FALHA AO CARREGAR A LISTAGEM
# ---------------------------------------------------------------
#
# 1. O ator acessa a tela de Tipos de Serviço.
# 2. Durante a consulta, ocorre uma falha na comunicação ou no processamento da solicitação.
# 3. O sistema apresenta uma mensagem de erro informando que não foi possível carregar os tipos de serviço.
# 4. O ator verifica que a falha é apresentada como erro de consulta, e não como uma listagem vazia.
#
# 🟠 [A3] - USUÁRIO SEM PERMISSÃO DE LISTAGEM
# ---------------------------------------------------------------
#
# 1. O ator está autenticado e consegue acessar o módulo, mas não possui a permissão SERVICO_LISTAR.
# 2. O ator tenta acessar a listagem de tipos de serviço.
# 3. A interface não apresenta os registros e exibe a mensagem "Você não tem permissão para visualizar tipos de serviço.".
# 4. Caso a solicitação alcance o backend sem a permissão exigida, a autorização do endpoint deve impedir a consulta.
#
# 🟣 [RN1] - REGISTROS EXIBIDOS
# ---------------------------------------------------------------
#
# - A listagem considera somente tipos de serviço com deletado=False.
# - Tipos de serviço com status verdadeiro e falso são retornados; o status não é utilizado como filtro de visibilidade.
# - Registros excluídos logicamente não devem aparecer nas consultas comuns.
#
# 🟣 [RN2] - INFORMAÇÕES DA TABELA
# ---------------------------------------------------------------
#
# - A tabela apresenta Nome, Descrição, Status e Ações.
# - O controle de status representa o valor booleano armazenado no registro.
# - Os dados apresentados devem corresponder ao tipo de serviço retornado pelo backend.
#
# 🟣 [RN3] - ORDENAÇÃO INICIAL
# ---------------------------------------------------------------
#
# - A consulta de listagem do backend é ordenada inicialmente pelo Nome em ordem crescente.
#
# 🟣 [RN4] - ACESSO À LISTAGEM
# ---------------------------------------------------------------
#
# - A opção do menu "Tipos de Serviço" depende da permissão SERVICO_MENU.
# - A consulta da listagem depende da autenticação e da permissão SERVICO_LISTAR.
# - A permissão SERVICO_LISTAR é diferente das permissões necessárias para visualizar detalhes, editar ou remover registros.
#
# 🟡 DADOS DE ENTRADA
# ---------------------------------------------------------------
#
# Registros de exemplo para a conferência da listagem:
#
# - Registro 1:
#   - Nome: Inspeção Preventiva
#   - Descrição: Verificação periódica dos sistemas solares
#   - Status: verdadeiro (ativo)
#   - Deletado: falso
#
# - Registro 2:
#   - Nome: Manutenção Corretiva
#   - Descrição: Correção de falhas identificadas nos sistemas solares
#   - Status: falso (inativo)
#   - Deletado: falso
#
# - Registro 3:
#   - Nome: Calibração de Equipamentos
#   - Descrição: Ajuste e verificação de equipamentos
#   - Status: verdadeiro
#   - Deletado: verdadeiro (excluído logicamente)
#
# ✅ RESULTADOS ESPERADOS
# ---------------------------------------------------------------
#
# - A tela de Tipos de Serviço deve ser acessível ao usuário que possui as permissões necessárias.
# - A tabela deve apresentar Nome, Descrição, Status e Ações.
# - Os registros ativos e inativos não excluídos logicamente devem aparecer.
# - O registro excluído logicamente não deve aparecer.
# - A listagem deve estar ordenada inicialmente por Nome em ordem crescente.
# - Os dados apresentados devem corresponder aos registros retornados pelo sistema.
# - Quando não houver registros, deve ser apresentada a mensagem "Nenhum tipo de serviço encontrado.".
# - Quando ocorrer falha na consulta, deve ser apresentado um erro, sem confundi-lo com ausência de registros.
