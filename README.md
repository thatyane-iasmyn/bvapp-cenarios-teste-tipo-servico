# BVApp — Cenários de Teste: Gestão de Tipos de Serviço

## 1. Sobre o projeto

Este repositório contém a documentação dos cenários de teste do módulo **Gestão de Tipos de Serviço** do BVApp, desenvolvido como parte das atividades avaliativas da disciplina de Engenharia de Testes.

O módulo faz parte da gestão de ordens de serviço da cooperativa de energia solar e é responsável pelo gerenciamento dos tipos de serviço utilizados na manutenção dos ativos.

O objetivo deste projeto é documentar cenários de teste relacionados aos requisitos funcionais do módulo, descrevendo os comportamentos esperados do sistema, os fluxos principais, os fluxos alternativos e as regras de negócio envolvidas.

A documentação foi elaborada com base nos requisitos funcionais e critérios de aceitação organizados no OpenProject, considerando também os comportamentos identificados na implementação do backend e do frontend do BVApp.

## 2. Objetivos

Documentar cenários que permitam verificar os principais comportamentos do módulo, contemplando:

- Cadastro de tipos de serviço;
- Validação dos dados informados;
- Listagem e consulta dos registros;
- Paginação e ordenação;
- Pesquisa de tipos de serviço;
- Visualização detalhada;
- Exportação de informações;
- Edição dos dados cadastrais;
- Alteração de status;
- Remoção lógica dos registros;
- Controle de permissões de acesso.

Cada cenário apresenta uma sequência de ações realizadas pelo ator e os resultados esperados do sistema, incluindo situações alternativas, erros e restrições aplicáveis.

## 3. Escopo

O projeto contempla as funcionalidades pertencentes ao módulo Gestão de Tipos de Serviço do BVApp, organizado nas seguintes Features:

| Feature | Identificador | Funcionalidade |
|---|---|---|
| Cadastro de Tipo de Serviço | 25715 | Permite cadastrar novos tipos de serviço. |
| Consulta de Tipo de Serviço | 25728 | Permite listar, pesquisar, visualizar e exportar tipos de serviço. |
| Atualização de Tipo de Serviço | 25911 | Permite editar dados e alterar o status dos registros. |
| Exclusão de Tipo de Serviço | 25912 | Permite remover logicamente tipos de serviço, respeitando as restrições existentes. |

Os cenários estão relacionados às User Stories e aos critérios de aceitação correspondentes no OpenProject.

## 4. Organização dos arquivos

Os cenários estão organizados em arquivos individuais, seguindo uma estrutura de diretórios que facilita a localização, manutenção e evolução da documentação.

```text
bvapp-cenarios-teste/
│
├── README.md
│
└── tipo_servico/
    ├── __init__.py
    │
    ├── test_uc001_manter_tipo_servico.py
    ├── test_uc002_validar_cadastro_tipo_servico.py
    ├── test_uc003_listar_tipos_servico.py
    ├── test_uc004_paginacao_ordenacao.py
    ├── test_uc005_pesquisar_tipos_servico.py
    ├── test_uc006_visualizar_tipo_servico.py
    ├── test_uc007_editar_tipo_servico.py
    ├── test_uc008_alterar_status_tipo_servico.py
    ├── test_uc009_remover_tipo_servico_restricoes.py
    └── test_uc013_permissoes_acesso_modulo.py
```

## 5. Cenários de teste documentados

Os cenários foram organizados conforme as funcionalidades do módulo, mantendo a identificação individual de cada caso de uso.

| Identificador | Cenário | Descrição |
|---|---|---|
| UC001 | Manter Tipo de Serviço | Descreve o fluxo completo de cadastro, consulta, atualização e remoção de um tipo de serviço. |
| UC002 | Validar cadastro de Tipo de Serviço | Verifica campos obrigatórios, duplicidade, valores compostos por espaços, falhas e cancelamento do cadastro. |
| UC003 | Listar Tipos de Serviço | Verifica a apresentação dos registros, seus dados, status, estados da listagem e permissões. |
| UC004 | Consultar Tipos de Serviço com Paginação e Ordenação | Verifica a navegação entre páginas, alteração da quantidade de registros e ordenação. |
| UC005 | Pesquisar Tipos de Serviço | Verifica a pesquisa por nome, descrição e identificador, além do tratamento do termo informado. |
| UC006 | Visualizar Detalhes de Tipo de Serviço | Verifica a consulta e apresentação dos detalhes de um tipo de serviço selecionado. |
| UC007 | Editar Tipo de Serviço | Verifica o carregamento dos dados atuais, validação, atualização e cancelamento da edição. |
| UC008 | Alterar Status de Tipo de Serviço | Verifica a alteração entre os estados ativo e inativo, incluindo confirmação e feedback. |
| UC009 | Remover Tipo de Serviço e Verificar Restrições | Verifica a remoção lógica, as restrições por serviços associados e os fluxos de confirmação e cancelamento. |
| UC013 | Verificar Permissões de Acesso ao Módulo de Tipo de Serviço | Verifica o acesso ao menu e às funcionalidades de acordo com as permissões do usuário. |

## 6. Estrutura utilizada nos cenários

Os arquivos seguem como referência o formato do exemplo UC001 — Manter Produtos, apresentado na Aula 06 da disciplina de Engenharia de Testes.

Sempre que aplicável, cada cenário apresenta:

- **Identificador e título:** identificação única do cenário.
- **Autor:** responsável pela elaboração.
- **Objetivo:** finalidade do cenário.
- **Requisitos relacionados:** User Stories e critérios de aceitação associados.
- **Ator:** usuário responsável por executar as ações.
- **Pré-condições:** condições necessárias para iniciar o cenário.
- **Fluxo principal (FP):** sequência de ações e resultados esperados para o fluxo principal.
- **Fluxos alternativos (A):** situações alternativas, como erros, cancelamentos, dados inválidos e restrições.
- **Regras de negócio (RN):** condições que o sistema deve respeitar.
- **Dados de entrada:** informações utilizadas nos fluxos descritos.
- **Resultados esperados:** comportamentos que devem ser apresentados pelo sistema.

Os passos são descritos de forma sequencial, identificando as ações do ator e as respostas esperadas do sistema.

## 7. Regras de negócio e tratamento de situações alternativas

Além dos fluxos principais, os cenários contemplam situações que podem alterar o resultado de uma operação, como:

- Tentativa de cadastro com campos obrigatórios não preenchidos;
- Tentativa de cadastro com nome duplicado;
- Pesquisa sem resultados;
- Falhas durante carregamento ou processamento;
- Usuário sem a permissão necessária;
- Cancelamento de operações;
- Tentativa de remoção de registros com serviços associados;
- Consulta de registros inexistentes ou excluídos logicamente.

Quando existe diferença entre o comportamento observado na interface e no backend, essa particularidade é identificada na documentação.

Questões que dependem de esclarecimento dos stakeholders são mantidas como pendências, sem presumir regras de negócio não confirmadas.

## 8. Relação com os requisitos funcionais

Os cenários foram elaborados a partir das User Stories do módulo Gestão de Tipos de Serviço, mantendo a rastreabilidade entre os requisitos funcionais do OpenProject e suas respectivas documentações.

Essa relação permite identificar quais requisitos estão sendo contemplados em cada cenário e facilita futuras revisões e o reaproveitamento da documentação em outras etapas do projeto.

O cenário UC001 contempla conjuntamente as quatro operações do CRUD, conforme solicitado na atividade avaliativa. Os demais cenários detalham comportamentos específicos e situações complementares das funcionalidades.

## 9. Tecnologias e ferramentas

- **Python:** linguagem utilizada na organização dos arquivos de documentação.
- **OpenProject:** ferramenta utilizada para organização dos requisitos funcionais e critérios de aceitação do BVApp.
- **Git e GitHub:** ferramentas utilizadas para versionamento e disponibilização do projeto.

Os arquivos possuem extensão `.py`, mas seu conteúdo é destinado à documentação dos cenários por meio de comentários estruturados. Não representam testes automatizados executáveis.

## 10. Escopo da atividade

Este repositório corresponde à etapa de especificação e organização dos cenários de teste.

Não faz parte do escopo desta entrega:

- Implementar funcionalidades do BVApp;
- Criar interfaces;
- Automatizar testes;
- Executar testes;
- Desenvolver uma aplicação independente para o módulo.

O objetivo é produzir documentação clara, rastreável e organizada, que possa ser utilizada como referência em etapas futuras de Engenharia de Testes.

## 11. Autoria

**Responsável pela elaboração dos cenários:**

Thatyane Iasmyn Andrade Alves

**Curso:** Engenharia de Software — IFPB

**Projeto:** BVApp — Gestão de Tipos de Serviço

**Disciplina:** Engenharia de Testes

---

Este repositório foi desenvolvido como parte da atividade avaliativa de elaboração de cenários de teste do BVApp, com o propósito de documentar e organizar os comportamentos funcionais do módulo Gestão de Tipos de Serviço.