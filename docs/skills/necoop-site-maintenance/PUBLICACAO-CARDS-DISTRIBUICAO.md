# Módulo operacional — Cards e distribuição de novas publicações

Complementa a skill `NECOOP Site Maintenance V2`. Acionar obrigatoriamente sempre que nova notícia, artigo ou conteúdo for publicado no site.

## Hierarquia das instruções

Este módulo governa o fluxo editorial, os formatos de divulgação, a identidade visual, a aprovação e a entrega multicanal. Para **toda operação técnica no Buffer**, a fonte de verdade é a skill existente na Biblioteca ChatGPT:

`skill-publicacao-necoop-buffer-instagram-v2.md`

Consultar e seguir essa skill antes de operar o Buffer. Ela contém o procedimento validado de mídia, parâmetros da integração, criação de rascunhos e verificações. Este módulo não replica nem redefine esses parâmetros. Em caso de divergência técnica, interromper a operação e conferir a skill de referência; não improvisar nem substituir a integração validada. A referência não significa que o arquivo da Biblioteca foi alterado ou sincronizado com este repositório.

## Gatilho

Após publicação e verificação pública da matéria, iniciar a preparação do pacote de divulgação, sem aguardar novo pedido. A preparação é automática; publicação nos canais continua condicionada à aprovação humana.

## Entregáveis obrigatórios

1. Card Instagram vertical 4:5 (preferencialmente 1080 × 1350 px).
2. Card X horizontal (preferencialmente 1600 × 900 px).
3. Card WhatsApp quadrado (preferencialmente 1080 × 1080 px).
4. Texto específico para Instagram e X, com URL direta da matéria.
5. **Post completo para WhatsApp: imagem + texto de mensagem + URL direta clicável**, pronto para encaminhamento. A imagem isolada não conclui a tarefa.
6. Rascunhos no Buffer para Instagram e X, com os respectivos cards anexados, seguindo a skill técnica de referência.
7. Pacote organizado com arquivos finais, prévias, textos e caminhos registrados.

## Identidade visual e mensagem

- Usar sempre o logo oficial correto do NECOOP. Localizar e verificar o arquivo no repositório GitHub, preferencialmente `assets/img/logos/logo-necoop.png` (referenciado em `header.html`), ou usar o arquivo original fornecido pelo responsável humano. Não redesenhar, substituir por texto digitado ou usar logo aproximado. Se não for possível obter/verificar o arquivo, interromper a finalização.
- O logo oficial deve estar efetivamente incorporado aos pixels/composição de **cada um dos três cards finais**. Menção ao logo no prompt, espaço reservado ou texto “NECOOP” não atende ao requisito.
- **Gate obrigatório de QA do logo (fail-closed):** abrir/inspecionar individualmente cada PNG final, em tamanho integral e prévia reduzida. Confirmar logo visível, íntegro, legível, sem corte, distorção ou sobreposição e com contraste adequado. Se qualquer formato falhar, corrigir e reexportar. Não entregar como final nem anexar ao Buffer até aprovação do teste.
- Registrar o caminho/nome do arquivo-fonte do logo. Quando fornecido pelo responsável humano, usar o original; redimensionamento proporcional é permitido.
- Incluir chamada editorial curta, como **“Novo post do NECOOP”**, visível sem competir com o tema/título. O card deve comunicar nova publicação, não apenas lembrete.
- Hierarquia sugerida: marca NECOOP + chamada “Novo post do NECOOP” + tema/título conciso + informação-chave + convite para ler.
- Identificar **ObservaCoop — Observatório do Cooperativismo** quando a matéria for publicada nessa seção ou tratar diretamente de seu conteúdo. Usá-lo como editoria secundária, mantendo NECOOP como marca principal. Não atribuir ObservaCoop a outras seções; em dúvida, conferir a página publicada.
- Adaptar composição e texto a cada canal, preservando legibilidade móvel e consistência visual.

## Link e acesso à matéria

- Usar a URL pública direta da página específica (permalink), nunca apenas a Home ou página geral do Observatório.
- Inserir o link direto nos textos de Instagram, X e WhatsApp e testá-lo antes da entrega.
- O card pode exibir domínio curto ou “Leia a matéria”; não depender de URL longa impressa, pois ela não será clicável.
- A publicação completa exige texto/caption com link, além da imagem.

## Buffer — execução subordinada à skill técnica

- Seguir integralmente `skill-publicacao-necoop-buffer-instagram-v2.md`, disponível na Biblioteca ChatGPT, para consultar canais, preparar mídia, criar rascunhos e validar resultados.
- Criar rascunhos para os canais oficiais NECOOP de Instagram e X, com o card correspondente e texto adaptado contendo a URL direta.
- Não presumir IDs/canais; confirmar os canais oficiais na integração.
- A exigência editorial deste módulo é: card correto anexado a cada rascunho; texto completo com link; canal correto; status de rascunho confirmado; nenhuma publicação ou agenda sem autorização explícita.
- Se a integração Buffer MCP não estiver disponível na sessão, ou se alguma etapa falhar, registrar objetivamente a pendência e interromper o fluxo afetado. Não improvisar outra plataforma/automação e não afirmar conclusão sem confirmação operacional.
- Registrar identificadores/links dos rascunhos, quando retornados, e o resultado das verificações. A referência à skill não autoriza afirmar que um rascunho foi criado.

## Hospedagem e arquivamento dos cards

Para o Buffer, seguir o procedimento de hospedagem e URL pública direta definido na skill técnica. No fluxo já validado do NECOOP, os cards são hospedados no próprio repositório GitHub, em pasta específica vinculada à publicação; a URL pública direta da imagem é distinta do permalink da matéria.

- Seguir a convenção de diretórios existente; não criar estrutura paralela sem necessidade.
- Versionar apenas arquivos finais aprovados, com nomes claros e estáveis; não usar temporários ou prévias.
- Testar a URL pública direta antes de fornecer mídia ao Buffer.
- Registrar caminho do arquivo e URL pública usada. Se commit, acesso público ou associação da mídia falhar, interromper a criação/validação do rascunho afetado.

## WhatsApp — pacote completo para encaminhamento

WhatsApp não é entrega de imagem isolada. Preparar:

**A. Imagem:** card quadrado 1080 × 1080 px, com logo oficial validado e chamada editorial.

**B. Texto separado, copiável:**
- chamada breve para a nova publicação do NECOOP;
- síntese clara do assunto e, se pertinente, dado/prazo central;
- convite à leitura;
- **URL pública direta da matéria em texto puro**, para reconhecimento como link clicável.

Entregar explicitamente o PNG e o texto final copiável, mantendo o link completo no texto. Não inserir o link somente na imagem nem considerar concluído o trabalho com o PNG isolado. O responsável humano fará o encaminhamento; não enviar mensagens a contatos ou grupos.

## Procedimento editorial

1. Confirmar publicação da matéria e testar a URL pública direta.
2. Extrair da página validada título, ideia central, dados/prazos essenciais e seção editorial; não inventar fatos.
3. Localizar e incorporar o logo oficial, confirmando sua origem.
4. Definir mensagem visual central, incluindo “Novo post do NECOOP”; identificar ObservaCoop somente quando aplicável.
5. Criar os três formatos; Instagram e X não devem ficar sem imagem quando houver recurso visual adequado.
6. Executar o QA individual do logo nos três PNGs.
7. Conferir acentuação, números, datas, logo, URL, contraste, margens e legibilidade.
8. Preparar textos específicos para Instagram, X e WhatsApp. WhatsApp deve incluir imagem + texto copiável + link.
9. Apresentar cards, prévias e textos ao responsável humano para aprovação editorial.
10. Após aprovação do material, organizar arquivos finais e versionar cópias na pasta GitHub vinculada à publicação. Não publicar temporários no site.
11. Seguir a skill técnica de Buffer para criar e validar rascunhos de Instagram e X com os cards correspondentes. Manter como rascunho até autorização explícita.
12. Entregar o pacote WhatsApp completo para encaminhamento manual.
13. Registrar URL da matéria, seção/editoria, arquivo-fonte do logo, caminhos/URLs GitHub, arquivos finais, textos, resultado do QA visual, identificadores/status dos rascunhos, pacote WhatsApp e aprovação.

## Checklist

- [ ] URL direta pública da matéria conferida
- [ ] Skill técnica `skill-publicacao-necoop-buffer-instagram-v2.md` consultada para operação Buffer
- [ ] Arquivo-fonte do logo oficial identificado e registrado
- [ ] Logo oficial incorporado ao PNG do Instagram
- [ ] Logo oficial incorporado ao PNG do X
- [ ] Logo oficial incorporado ao PNG do WhatsApp
- [ ] QA visual individual dos três PNGs aprovado
- [ ] Chamada “Novo post do NECOOP” incluída
- [ ] ObservaCoop identificado, se aplicável, como editoria secundária
- [ ] Card Instagram 4:5
- [ ] Card X horizontal
- [ ] Card WhatsApp quadrado
- [ ] Legenda Instagram completa, com URL direta
- [ ] Texto X adaptado, com URL direta
- [ ] WhatsApp entregue como imagem + texto copiável + URL clicável
- [ ] Cards finais hospedados na pasta GitHub vinculada à publicação
- [ ] URLs públicas diretas dos cards testadas
- [ ] Rascunho Instagram criado via Buffer, com card correto e canal confirmado
- [ ] Rascunho X criado via Buffer, com card correto e canal confirmado
- [ ] Status de ambos confirmado como rascunho, não agendados/publicados
- [ ] Revisão/aprovação humana registrada
- [ ] Buffer mantido em rascunho até autorização
- [ ] Registro dos materiais e status atualizado

## Regras de controle

- Nunca afirmar que um rascunho foi criado, que uma imagem foi anexada ou que uma publicação foi enviada sem confirmação operacional.
- Se a matéria não estiver pública, o logo não puder ser verificado/incorporado, faltar recurso visual essencial ou houver dúvida factual/editorial, registrar a pendência e não improvisar.
- Se Buffer MCP não estiver disponível, registrar a limitação desta sessão; não questionar nem substituir a integração já validada pelo projeto.
- A preparação do pacote é obrigatória para cada nova publicação; a postagem efetiva depende de aprovação humana.
