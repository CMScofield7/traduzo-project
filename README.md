# Traduzo - Aplicativo de Tradução em Flask

Bem-vindo ao "Traduzo", um aplicativo desenvolvido em Flask que oferece serviços de tradução. Este projeto foi criado como parte do curso da Trybe para demonstrar o uso do framework Flask na criação de uma API e seguir a arquitetura Model-View-Controller (MVC).

## Objetivo

O objetivo do "Traduzo" é fornecer uma plataforma simples e eficaz para traduzir texto de um idioma para outro. O aplicativo é uma API de tradução que oferece as seguintes funcionalidades:

**Tradução de Texto**: Os usuários podem enviar um texto a ser traduzido, especificando o idioma de origem e o idioma de destino.

## Arquitetura MVC

O "Traduzo" segue a arquitetura Model-View-Controller (MVC), que organiza o código em três componentes principais:

- **Model**: Lida com a lógica de negócios e a manipulação dos dados. Neste projeto, o modelo trata das traduções e do histórico de traduções.

- **View**: Lida com a apresentação dos dados ao usuário. Em Flask, as visualizações são representadas pelas rotas que determinam como os resultados da API são exibidos.

- **Controller**: Faz a ponte entre o modelo e a visualização. É responsável por receber as solicitações dos usuários, processá-las usando o modelo e renderizar a resposta apropriada para a visualização.

## Executando o Projeto

Para executar o projeto localmente, siga as instruções abaixo:

1. Clone este repositório.

2. Certifique-se de que o Python esteja instalado no teu sistema.

3. Instale as dependências do projeto (preferencialmente num ambiente virtual) com o seguinte comando:
   ```shell
   pip install -r requirements.txt
   ```


<!-- Olá, Tryber!
Esse é apenas um arquivo inicial para o README do seu projeto.
É essencial que você preencha esse documento por conta própria, ok?
Não deixe de usar nossas dicas de escrita de README de projetos, e deixe sua criatividade brilhar!
:warning: IMPORTANTE: você precisa deixar nítido:
- quais arquivos/pastas foram desenvolvidos por você; 
- quais arquivos/pastas foram desenvolvidos por outra pessoa estudante;
- quais arquivos/pastas foram desenvolvidos pela Trybe.
-->
