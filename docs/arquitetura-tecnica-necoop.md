# Arquitetura Técnica — Projeto de Manutenção do Site NECOOP

**Versão:** 1.0  
**Data:** 2026-08-23  
**Status:** Diretriz de projeto

## 1. Princípio geral

O projeto adota a estratégia **processamento local primeiro; IA quando houver ganho real de interpretação, síntese, classificação ou decisão editorial**.

O objetivo é reduzir custos e uso desnecessário de IA, preservar os documentos originais, manter rastreabilidade e permitir que o acervo cresça sem depender de processamento em nuvem.

## 2. Arquitetura

```text
IDrive / Cloud-Drive
        |
        v
Acervo local NECOOP
        |
        v
Processamento local
(texto, metadados, OCR, conversão, deduplicação)
        |
        v
Dados estruturados / fichas
        |
        v
Obsidian
        |
        +--> conhecimento geral
        |
        +--> curadoria NECOOP
                  |
                  v
          IA quando necessária
                  |
                  v
               GitHub
                  |
                  v
            GitHub Pages
                  |
                  v
             Site NECOOP
```

## 3. Papéis dos componentes

### IDrive / Cloud-Drive
Camada de armazenamento, preservação e sincronização dos arquivos de trabalho e do acervo.

### Processamento local
Responsável pelas tarefas mecânicas e repetitivas: extração de texto, leitura de metadados, OCR quando necessário, conversões, identificação de duplicatas, geração de índices e logs.

### Obsidian
Sistema geral de conhecimento do usuário. A área NECOOP deve ser uma parte do vault, não um vault exclusivo do site.

### IA
Usada seletivamente para tarefas que exigem interpretação: síntese fiel, classificação temática, identificação de relações, curadoria, elaboração editorial e apoio à produção de notícias e páginas.

### GitHub
Repositório oficial do código e dos conteúdos publicados do site, com controle de versões.

### GitHub Pages
Camada pública de distribuição do site.

## 4. Acervo documental

A pasta local de trabalho atualmente adotada é:

`~/Cloud-Drive/Necoop web/`

Os documentos originais não devem ser alterados pelos processos de ingestão.

O processamento deve gerar arquivos derivados em diretórios separados, com logs e possibilidade de reprocessamento incremental.

## 5. Pipeline de PDFs

Para cada PDF:

1. preservar o original;
2. identificar arquivo e tamanho;
3. extrair metadados incorporados;
4. extrair texto localmente;
5. verificar qualidade da extração;
6. aplicar OCR somente quando necessário;
7. identificar título, autores e ano de forma preliminar;
8. gerar ficha estruturada;
9. registrar status e eventuais erros;
10. encaminhar para curadoria humana/IA somente quando houver necessidade.

## 6. Curadoria e publicação

Nenhum documento deve ser publicado automaticamente apenas porque foi ingerido.

A catalogação deverá distinguir pelo menos:

- documento fonte;
- documento publicável integralmente;
- documento usado como fonte para conteúdo;
- documento que deve ser disponibilizado apenas por referência/link externo.

A publicação deve considerar direitos de disponibilização e decisão editorial.

## 7. Processamento incremental

O pipeline deverá manter checkpoint/log para evitar reprocessar documentos já tratados. O objetivo é permitir expansão gradual do acervo de dezenas para centenas ou milhares de arquivos.

## 8. Estrutura futura recomendada

```text
Necoop web/
├── 00_Projeto/
├── 01_Site/
├── 02_Acervo/
│   ├── Publicacoes/
│   ├── Teses_Dissertacoes/
│   ├── Livros_Capitulos/
│   ├── Relatorios/
│   └── Materiais/
├── 03_Conteudo/
│   ├── Noticias/
│   ├── Projetos/
│   └── Paginas/
├── 04_Midia/
│   ├── Imagens/
│   ├── Fotografias/
│   └── Videos/
└── 05_Para_Publicar/
```

Esta estrutura é uma proposta e não deve ser aplicada por movimentação automática de arquivos sem validação.

## 9. Diretriz de desenvolvimento

O projeto deve priorizar soluções gratuitas, locais, abertas e de baixa dependência externa sempre que tecnicamente adequadas.

A automação deve ser construída incrementalmente, começando pelo processamento local dos 17 PDFs atualmente disponíveis no acervo de trabalho.
