# UC006 - Visualizar Detalhes de Tipo de Serviço
#
# Autor: Thatyane Iasmyn Andrade Alves
#
# Objetivo:
# Permitir que um usuário autorizado visualize os detalhes de um tipo de serviço selecionado na listagem,
# conferindo as informações Nome e Descrição correspondentes ao registro consultado.
#
# Requisitos relacionados:
# - US 25914 — Visualização detalhada de Tipo de Serviço.
# - US 25730 — Listagem de tipos de serviços.
# - Feature 25728 — Consulta de Tipo de Serviço.
#
# Ator:
# - Usuário autenticado com a permissão SERVICO_VISUALIZAR.
#
# Pré-condições:
# - O usuário está autenticado no BVApp.
# - O usuário possui a permissão SERVICO_MENU para acessar a opção no menu.
# - O usuário possui a permissão SERVICO_LISTAR para visualizar a listagem.
# - O usuário possui a permissão SERVICO_VISUALIZAR para utilizar a ação de visualização detalhada.
# - Existe pelo menos um tipo de serviço cadastrado e não excluído logicamente.
#
# 🟢 [FP] - VISUALIZAR DETALHES DE UM TIPO DE SERVIÇO
# ---------------------------------------------------------------
#
# 1. O ator acessa o sistema BVApp.
#
# 2. O ator seleciona a opção "Tipos de Serviço" no menu lateral.
#
# 3. O sistema apresenta a listagem de tipos de serviço.
#
# 4. O ator localiza um tipo de serviço que deseja consultar.
#
# 5. O ator seleciona a ação de visualização correspondente ao registro.
#
# 6. O sistema inicia a consulta dos dados do tipo de serviço selecionado pelo identificador do registro.
#
# 7. Enquanto os dados são carregados, o sistema apresenta a mensagem "Carregando dados do tipo de serviço...".
#
# 8. O backend consulta o registro pelo identificador informado, desde que ele não esteja excluído logicamente.
#
# 9. Após receber os dados, o sistema abre/apresenta o modal de visualização detalhada.
#
# 10. O modal apresenta os seguintes campos:
#     - Nome;
#     - Descrição.
#
# 11. O ator confere o Nome e a Descrição apresentados.
#
# 12. O ator verifica que as informações correspondem ao tipo de serviço selecionado na listagem.
#
# 13. O ator fecha o modal de visualização.
#
# 14. O sistema retorna à listagem, que permanece disponível para consulta.
#
# 🟠 [A1] - VISUALIZAR TIPO DE SERVIÇO INEXISTENTE OU EXCLUÍDO
# ---------------------------------------------------------------
#
# 1. É solicitada a visualização de um identificador que não corresponde a um tipo de serviço existente ou que esteja excluído logicamente.
#
# 2. O backend não encontra um registro elegível e retorna HTTP 404.
#
# 3. A interface apresenta a mensagem genérica "Erro ao carregar".
#
# 4. O ator verifica que os detalhes não são apresentados como se o registro tivesse sido encontrado.
#
# 🟠 [A2] - FALHA AO CARREGAR OS DETALHES
# ---------------------------------------------------------------
#
# 1. O ator seleciona a ação de visualização de um tipo de serviço existente.
#
# 2. Durante a consulta, ocorre uma falha de comunicação ou de processamento.
#
# 3. A interface apresenta a mensagem "Erro ao carregar".
#
# 4. O ator verifica que os dados não são apresentados como se a consulta tivesse sido concluída com sucesso.
#
# 🟠 [A3] - USUÁRIO SEM PERMISSÃO PARA VISUALIZAR
# ---------------------------------------------------------------
#
# 1. O ator está autenticado e consegue acessar a listagem por possuir SERVICO_LISTAR, mas não possui SERVICO_VISUALIZAR.
#
# 2. O sistema não disponibiliza a ação de visualizar para esse usuário.
#
# 3. Caso uma solicitação de visualização alcance o backend sem a permissão exigida, o endpoint deve impedir o acesso.
#
# 4. O ator verifica que não consegue obter os detalhes por meio da funcionalidade protegida.
#
# 🟣 [RN1] - PERMISSÕES
# ---------------------------------------------------------------
#
# - O acesso ao menu "Tipos de Serviço" depende da permissão SERVICO_MENU.
# - A listagem depende da permissão SERVICO_LISTAR.
# - A ação de visualizar detalhes depende da permissão SERVICO_VISUALIZAR.
# - O endpoint de consulta individual exige autenticação e a permissão SERVICO_VISUALIZAR.
#
# 🟣 [RN2] - IDENTIFICAÇÃO DO REGISTRO
# ---------------------------------------------------------------
#
# - A consulta detalhada é realizada pelo identificador do tipo de serviço selecionado.
# - O backend considera elegíveis apenas registros que não tenham sido excluídos logicamente.
# - Um identificador inexistente ou associado a um registro excluído logicamente resulta em HTTP 404.
#
# 🟣 [RN3] - INFORMAÇÕES APRESENTADAS NO MODAL
# ---------------------------------------------------------------
#
# - O componente visual apresenta somente Nome e Descrição.
# - Embora a resposta do backend contenha também ID e Status, esses campos não são exibidos no modal.
# - O wrapper recebe e mapeia dados de serviços e prestadores associados, mas o componente de visualização não os apresenta.
# - O fechamento do modal retorna o usuário à listagem.
#
# 🟡 DADOS DE ENTRADA
# ---------------------------------------------------------------
#
# Tipo de serviço disponível para consulta:
# - ID: 101.
# - Nome: Inspeção Preventiva.
# - Descrição: Verificação periódica das condições de funcionamento dos sistemas solares.
# - Status: verdadeiro (ativo).
# - Deletado: falso.
#
# Dados para fluxos alternativos:
# - Identificador inexistente: 999999.
# - Identificador de tipo de serviço previamente excluído logicamente.
# - Usuário autenticado sem a permissão SERVICO_VISUALIZAR.
#
# ✅ RESULTADOS ESPERADOS
# ---------------------------------------------------------------
#
# - O usuário autorizado deve conseguir solicitar a visualização a partir da listagem.
# - Durante a consulta, deve ser apresentada a mensagem "Carregando dados do tipo de serviço...".
# - Quando a consulta for concluída, o modal deve apresentar Nome e Descrição do registro selecionado.
# - O modal não deve apresentar ID, Status, serviços associados ou prestadores associados.
# - Ao fechar o modal, o usuário deve retornar à listagem.
# - Para registro inexistente ou excluído logicamente, o backend deve retornar HTTP 404 e a interface deve apresentar "Erro ao carregar".
# - Em caso de falha de carregamento, a interface deve apresentar "Erro ao carregar".
# - Usuários sem SERVICO_VISUALIZAR não devem conseguir utilizar a ação protegida de visualização.
