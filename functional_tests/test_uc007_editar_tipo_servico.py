
# UC007 - Editar Tipo de Serviço
#
# Autor: Thatyane Iasmyn Andrade Alves
#
# Objetivo:
# Permitir que um usuário autorizado edite os dados de um tipo de serviço existente,
# verificando o carregamento dos valores atuais, a validação do formulário,
# a atualização dos dados e o retorno apresentado pelo sistema.
#
# Requisitos relacionados:
# - US 25918 — Editar dados de Tipo de Serviço.
# - US 26979 — Edição visual de Tipo de Serviço.
# - US 25730 — Listagem de tipos de serviços.
# - Feature 25911 — Atualização de Tipo de Serviço.
#
# Ator:
# - Usuário autenticado com as permissões SERVICO_MENU, SERVICO_LISTAR e SERVICO_EDITAR.
#
# Pré-condições:
# - O usuário está autenticado no BVApp.
# - O usuário possui as permissões necessárias para acessar a listagem e editar registros.
# - Existe um tipo de serviço cadastrado e não excluído logicamente.
# - Para o fluxo principal, o nome utilizado na alteração não pertence a outro tipo de serviço.
# - Para os fluxos alternativos, existem registros que permitem verificar duplicidade e falhas.
#
# 🟢 [FP] - EDITAR DADOS DE UM TIPO DE SERVIÇO
# ---------------------------------------------------------------
#
# 1. O ator acessa o menu "Tipos de Serviço".
#
# 2. O sistema apresenta a listagem de tipos de serviço.
#
# 3. O ator localiza o registro que deseja editar e seleciona a ação "Editar".
#
# 4. O sistema abre o modal "Editar Tipo de Serviço" e inicia a consulta
#    dos dados atuais do tipo de serviço selecionado pelo identificador.
#
# 5. Enquanto os dados são carregados, o sistema apresenta uma indicação de carregamento.
#
# 6. Após receber os dados, o sistema apresenta os campos Nome e Descrição
#    previamente preenchidos com os valores atuais do registro.
#
# 7. O ator altera os dados para:
#    - Nome: "Manutenção Preventiva de Sistemas Solares";
#    - Descrição: "Inspeção periódica e manutenção preventiva dos sistemas solares".
#
# 8. O ator seleciona a opção para salvar as alterações.
#
# 9. Antes de enviar os dados, a interface remove os espaços em branco
#    existentes no início e no final dos valores de Nome e Descrição.
#
# 10. A interface valida o preenchimento dos campos obrigatórios.
#
# 11. A interface verifica se o nome informado já pertence a outro tipo de serviço,
#     desconsiderando diferenças entre letras maiúsculas/minúsculas e acentos,
#     sem comparar o registro com ele próprio.
#
# 12. O sistema apresenta o estado "Salvando..." durante o envio da atualização.
#
# 13. A interface envia Nome e Descrição ao backend por meio da operação PUT.
#
# 14. O backend realiza suas validações, atualiza o registro identificado
#     e retorna os dados atualizados.
#
# 15. Após o sucesso, o sistema fecha o modal e apresenta a mensagem
#     "Tipo de serviço atualizado com sucesso!".
#
# 16. O sistema atualiza a listagem.
#
# 17. O ator verifica que o registro permanece na listagem com o mesmo identificador,
#     apresentando o Nome e a Descrição atualizados.
#
# 🟠 [A1] - CAMPO OBRIGATÓRIO NÃO PREENCHIDO
# ---------------------------------------------------------------
#
# 1. O ator abre o formulário de edição de um tipo de serviço.
#
# 2. O sistema apresenta Nome e Descrição preenchidos com os dados atuais.
#
# 3. O ator apaga o conteúdo do campo Nome ou do campo Descrição.
#
# 4. O ator tenta salvar a alteração.
#
# 5. A interface identifica o campo obrigatório não preenchido e impede o envio.
#
# 6. O sistema apresenta a mensagem correspondente:
#    - "Nome é obrigatório"; ou
#    - "Descrição é obrigatória".
#
# 7. O ator verifica que o formulário continua disponível para correção
#    e que os dados anteriormente gravados não foram alterados.
#
# 🟠 [A2] - NOME JÁ UTILIZADO POR OUTRO TIPO DE SERVIÇO
# ---------------------------------------------------------------
#
# 1. O ator abre o formulário de edição de um tipo de serviço.
#
# 2. O ator informa um Nome que já pertence a outro registro,
#    considerando também diferenças de maiúsculas/minúsculas ou acentos.
#
# 3. O ator mantém uma Descrição válida e tenta salvar.
#
# 4. A interface identifica a duplicidade, desconsiderando
#    o registro que está sendo editado.
#
# 5. O sistema apresenta "Já existe um tipo de serviço com esse nome"
#    e impede o envio.
#
# 6. O ator verifica que os dados originais permanecem inalterados.
#
# 🟠 [A3] - CANCELAR A EDIÇÃO
# ---------------------------------------------------------------
#
# 1. O ator abre o formulário de edição de um tipo de serviço.
#
# 2. O sistema apresenta os dados atuais preenchidos.
#
# 3. O ator altera Nome e/ou Descrição.
#
# 4. Antes de salvar, seleciona "Cancelar" ou fecha o modal.
#
# 5. O sistema fecha o formulário sem enviar a atualização.
#
# 6. O ator verifica que o registro mantém os dados anteriormente cadastrados.
#
# 🟠 [A4] - FALHA AO CARREGAR OS DADOS PARA EDIÇÃO
# ---------------------------------------------------------------
#
# 1. O ator seleciona a ação "Editar" de um tipo de serviço.
#
# 2. Ocorre uma falha durante a consulta dos dados atuais do registro.
#
# 3. O sistema apresenta a mensagem
#    "Erro ao buscar tipo de serviço para edição".
#
# 4. O formulário não deve ser apresentado como se os dados
#    tivessem sido carregados corretamente.
#
# 🟠 [A5] - REGISTRO NÃO ENCONTRADO DURANTE A ATUALIZAÇÃO
# ---------------------------------------------------------------
#
# 1. O ator inicia a edição de um tipo de serviço.
#
# 2. Antes da atualização, o registro deixa de estar disponível
#    para a operação de edição.
#
# 3. O ator tenta salvar as alterações.
#
# 4. O backend não encontra o registro solicitado e retorna HTTP 404.
#
# 5. A interface apresenta o erro retornado pela operação,
#    sem indicar sucesso.
#
# 6. O ator verifica que a listagem não apresenta os dados
#    como se a atualização tivesse sido concluída.
#
# 🟠 [A6] - ERRO RETORNADO PELO BACKEND AO SALVAR
# ---------------------------------------------------------------
#
# 1. O ator informa dados no formulário e seleciona a opção para salvar.
#
# 2. Ocorre uma falha na atualização ou o backend rejeita os dados,
#    por exemplo, por conflito de unicidade.
#
# 3. A interface apresenta a mensagem de erro retornada pela operação.
#
# 4. O sistema não apresenta a mensagem de sucesso.
#
# 5. O ator verifica que os dados apresentados permanecem de acordo
#    com o estado confirmado pelo backend.
#
# 🟠 [A7] - USUÁRIO SEM PERMISSÃO PARA EDITAR
# ---------------------------------------------------------------
#
# 1. O ator está autenticado e acessa a listagem,
#    mas não possui SERVICO_EDITAR.
#
# 2. O sistema não disponibiliza a ação de edição para esse usuário.
#
# 3. Caso uma solicitação de edição alcance o backend sem a permissão exigida,
#    o backend deve impedir a operação.
#
# 4. O ator verifica que não consegue alterar os dados do tipo de serviço.
#
# 🟣 [RN1] - PERMISSÕES
# ---------------------------------------------------------------
#
# - O acesso ao menu depende da permissão SERVICO_MENU.
# - A listagem depende da permissão SERVICO_LISTAR.
# - A edição exige usuário autenticado e a permissão SERVICO_EDITAR.
#
# 🟣 [RN2] - CAMPOS E VALIDAÇÃO NA INTERFACE
# ---------------------------------------------------------------
#
# - O formulário de edição apresenta Nome e Descrição previamente preenchidos.
# - Os dois campos são obrigatórios na interface.
# - A interface remove espaços em branco das extremidades dos valores
#   antes de validar e enviar.
# - A interface verifica duplicidade desconsiderando diferenças de caixa
#   e acentos, sem comparar o registro com ele próprio.
#
# 🟣 [RN3] - COMPORTAMENTO DO BACKEND
# ---------------------------------------------------------------
#
# - O endpoint PUT aceita Nome, Descrição ou ambos os campos.
# - Os campos não enviados permanecem com seus valores anteriores.
# - O backend remove espaços das extremidades antes de gravar os valores recebidos.
# - O backend verifica duplicidade do Nome por igualdade exata
#   e respeita a restrição de unicidade do banco de dados.
# - Essa comparação não é idêntica à validação da interface.
# - O endpoint retorna HTTP 200 com os dados atualizados quando a operação é concluída.
# - Quando o registro não é encontrado pela operação de atualização,
#   o backend retorna HTTP 404.
#
# 🟣 [RN4] - COMPORTAMENTO DA EDIÇÃO PELA INTERFACE
# ---------------------------------------------------------------
#
# - A interface exige o preenchimento dos dois campos, Nome e Descrição.
# - A interface envia os dois campos na operação de edição.
# - A possibilidade de atualização parcial existe no backend,
#   mas não é disponibilizada pelo formulário atual.
#
# 🟡 DADOS DE ENTRADA
# ---------------------------------------------------------------
#
# Tipo de serviço previamente cadastrado:
# - ID: 201.
# - Nome: Inspeção Preventiva.
# - Descrição: Verificação periódica dos sistemas solares.
#
# Dados da edição:
# - Nome: Manutenção Preventiva de Sistemas Solares.
# - Descrição: Inspeção periódica e manutenção preventiva dos sistemas solares.
#
# Dados para fluxos alternativos:
# - Nome duplicado: Manutenção Corretiva.
# - Nome com variação de caixa/acentos:
#   MANUTENCAO CORRETIVA.
# - Campo Nome vazio.
# - Campo Descrição vazio.
# - Identificador inexistente: 999999.
#
# ✅ RESULTADOS ESPERADOS
# ---------------------------------------------------------------
#
# - O formulário deve carregar Nome e Descrição atuais do registro selecionado.
# - A interface deve exigir o preenchimento dos dois campos.
# - A interface deve remover espaços das extremidades e verificar duplicidade
#   conforme sua regra de comparação.
# - A atualização bem-sucedida deve preservar o identificador
#   e alterar os dados do registro selecionado.
# - O sistema deve apresentar "Tipo de serviço atualizado com sucesso!"
#   após a conclusão.
# - O cancelamento não deve enviar nem gravar as alterações.
# - Erros de carregamento ou atualização devem ser apresentados
#   sem mensagem de sucesso.
# - Usuários sem SERVICO_EDITAR não devem conseguir executar a edição.
