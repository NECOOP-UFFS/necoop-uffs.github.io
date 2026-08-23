# Skill: NECOOP Site Maintenance

## Purpose

Manter e evoluir o site do Núcleo de Estudos em Cooperação (NECOOP), articulando acervo científico, produção de conhecimento, notícias, projetos, extensão, monitoramento temático e publicação controlada no GitHub Pages.

## Core principle

**Process local-first. Use AI only where interpretation, synthesis, classification, editorial judgment or contextual reasoning adds value.**

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

## Data rules

- Nunca modificar o PDF original durante ingestão.
- Não publicar automaticamente um documento ingerido.
- Preservar rastreabilidade entre original, ficha, conteúdo derivado e publicação.
- Usar processamento incremental e checkpoints.
- Preferir ferramentas locais gratuitas/open-source quando adequadas.
- Evitar enviar para IA grandes volumes de texto que possam ser processados localmente.

## Editorial rules

O NECOOP deve ser tratado como plataforma de conhecimento, não apenas como vitrine institucional. Conteúdos devem articular pesquisa, extensão, formação, cooperação, economia solidária, agroecologia e reforma agrária, preservando a especificidade de cada documento e evitando atribuições não sustentadas pelas fontes.

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
