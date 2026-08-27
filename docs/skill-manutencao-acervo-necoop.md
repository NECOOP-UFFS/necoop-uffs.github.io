# Skill — Manutenção incremental do acervo e publicações do NECOOP

## Finalidade

Manter o acervo digital do site do NECOOP atualizado a partir da pasta local sincronizada com o iDrive, combinando processamento local, revisão humana e atualização assistida do site.

## Princípio operacional

A pasta local é a **caixa de entrada do acervo**, não a publicação automática.

```text
~/Cloud-Drive/Necoop web/
        ↓
processamento local dos PDFs
        ↓
catalogação / revisão humana
        ↓
solicitação ao assistente: "atualize o acervo NECOOP"
        ↓
matriz editorial
        ↓
site / GitHub
```

Adicionar um PDF à pasta **não publica o documento automaticamente**.

## Procedimento para novos materiais

Quando um novo PDF for destinado ao site:

1. Copiar o PDF para:
   `~/Cloud-Drive/Necoop web/Arquivos do site necoop (via chatgpt)/`
2. Se for produção própria ou de membro do NECOOP, deixá-lo nessa pasta para o fluxo de publicações.
3. Se for obra de terceiro que o NECOOP deseja indicar, registrar como **Leitura recomendada**.
4. Executar o processamento/catalogação local somente quando necessário. Como a entrada de novos materiais é eventual, não é necessário manter um processo automático contínuo.
5. Fazer a revisão humana dos dados bibliográficos no catálogo CSV.
6. Solicitar ao assistente a atualização do acervo/site. Exemplos:
   - "Há novos PDFs na pasta NECOOP. Atualize o catálogo e o site."
   - "Atualize as publicações do NECOOP com os novos materiais revisados."
   - "Inclua este PDF como leitura recomendada."
7. O assistente deve comparar o catálogo revisado com o conteúdo já publicado, identificar somente os novos/alterados registros e preparar a atualização incremental.
8. Antes da publicação, verificar correspondência inequívoca entre `registro → PDF → link público`.

## Coleções editoriais

### Produção dos membros

Produção científica e técnica de integrantes/membros do NECOOP.

### Materiais do NECOOP

Guias, jogos, materiais didáticos, metodologias e outros produtos institucionais do Núcleo.

### Leituras recomendadas

Obras de outros autores selecionadas pelo NECOOP por sua relevância para estudo, pesquisa, formação ou extensão. Não devem ser apresentadas como produção do Núcleo.

### Biblioteca / Acervo

Estudos de caso, relatos de prática e documentos de referência que não se enquadram necessariamente nas três coleções anteriores.

## Regra de publicação incremental

A ausência de um dado bibliográfico não impede a publicação quando a identificação do documento é suficientemente segura. Campos faltantes permanecem vazios ou são marcados como pendentes e podem ser completados posteriormente.

**Não inventar dados bibliográficos.** Dados confirmados pela revisão humana têm precedência sobre inferências automáticas.

## Processamento local

O processamento pesado dos PDFs deve ocorrer localmente, usando ferramentas como `pdftotext`, `pdfinfo`, SHA-256 e scripts Python. Isso reduz uso desnecessário de IA e preserva os arquivos originais.

A IA deve ser usada principalmente para:

- organização editorial;
- classificação temática;
- conferência e complementação bibliográfica quando solicitada;
- elaboração de descrições/resumos editoriais;
- atualização das páginas do site;
- controle de consistência.

## Controle de integridade

Para cada documento publicado:

- preservar o PDF original;
- manter identificador estável;
- evitar renomeações desnecessárias;
- garantir que cada registro tenha exatamente um arquivo público correspondente;
- não reutilizar o mesmo nome/ID para documentos diferentes;
- verificar links após atualização.

## Regra de decisão

**Novo PDF na pasta ≠ publicação automática.**

**Novo PDF + revisão humana + solicitação de atualização = candidato à publicação.**

Isso permite um fluxo simples, parcialmente automatizado e supervisionado pelo responsável editorial do NECOOP.
