# Projeto de Ouvidoria Fase 2

Este projeto é uma aplicação de ouvidoria via CLI (Interface de Linha de Comando) desenvolvida em Python para gerenciar registros e interações com a ouvidoria. Este README explica a estrutura do projeto e a razão para a divisão dos arquivos e pastas, facilitando o entendimento e a manutenção do código.

## Estrutura do Projeto

O projeto está organizado da seguinte maneira:


Cada arquivo tem uma função específica dentro da aplicação, com responsabilidades bem definidas para facilitar a legibilidade, manutenção e colaboração do time.

### Arquivos e Funções

#### `main.py`
- **Função:** O arquivo `main.py` é o ponto de entrada da aplicação. 
- **Responsabilidade:** Ele é responsável por exibir o menu principal da ouvidoria, permitindo que o usuário navegue entre as diferentes funcionalidades do sistema.
- **Importações:** Este arquivo importa métodos e funções dos demais arquivos (`use_cases.py`, `helpers.py` e `operacoesbd.py`), garantindo que as funcionalidades estejam centralizadas e acessíveis a partir do menu.
- **Justificativa:** Centralizar o menu no `main.py` facilita a organização e permite uma única interface de controle da aplicação, enquanto delega as operações específicas para os módulos especializados.

#### `helpers.py`
- **Função:** Este arquivo contém funções auxiliares, conhecidas como "helpers".
- **Responsabilidade:** Armazena funções genéricas que podem ser usadas em diversas partes do projeto, como manipulação de strings, validação de entradas e formatação de dados.
- **Justificativa:** Manter as funções auxiliares em `helpers.py` permite que o código seja mais reutilizável e evita duplicação. Isso também facilita a atualização de funções comuns em um único local, reduzindo o esforço de manutenção.

#### `use_cases.py`
- **Função:** Este arquivo armazena os "casos de uso" ou as funcionalidades principais da ouvidoria.
- **Responsabilidade:** Aqui estão implementadas as operações principais, como cadastrar reclamações, consultar histórico, responder aos registros da ouvidoria, entre outras.
- **Justificativa:** Centralizar os casos de uso em um único arquivo permite uma visão clara das funcionalidades principais, facilitando a implementação e o entendimento de quais operações a ouvidoria suporta. Dessa forma, o `main.py` pode chamar diretamente os casos de uso, mantendo uma separação entre a lógica da aplicação e a interface.

#### `operacoesbd.py`
- **Função:** Este arquivo é responsável pela interação com o banco de dados.
- **Responsabilidade:** Contém as funções que executam operações CRUD (Create, Read, Update, Delete) no banco de dados, como adicionar, buscar, atualizar e remover registros.
- **Justificativa:** Manter a lógica de banco de dados separada permite que a aplicação seja mais modular e facilita a substituição ou alteração da camada de dados sem impactar as demais partes do sistema. Além disso, melhora a segurança e a manutenção ao encapsular diretamente as operações do banco.

### Benefícios da Estrutura

A divisão do projeto dessa forma traz alguns benefícios para o desenvolvimento em equipe:

1. **Modularidade:** Cada arquivo tem uma função bem definida, facilitando a identificação de onde cada funcionalidade está implementada.
2. **Manutenibilidade:** A separação em arquivos distintos torna o código mais organizado e facilita a manutenção. Quando uma mudança é necessária, é possível localizar rapidamente a seção específica do código.
3. **Facilidade de Colaboração:** Com responsabilidades separadas, os membros do grupo podem trabalhar em diferentes arquivos ao mesmo tempo, minimizando conflitos de versão.
4. **Escalabilidade:** A estrutura permite que novas funcionalidades sejam adicionadas com mais facilidade, seja expandindo `use_cases.py` para novos casos de uso, seja adicionando novos helpers ou operações de banco de dados.

### Instruções para Rodar o Projeto

Para rodar a aplicação, entre na pasta `src`:

```bash
cd src/
```

e execute o seguinte comando:
```bash
python3 main.py
```

ou clique no botão de ▶️ da sua IDE.

