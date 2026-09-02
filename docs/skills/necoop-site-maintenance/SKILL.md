# Skill: NECOOP Site Maintenance

## Purpose

Manter e evoluir o site do Núcleo de Estudos em Cooperação (NECOOP), articulando acervo científico, produção de conhecimento, notícias, projetos, extensão, monitoramento temático e publicação controlada no GitHub Pages.

## Core principle

**Process local-first. Use AI only where interpretation, synthesis, classification, editorial judgment or contextual reasoning adds value.**

**Nunca presumir que o arquivo local aberto é a versão atualmente publicada. Antes de alterar qualquer página, identificar explicitamente o estado público, o estado local e eventuais versões alternativas em produção.**

## Architecture

- **IDrive/Cloud-Drive:** armazenamento e preservação do acervo e arquivos de trabalho.
- **Local processing:** extração, OCR, metadados, conversão, deduplicação, índices e logs.
- **Obsidian:** sistema geral de conhecimento; a área NECOOP é um espaço especializado dentro do vault.
- **AI:** síntese, interpretação, classificação, relações entre documentos, curadoria e produção editorial.
- **GitHub:** versionamento e publicação dos conteúdos do site.
- **GitHub Pages:** distribuição pública.

## Modules

### pdf-ingest-local
Processa PDFs localmente sem alterar os originais.

Pipeline:
1. localizar arquivos;
2. registrar hash/tamanho/data;
3. extrair metadados;
4. extrair texto;
5. verificar qualidade;
6. executar OCR apenas quando necessário;
7. gerar metadados preliminares;
8. gerar ficha estruturada;
9. registrar logs/checkpoint;
10. encaminhar somente casos que exigem interpretação para IA/humano.

### content-curation
Classificar documentos e conteúdos segundo temas, tipos, territórios, projetos e potencial de publicação. Distinguir material publicável, material apenas catalogável e material que deve ser referenciado externamente.

### news-monitoring
Monitorar cooperação, cooperativismo, economia solidária, agroecologia, reforma agrária, agricultura familiar, políticas públicas e temas correlatos. Priorizar fontes confiáveis e produzir material editorial com contexto e fontes.

### site-publishing
Preparar e revisar conteúdos para o GitHub, verificar links, metadados, estrutura, acessibilidade e consistência antes da publicação.

## Protocolo obrigatório antes de alterar qualquer página

### 1. Identificar a página efetivamente publicada

Antes de editar HTML, CSS, imagens ou estrutura de uma página, o agente deve:

1. acessar a URL pública correspondente;
2. verificar qual conteúdo e layout estão efetivamente carregados;
3. registrar mentalmente ou em relatório curto o estado público observado;
4. identificar a URL exata da página que será alterada.

**Não considerar o conteúdo de uma cópia local, branch, arquivo de backup ou versão de desenvolvimento como sendo a página publicada sem confirmação.**

Para a Home, verificar explicitamente:

`https://necoop-uffs.github.io/index.html`

Quando houver dúvida entre páginas com nomes semelhantes, URLs antigas, arquivos legados ou versões V1/V2, interromper a edição até resolver a correspondência.

### 2. Identificar versões alternativas em produção

Depois de verificar a página pública, verificar o ambiente local/repositório de desenvolvimento para determinar:

- qual arquivo corresponde à página pública;
- se existem modificações locais não publicadas;
- se existe uma versão mais nova em desenvolvimento;
- se existem backups, versões congeladas, branches ou cópias alternativas;
- qual versão deve ser tomada como base para a alteração solicitada.

**Nunca assumir que `HEAD`, o arquivo aberto no editor ou a cópia local mais recente corresponde automaticamente ao site público.**

Quando houver uma versão alternativa mais nova, comparar a versão pública e a versão em desenvolvimento antes de editar. Registrar qual delas será preservada/evoluída.

### 3. Estabelecer a linha de base antes da edição

Antes de modificar uma página:

1. verificar `git status`;
2. verificar os últimos commits relevantes;
3. verificar diferenças locais (`git diff`) quando existirem;
4. identificar backups e versões anteriores relevantes;
5. fazer backup do arquivo que será alterado quando a alteração for substantiva;
6. confirmar que os recursos referenciados pela página existem no repositório.

**Não apagar, sobrescrever ou substituir alterações locais legítimas sem antes identificá-las.**

### 4. Alterar somente o alvo definido

O agente deve trabalhar de forma incremental e localizada.

- Não fazer substituições globais sem verificar todas as ocorrências.
- Não alterar outras páginas apenas porque parecem semelhantes.
- Não redesenhar páginas não incluídas na tarefa.
- Não substituir uma versão inteira por outra sem comparação prévia.
- Preservar conteúdo, links e estrutura existentes quando estiverem corretos.

Quando a tarefa for visual, primeiro alterar a página-alvo e seus recursos diretamente relacionados; depois avaliar a necessidade de propagar o padrão para outras páginas.

## Protocolo visual e editorial

O site do NECOOP deve ser **bonito, funcional, legível e expressivo do sentido do trabalho do Núcleo**. Não deve parecer apenas um conjunto de páginas textuais ou um catálogo de links.

### Texto + imagens

As páginas institucionais e de apresentação, especialmente a Home e as páginas de atuação, devem combinar adequadamente:

- texto claro e conciso;
- fotografias reais das atividades do NECOOP, quando disponíveis;
- elementos gráficos coerentes com a identidade do site;
- espaços em branco e boa hierarquia visual;
- navegação funcional;
- chamadas para conteúdos, projetos, produções e notícias.

**Não tratar imagens como decoração dispensável.** Fotografias devem ajudar a mostrar o que o NECOOP faz, onde atua, com quem trabalha e que tipo de conhecimento e experiência produz.

A apresentação visual deve contribuir para comunicar:

- pesquisa;
- extensão;
- formação;
- cooperação;
- cooperativismo;
- economia solidária;
- agroecologia;
- reforma agrária;
- território;
- experiências coletivas e transformação social.

### Seleção de fotografias

Quando houver acervo fotográfico próprio, priorizá-lo em relação a imagens genéricas de bancos ou imagens produzidas por IA.

**A associação entre fotografia e atividade/tema deve ser determinada ou aprovada pelo responsável humano quando houver contexto institucional específico.** O agente não deve inventar a identificação de uma fotografia nem atribuir uma atividade apenas com base na aparência visual.

Uma mesma fotografia pode ser pertinente a mais de uma temática ou seção quando isso for editorialmente justificável.

Não pedir novamente ao responsável identificações que já tenham sido registradas no projeto. Recuperar e reutilizar as decisões já tomadas quando estiverem disponíveis.

### Identidade visual

Melhorar a apresentação de forma incremental, preservando a identidade visual já estabelecida, salvo decisão explícita em contrário.

Não substituir desnecessariamente:

- paleta;
- tipografia;
- proporções;
- estilo de títulos;
- estrutura de cards;
- uso de espaços em branco;
- elementos institucionais.

A evolução visual deve partir do que já foi aprovado e evitar redesign radical sem justificativa.

## Protocolo específico para evolução da Home

A Home é a principal porta de entrada do site e deve ser tratada como página editorial central.

Antes de modificar a Home:

1. verificar a Home pública;
2. verificar a Home local;
3. identificar se há V1, V2, V2.x ou outra versão em desenvolvimento;
4. comparar as versões;
5. confirmar qual versão constitui a base atual de evolução;
6. preservar a versão pública até que a nova versão esteja conferida;
7. aplicar as fotografias e textos aprovados na versão correta;
8. testar localmente antes de publicar;
9. somente depois publicar no GitHub Pages;
10. verificar novamente a Home pública após a publicação.

**Uma página local visualmente diferente da página pública não é, por si só, um erro: pode ser uma versão em desenvolvimento. O erro é alterar a versão errada por não distinguir os estados.**

## Controle de publicação

Uma alteração só deve ser considerada publicada quando houver correspondência clara entre:

```text
página pública atual
        ↓
versão local/repositório escolhida como base
        ↓
alteração revisada
        ↓
commit/versionamento
        ↓
GitHub Pages
        ↓
verificação da URL pública
```

Após publicar uma alteração:

- verificar a URL pública;
- conferir se a página carregada corresponde à versão pretendida;
- conferir imagens, links e elementos essenciais;
- verificar se não foram introduzidas referências para arquivos inexistentes;
- considerar cache/CDN quando a alteração ainda não aparecer imediatamente.

Se a página pública não corresponder ao que foi publicado, **não iniciar novas alterações às cegas**. Primeiro diagnosticar branch, commit, GitHub Pages, cache ou arquivo efetivamente servido.

## Data rules

- Nunca modificar o PDF original durante ingestão.
- Não publicar automaticamente um documento ingerido.
- Preservar rastreabilidade entre original, ficha, conteúdo derivado e publicação.
- Usar processamento incremental e checkpoints.
- Preferir ferramentas locais gratuitas/open-source quando adequadas.
- Evitar enviar para IA grandes volumes de texto que possam ser processados localmente.

## Editorial rules

O NECOOP deve ser tratado como plataforma de conhecimento, não apenas como vitrine institucional. Conteúdos devem articular pesquisa, extensão, formação, cooperação, economia solidária, agroecologia e reforma agrária, preservando a especificidade de cada documento e evitando atribuições não sustentadas pelas fontes.

O site deve afirmar visual e editorialmente o sentido do trabalho do NECOOP. Sempre que apropriado, deve mostrar a relação entre conhecimento acadêmico, experiências concretas, processos educativos, organizações coletivas, territórios e transformação social.

Não transformar a página em excesso de texto para explicar aquilo que pode ser comunicado de forma mais clara por uma combinação equilibrada de texto, fotografia, estrutura e navegação.

## Manutenção incremental do site

Não reconstruir o acervo inteiro a cada inclusão.

Ao receber novos materiais, identificar apenas:
1. registros novos;
2. registros modificados;
3. links quebrados;
4. páginas que precisam ser atualizadas.

Preservar conteúdo e links existentes quando estiverem corretos.

## Procedimento de segurança para alterações

Toda alteração relevante deve ser reversível.

Antes de uma alteração substantiva:

- criar backup ou garantir que a versão anterior esteja recuperável pelo Git;
- fazer uma alteração por vez quando possível;
- verificar o diff antes do commit;
- evitar comandos destrutivos ou limpeza automática sem necessidade;
- não usar `git reset --hard`, `git clean` ou operações equivalentes para resolver problemas de desenvolvimento sem autorização explícita;
- não sobrescrever uma versão local sem saber o que ela contém.

Quando um comando for fornecido ao responsável para execução local, o comando deve ser previamente revisado e, sempre que possível, não destrutivo e específico para a tarefa.

## Regra de parada diante de ambiguidade

Se houver dúvida sobre:

- qual página está publicada;
- qual arquivo é a versão ativa;
- qual versão é mais nova;
- qual imagem corresponde a determinada atividade;
- qual alteração local deve ser preservada;
- qual branch/commit será publicado;

**não editar. Primeiro diagnosticar e esclarecer a ambiguidade.**

Essa regra tem prioridade sobre a tentativa de avançar rapidamente.

## First implementation target

O primeiro teste operacional desta skill é o lote de 17 PDFs atualmente localizado em:

`~/Cloud-Drive/Necoop web/Arquivos do site necoop (via chatgpt)/`

O primeiro objetivo é produzir um inventário local, texto extraído, metadados preliminares, fichas estruturadas e relatório de processamento, sem alterar os arquivos originais.

## Expected outputs

```text
_necoop_processado/
├── texto/
├── metadados/
├── fichas/
├── logs/
└── relatorio.csv
```

A implementação dos scripts locais pode evoluir separadamente do conteúdo do site.

## Version note

Esta versão incorpora um protocolo reforçado de **identificação da versão publicada, identificação de versões em desenvolvimento, preservação da linha de base e controle visual/editorial da relação entre texto e imagens**, após ocorrência de alterações iniciadas sobre uma versão diferente daquela efetivamente carregada no site público.
