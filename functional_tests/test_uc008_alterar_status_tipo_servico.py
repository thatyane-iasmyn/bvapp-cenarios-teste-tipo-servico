# UC008 - Alterar Status de Tipo de Serviço
#
# Autor: Thatyane Iasmyn Andrade Alves
#
# Objetivo:
# Permitir que um usuário autorizado altere o status de um tipo de serviço entre
# verdadeiro e falso, verificando a confirmação da operação, a persistência do novo
# valor e a atualização da informação apresentada na listagem.
#
# Requisitos relacionados:
# - US 29533 — Alterar status de Tipo de Serviço.
# - US 25730 — Listagem de tipos de serviços.
# - Feature 25911 — Atualização de Tipo de Serviço.
# - Feature 25728 — Consulta de Tipo de Serviço.
#
# Ator:
# - Usuário autenticado com as permissões SERVICO_MENU, SERVICO_LISTAR e SERVICO_EDITAR.
#
# Pré-condições:
# - O usuário está autenticado no BVApp.
# - O usuário possui SERVICO_MENU e SERVICO_LISTAR para acessar a listagem.
# - O usuário possui SERVICO_EDITAR para alterar o status.
# - Existe pelo menos um tipo de serviço cadastrado e não excluído logicamente.
# - O tipo de serviço selecionado não está sendo removido durante a operação.
#
# 🟢 [FP] - ALTERAR O STATUS DE UM TIPO DE SERVIÇO
# ---------------------------------------------------------------
#
# 1. O ator acessa o menu "Tipos de Serviço".
#
# 2. O sistema apresenta a listagem, incluindo a coluna "Status".
#
# 3. O ator localiza um tipo de serviço cujo status está representado pelo switch.
#
# 4. O ator aciona o switch correspondente ao registro escolhido.
#
# 5. O sistema apresenta o modal de confirmação com o título "Confirmar Alteracao",
#    a pergunta sobre a alteração do status e as opções "Confirmar" e "Cancelar".
#
# 6. O ator seleciona "Confirmar".
#
# 7. O sistema envia ao backend o novo valor booleano do status por meio da operação PATCH.
#
# 8. Enquanto a solicitação está em andamento, o switch do registro permanece desabilitado,
#    evitando novas solicitações simultâneas.
#
# 9. O backend grava o novo valor no campo status e retorna os dados atualizados do tipo de serviço.
#
# 10. A interface atualiza os dados da listagem e fecha a confirmação.
#
# 11. O sistema apresenta a mensagem "Status do tipo de servico alterado com sucesso!".
#
# 12. O ator verifica que o switch do registro selecionado representa o novo valor booleano.
#
# 🟠 [A1] - CANCELAR A ALTERAÇÃO DE STATUS
# ---------------------------------------------------------------
#
# 1. O ator aciona o switch de um tipo de serviço.
# 2. O sistema apresenta o modal de confirmação.
# 3. O ator seleciona "Cancelar".
# 4. O sistema fecha o modal sem enviar a solicitação PATCH.
# 5. O ator verifica que o status original permanece apresentado no switch.
#
# 🟠 [A2] - USUÁRIO SEM PERMISSÃO PARA ALTERAR STATUS
# ---------------------------------------------------------------
#
# 1. O ator está autenticado, possui SERVICO_LISTAR, mas não possui SERVICO_EDITAR.
# 2. O sistema apresenta a listagem, mas o switch de status fica desabilitado para esse usuário.
# 3. O ator verifica que não consegue iniciar a alteração do status pela interface.
# 4. Caso uma solicitação alcance o backend sem a permissão exigida, o backend deve impedir a operação.
#
# 🟠 [A3] - TIPO DE SERVIÇO NÃO ENCONTRADO
# ---------------------------------------------------------------
#
# 1. O ator inicia a alteração do status de um tipo de serviço.
# 2. Antes de o backend processar a solicitação, o registro deixa de existir ou é removido logicamente.
# 3. O backend não encontra um registro elegível e retorna HTTP 404.
# 4. A interface apresenta o erro retornado pela operação e fecha a confirmação.
# 5. O sistema não apresenta mensagem de sucesso nem deve indicar um novo status não confirmado.
#
# 🟠 [A4] - FALHA AO ATUALIZAR O STATUS
# ---------------------------------------------------------------
#
# 1. O ator confirma a alteração do status.
# 2. Ocorre uma falha durante o processamento da solicitação.
# 3. O backend retorna erro; em caso de exceção genérica, a resposta prevista no endpoint é HTTP 500
#    com a mensagem "Erro ao atualizar status do tipo de serviço.".
# 4. A interface apresenta a mensagem de erro retornada pela API ou a mensagem padrão de erro.
# 5. O sistema não apresenta a mensagem de sucesso.
# 6. O ator verifica que a interface não apresenta como confirmado um status que não foi salvo.
#
# 🟣 [RN1] - PERMISSÕES
# ---------------------------------------------------------------
#
# - O acesso ao menu depende de SERVICO_MENU.
# - A listagem depende de SERVICO_LISTAR.
# - A alteração de status exige autenticação e SERVICO_EDITAR.
# - O switch fica desabilitado quando o usuário não possui SERVICO_EDITAR.
#
# 🟣 [RN2] - REPRESENTAÇÃO E PERSISTÊNCIA DO STATUS
# ---------------------------------------------------------------
#
# - O status é armazenado como valor booleano.
# - O switch representa o valor atual do campo status.
# - O modelo define valor padrão verdadeiro para novos tipos de serviço.
# - A operação de alteração utiliza PATCH e recebe um campo status booleano obrigatório.
# - Após a alteração bem-sucedida, o backend retorna HTTP 200 com os dados atualizados.
#
# 🟣 [RN3] - CONFIRMAÇÃO E PROCESSAMENTO
# ---------------------------------------------------------------
#
# - A interface solicita confirmação antes de enviar a alteração.
# - O usuário pode cancelar sem modificar o registro.
# - Durante o envio, o switch fica desabilitado para evitar solicitações simultâneas.
# - Após sucesso ou erro, a confirmação é fechada e o resultado é apresentado ao usuário.
#
# 🟣 [RN4] - VISIBILIDADE DO REGISTRO
# ---------------------------------------------------------------
#
# - A listagem, pesquisa e exportação não filtram os tipos de serviço pelo valor do status.
# - Tipos com status verdadeiro ou falso continuam disponíveis nesses fluxos, desde que não
#   tenham sido removidos logicamente.
#
# 🟡 DADOS DE ENTRADA
# ---------------------------------------------------------------
#
# Tipo de serviço previamente cadastrado:
# - ID: 301.
# - Nome: Inspeção Preventiva.
# - Descrição: Verificação periódica dos sistemas solares.
# - Status atual: verdadeiro.
#
# Dados enviados para a alteração:
# - Novo status: falso.
#
# Dados para fluxos alternativos:
# - Usuário autenticado sem SERVICO_EDITAR.
# - Identificador inexistente: 999999.
# - Registro removido logicamente antes do processamento.
# - Falha de processamento da solicitação PATCH.
#
# ✅ RESULTADOS ESPERADOS
# ---------------------------------------------------------------
#
# - O switch deve representar o status atual do tipo de serviço.
# - Ao acionar o switch, a interface deve solicitar confirmação.
# - Ao confirmar, o sistema deve enviar o novo valor booleano ao backend.
# - Após sucesso, a listagem deve refletir o novo status e apresentar a mensagem de confirmação.
# - Ao cancelar, nenhuma alteração deve ser enviada ou gravada.
# - O switch deve permanecer desabilitado para usuários sem SERVICO_EDITAR e durante o processamento.
# - Erros e registros inexistentes devem ser informados sem mensagem de sucesso.
# - O tipo de serviço deve continuar aparecendo na listagem mesmo após a mudança do status, desde que não tenha sido excluído logicamente.
#