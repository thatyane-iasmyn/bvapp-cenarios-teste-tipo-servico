
# UC009 - Remover Tipo de Serviço e Verificar Restrições
#
# Autor: Thatyane Iasmyn Andrade Alves
#
# Objetivo:
# Permitir que um usuário autorizado solicite a remoção de um tipo de serviço,
# verificando a confirmação, a remoção lógica, a atualização da listagem
# e o impedimento da operação quando existirem serviços associados
# ainda não excluídos logicamente.
#
# Requisitos relacionados:
# - US 25919 — Remoção de Tipo de Serviço.
# - US 25730 — Listagem de tipos de serviços.
# - Feature 25912 — Exclusão de Tipo de Serviço.
# - Feature 25728 — Consulta de Tipo de Serviço.
#
# Ator:
# - Usuário autenticado com as permissões SERVICO_MENU, SERVICO_LISTAR
#   e SERVICO_EXCLUIR.
#
# Pré-condições:
# - O usuário está autenticado no BVApp.
# - O usuário possui SERVICO_MENU e SERVICO_LISTAR para acessar a listagem.
# - O usuário possui SERVICO_EXCLUIR para solicitar remoções.
# - Existem tipos de serviço cadastrados e não excluídos logicamente
#   para os fluxos previstos.
# - Para o fluxo principal, o tipo selecionado não possui Serviço associado
#   ainda não excluído logicamente.
#
# 🟢 [FP] - REMOVER UM TIPO DE SERVIÇO SEM VÍNCULO IMPEDITIVO
# ---------------------------------------------------------------
#
# 1. O ator acessa o menu "Tipos de Serviço".
#
# 2. O sistema apresenta a listagem de tipos de serviço.
#
# 3. O ator localiza um tipo de serviço que não possui Serviços associados
#    ainda não excluídos logicamente.
#
# 4. O ator seleciona a ação "Remover" correspondente ao registro.
#
# 5. O sistema apresenta o modal "Remover Tipo de Serviço" com a pergunta
#    "Tem certeza que deseja remover este tipo de serviço?"
#    e as opções "Remover" e "Cancelar".
#
# 6. O ator confirma a operação selecionando "Remover".
#
# 7. Durante o processamento, a interface apresenta o estado "Removendo...".
#
# 8. A interface envia a solicitação de exclusão ao backend por meio
#    da operação DELETE.
#
# 9. O backend verifica se o tipo de serviço existe, se ainda não está
#    excluído logicamente e se há algum Serviço associado com deletado=False.
#
# 10. Como não existe Serviço associado que impeça a operação,
#     o backend marca o tipo de serviço como excluído logicamente,
#     sem apagar fisicamente o registro do banco de dados.
#
# 11. O backend conclui a operação com HTTP 204, sem corpo de resposta.
#
# 12. A interface atualiza a listagem e apresenta a mensagem de sucesso.
#
# 13. O ator verifica que o tipo de serviço removido não aparece mais
#     nas consultas comuns do módulo.
#
# 🟠 [A1] - CANCELAR A REMOÇÃO
# ---------------------------------------------------------------
#
# 1. O ator seleciona a ação "Remover" de um tipo de serviço.
#
# 2. O sistema apresenta o modal de confirmação.
#
# 3. O ator seleciona "Cancelar" ou fecha o modal.
#
# 4. O sistema fecha a confirmação sem enviar a solicitação DELETE.
#
# 5. O ator verifica que o tipo de serviço continua aparecendo na listagem
#    e permanece disponível para consulta.
#
# 🟠 [A2] - REMOÇÃO IMPEDIDA POR SERVIÇO NÃO EXCLUÍDO
# ---------------------------------------------------------------
#
# 1. O ator seleciona a ação "Remover" de um tipo de serviço que possui
#    pelo menos um Serviço associado cujo campo deletado é falso.
#
# 2. O sistema apresenta o modal de confirmação.
#
# 3. O ator confirma a remoção.
#
# 4. A interface apresenta "Removendo..." e envia a solicitação DELETE.
#
# 5. O backend identifica o Serviço associado que ainda não foi
#    excluído logicamente.
#
# 6. O backend impede a operação e retorna HTTP 409 (conflito),
#    com a mensagem de impedimento.
#
# 7. A interface apresenta o aviso "Exclusão de tipo de serviço não permitida"
#    e a mensagem retornada pela API, quando disponível.
#
# 8. O ator verifica que o tipo de serviço permanece na listagem
#    e não foi removido.
#
# 🟠 [A3] - SERVIÇOS ASSOCIADOS JÁ EXCLUÍDOS LOGICAMENTE
# ---------------------------------------------------------------
#
# 1. O ator seleciona a ação "Remover" de um tipo de serviço que possui
#    Serviços associados, mas todos esses Serviços estão marcados
#    como excluídos logicamente.
#
# 2. O sistema apresenta o modal de confirmação.
#
# 3. O ator confirma a operação.
#
# 4. O backend verifica os Serviços associados e não encontra nenhum
#    com deletado=False.
#
# 5. O backend permite a remoção lógica do tipo de serviço
#    e conclui a operação com HTTP 204.
#
# 6. A interface atualiza a listagem e apresenta a mensagem de sucesso.
#
# 7. O ator verifica que o tipo de serviço não aparece mais na listagem.
#
# 🟠 [A4] - REGISTRO INEXISTENTE OU JÁ EXCLUÍDO
# ---------------------------------------------------------------
#
# 1. É solicitada a remoção de um identificador que não corresponde
#    a um tipo de serviço existente ou que já esteja excluído logicamente.
#
# 2. O backend não encontra um registro elegível e retorna HTTP 404.
#
# 3. A interface apresenta o aviso "Exclusão de tipo de serviço não permitida"
#    acompanhado da mensagem de erro retornada pela API, quando disponível.
#
# 4. O sistema não apresenta mensagem de sucesso.
#
# 🟠 [A5] - EXISTÊNCIA DE PRESTADOR DE SERVIÇO ASSOCIADO
# ---------------------------------------------------------------
#
# 1. O ator seleciona um tipo de serviço que possui associação
#    com registro(s) de PrestadorServico, mas não possui Serviço associado
#    com deletado=False.
#
# 2. O ator confirma a remoção.
#
# 3. O backend executa a verificação de impedimento considerando
#    os Serviços associados não excluídos logicamente.
#
# 4. Como não existe Serviço nessas condições, a existência isolada
#    de PrestadorServico não impede a remoção na implementação atual.
#
# 5. O backend realiza a remoção lógica e conclui a operação com HTTP 204.
#
# 6. A interface atualiza a listagem e apresenta a mensagem de sucesso.
#
# Observação: este fluxo documenta o comportamento identificado
# na implementação. A verificação de impedimento não considera
# isoladamente a associação com PrestadorServico.
#
# 🟠 [A6] - USUÁRIO SEM PERMISSÃO PARA EXCLUIR
# ---------------------------------------------------------------
#
# 1. O ator está autenticado e possui SERVICO_LISTAR,
#    mas não possui SERVICO_EXCLUIR.
#
# 2. O sistema não disponibiliza a ação de remoção para esse usuário.
#
# 3. Caso uma solicitação de exclusão alcance o backend
#    sem a permissão exigida, o backend deve impedir a operação.
#
# 4. O ator verifica que não consegue remover o tipo de serviço.
#
# 🟠 [A7] - FALHA DURANTE A SOLICITAÇÃO DE REMOÇÃO
# ---------------------------------------------------------------
#
# 1. O ator confirma a remoção de um tipo de serviço.
#
# 2. Ocorre uma falha de comunicação ou processamento durante a solicitação.
#
# 3. A interface apresenta o aviso de falha e a mensagem de erro disponível.
#
# 4. O sistema não apresenta mensagem de sucesso.
#
# 5. O ator verifica que o estado apresentado na listagem corresponde
#    ao estado confirmado pelo backend.
#
# 🟣 [RN1] - PERMISSÕES
# ---------------------------------------------------------------
#
# - O menu depende de SERVICO_MENU.
# - A listagem depende de SERVICO_LISTAR.
# - A remoção exige autenticação e SERVICO_EXCLUIR.
#
# 🟣 [RN2] - CONFIRMAÇÃO
# ---------------------------------------------------------------
#
# - A interface solicita confirmação antes de enviar a exclusão.
# - Cancelar ou fechar a confirmação não deve enviar a operação.
# - Durante a solicitação, o botão apresenta "Removendo...".
#
# 🟣 [RN3] - EXCLUSÃO LÓGICA
# ---------------------------------------------------------------
#
# - A remoção marca o registro como deletado=True.
# - O registro não é apagado fisicamente do banco de dados.
# - Registros removidos logicamente deixam de aparecer nas consultas comuns
#   de listagem, pesquisa e visualização.
# - A operação bem-sucedida retorna HTTP 204, sem corpo.
# - Um tipo inexistente ou já removido resulta em HTTP 404.
#
# 🟣 [RN4] - RESTRIÇÃO POR SERVIÇOS ASSOCIADOS
# ---------------------------------------------------------------
#
# - A remoção é impedida quando existe pelo menos um Serviço associado
#   com deletado=False.
# - Nessa situação, o backend retorna HTTP 409 (conflito).
# - A presença exclusiva de Serviços já excluídos logicamente
#   não impede a remoção.
# - A verificação de impedimento não considera, isoladamente,
#   a existência de registros de PrestadorServico.
#
# 🟡 DADOS DE ENTRADA
# ---------------------------------------------------------------
#
# Registro para o fluxo principal:
# - ID: 401.
# - Nome: Inspeção Preventiva.
# - Descrição: Verificação periódica dos sistemas solares.
# - Condição: sem Serviço associado não excluído logicamente.
#
# Registro para remoção impedida:
# - ID: 402.
# - Nome: Manutenção Corretiva.
# - Condição: possui pelo menos um Serviço associado com deletado=False.
#
# Registro para serviços relacionados já excluídos:
# - ID: 403.
# - Nome: Limpeza Técnica.
# - Condição: possui Serviços associados, todos com deletado=True.
#
# Registro para associação com prestador:
# - ID: 404.
# - Nome: Inspeção de Equipamentos.
# - Condição: possui PrestadorServico associado, mas nenhum Serviço
#   associado com deletado=False.
#
# Dados para fluxos alternativos:
# - Identificador inexistente: 999999.
# - Registro previamente excluído logicamente.
# - Usuário autenticado sem SERVICO_EXCLUIR.
#
# ✅ RESULTADOS ESPERADOS
# ---------------------------------------------------------------
#
# - O sistema deve solicitar confirmação antes da remoção.
# - Cancelar a operação deve manter o registro inalterado.
# - A remoção permitida deve marcar o registro como excluído logicamente
#   e retornar HTTP 204.
# - Após a remoção, o registro não deve aparecer nas consultas comuns do módulo.
# - A remoção deve ser impedida quando houver Serviço associado
#   não excluído logicamente, com HTTP 409.
# - Serviços associados já excluídos logicamente não devem impedir a remoção.
# - A associação isolada com PrestadorServico não impede a remoção
#   na implementação atual.
# - Registro inexistente ou já removido deve resultar em HTTP 404.
# - Falhas devem ser apresentadas sem mensagem de sucesso.
