# Padrão obrigatório — Cabeçalho compartilhado e navegação

Este padrão complementa a skill **NECOOP Site Maintenance V2** e deve ser aplicado a toda página do site, inclusive páginas e matérias dentro de `/posts/`. O problema de links que incorporam indevidamente `/posts/` já se repetiu; portanto, tratar cabeçalho e navegação como componente estrutural crítico, não como ajuste pontual.

## 1. Fonte única de verdade

- `header.html` é a única fonte do conteúdo do cabeçalho institucional: logotipo, textos, links, menus e elementos de navegação.
- Não copiar nem recriar esses elementos em páginas individuais.
- Toda alteração visual ou funcional do cabeçalho deve ocorrer no componente compartilhado.
- Páginas devem conter apenas o ponto de inserção e a chamada ao carregador comum.

## 2. Carregador compartilhado

- Usar um único script reutilizável (por exemplo, `assets/js/header-loader.js`) para carregar `header.html`.
- Não manter implementações `fetch()` diferentes e inline em cada página.
- A URL do componente e dos recursos deve ser construída de forma robusta a partir da raiz do site, não do diretório da página atual.
- Para GitHub Pages no domínio do projeto NECOOP, validar a raiz pública real antes de adotar caminhos absolutos. Não presumir que `/` sempre corresponda à raiz do repositório em qualquer ambiente.
- Se houver ambientes local, preview e produção, o carregador deve contemplar corretamente a base path de cada um, sem produzir URLs com `/posts/` indevido.

## 3. Links e recursos

- Links de navegação para páginas institucionais devem apontar para os destinos canônicos na raiz publicada, nunca ser resolvidos relativamente ao diretório `/posts/`.
- Exemplo: “Sobre o NECOOP” deve abrir `https://necoop-uffs.github.io/sobre.html`, e não `https://necoop-uffs.github.io/posts/sobre.html`.
- O logotipo e demais recursos compartilhados também devem resolver corretamente em páginas de raiz e em `/posts/`.
- Não corrigir o problema adicionando cópias de `header.html`, logo ou páginas institucionais dentro de `/posts/`.

## 4. Auditoria obrigatória antes da publicação

Antes de aprovar qualquer alteração no cabeçalho ou criar/alterar páginas:

1. inventariar todas as páginas HTML que inserem o cabeçalho;
2. identificar e eliminar chamadas inline divergentes ao cabeçalho;
3. confirmar que todas usam o carregador compartilhado;
4. verificar os `href` e `src` finais após a inserção do componente, não apenas o texto do arquivo-fonte;
5. testar pelo menos uma página na raiz e uma página dentro de `/posts/`;
6. confirmar logotipo visível, navegação funcional e ausência de destinos com `/posts/` indevido;
7. verificar também URLs diretas dos recursos compartilhados e erros de console/rede.

## 5. Teste de regressão obrigatório

A correção não está concluída apenas porque o commit foi feito ou o arquivo-fonte parece correto. Após o deploy do GitHub Pages, abrir e testar:

- `https://necoop-uffs.github.io/index.html`
- `https://necoop-uffs.github.io/sobre.html`
- uma matéria publicada em `/posts/`

Em cada página, testar o logotipo e todos os links do cabeçalho. Registrar URL testada, resultado e commit correspondente. Se qualquer link gerar `/posts/` antes de uma página da raiz, ou se o cabeçalho/logo não carregar, interromper a publicação de novas alterações e diagnosticar versão servida, base path, cache e carregamento.

## 6. Regra contra correções às cegas

Como esse defeito já ocorreu repetidamente:

- não fazer correções isoladas em páginas sem antes identificar a causa comum;
- não declarar resolvido com base apenas no código local ou no merge;
- não presumir que o cache seja a causa sem comparar o recurso efetivamente servido;
- preservar o diagnóstico e o resultado dos testes no registro da alteração.
