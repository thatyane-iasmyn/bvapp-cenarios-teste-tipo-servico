# UC005 - Pesquisar Tipos de Serviço
#
# Autor: Thatyane Iasmyn Andrade Alves
#
# Objetivo:
# Permitir que um usuário autorizado pesquise tipos de serviço por meio
# de um campo textual, verificando os resultados correspondentes ao termo
# informado e a integração da pesquisa com a listagem paginada e ordenada.
#
# Requisitos relacionados:
# - US 28369 — Pesquisar e Filtrar Tipos de Serviço.
# - US 25730 — Listagem de tipos de serviços.
# - US 25913 — Consulta de Tipos de Serviço.
# - Feature 25728 — Consulta de Tipo de Serviço.
# - CA09 — Pesquisa (novo critério da Feature 25728).
#
# Ator:
# - Usuário autenticado com a permissão SERVICO_LISTAR.
#
# Pré-condições:
# - O usuário está autenticado no BVApp.
# - O usuário possui as permissões SERVICO_MENU e SERVICO_LISTAR.
# - Existem tipos de serviço não excluídos logicamente cadastrados
#   com nomes, descrições e identificadores conhecidos.
# - Os dados de exemplo permitem pesquisar por correspondência parcial
#   em Nome, Descrição e ID.
#
# 🟢 [FP] - PESQUISAR TIPOS DE SERVIÇO
# ---------------------------------------------------------------
#
# 1. O ator acessa o sistema BVApp.
#
# 2. O ator seleciona a opção "Tipos de Serviço" no menu lateral.
#
# 3. O sistema apresenta a listagem de tipos de serviço.
#
# 4. O sistema disponibiliza um campo de pesquisa com o placeholder
#    "Buscar por nome ou descrição".
#
# 5. O ator informa no campo de pesquisa o termo "Preventiva".
#
# 6. O ator envia o formulário de pesquisa.
#
# 7. A interface remove os espaços em branco das extremidades
#    do termo informado e envia o parâmetro de busca junto com
#    os parâmetros de paginação e ordenação.
#
# 8. O backend realiza a pesquisa por correspondência parcial
#    nos campos Nome, Descrição e ID, utilizando a busca textual
#    implementada.
#
# 9. O sistema atualiza a listagem e apresenta os registros
#    correspondentes ao termo informado.
#
# 10. O ator verifica que os registros apresentados correspondem
#     ao termo pesquisado e que os demais registros não correspondentes
#     não são exibidos.
#
# 11. O ator verifica que os resultados continuam sujeitos
#     à paginação e à ordenação da listagem.
#
# 🟠 [A1] - PESQUISAR POR PARTE DO NOME
# ---------------------------------------------------------------
#
# 1. O ator informa apenas parte do nome de um tipo de serviço
#    no campo de pesquisa.
#
# 2. O ator envia a pesquisa.
#
# 3. O sistema apresenta os registros cujo Nome contém
#    o trecho informado.
#
# 4. O ator verifica que a correspondência parcial foi considerada,
#    sem exigir que o termo corresponda ao nome completo.
#
# 🟠 [A2] - PESQUISAR POR PARTE DA DESCRIÇÃO
# ---------------------------------------------------------------
#
# 1. O ator informa um trecho existente na descrição de um
#    tipo de serviço.
#
# 2. O ator envia a pesquisa.
#
# 3. O sistema apresenta os registros cuja Descrição contém
#    o trecho informado.
#
# 4. O ator verifica que o resultado corresponde à descrição pesquisada.
#
# 🟠 [A3] - PESQUISAR PELO IDENTIFICADOR
# ---------------------------------------------------------------
#
# 1. O ator informa no campo de pesquisa o identificador
#    de um tipo de serviço.
#
# 2. O ator envia a pesquisa.
#
# 3. O backend também considera o campo ID na busca,
#    embora o placeholder da interface mencione somente Nome e Descrição.
#
# 4. O sistema apresenta o registro correspondente ao identificador
#    informado, caso esteja disponível e não tenha sido excluído
#    logicamente.
#
# Observação: este fluxo registra um comportamento adicional
# implementado pelo backend. A interface não informa explicitamente
# que o identificador também pode ser utilizado na pesquisa.
#
# 🟠 [A4] - PESQUISA SEM DIFERENCIAR MAIÚSCULAS E MINÚSCULAS
# ---------------------------------------------------------------
#
# 1. O ator realiza uma pesquisa utilizando um termo com letras minúsculas.
#
# 2. O ator realiza novamente a pesquisa utilizando o mesmo termo
#    com letras maiúsculas ou combinação diferente de caixa.
#
# 3. O backend utiliza o operador ILIKE na pesquisa textual.
#
# 4. O ator verifica que a pesquisa não diferencia maiúsculas
#    e minúsculas no comportamento implementado pelo banco utilizado.
#
# 🟠 [A5] - PESQUISA COM ESPAÇOS NAS EXTREMIDADES
# ---------------------------------------------------------------
#
# 1. O ator informa um termo de pesquisa com espaços antes
#    e/ou depois do texto.
#
# 2. O ator envia o formulário.
#
# 3. A interface remove os espaços das extremidades
#    antes de enviar o parâmetro de busca.
#
# 4. O sistema apresenta os resultados correspondentes
#    ao termo sem os espaços externos.
#
# 🟠 [A6] - PESQUISA SEM RESULTADOS
# ---------------------------------------------------------------
#
# 1. O ator informa um termo que não corresponde ao Nome,
#    à Descrição ou ao ID de nenhum tipo de serviço disponível.
#
# 2. O ator envia a pesquisa.
#
# 3. O backend retorna uma consulta sem registros correspondentes.
#
# 4. O sistema apresenta a mensagem
#    "Nenhum tipo de serviço encontrado.".
#
# 5. O ator verifica que nenhum registro que não corresponda
#    ao termo foi apresentado.
#
# 🟠 [A7] - LIMPAR A PESQUISA
# ---------------------------------------------------------------
#
# 1. O ator realizou uma pesquisa e está visualizando
#    os resultados filtrados.
#
# 2. O ator apaga manualmente o texto do campo de pesquisa.
#
# 3. O ator envia novamente o formulário.
#
# 4. A interface envia a consulta sem o termo de busca.
#
# 5. O sistema apresenta novamente os registros disponíveis,
#    respeitando a paginação e a ordenação vigentes.
#
# Observação: a interface não apresenta um botão separado
# de limpar pesquisa; o texto deve ser apagado manualmente
# e o formulário enviado novamente.
#
# 🟠 [A8] - PESQUISA COM TERMO VAZIO OU SOMENTE ESPAÇOS
# ---------------------------------------------------------------
#
# 1. O ator deixa o campo de pesquisa vazio ou informa
#    somente espaços em branco.
#
# 2. O ator envia o formulário.
#
# 3. A interface remove os espaços das extremidades.
#
# 4. Quando o termo fica vazio, a consulta é enviada sem
#    uma condição textual efetiva de pesquisa.
#
# 5. O sistema apresenta novamente a listagem sem restringir
#    os resultados pelo termo anterior.
#
# 🟠 [A9] - FALHA AO REALIZAR A PESQUISA
# ---------------------------------------------------------------
#
# 1. O ator informa um termo e envia a pesquisa.
#
# 2. Durante a consulta, ocorre uma falha na comunicação
#    ou no processamento da solicitação.
#
# 3. O sistema apresenta o feedback de erro da consulta.
#
# 4. O ator verifica que a falha não é apresentada como
#    se fosse uma pesquisa sem resultados.
#
# 🟣 [RN1] - PERMISSÃO
# ---------------------------------------------------------------
#
# - A pesquisa é realizada na listagem de tipos de serviço.
# - O acesso ao menu depende de SERVICO_MENU.
# - A pesquisa e a consulta dos resultados exigem autenticação
#   e SERVICO_LISTAR.
#
# 🟣 [RN2] - CAMPOS PESQUISADOS
# ---------------------------------------------------------------
#
# - O campo visível na interface possui o placeholder
#   "Buscar por nome ou descrição".
# - O backend utiliza o parâmetro `busca` e pesquisa nos campos
#   Nome, Descrição e ID.
# - A pesquisa considera correspondência parcial.
# - O backend utiliza ILIKE, realizando a pesquisa sem diferenciar
#   maiúsculas e minúsculas no banco utilizado.
#
# 🟣 [RN3] - TRATAMENTO DO TERMO
# ---------------------------------------------------------------
#
# - A interface remove espaços em branco das extremidades
#   do termo antes de enviá-lo.
# - Um termo vazio não restringe a consulta por texto.
# - Não há botão separado de limpeza; o usuário apaga o texto
#   e envia novamente o formulário.
#
# 🟣 [RN4] - INTEGRAÇÃO COM A LISTAGEM
# ---------------------------------------------------------------
#
# - A pesquisa utiliza a mesma consulta paginada da listagem.
# - O parâmetro de busca é enviado junto com os parâmetros
#   de paginação e ordenação.
# - A ordenação aceita Nome ou Descrição, em ordem crescente
#   ou decrescente.
# - Tipos ativos e inativos podem aparecer nos resultados,
#   desde que não tenham sido excluídos logicamente.
#
# 🟡 DADOS DE ENTRADA
# ---------------------------------------------------------------
#
# Registros previamente cadastrados para a pesquisa:
#
# - ID: 101;
#   Nome: Inspeção Preventiva;
#   Descrição: Verificação periódica dos sistemas solares.
#
# - ID: 102;
#   Nome: Manutenção Corretiva;
#   Descrição: Correção de falhas identificadas nos equipamentos.
#
# - ID: 103;
#   Nome: Limpeza Técnica;
#   Descrição: Limpeza e conservação de painéis solares.
#
# Termos de pesquisa:
# - Nome: Preventiva.
# - Descrição: equipamentos.
# - ID: 102.
# - Variação de caixa: preventiva / PREVENTIVA.
# - Espaços externos: "  Corretiva  ".
# - Sem resultado: termo inexistente nos registros.
# - Limpeza: campo vazio ou contendo somente espaços.
#
# ✅ RESULTADOS ESPERADOS
# ---------------------------------------------------------------
#
# - A pesquisa deve considerar correspondência parcial em Nome,
#   Descrição e ID, conforme a implementação atual.
# - A pesquisa deve utilizar o parâmetro enviado com espaços
#   das extremidades removidos pela interface.
# - A busca deve considerar maiúsculas e minúsculas conforme
#   o operador ILIKE utilizado pelo backend.
# - A interface deve apresentar somente os registros correspondentes
#   ao termo pesquisado.
# - A pesquisa deve permanecer integrada à paginação e à ordenação.
# - A pesquisa pelo ID deve ser possível pelo backend,
#   embora o placeholder mencione Nome e Descrição.
# - Quando não houver resultados, deve ser apresentada
#   a mensagem "Nenhum tipo de serviço encontrado.".
# - Ao apagar o termo e enviar novamente o formulário,
#   a listagem deve voltar a apresentar os registros sem
#   a restrição textual.
# - Falhas na consulta devem ser apresentadas como erros,
#   não como ausência de resultados.