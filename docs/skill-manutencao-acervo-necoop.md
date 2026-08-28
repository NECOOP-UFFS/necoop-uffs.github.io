# Skill — Manutenção incremental do acervo e publicações do NECOOP

## Finalidade

Manter o acervo digital e as páginas do site do NECOOP atualizados de forma incremental, combinando processamento local, revisão humana, Google Drive como repositório público dos arquivos e atualização assistida do site.

## Arquitetura do acervo

O **GitHub hospeda o site** (HTML, CSS, JavaScript e recursos gráficos). O **Google Drive hospeda os documentos públicos** (PDF, EPUB e outros formatos aprovados). O site funciona como catálogo, interface editorial e porta de acesso aos documentos.

Os documentos não devem ser copiados para o repositório GitHub apenas para viabilizar o download.

A pasta local sincronizada é área de trabalho e backup, não o repositório público oficial.

```text
~/Cloud-Drive/Necoop web/
        ↓
01_novos_arquivos/
        ↓
processamento/catálogo/revisão humana
        ↓
decisão editorial
        ↓
Google Drive (arquivo público)
        ↓
link individual testado
        ↓
página do NECOOP / GitHub
        ↓
confirmação de acesso
        ↓
02_arquivos_enviados/
```

## Estrutura local operacional

Dentro de:

`~/Cloud-Drive/Necoop web/Arquivos do site necoop (via chatgpt)/`

usar:

- `01_novos_arquivos/` — materiais aguardando decisão/publicação;
- `02_arquivos_enviados/` — materiais cuja publicação no Google Drive e no site foi confirmada.

A área principal não deve ser usada como depósito permanente de arquivos já processados.

O arquivo `.sync.ffs_db` e outros artefatos técnicos de sincronização devem ser ignorados pelo fluxo editorial.

## Procedimento para novos materiais

Quando um novo PDF, EPUB ou outro material aprovado for destinado ao site:

1. Colocar o arquivo em `01_novos_arquivos/`.
2. Identificar se é produção de integrante/membro do NECOOP, material institucional do Núcleo ou obra de terceiro.
3. Fazer processamento local somente quando útil/necessário. A entrada de novos materiais é eventual; não manter processamento automático contínuo sem necessidade.
4. Revisar humanamente os dados bibliográficos no catálogo.
5. Decidir a coleção editorial e se o material será publicado.
6. Garantir que o arquivo esteja no Google Drive e configurado para acesso público sem login.
7. Obter o link individual do arquivo no Drive.
8. Solicitar ao assistente a atualização do acervo/site. Exemplos:
   - “Há novos materiais na pasta NECOOP. Atualize o catálogo e o site.”
   - “Publique estes materiais nas páginas correspondentes.”
   - “Inclua este material como leitura recomendada.”
9. O assistente deve comparar catálogo, arquivos e site existentes e trabalhar apenas nos novos/alterados registros.
10. Antes de considerar o material publicado, testar o link em condição de visitante sem login.
11. Somente após a confirmação, mover o arquivo para `02_arquivos_enviados/`.

## Regra fundamental de publicação

**Adicionar um arquivo à pasta local não publica o documento.**

Publicação significa, simultaneamente:

```text
arquivo disponível no Google Drive
+
link público individual correto
+
registro na página adequada do site
+
link testado sem login
```

## Coleções editoriais

### Publicações

Produção científica e técnica de integrantes/membros do NECOOP.

### Materiais do NECOOP / Recursos Educativos

Guias, jogos, materiais didáticos, metodologias e outros produtos institucionais do Núcleo.

### Leituras recomendadas

Obras de outros autores selecionadas pelo NECOOP por sua relevância para estudo, pesquisa, formação ou extensão. Nunca apresentá-las como produção do Núcleo.

### Biblioteca / Acervo

Estudos de caso, relatos de prática, documentos institucionais e materiais de referência que não se enquadram necessariamente nas coleções anteriores.

## Metadados: regra de suficiência

Não exigir DOI, ISBN, evento, editora, volume, número, páginas ou outros campos de todos os documentos.

Para a apresentação pública, priorizar:

- título;
- autoria;
- data/ano.

Esses campos podem permanecer não preenchidos no catálogo interno quando a informação não estiver disponível.

Campos bibliográficos ausentes **não devem aparecer na ficha pública**. Não exibir rótulos vazios como “DOI:”, “ISBN:” ou “Editora:” quando não houver informação.

A ausência de metadados secundários não impede a publicação quando a identificação do documento é suficientemente segura.

**Nunca inventar dados bibliográficos.** Dados confirmados pela revisão humana têm precedência sobre inferências automáticas.

## Processamento local

O processamento pesado dos PDFs deve ocorrer localmente, preferencialmente com `pdftotext`, `pdfinfo`, SHA-256 e scripts Python. Isso reduz uso desnecessário de IA paga e preserva os arquivos originais.

O processamento local pode produzir texto extraído, metadados preliminares e fichas de revisão, mas resultados automáticos são auxiliares.

A IA deve ser utilizada principalmente para:

- organização editorial;
- classificação temática;
- conferência bibliográfica quando solicitada;
- elaboração de descrições e resumos editoriais;
- atualização das páginas;
- controle de consistência;
- identificação de problemas de navegação e apresentação.

Não criar novas versões de processamento (por exemplo, V0.3.x) apenas para resolver pequenas imperfeições de catalogação quando uma revisão humana assistida for mais eficiente.

## Google Drive e links

O Google Drive é o repositório público dos arquivos. Para cada documento publicado, usar o link individual do arquivo, e não depender apenas do link da pasta.

Padrão esperado de link de visualização:

`https://drive.google.com/file/d/ID_DO_ARQUIVO/view?usp=sharing`

O identificador deve corresponder inequivocamente ao documento catalogado.

Não inferir IDs nem associar links por aproximação.

Antes de mover o arquivo para `02_arquivos_enviados/`, testar o acesso em janela anônima/privativa ou equivalente, sem autenticação Google.

## Controle de integridade

Para cada documento publicado:

- preservar o arquivo original local enquanto fizer parte do fluxo de trabalho;
- manter identificador estável;
- evitar renomeações desnecessárias;
- garantir correspondência inequívoca `registro → arquivo → link`;
- não reutilizar o mesmo ID do Drive para documentos diferentes;
- verificar links após atualização da página;
- não considerar publicado um arquivo cujo link ainda não foi testado.

## Manutenção incremental do site

Não reconstruir o acervo inteiro a cada inclusão.

Ao receber novos materiais, identificar apenas:

1. registros novos;
2. registros modificados;
3. links quebrados;
4. páginas que precisam ser atualizadas.

Preservar conteúdo e links existentes quando estiverem corretos.

## Auditoria visual e editorial

A manutenção do acervo deve ser acompanhada periodicamente de auditoria das páginas, observando:

- clareza da hierarquia de informação;
- navegação;
- consistência visual;
- qualidade e quantidade de imagens;
- legibilidade;
- equilíbrio entre texto e elementos visuais;
- adequação das páginas às comunidades acadêmica, regional, nacional e internacional.

Imagens devem contribuir para a identidade e compreensão do NECOOP, não ser inseridas apenas como decoração.

## Memória e notícias históricas

Notícias antigas do site anterior (incluindo Wix) podem ser incorporadas ao novo site como acervo histórico, após seleção editorial.

Preservar, quando disponível, data, autoria, contexto e referência à atividade original. Não apresentar conteúdo histórico como notícia atual.

## Regra de decisão

**Novo arquivo ≠ publicação automática.**

**Novo arquivo + revisão humana + decisão editorial + arquivo público no Drive + link testado + atualização do site = publicação.**

O fluxo deve permanecer **parcialmente automatizado e supervisionado por revisão humana**, priorizando economia de tempo, baixo consumo de IA e integridade editorial do acervo.
