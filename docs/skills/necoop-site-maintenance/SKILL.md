# Skill: NECOOP Site Maintenance V2

## Purpose

Manter e evoluir o site do Núcleo de Estudos em Cooperação (NECOOP) como plataforma institucional e de conhecimento, articulando pesquisa, extensão, formação, acervo, publicações, notícias, projetos, monitoramento temático e publicação controlada no GitHub Pages.

A skill deve funcionar como **protocolo operacional de atualização de páginas**, não apenas como orientação geral de manutenção.

## Core principles

1. **Local-first.** Usar processamento local sempre que possível; usar IA para interpretação, síntese, classificação, curadoria, produção editorial e raciocínio contextual.
2. **Published-first diagnosis.** Nunca presumir que arquivo local, `HEAD`, branch ou versão de desenvolvimento corresponde ao site público.
3. **Incremental evolution.** Evoluir a versão publicada de forma incremental, preservando o que já funciona.
4. **Human editorial authority.** O responsável humano decide ou aprova as escolhas editoriais institucionais, especialmente fotografias e sua associação às seções.
5. **Originals are immutable.** Nunca alterar os arquivos originais do acervo para preparar material para o site.
6. **Every change is traceable and reversible.** Toda alteração relevante deve ser rastreável pelo Git ou por registro de trabalho e deve poder ser revertida.
7. **Stop on ambiguity.** Dúvidas sobre versão publicada, arquivo ativo, imagem, branch, commit ou escopo devem interromper a edição até serem resolvidas.

## Project storage map

O projeto possui duas áreas físicas principais, com funções distintas.

### A. Repositório Git do site

`/home/pedro/Documentos/2026/A - Projetos/NECOOP Site e observatório/necoop-uffs.github.io`

Função: código, HTML, CSS, conteúdos e cópias de recursos efetivamente preparados para o site e versionados/publicáveis.

### B. Acervo visual

`/home/pedro/Cloud-Drive/Necoop web/acervo_visual/`

Função: acervo mestre de fotografias e recursos visuais candidatos ou históricos.

**Regra:** o acervo visual não é o diretório de publicação do site.

### Fluxo padrão de recursos visuais

```text
ACERVO VISUAL
    ↓
CANDIDATAS
    ↓
PRANCHA AUTOMÁTICA
    ↓
SELEÇÃO DO USUÁRIO
    ↓
MATRIZ EDITORIAL
    ↓
CÓPIA/PREPARAÇÃO PARA WEB
    ↓
GIT
    ↓
PÁGINA
```

Não colocar fotografias candidatas diretamente nas pastas de publicação do Git apenas para testá-las.

## Architecture

- **Acervo visual/Cloud-Drive:** preservação e fonte dos recursos originais.
- **Local processing:** inventário, hashes, metadados, conversão, redimensionamento, orientação, deduplicação, índices e logs.
- **Obsidian:** sistema geral de conhecimento; a área NECOOP é um espaço especializado.
- **AI:** síntese, interpretação, classificação, relações entre documentos, curadoria e produção editorial, sem substituir decisões editoriais humanas institucionais.
- **GitHub:** versionamento e publicação dos conteúdos do site.
- **GitHub Pages:** distribuição pública.

## Operational workflow

Toda atualização relevante de página deve seguir esta sequência:

```text
PEDIDO
  ↓
GATE 0 — ESTADO PUBLICADO × LOCAL
  ↓
GATE 1 — ESCOPO
  ↓
DIAGNÓSTICO DA PÁGINA
  ↓
PREPARAÇÃO DE RECURSOS
  ↓
SELEÇÃO EDITORIAL HUMANA
  ↓
PREPARAÇÃO DAS CÓPIAS
  ↓
IMPLEMENTAÇÃO
  ↓
TESTE LOCAL
  ↓
VALIDAÇÃO HUMANA
  ↓
GATE GIT
  ↓
COMMIT
  ↓
FETCH / DIAGNÓSTICO DE DIVERGÊNCIA
  ↓
PUSH
  ↓
VERIFICAÇÃO PÚBLICA
  ↓
REGISTRO DA ALTERAÇÃO
```

Nenhuma etapa posterior deve mascarar uma falha de etapa anterior.

# Module 0 — State identification

## GATE 0 — Identificar o estado atual antes de editar

Antes de alterar HTML, CSS, imagens ou estrutura:

1. acessar a URL pública correspondente;
2. verificar conteúdo e layout efetivamente carregados;
3. identificar a URL exata da página-alvo;
4. identificar branch e commit remoto relevantes;
5. verificar branch e commit locais;
6. verificar `git status`;
7. verificar diferenças local/remoto;
8. procurar versões V1, V2, V2.x, backups ou outras cópias relevantes;
9. determinar qual versão será a base da evolução.

Para a Home, verificar explicitamente:

`https://necoop-uffs.github.io/index.html`

**Nunca considerar automaticamente `HEAD`, arquivo aberto no editor, backup ou cópia local mais recente como versão publicada.**

Se houver ambiguidade, parar.

# Module 1 — Scope and baseline

## GATE 1 — Definir escopo

Registrar antes da edição:

```text
Página-alvo:
Objetivo:
Elementos a alterar:
Elementos que não serão alterados:
Recursos necessários:
```

Trabalhar apenas dentro do escopo definido.

## Linha de base

Antes de uma alteração substantiva:

- executar/verificar `git status`;
- verificar commits recentes relevantes;
- verificar `git diff` quando houver alterações;
- identificar backups;
- confirmar existência dos recursos referenciados;
- preservar alterações locais legítimas.

Não apagar ou sobrescrever trabalho local sem diagnóstico.

# Module 2 — Page diagnosis

Antes da implementação, diagnosticar a página-alvo em quatro dimensões:

### Estrutura

- HTML;
- CSS relacionado;
- imagens;
- links;
- títulos e seções.

### Conteúdo

- o que existe;
- o que falta;
- duplicações;
- informações potencialmente desatualizadas;
- coerência com a arquitetura do site.

### Visual

- hierarquia;
- espaçamento;
- tipografia;
- imagens;
- cards;
- contraste;
- responsividade;
- coerência com a identidade existente.

### Editorial

- o que a página comunica;
- para quem comunica;
- relação com pesquisa, extensão, formação e território;
- coerência com o papel do NECOOP como plataforma de conhecimento.

# Module 3 — Visual archive and image selection

## Regra de autoridade editorial

**A seleção final das fotografias e a associação fotografia → página/seção são decisões do usuário/responsável humano. A IA não deve escolher autonomamente a fotografia final nem atribuir uma atividade específica apenas pela aparência da imagem.**

A IA pode localizar, organizar, catalogar, preparar, verificar e apresentar candidatos.

Quando decisões de seleção já estiverem registradas no projeto, reutilizá-las; não pedir novamente escolhas já estabelecidas.

Uma mesma fotografia pode ser usada em mais de uma temática quando isso tiver sido decidido/aprovado editorialmente.

## Prioridade das imagens

Quando disponíveis, priorizar:

1. fotografias próprias/históricas do NECOOP;
2. fotografias existentes no acervo visual;
3. outros recursos documentais devidamente identificados;
4. imagens externas somente quando justificadas e com fonte/licença adequadamente verificadas.

Não substituir fotografia documental por imagem gerada por IA.

## Geração automática de prancha

A skill deve prever uma ferramenta local de geração de prancha, inicialmente denominada:

`gerar_prancha_necoop.py`

Entrada:
- a ferramenta deve receber explicitamente o diretório de candidatas a processar;
- não deve varrer automaticamente todo o acervo quando usada para uma seleção específica.

Estrutura operacional do fluxo de pranchas:

`/home/pedro/Cloud-Drive/Necoop web/acervo_visual/_processamento_pranchas/`

com:

```text
candidatos/
pranchas/
inventarios/
selecoes/
```

As saídas de trabalho devem permanecer nessa camada operacional, sem modificar os originais do acervo.

A ferramenta deve:

- localizar imagens candidatas;
- gerar miniaturas;
- preservar proporções;
- numerar cada imagem de maneira inequívoca;
- exibir nome do arquivo;
- informar, quando possível, dimensões e orientação;
- gerar uma prancha visual única ou conjunto de pranchas quando o volume exigir;
- gerar inventário textual/CSV correspondente;
- nunca alterar o arquivo original.

A prancha é um **instrumento de seleção humana**, não uma seleção automatizada pela IA.

## Matriz editorial de imagens

Depois da seleção humana, registrar:

| ID | Arquivo original | Página | Seção | Status |
|---:|---|---|---|---|
| ... | ... | ... | ... | selecionada |

A matriz deve permitir reconstruir posteriormente por que uma determinada imagem foi usada em determinada seção.

# Module 4 — Image preparation

Somente depois da seleção humana, preparar as cópias para o site.

Operações permitidas sobre cópias:

- cópia;
- renomeação;
- redimensionamento;
- compressão;
- conversão de formato;
- correção técnica de orientação;
- corte, quando explicitamente solicitado ou necessário para adequação visual.

Fluxo:

```text
ORIGINAL
   ≠
CÓPIA DE TRABALHO
   ≠
VERSÃO WEB
```

## Regra de orientação e edição

Quando o usuário fornecer uma fotografia e solicitar rotação, corte, redimensionamento ou outra transformação, trabalhar sobre uma cópia da fotografia fornecida.

**Não usar geração de imagem para substituir, recriar ou “corrigir” uma fotografia documental existente.**

Registrar transformações relevantes quando necessário:

```text
original:
tratamento:
resultado:
```

## Estrutura de publicação de imagens no Git

Manter a lógica de lotes/rodadas:

```text
assets/img/necoop/
├── rodada1/
├── rodada2/
└── ...
```

Somente imagens efetivamente selecionadas/preparadas devem entrar nessas pastas de publicação.

Arquivos temporários, backups e candidatos não devem ser publicados.

# Module 5 — Page implementation

Implementar de forma localizada:

- alterar somente os arquivos necessários;
- evitar substituições globais;
- não alterar outras páginas sem escopo;
- preservar conteúdo correto;
- preservar links corretos;
- manter a identidade visual existente;
- inserir somente recursos selecionados.

## Identidade visual

A evolução deve ser incremental. Preservar, salvo decisão explícita em contrário:

- paleta;
- tipografia;
- proporções;
- estilo de títulos;
- cards;
- espaços em branco;
- elementos institucionais.

O objetivo é melhorar a apresentação, não reiniciar o design.

## Texto + imagens

Quando houver recursos adequados, páginas institucionais e de atuação devem equilibrar:

- texto claro e conciso;
- fotografias reais;
- hierarquia visual;
- espaços em branco;
- navegação;
- chamadas para projetos, produções, recursos e notícias.

As imagens devem contribuir para mostrar o que o NECOOP faz, onde atua, com quem trabalha e que conhecimentos/experiências produz.

# Module 6 — Local validation

Antes do commit, verificar tecnicamente:

### HTML/CSS

- página carrega;
- estrutura íntegra;
- CSS aplicado corretamente;
- links válidos;
- referências a arquivos existentes.

### Imagens

- arquivo correto;
- orientação correta;
- proporção/corte adequado;
- nenhuma repetição indevida;
- `alt` adequado;
- caminho correto.

### Visual

Verificar pelo menos:

- desktop;
- largura intermediária;
- celular;
- hierarquia;
- legibilidade;
- equilíbrio texto/imagem.

# Module 7 — Human validation

A validação técnica da IA não substitui a aprovação editorial humana.

O usuário/responsável deve poder avaliar especialmente:

- fotografia escolhida;
- ordem das imagens;
- associação imagem/seção;
- destaque visual;
- significado institucional;
- adequação do texto.

Quando o usuário aprovar, a alteração pode seguir para o gate Git.

# Module 8 — Git safety gate

Antes do commit, verificar:

```bash
git status
git diff
git diff --cached
git diff --cached --name-only
```

Confirmar que não entraram no staging:

- backups;
- arquivos temporários;
- candidatos não selecionados;
- arquivos fora do escopo;
- recursos de trabalho.

Antes de qualquer publicação, revisar o conjunto exato de arquivos do commit.

## Operações proibidas sem autorização explícita

Não usar para “resolver” problemas de fluxo:

```bash
git reset --hard
git clean
 git push --force
```

ou operações equivalentes destrutivas.

# Module 9 — Remote synchronization

Antes do `push`:

```bash
git fetch origin
git status
git log --oneline --decorate
git log --oneline --left-right HEAD...origin/main
```

Se houver divergência entre local e remoto, diagnosticar primeiro.

Preferir integração segura por `rebase` ou `merge`, conforme o histórico, preservando ambos os trabalhos.

Nunca usar `force push` como primeira solução.

# Module 10 — Publication

Fluxo:

```text
commit
  ↓
fetch
  ↓
diagnóstico de divergência
  ↓
push
  ↓
aguardar GitHub Pages
```

Uma alteração não é considerada publicada apenas porque o `push` foi aceito.

# Module 11 — Public verification

Depois da publicação, verificar a URL pública e comparar com a versão pretendida.

Conferir:

- página correta;
- layout;
- imagens;
- orientação das imagens;
- links;
- recursos carregados;
- ausência de arquivos inexistentes;
- correspondência entre commit e conteúdo servido.

Se a página pública não corresponder ao esperado, não iniciar novas alterações às cegas. Diagnosticar primeiro:

- branch;
- commit;
- GitHub Pages;
- arquivo efetivamente servido;
- cache/CDN;
- estado remoto.

# Module 12 — Change record

Para alterações relevantes, registrar:

```text
Página:
Versão/rodada:
Data:
Objetivo:
Alterações:
Imagens utilizadas:
Decisões editoriais:
Commit:
URL pública:
Observações:
```

Esse registro deve preservar a rastreabilidade das decisões e facilitar futuras rodadas.

# Module 13 — Rollback

Toda alteração relevante deve poder ser revertida.

Preferir:

- reversão de commit;
- restauração de arquivo específico;
- recuperação de versão identificada.

Evitar operações destrutivas para resolver problemas de desenvolvimento.

# Module 14 — Page-specific protocol: Home

A Home é a principal porta de entrada e deve ser tratada como página editorial central.

Antes de modificar:

1. verificar Home pública;
2. verificar Home local;
3. identificar V1/V2/V2.x ou outra versão;
4. comparar estados;
5. escolher explicitamente a base;
6. preservar a versão pública até validar a nova;
7. aplicar somente textos/imagens aprovados;
8. testar localmente;
9. validar visualmente;
10. publicar;
11. verificar novamente a Home pública.

Uma Home local diferente da pública não é automaticamente erro; pode ser desenvolvimento. O erro é não distinguir os estados.

# Module 15 — Content and editorial rules

O NECOOP deve ser tratado como plataforma de conhecimento, não apenas como vitrine institucional.

O conteúdo deve articular, conforme pertinente:

- pesquisa;
- extensão;
- formação;
- cooperação;
- cooperativismo;
- economia solidária;
- agroecologia;
- reforma agrária;
- agricultura familiar;
- território;
- experiências coletivas;
- transformação social.

Não inventar informações, autoria, datas, atividades, identificação de pessoas ou contexto de fotografias.

Para documentos e publicações:

- não inventar metadados bibliográficos;
- publicar somente dados confirmados;
- preservar rastreabilidade para a fonte;
- distinguir conteúdo próprio de textos de outros autores;
- não duplicar desnecessariamente arquivos que já têm acervo em sua origem.

# Module 16 — Existing content/acervo modules

## pdf-ingest-local

Processar PDFs localmente sem alterar originais:

1. localizar;
2. registrar hash/tamanho/data;
3. extrair metadados;
4. extrair texto;
5. verificar qualidade;
6. OCR quando necessário;
7. gerar metadados preliminares;
8. gerar ficha estruturada;
9. registrar logs/checkpoint;
10. encaminhar para IA/humano apenas o que exigir interpretação.

## content-curation

Classificar documentos por temas, tipos, territórios, projetos e potencial de publicação. Distinguir material publicável, catalogável e material que deve ser apenas referenciado externamente.

## news-monitoring

Monitorar cooperação, cooperativismo, economia solidária, agroecologia, reforma agrária, agricultura familiar, políticas públicas e temas correlatos, priorizando fontes confiáveis e produzindo material editorial contextualizado.

## site-publishing

Preparar conteúdos para o GitHub, verificar links, metadados, estrutura, acessibilidade, imagens e consistência antes da publicação.

# Module 17 — Maintenance and incremental updates

Não reconstruir o acervo ou páginas inteiras a cada atualização.

Para novos materiais, identificar apenas:

1. registros novos;
2. registros modificados;
3. links quebrados;
4. páginas que realmente precisam de atualização.

Preservar conteúdo e links existentes quando estiverem corretos.

# Module 18 — Local tools

A skill deve evoluir acompanhada de ferramentas locais específicas:

```text
tools/necoop/
├── gerar_prancha_necoop.py
├── inventariar_acervo.py
├── verificar_imagens.py
├── verificar_links.py
├── verificar_site.py
└── preparar_imagens_web.py
```

Prioridade de implementação:

1. `gerar_prancha_necoop.py`;
2. `inventariar_acervo.py`;
3. `verificar_imagens.py`;
4. `verificar_links.py`;
5. `verificar_site.py`;
6. `preparar_imagens_web.py`.

As ferramentas devem ser não destrutivas, trabalhar por padrão sobre cópias/índices e produzir saídas identificáveis.

# Rule of responsibility

| Decisão/ação | IA | Usuário |
|---|:---:|:---:|
| Diagnóstico técnico | ✓ | |
| Organização do acervo | ✓ | |
| Geração da prancha | ✓ | |
| Seleção final das fotos | | **✓** |
| Associação foto/seção | sugestão técnica | **✓ decisão** |
| Preparação técnica da imagem | ✓ | |
| Conteúdo factual | pesquisa/verificação | **aprovação quando institucional** |
| Proposta de design incremental | ✓ | **aprovação** |
| Código | ✓ | |
| Teste técnico | ✓ | |
| Aprovação visual/editorial | | **✓** |
| Commit/push | ✓ | acompanhamento |

# Stop conditions

Parar antes de editar quando houver dúvida sobre:

- qual página está publicada;
- qual arquivo é a versão ativa;
- qual versão é mais nova;
- qual imagem foi escolhida;
- qual imagem corresponde a uma atividade;
- qual alteração local deve ser preservada;
- qual branch/commit será publicado;
- qual é o escopo da alteração.

A segurança do estado do projeto tem prioridade sobre velocidade.

# Expected process outputs

Uma rodada de atualização visual pode produzir:

```text
acervo_visual/
└── _processamento_pranchas/
    ├── candidatos/
    ├── pranchas/
    ├── inventarios/
    └── selecoes/

A camada `_processamento_pranchas/` é operacional e não substitui a organização histórica do acervo. Os originais permanecem em seus locais de origem.

Git/
└── assets/img/necoop/
    ├── rodada1/
    ├── rodada2/
    └── ...
```

Além disso:

- prancha visual;
- inventário/CSV;
- matriz editorial de imagens;
- arquivos preparados;
- diff revisado;
- commit identificado;
- verificação pública.

# Version note

**V2.1** consolida o protocolo operacional e incorpora o aprendizado da primeira rodada de atualização visual: separação rigorosa entre estado publicado e desenvolvimento; definição explícita das duas áreas físicas do projeto; seleção fotográfica sob autoridade do usuário; geração automatizada de pranchas; matriz editorial; preservação de originais; controle de transformações; gates técnicos/editoriais/Git; sincronização remota segura; verificação pública; registro e rollback.
