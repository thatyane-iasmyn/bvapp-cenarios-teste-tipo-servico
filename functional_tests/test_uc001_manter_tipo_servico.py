# UC001 - Manter Tipo de Serviço
#
# Autor: Thatyane Iasmyn Andrade Alves
#
# Objetivo:
# Permitir que um usuário autorizado realize o ciclo completo de manutenção de um tipo de serviço, contemplando cadastro, consulta na listagem, atualização dos dados e remoção lógica do registro.
#
# Requisitos relacionados:
# - US 25724 — Cadastro básico de tipo de serviço.
# - US 25730 — Listagem de tipos de serviços.
# - US 25918 — Editar dados de Tipo de Serviço.
# - US 25919 — Remoção de Tipo de Serviço.
# - Features relacionadas: 25715, 25728, 25911 e 25912.
#
# Ator:
# - Usuário autenticado com as permissões SERVICO_ADICIONAR, SERVICO_LISTAR, SERVICO_EDITAR e SERVICO_EXCLUIR.
#
# Pré-condições:
# - O usuário está autenticado no BVApp.
# - O usuário possui as permissões necessárias para executar as quatro operações.
# - Existe acesso ao menu de Tipos de Serviço por meio da permissão SERVICO_MENU.
# - O nome utilizado no cadastro ainda não está cadastrado.
# - Para concluir a remoção no fluxo principal, o tipo de serviço não possui Serviços associados que ainda não tenham sido excluídos logicamente.
#
# 🟢 [FP] - FLUXO PRINCIPAL
# ---------------------------------------------------------------
#
# 1. O ator acessa o menu "Tipos de Serviço".
#
# 2. O sistema exibe a tela de listagem de tipos de serviço, com as colunas Nome, Descrição, Status e Ações.
#
# 3. O ator seleciona a opção "Adicionar".
#
# 4. O sistema abre o modal "Adicionar Tipo de Serviço", apresentando os campos:
#    - Nome do tipo de serviço;
#    - Descrição do tipo de serviço.
#
# 5. O ator preenche os campos com os seguintes dados:
#    - Nome: "Manutenção Preventiva de Painéis";
#    - Descrição: "Inspeção e manutenção preventiva de painéis solares".
#
# 6. O ator seleciona a opção para salvar o cadastro.
#
# 7. O sistema valida o preenchimento dos campos e verifica a existência de nome duplicado conforme as validações disponíveis na interface e no backend.
#
# 8. O sistema envia os dados para cadastro.
#
# 9. O backend cria o tipo de serviço com status inicial verdadeiro.
#
# 10. O sistema fecha o modal e apresenta a mensagem "Tipo de serviço criado com sucesso!".
#
# 11. O sistema atualiza a listagem.
#
# 12. O ator verifica que o novo tipo de serviço aparece na tabela, com o nome e a descrição informados e o status correspondente ao valor inicial verdadeiro.
#
# 13. Para consultar o registro, o ator localiza o tipo de serviço na listagem e confere seus dados.
#
# 14. O ator seleciona a ação "Editar" correspondente ao registro.
#
# 15. O sistema busca os dados atuais do tipo de serviço e abre o modal "Editar Tipo de Serviço", com Nome e Descrição previamente preenchidos.
#
# 16. O ator altera os dados para:
#    - Nome: "Manutenção Preventiva de Sistemas Solares";
#    - Descrição: "Inspeção periódica e manutenção preventiva dos sistemas solares".
#
# 17. O ator seleciona a opção para salvar as alterações.
#
# 18. O sistema remove os espaços em branco das extremidades dos valores, valida os campos e verifica a duplicidade do nome na interface.
#
# 19. O sistema envia a atualização ao backend.
#
# 20. O backend atualiza o registro selecionado, mantendo os campos não enviados inalterados.
#
# 21. O sistema fecha o modal, apresenta a mensagem "Tipo de serviço atualizado com sucesso!" e atualiza a listagem.
#
# 22. O ator verifica que o mesmo registro continua na listagem, agora com o nome e a descrição atualizados.
#
# 23. O ator seleciona a ação "Remover" correspondente ao tipo de serviço atualizado.
#
# 24. O sistema apresenta o modal "Remover Tipo de Serviço" com a pergunta "Tem certeza que deseja remover este tipo de serviço?" e as opções "Remover" e "Cancelar".
#
# 25. O ator confirma a remoção selecionando "Remover".
#
# 26. O sistema apresenta o estado de processamento "Removendo..." e envia a solicitação de remoção ao backend.
#
# 27. O backend verifica se existem Serviços associados ao tipo de serviço que ainda não foram excluídos logicamente.
#
# 28. Como não existem Serviços nessas condições, o backend marca o tipo de serviço como excluído logicamente, sem apagar fisicamente o registro do banco de dados.
#
# 29. O sistema atualiza a listagem e apresenta uma mensagem de sucesso.
#
# 30. O ator verifica que o tipo de serviço removido não aparece mais na listagem.
#
# 🟠 [A1] - CANCELAR O CADASTRO
# ---------------------------------------------------------------
#
# 1. O ator acessa a opção "Adicionar".
# 2. O sistema apresenta o modal de cadastro.
# 3. O ator informa os dados, mas seleciona "Cancelar" antes de salvar.
# 4. O sistema fecha o modal sem enviar a solicitação de cadastro.
# 5. O ator verifica que o tipo de serviço não foi incluído na listagem.
#
# 🟠 [A2] - CANCELAR A EDIÇÃO
# ---------------------------------------------------------------
#
# 1. O ator seleciona a opção "Editar" de um tipo de serviço existente.
# 2. O sistema apresenta o formulário com os dados atuais preenchidos.
# 3. O ator altera um ou mais campos, mas seleciona "Cancelar" antes de salvar.
# 4. O sistema fecha o modal sem enviar a atualização.
# 5. O ator verifica que os dados anteriormente cadastrados permanecem inalterados.
#
# 🟠 [A3] - CANCELAR A REMOÇÃO
# ---------------------------------------------------------------
#
# 1. O ator seleciona a opção "Remover" de um tipo de serviço.
# 2. O sistema apresenta o modal de confirmação.
# 3. O ator seleciona "Cancelar".
# 4. O sistema fecha o modal sem enviar a solicitação de exclusão.
# 5. O ator verifica que o tipo de serviço continua aparecendo na listagem.
#
# 🟠 [A4] - REMOÇÃO IMPEDIDA POR SERVIÇO ASSOCIADO
# ---------------------------------------------------------------
#
# 1. O ator seleciona a opção "Remover" de um tipo de serviço que possui pelo menos um Serviço associado e não excluído logicamente.
# 2. O sistema apresenta o modal de confirmação.
# 3. O ator confirma a remoção.
# 4. O backend identifica o vínculo impeditivo e rejeita a operação, retornando conflito (HTTP 409).
# 5. O sistema apresenta o aviso "Exclusão de tipo de serviço não permitida" e a mensagem de erro retornada pela API, quando disponível.
# 6. O ator verifica que o tipo de serviço permanece na listagem e não foi removido.
#
# 🟠 [A5] - FALHA DURANTE UMA OPERAÇÃO
# ---------------------------------------------------------------
#
# 1. Durante o cadastro, a edição ou a remoção, ocorre uma falha que impede a conclusão da operação.
# 2. O sistema apresenta uma mensagem de erro correspondente à operação.
# 3. O sistema não apresenta mensagem de sucesso para a operação que falhou.
# 4. O ator verifica que os dados exibidos permanecem de acordo com o estado confirmado pelo backend.
#
# 🟣 [RN1] - PERMISSÕES
# ---------------------------------------------------------------
#
# - O cadastro exige autenticação e a permissão SERVICO_ADICIONAR.
# - A listagem exige autenticação e a permissão SERVICO_LISTAR.
# - A edição exige autenticação e a permissão SERVICO_EDITAR.
# - A remoção exige autenticação e a permissão SERVICO_EXCLUIR.
# - A opção do menu "Tipos de Serviço" depende da permissão SERVICO_MENU.
#
# 🟣 [RN2] - CAMPOS DO TIPO DE SERVIÇO
# ---------------------------------------------------------------
#
# - O cadastro utiliza os campos Nome e Descrição.
# - Ambos são obrigatórios na interface de cadastro e no schema de entrada do backend.
# - O formulário de edição também exige Nome e Descrição na interface.
# - O endpoint PUT do backend permite atualizar Nome, Descrição ou ambos, mantendo os campos não enviados com os valores anteriores.
#
# 🟣 [RN3] - DUPLICIDADE E NORMALIZAÇÃO
# ---------------------------------------------------------------
#
# - Na interface, a verificação de duplicidade considera equivalentes nomes que diferem apenas por letras maiúsculas/minúsculas ou acentos.
# - No backend, a verificação prévia compara o nome por igualdade exata e o banco possui restrição de unicidade.
# - Os comportamentos de comparação da interface e do backend não são idênticos.
# - No cadastro, a interface não remove espaços das extremidades antes de validar ou enviar os valores.
# - Na edição, a interface remove os espaços das extremidades de Nome e Descrição antes de validar e enviar.
#
# 🟣 [RN4] - STATUS INICIAL
# ---------------------------------------------------------------
#
# - Um tipo de serviço criado recebe status inicial verdadeiro, correspondente ao estado ativo na representação do módulo.
# - Tipos ativos e inativos continuam aparecendo nas consultas comuns, desde que não tenham sido excluídos logicamente.
#
# 🟣 [RN5] - EXCLUSÃO LÓGICA E RESTRIÇÕES
# ---------------------------------------------------------------
#
# - A remoção é lógica: o registro é marcado como excluído e não é apagado fisicamente do banco de dados.
# - Tipos de serviço excluídos logicamente deixam de aparecer nas consultas comuns do módulo.
# - A remoção é impedida quando existe pelo menos um Serviço associado que não foi excluído logicamente.
# - A verificação de impedimento não considera, isoladamente, a existência de registros associados de PrestadorServico.
#
# 🟡 DADOS DE ENTRADA
# ---------------------------------------------------------------
#
# Cadastro:
# - Nome: Manutenção Preventiva de Painéis
# - Descrição: Inspeção e manutenção preventiva de painéis solares
#
# Edição:
# - Nome: Manutenção Preventiva de Sistemas Solares
# - Descrição: Inspeção periódica e manutenção preventiva dos sistemas solares
#
# Dados de apoio para fluxos alternativos:
# - Nome já cadastrado: Manutenção Preventiva de Painéis
# - Nome informado para verificar duplicidade na interface: MANUTENCAO PREVENTIVA DE PAINEIS
# - Tipo de serviço com Serviço associado não excluído logicamente: registro previamente preparado para o fluxo alternativo A4.
#
# ✅ RESULTADOS ESPERADOS
# ---------------------------------------------------------------
#
# - O tipo de serviço é criado com os dados informados e status inicial verdadeiro.
# - O novo registro aparece na listagem após o cadastro.
# - A consulta da listagem apresenta os dados correspondentes ao registro criado.
# - A edição atualiza Nome e Descrição do mesmo registro, sem criar outro tipo de serviço.
# - O cancelamento da edição mantém os dados anteriores.
# - A remoção confirmada marca o registro como excluído logicamente e faz com que ele deixe de aparecer nas consultas comuns.
# - A remoção de um tipo que possui Serviço não excluído logicamente associado é impedida; o registro permanece disponível.
