# Módulo operacional — Cards e distribuição de novas publicações

Complementa a skill `NECOOP Site Maintenance V2`. Acionar obrigatoriamente sempre que nova notícia, artigo ou conteúdo for publicado no site.

## Gatilho

Após publicação e verificação pública da matéria, iniciar o pacote de divulgação, sem aguardar novo pedido. A preparação é automática; publicação nos canais continua condicionada à aprovação humana.

## Entregáveis obrigatórios

1. Card Instagram vertical 4:5 (preferencialmente 1080 × 1350 px).
2. Card X horizontal (preferencialmente 1600 × 900 px).
3. Card WhatsApp quadrado (preferencialmente 1080 × 1080 px).
4. Texto de apoio específico para Instagram e X, com URL direta da matéria.
5. **Post completo para WhatsApp: imagem + texto de mensagem + URL direta clicável**, pronto para encaminhamento. A imagem isolada não conclui a tarefa.
6. Rascunhos no Buffer para Instagram e X, com os respectivos cards anexados.
7. Pacote organizado com arquivos finais, prévia, textos e caminhos registrados.

## Identidade visual e mensagem

- **Usar sempre o logo oficial correto do NECOOP.** Antes de criar a arte, localizar e verificar o arquivo no repositório GitHub, preferencialmente o recurso institucional já utilizado pelo site (atualmente referenciado em `header.html` como `assets/img/logos/logo-necoop.png`). Não redesenhar, substituir por texto digitado ou usar logo aproximado. Se não for possível obter/verificar o arquivo correto, interromper a finalização e solicitar o recurso; não publicar card sem logo.
- O arquivo correto deve ser efetivamente incorporado aos pixels/à composição de **cada um dos três cards finais**. Localizar o arquivo ou mencionar o logo no prompt não comprova sua incorporação. Não considerar como concluído se o card tiver apenas “NECOOP” digitado, um espaço reservado, um logo semelhante ou o logo presente somente em um dos formatos.
- **Gate obrigatório de QA do logo (fail-closed):** após exportar, abrir/inspecionar visualmente cada PNG final, em tamanho integral e em prévia reduzida. Confirmar que o logo oficial está visível, íntegro, legível, sem corte, sem distorção e sem sobreposição, com contraste adequado ao fundo. Conferir os três arquivos individualmente. Se qualquer formato falhar, corrigir e exportar novamente; não entregar como final, não anexar ao Buffer e não avançar para publicação até passar no teste.
- Registrar o caminho/nome do arquivo-fonte do logo utilizado. Quando o recurso tiver sido fornecido pelo responsável humano, usar esse arquivo original, sem redesenhá-lo; redimensionamento proporcional é permitido.
- Incluir uma chamada editorial curta, como **“Novo post do NECOOP”**, visível mas sem competir com o título/tema da matéria. O card deve comunicar que se trata de uma nova publicação, não apenas de um lembrete de prazo.
- Hierarquia sugerida: identificação NECOOP + selo/chamada “Novo post do NECOOP” + tema/título conciso + informação-chave + convite para ler.
- A seção **ObservaCoop — Observatório do Cooperativismo** deve ser identificada quando a matéria tiver sido publicada nessa seção ou tratar diretamente de conteúdo do ObservaCoop. Apresentá-la como assinatura/editoria secundária, preservando NECOOP como marca institucional principal. Não atribuir ObservaCoop a conteúdos de outras seções; em caso de dúvida, conferir a página publicada.
- Adaptar composição e quantidade de texto ao formato de cada canal, mantendo legibilidade em telas móveis e consistência visual.

## Link e acesso à matéria

- Usar sempre a **URL pública direta da página específica** (permalink), nunca apenas a Home ou página geral do Observatório.
- Nos textos de Instagram, X e WhatsApp, inserir o link direto e testá-lo antes da entrega.
- O card pode exibir domínio curto ou chamada “Leia a matéria”; não depender de URL longa impressa na imagem. URLs impressas em cards não são clicáveis.
- **A conclusão do post exige texto/caption acompanhado do link**, além da imagem. Não entregar apenas o card como se fosse a publicação completa.

## Buffer MCP — fluxo operacional obrigatório

A integração Buffer MCP no ChatGPT já foi conectada e testada com sucesso no fluxo anterior do NECOOP. **Usar essa integração diretamente no ChatGPT** para criar rascunhos; não substituir por outra plataforma, automação ou integração local.

1. Confirmar que o Buffer MCP está disponível na sessão. Consultar os canais conectados e selecionar os canais oficiais do NECOOP para Instagram e X, sem presumir IDs ou escolher canais pessoais.
2. Preparar o texto específico de cada rede. Incluir a URL pública direta da matéria no texto/caption; para Instagram, incluir o link completo na legenda, mesmo sabendo que URLs em legendas geralmente não ficam clicáveis.
3. Criar pelo Buffer MCP um **rascunho** para o canal Instagram NECOOP, com o card vertical final anexado e a legenda completa.
4. Criar pelo Buffer MCP um **rascunho** para o canal X NECOOP, com o card horizontal final anexado e texto adaptado ao limite/formato da rede, incluindo a URL direta.
5. Utilizar o procedimento de mídia aceito pela integração MCP já validada, conforme a seção **Hospedagem dos cards no GitHub para o Buffer** abaixo. Não declarar que o card foi anexado apenas porque foi mencionado, selecionado ou incluído no texto: confirmar na resposta da ação e, quando possível, consultar/abrir o rascunho para verificar a mídia associada.
6. Confirmar separadamente para cada rede: canal correto, texto completo, URL direta, imagem/card correspondente e status **rascunho**. Não agendar nem publicar.
7. Se o Buffer MCP não estiver disponível nesta sessão, ou se alguma operação falhar, não improvisar outro caminho nem afirmar conclusão. Registrar objetivamente a etapa pendente e retomar quando a integração estiver acessível.
8. Entregar os links/identificadores dos rascunhos, quando retornados pela integração, e um resumo do status. **Nunca acionar publicação imediata, agendamento ou envio final sem autorização explícita do responsável humano.**

## Hospedagem dos cards no GitHub para o Buffer — caminho já validado

O requisito de URL pública de mídia do Buffer foi resolvido no fluxo do NECOOP: **hospedar o arquivo do card no próprio repositório GitHub, em uma pasta específica vinculada à publicação correspondente**, e fornecer ao Buffer a URL pública direta do arquivo.

Procedimento obrigatório:

1. No repositório `NECOOP-UFFS/necoop-uffs.github.io`, criar/usar uma pasta de mídia específica associada à matéria/post (seguir a convenção de diretórios já utilizada no repositório; não criar uma estrutura paralela sem necessidade).
2. Salvar nessa pasta os arquivos finais aprovados dos cards de Instagram e X, preservando nomes claros e estáveis. Não usar arquivos temporários, prévias ou versões ainda não aprovadas.
3. Obter a URL pública direta de cada imagem hospedada no GitHub, preferencialmente a URL raw/publicamente acessível que foi aceita no fluxo Buffer já testado. Testar a URL em acesso público antes de enviar ao MCP.
4. Ao criar cada rascunho via Buffer MCP, associar a URL do arquivo correto: card vertical ao Instagram e card horizontal ao X. Não confundir permalink da matéria com URL pública da mídia; são recursos distintos e ambos devem estar no post quando aplicável.
5. Verificar o retorno do MCP e, quando possível, abrir o rascunho no Buffer para confirmar que a imagem foi efetivamente carregada/associada. Uma URL inserida no texto não equivale a anexo de mídia.
6. Registrar no pacote de divulgação os caminhos dos arquivos no repositório e as URLs públicas utilizadas no Buffer. Manter a relação entre pasta/card e a publicação específica para facilitar auditoria e reutilização.
7. Se o upload/commit, acesso público ou associação da mídia falhar, não substituir por OpenClaw, serviço externo ou outra automação. Registrar a pendência e interromper a criação/validação do rascunho afetado.

## WhatsApp — pacote completo para encaminhamento

WhatsApp não é tratado como entrega de imagem isolada. Preparar um conjunto de duas partes, pronto para o usuário encaminhar:

**A. Imagem:** card quadrado 1080 × 1080 px, com logo oficial validado e chamada editorial.

**B. Texto da mensagem, enviado separadamente abaixo/junto da imagem:**
- breve chamada para a nova publicação do NECOOP;
- síntese clara do assunto e, se pertinente, dado/prazo central;
- convite para leitura;
- **URL pública direta da matéria em texto puro**, para que o WhatsApp a reconheça como link clicável.

Entregar explicitamente o PNG e o texto final copiável, mantendo o link completo no texto. Não inserir o link somente dentro da imagem nem considerar concluído o trabalho ao disponibilizar apenas o PNG. O usuário fará o encaminhamento aos contatos; não enviar mensagens a contatos ou grupos.

## Procedimento

1. Confirmar que a matéria está publicada e que a URL pública direta abre corretamente.
2. Extrair da página validada título, ideia central, dados/prazos essenciais e seção editorial. Não inventar fatos.
3. Localizar e incorporar o logo oficial do NECOOP no GitHub ou usar arquivo original fornecido pelo responsável humano; confirmar a origem do recurso.
4. Definir mensagem visual central e incluir “Novo post do NECOOP”. Identificar ObservaCoop apenas quando aplicável, como editoria secundária.
5. Criar os três formatos; usar arte/imagem pertinente e não deixar os rascunhos de Instagram ou X sem imagem.
6. Executar o **Gate obrigatório de QA do logo** em cada PNG exportado. A simples existência do arquivo-fonte ou a presença de uma marca textual “NECOOP” não atende ao requisito.
7. Conferir acentuação, números, datas, logo, URL direta, contraste, margens e legibilidade em cada formato.
8. Preparar os textos específicos para Instagram, X e WhatsApp. Para WhatsApp, garantir imagem + mensagem copiável + link clicável.
9. Apresentar os cards, prévia e textos por canal ao responsável humano para aprovação editorial.
10. Após aprovação do material, organizar os arquivos finais no local de materiais de divulgação; versionar cópias no repositório na pasta específica da publicação, conforme a seção de hospedagem acima. Não publicar temporários ou rascunhos no site.
11. Usar o Buffer MCP conforme o procedimento acima para criar rascunhos de Instagram e X, anexando obrigatoriamente os respectivos cards por suas URLs públicas no GitHub. Manter como rascunho até autorização explícita; nunca presumir autorização para publicar.
12. Entregar o pacote WhatsApp completo (PNG + texto com URL direta clicável) para encaminhamento manual pelo responsável.
13. Registrar URL da matéria, seção/editoria, arquivo-fonte do logo, caminhos/URLs GitHub dos cards, arquivos finais, textos, resultado da checagem visual, identificadores/status dos rascunhos no Buffer, pacote WhatsApp e aprovação.

## Checklist

- [ ] URL direta pública da matéria conferida
- [ ] Arquivo-fonte do logo oficial identificado e registrado
- [ ] Logo oficial realmente incorporado ao PNG do Instagram
- [ ] Logo oficial realmente incorporado ao PNG do X
- [ ] Logo oficial realmente incorporado ao PNG do WhatsApp
- [ ] QA visual individual dos três PNGs aprovado (integridade, proporção, corte, contraste e legibilidade)
- [ ] Chamada “Novo post do NECOOP” incluída
- [ ] ObservaCoop identificado, se aplicável, como editoria secundária
- [ ] Card Instagram 4:5
- [ ] Card X horizontal
- [ ] Card WhatsApp quadrado
- [ ] Legenda Instagram completa, com URL direta
- [ ] Texto X adaptado, com URL direta
- [ ] Post WhatsApp entregue como imagem + texto copiável + URL clicável
- [ ] Cards finais hospedados na pasta GitHub vinculada à publicação
- [ ] URLs públicas diretas dos cards testadas
- [ ] Rascunho Instagram criado via Buffer MCP, com card correto anexado e canal confirmado
- [ ] Rascunho X criado via Buffer MCP, com card correto anexado e canal confirmado
- [ ] Status de ambos confirmado como rascunho (não agendados/publicados)
- [ ] Revisão/aprovação humana
- [ ] Buffer mantido em rascunho até autorização
- [ ] Registro dos materiais e status atualizado

## Regras de controle

- Nunca afirmar que um rascunho foi criado, que uma imagem foi anexada ou que uma publicação foi enviada sem confirmação operacional.
- Se a matéria não estiver pública, o logo não puder ser verificado/incorporado, faltar recurso visual essencial ou houver dúvida factual/editorial, registrar a pendência e não improvisar.
- Se o Buffer MCP não estiver disponível no contexto de execução, registrar a limitação desta sessão; não questionar nem substituir a integração já validada pelo projeto.
- A preparação do pacote é obrigatória para cada nova publicação; a postagem efetiva depende de aprovação humana.
