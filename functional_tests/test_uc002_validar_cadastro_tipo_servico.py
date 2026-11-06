
# UC002 - Validar cadastro de Tipo de Serviço
#
# Autor: Thatyane Iasmyn Andrade Alves
#
# Objetivo:
# Verificar as validações realizadas durante o cadastro de um tipo de serviço,
# contemplando o preenchimento dos campos obrigatórios, a identificação
# de nomes duplicados e o comportamento do formulário diante de dados
# inválidos ou falhas na solicitação.
#
# Requisitos relacionados:
# - US 25724 — Cadastro básico de tipo de serviço.
# - US 25917 — Inclusão visual de tipo de serviço.
# - Critérios de aceitação relacionados ao cadastro:
#   - 25718 — Campos obrigatórios.
#   - 25719 — Prevenção de duplicidade.
#   - 25720 — Validação dos campos.
#   - 25721 — Mensagem de sucesso.
#   - 25722 — Cancelamento do cadastro.
#
# Ator:
# - Usuário autenticado com a permissão SERVICO_ADICIONAR.
#
# Pré-condições:
# - O usuário está autenticado no BVApp.
# - O usuário possui a permissão SERVICO_MENU para acessar a opção do módulo.
# - O usuário possui a permissão SERVICO_ADICIONAR.
# - A tela de Tipos de Serviço está acessível.
# - Para verificar duplicidade, existe previamente um tipo de serviço
#   cadastrado com o nome "Manutenção Preventiva de Painéis".
# - Para verificar o comportamento com espaços em branco, não existe
#   previamente um tipo de serviço cujo nome seja composto exclusivamente
#   pelos mesmos espaços utilizados no cenário.
#
# 🟢 [FP] - CADASTRO COM DADOS VÁLIDOS
# ---------------------------------------------------------------
#
# 1. O ator acessa a tela de Tipos de Serviço.
# 2. O ator seleciona a opção "Adicionar".
# 3. O sistema apresenta o modal "Adicionar Tipo de Serviço",
#    com a orientação "Preencha os dados do tipo de serviço".
# 4. O sistema apresenta os campos "Nome do tipo de serviço"
#    e "Descrição do tipo de serviço", ambos identificados como obrigatórios.
# 5. O ator informa os seguintes dados:
#    - Nome: "Inspeção Preventiva de Sistemas Solares";
#    - Descrição: "Verificação periódica das condições de funcionamento
#      dos sistemas solares".
# 6. O ator seleciona a opção para salvar.
# 7. O sistema verifica se os campos possuem valores não vazios
#    e consulta os tipos de serviço existentes para verificar duplicidade
#    do nome.
# 8. O sistema apresenta o estado "Salvando..." durante o envio.
# 9. O backend recebe Nome e Descrição e realiza as validações
#    de entrada e de duplicidade implementadas.
# 10. O cadastro é concluído com sucesso.
# 11. O sistema fecha o modal e apresenta a mensagem
#     "Tipo de serviço criado com sucesso!".
# 12. O ator verifica que o novo tipo de serviço aparece na listagem.
#
# 🟠 [A1] - NOME NÃO INFORMADO
# ---------------------------------------------------------------
#
# 1. O ator abre o formulário de cadastro.
# 2. O ator deixa o campo Nome do tipo de serviço vazio.
# 3. O ator preenche o campo Descrição com
#    "Verificação periódica dos sistemas solares".
# 4. O ator seleciona a opção para salvar.
# 5. O sistema impede o envio do cadastro e apresenta a mensagem
#    "Nome é obrigatório".
# 6. O ator verifica que o tipo de serviço não foi cadastrado.
#
# 🟠 [A2] - DESCRIÇÃO NÃO INFORMADA
# ---------------------------------------------------------------
#
# 1. O ator abre o formulário de cadastro.
# 2. O ator informa o Nome "Inspeção Preventiva de Sistemas Solares".
# 3. O ator deixa o campo Descrição vazio.
# 4. O ator seleciona a opção para salvar.
# 5. O sistema impede o envio do cadastro e apresenta a mensagem
#    "Descrição é obrigatória".
# 6. O ator verifica que o tipo de serviço não foi cadastrado.
#
# 🟠 [A3] - NOME DUPLICADO
# ---------------------------------------------------------------
#
# 1. O ator abre o formulário de cadastro.
# 2. O ator informa o Nome "MANUTENCAO PREVENTIVA DE PAINEIS",
#    considerando que já existe um registro chamado
#    "Manutenção Preventiva de Painéis".
# 3. O ator informa uma descrição válida.
# 4. O ator seleciona a opção para salvar.
# 5. A interface compara os nomes desconsiderando diferenças
#    entre letras maiúsculas/minúsculas e acentos.
# 6. O sistema identifica a duplicidade, impede o envio do cadastro
#    e apresenta a mensagem "Já existe um tipo de serviço com esse nome".
# 7. O ator verifica que nenhum novo registro foi criado.
#
# 🟠 [A4] - CAMPOS PREENCHIDOS SOMENTE COM ESPAÇOS
# ---------------------------------------------------------------
#
# 1. O ator abre o formulário de cadastro.
# 2. O ator informa um ou mais espaços no campo Nome.
# 3. O ator informa um ou mais espaços no campo Descrição.
# 4. O ator seleciona a opção para salvar.
# 5. A interface verifica se os campos estão vazios, mas não remove
#    os espaços antes da validação. Por isso, os valores compostos
#    somente por espaços passam pela verificação de preenchimento.
# 6. O backend também rejeita somente strings exatamente vazias
#    e não remove os espaços no fluxo de criação.
# 7. Como não existe outro registro com o mesmo Nome composto
#    pelos espaços informados, o backend aceita a gravação.
# 8. O sistema conclui o cadastro e apresenta a mensagem
#    "Tipo de serviço criado com sucesso!".
# 9. O ator verifica que o registro foi incluído na listagem.
#
# Observação: este fluxo documenta o comportamento atualmente implementado.
# A aceitação de valores compostos somente por espaços é uma característica
# da validação atual do cadastro.
#
# 🟠 [A5] - FALHA NO ENVIO DO CADASTRO
# ---------------------------------------------------------------
#
# 1. O ator preenche Nome e Descrição com valores válidos
#    e solicita o cadastro.
# 2. Durante a comunicação com o backend ou durante a gravação,
#    ocorre uma falha que impede a conclusão da operação.
# 3. O sistema apresenta uma mensagem de erro correspondente
#    à falha ocorrida.
# 4. O sistema não apresenta a mensagem de sucesso.
# 5. O ator verifica que não recebeu confirmação de que o cadastro
#    foi concluído com sucesso.
#
# 🟠 [A6] - CANCELAR O CADASTRO
# ---------------------------------------------------------------
#
# 1. O ator abre o formulário e preenche um ou ambos os campos.
# 2. Antes de salvar, seleciona "Cancelar".
# 3. O sistema fecha o modal sem enviar a solicitação de cadastro.
# 4. O ator verifica que nenhum registro novo foi criado.
#
# 🟣 [RN1] - CAMPOS OBRIGATÓRIOS
# ---------------------------------------------------------------
#
# - Nome e Descrição são campos obrigatórios no formulário
#   e no schema de criação do backend.
# - Quando o valor é exatamente vazio, a interface impede
#   o envio e apresenta uma mensagem específica para o campo.
# - O backend retorna erro HTTP 400 para Nome ou Descrição
#   exatamente vazios.
#
# 🟣 [RN2] - DUPLICIDADE
# ---------------------------------------------------------------
#
# - A interface consulta os tipos de serviço existentes e compara
#   os nomes desconsiderando maiúsculas/minúsculas e acentos.
# - Quando encontra equivalência na comparação da interface,
#   impede o envio e apresenta "Já existe um tipo de serviço com esse nome".
# - O backend verifica duplicidade por igualdade exata e o banco
#   possui restrição de unicidade.
# - A comparação realizada na interface não é idêntica
#   à verificação realizada pelo backend.
#
# 🟣 [RN3] - ESPAÇOS EM BRANCO NO CADASTRO
# ---------------------------------------------------------------
#
# - No formulário de cadastro, a interface não executa trim()
#   antes de validar ou enviar Nome e Descrição.
# - O backend rejeita strings exatamente vazias, mas não remove
#   espaços no fluxo de cadastro.
# - Portanto, valores compostos somente por espaços não são barrados
#   pelas verificações de vazio atualmente implementadas.
#
# 🟣 [RN4] - FEEDBACK DA OPERAÇÃO
# ---------------------------------------------------------------
#
# - Durante o envio, o botão apresenta "Salvando...".
# - Após sucesso, a interface apresenta
#   "Tipo de serviço criado com sucesso!".
# - Quando ocorre erro na chamada, a interface apresenta
#   uma mensagem de erro correspondente à falha.
# - Cancelar fecha o formulário sem realizar a gravação.
#
# 🟡 DADOS DE ENTRADA
# ---------------------------------------------------------------
#
# Cadastro válido:
# - Nome: Inspeção Preventiva de Sistemas Solares
# - Descrição: Verificação periódica das condições de funcionamento
#   dos sistemas solares
#
# Nome duplicado:
# - Nome já existente: Manutenção Preventiva de Painéis
# - Nome informado: MANUTENCAO PREVENTIVA DE PAINEIS
#
# Campos inválidos:
# - Nome vazio e Descrição preenchida
# - Nome preenchido e Descrição vazia
#
# Campos compostos somente por espaços:
# - Nome: "   "
# - Descrição: "   "
#
# ✅ RESULTADOS ESPERADOS
# ---------------------------------------------------------------
#
# - O cadastro com dados válidos deve ser concluído e apresentar
#   a mensagem de sucesso.
# - O cadastro sem Nome deve ser impedido com a mensagem
#   "Nome é obrigatório".
# - O cadastro sem Descrição deve ser impedido com a mensagem
#   "Descrição é obrigatória".
# - O cadastro de nome considerado duplicado pela comparação
#   da interface deve ser impedido com a mensagem correspondente.
# - O cadastro com campos compostos somente por espaços não é impedido
#   pelas verificações de vazio atuais. Sem conflito de unicidade,
#   o registro pode ser persistido.
# - O cancelamento deve fechar o modal sem criar o registro.
# - Uma falha na operação deve apresentar erro e não deve ser
#   apresentada como sucesso.
