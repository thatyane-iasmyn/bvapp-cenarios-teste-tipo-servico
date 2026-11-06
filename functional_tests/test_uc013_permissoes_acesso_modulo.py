
# UC013 - Verificar Permissões de Acesso ao Módulo de Tipo de Serviço
#
# Autor: Thatyane Iasmyn Andrade Alves
#
# Objetivo:
# Verificar se o acesso ao menu e às funcionalidades de cadastro, consulta,
# visualização, edição, alteração de status, exportação e exclusão de tipos
# de serviço respeita as permissões exigidas pelo módulo.
#
# Requisitos relacionados:
# - US 25724 — Cadastro básico de tipo de serviço.
# - US 25917 — Inclusão visual de tipo de serviço.
# - US 25730 — Listagem de tipos de serviços.
# - US 25913 — Consulta de Tipos de Serviço.
# - US 25914 — Visualização detalhada de Tipo de Serviço.
# - US 26980 — Exportar Tipos de Serviço.
# - US 28369 — Pesquisar e Filtrar Tipos de Serviço.
# - US 25918 — Editar dados de Tipo de Serviço.
# - US 26979 — Edição visual de Tipo de Serviço.
# - US 29533 — Alterar status de Tipo de Serviço.
# - US 25919 — Remoção de Tipo de Serviço.
# - Features relacionadas: 25715, 25728, 25911 e 25912.
#
# Ator:
# - Usuário autenticado no BVApp, com diferentes conjuntos de permissões
#   conforme cada fluxo.
#
# Pré-condições:
# - Existem contas de teste preparadas com permissões distintas.
# - Existe pelo menos um tipo de serviço cadastrado e não excluído logicamente.
# - Os usuários de teste estão autenticados quando o fluxo exigir autenticação.
# - As permissões disponíveis são as permissões genéricas SERVICO_*
#   utilizadas pelo módulo.
#
# 🟢 [FP] - ACESSAR AS FUNCIONALIDADES COM AS PERMISSÕES CORRESPONDENTES
# ---------------------------------------------------------------
#
# 1. O ator realiza login no BVApp com uma conta que possui as permissões
#    necessárias para acessar o módulo e executar as operações.
#
# 2. O sistema identifica as permissões do usuário autenticado.
#
# 3. O sistema apresenta no menu lateral a opção "Tipos de Serviço",
#    pois o usuário possui a permissão SERVICO_MENU.
#
# 4. O ator seleciona "Tipos de Serviço".
#
# 5. O sistema apresenta a listagem porque o usuário possui SERVICO_LISTAR.
#
# 6. O ator verifica que a opção de adicionar está disponível
#    porque possui SERVICO_ADICIONAR.
#
# 7. O ator verifica que a ação de visualizar está disponível
#    porque possui SERVICO_VISUALIZAR.
#
# 8. O ator verifica que as ações de editar e alterar status estão
#    disponíveis porque possui SERVICO_EDITAR.
#
# 9. O ator verifica que a ação de remover está disponível
#    porque possui SERVICO_EXCLUIR.
#
# 10. O ator verifica que a exportação em lote da listagem está disponível
#     porque possui SERVICO_LISTAR.
#
# 11. O ator verifica que a exportação individual em PDF está disponível
#     no fluxo de visualização porque possui SERVICO_VISUALIZAR.
#
# 12. O ator utiliza cada ação protegida, respeitando os respectivos
#     fluxos funcionais, e verifica que o sistema permite o acesso
#     quando a permissão correspondente está ativa.
#
# 🟠 [A1] - USUÁRIO NÃO POSSUI SERVICO_MENU
# ---------------------------------------------------------------
#
# 1. O ator realiza login com uma conta que não possui SERVICO_MENU.
#
# 2. O sistema não apresenta a opção "Tipos de Serviço"
#    no menu lateral.
#
# 3. O ator verifica que o módulo não está disponível pelo menu.
#
# 🟠 [A2] - USUÁRIO NÃO POSSUI SERVICO_LISTAR
# ---------------------------------------------------------------
#
# 1. O ator realiza login com uma conta que possui SERVICO_MENU,
#    mas não possui SERVICO_LISTAR.
#
# 2. O ator acessa a opção "Tipos de Serviço".
#
# 3. A interface não disponibiliza a consulta/listagem e apresenta
#    a mensagem "Você não tem permissão para visualizar tipos de serviço.".
#
# 4. O ator verifica que não consegue consultar, pesquisar ou paginar
#    os registros, nem realizar a exportação em lote da listagem.
#
# 🟠 [A3] - USUÁRIO NÃO POSSUI SERVICO_ADICIONAR
# ---------------------------------------------------------------
#
# 1. O ator acessa a listagem com SERVICO_LISTAR,
#    mas não possui SERVICO_ADICIONAR.
#
# 2. O sistema não disponibiliza a ação "Adicionar" para esse usuário.
#
# 3. O ator verifica que não consegue iniciar o cadastro pela interface.
#
# 4. Caso uma solicitação de cadastro alcance o backend
#    sem SERVICO_ADICIONAR, o backend deve impedir a operação.
#
# 🟠 [A4] - USUÁRIO NÃO POSSUI SERVICO_VISUALIZAR
# ---------------------------------------------------------------
#
# 1. O ator acessa a listagem com SERVICO_LISTAR,
#    mas não possui SERVICO_VISUALIZAR.
#
# 2. O sistema não disponibiliza a ação de visualização detalhada.
#
# 3. O ator verifica que não consegue abrir os detalhes
#    pela funcionalidade protegida.
#
# 4. A interface também não deve disponibilizar a exportação individual
#    em PDF, pois ela está associada ao fluxo de visualização detalhada.
#
# 5. Caso uma solicitação de consulta individual alcance o backend
#    sem SERVICO_VISUALIZAR, o backend deve impedir a operação.
#
# 🟠 [A5] - USUÁRIO NÃO POSSUI SERVICO_EDITAR
# ---------------------------------------------------------------
#
# 1. O ator acessa a listagem com SERVICO_LISTAR,
#    mas não possui SERVICO_EDITAR.
#
# 2. O sistema não disponibiliza a ação "Editar".
#
# 3. O switch de status permanece desabilitado para esse usuário.
#
# 4. O ator verifica que não consegue alterar Nome, Descrição ou Status.
#
# 5. Caso uma solicitação PUT ou PATCH alcance o backend
#    sem SERVICO_EDITAR, o backend deve impedir a operação.
#
# 🟠 [A6] - USUÁRIO NÃO POSSUI SERVICO_EXCLUIR
# ---------------------------------------------------------------
#
# 1. O ator acessa a listagem com SERVICO_LISTAR,
#    mas não possui SERVICO_EXCLUIR.
#
# 2. O sistema não disponibiliza a ação de remoção.
#
# 3. O ator verifica que não consegue iniciar a exclusão pela interface.
#
# 4. Caso uma solicitação DELETE alcance o backend
#    sem SERVICO_EXCLUIR, o backend deve impedir a operação.
#
# 🟠 [A7] - USUÁRIO NÃO AUTENTICADO
# ---------------------------------------------------------------
#
# 1. O ator tenta acessar o módulo sem realizar login
#    ou após perder a autenticação.
#
# 2. O sistema deve impedir o acesso à área protegida do dashboard.
#
# 3. Caso uma solicitação protegida alcance o backend
#    sem autenticação JWT válida, o acesso deve ser negado.
#
# 4. O ator verifica que não consegue executar operações do módulo
#    sem autenticação.
#
# 🟠 [A8] - PERMISSÃO NÃO ATIVA NO SISTEMA
# ---------------------------------------------------------------
#
# 1. O ator possui uma permissão declarada em sua sessão/token,
#    mas essa permissão não está ativa no cadastro de permissões do sistema.
#
# 2. O ator tenta executar a operação correspondente à permissão.
#
# 3. O backend verifica a presença da permissão e seu estado ativo.
#
# 4. O backend impede a operação quando a permissão não está ativa.
#
# 5. O ator verifica que a operação não foi concluída.
#
# 🟣 [RN1] - AUTENTICAÇÃO
# ---------------------------------------------------------------
#
# - As operações protegidas do módulo exigem usuário autenticado.
# - O backend utiliza autenticação JWT nas rotas do módulo.
# - Solicitações sem autenticação válida não devem concluir operações protegidas.
#
# 🟣 [RN2] - PERMISSÕES DO MÓDULO
# ---------------------------------------------------------------
#
# - SERVICO_MENU: controla a apresentação do item "Tipos de Serviço"
#   no menu lateral.
#
# - SERVICO_LISTAR: permite consultar, listar, pesquisar e paginar
#   tipos de serviço, além de realizar a exportação em lote da listagem.
#
# - SERVICO_ADICIONAR: permite cadastrar novos tipos de serviço.
#
# - SERVICO_VISUALIZAR: permite consultar os detalhes de um tipo de serviço
#   e acessar a exportação individual disponível no fluxo de visualização.
#
# - SERVICO_EDITAR: permite editar Nome e Descrição e alterar o Status.
#
# - SERVICO_EXCLUIR: permite solicitar a remoção de um tipo de serviço.
#
# 🟣 [RN3] - CONTROLES DA INTERFACE
# ---------------------------------------------------------------
#
# - A interface condiciona a apresentação das ações às permissões do usuário.
# - Sem SERVICO_LISTAR, a interface não disponibiliza a listagem
#   e informa a falta de permissão.
# - Sem SERVICO_ADICIONAR, a ação de cadastro não deve ser disponibilizada.
# - Sem SERVICO_VISUALIZAR, a ação de detalhes e a exportação individual
#   associada à visualização não devem ser disponibilizadas.
# - Sem SERVICO_EDITAR, a ação de edição não deve ser disponibilizada
#   e o switch de status fica desabilitado.
# - Sem SERVICO_EXCLUIR, a ação de remoção não deve ser disponibilizada.
#
# 🟣 [RN4] - AUTORIZAÇÃO NO BACKEND
# ---------------------------------------------------------------
#
# - As rotas do backend verificam autenticação JWT
#   e a permissão correspondente à operação.
# - A checagem considera se a permissão está presente e ativa no sistema.
# - Solicitações sem a permissão exigida devem ser impedidas pelo backend,
#   mesmo que sejam tentadas diretamente, sem utilizar os controles
#   da interface.
# - As permissões são genéricas SERVICO_* e compartilhadas pelo projeto;
#   não são permissões exclusivas do módulo de Tipo de Serviço.
#
# 🟡 DADOS DE ENTRADA
# ---------------------------------------------------------------
#
# Contas de teste sugeridas, previamente preparadas
# com as permissões indicadas:
#
# Usuário A — acesso completo ao módulo:
# - Autenticado.
# - SERVICO_MENU, SERVICO_LISTAR, SERVICO_ADICIONAR,
#   SERVICO_VISUALIZAR, SERVICO_EDITAR e SERVICO_EXCLUIR.
#
# Usuário B — acesso à listagem:
# - Autenticado.
# - SERVICO_MENU e SERVICO_LISTAR.
# - Sem SERVICO_ADICIONAR, SERVICO_VISUALIZAR,
#   SERVICO_EDITAR e SERVICO_EXCLUIR.
#
# Usuário C — acesso à listagem e edição:
# - Autenticado.
# - SERVICO_MENU, SERVICO_LISTAR e SERVICO_EDITAR.
# - Sem SERVICO_ADICIONAR, SERVICO_VISUALIZAR e SERVICO_EXCLUIR.
#
# Usuário D — sem acesso ao menu:
# - Autenticado.
# - Sem SERVICO_MENU.
#
# Usuário E — não autenticado:
# - Sem sessão válida ou token JWT válido.
#
# Usuário F — permissão inativa:
# - Autenticado.
# - Possui uma permissão declarada na sessão/token de teste,
#   mas essa permissão está desativada no cadastro de permissões do sistema.
#
# ✅ RESULTADOS ESPERADOS
# ---------------------------------------------------------------
#
# - O item "Tipos de Serviço" deve aparecer no menu somente
#   para quem possui SERVICO_MENU.
# - A listagem, pesquisa e paginação devem exigir SERVICO_LISTAR.
# - A exportação em lote da listagem deve exigir SERVICO_LISTAR.
# - O cadastro deve exigir SERVICO_ADICIONAR.
# - A visualização detalhada e a exportação individual devem exigir
#   SERVICO_VISUALIZAR.
# - A edição e a alteração de status devem exigir SERVICO_EDITAR.
# - A remoção deve exigir SERVICO_EXCLUIR.
# - Usuários sem a permissão correspondente não devem conseguir
#   executar a operação pela interface.
# - O backend deve impedir solicitações protegidas sem autenticação
#   ou sem a permissão correspondente.
# - As permissões devem estar ativas no sistema para serem consideradas válidas.
# - Nenhuma operação não autorizada deve apresentar mensagem de sucesso
#   ou alterar os dados.
