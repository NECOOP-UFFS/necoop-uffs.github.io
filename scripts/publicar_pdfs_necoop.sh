#!/usr/bin/env bash
set -euo pipefail

# NECOOP — publicação local dos PDFs do catálogo editorial
# Execute a partir da raiz do clone local do repositório.

SOURCE="$HOME/Cloud-Drive/Necoop web/Arquivos do site necoop (via chatgpt)"
DEST="publicacoes"

mkdir -p "$DEST"

copy_pdf() {
  local src="$1"
  local dst="$2"

  if [[ ! -f "$SOURCE/$src" ]]; then
    echo "ERRO: PDF não encontrado: $SOURCE/$src" >&2
    exit 1
  fi

  cp -f "$SOURCE/$src" "$DEST/$dst"
  echo "OK: $dst"
}

copy_pdf "Analises_das_causas_das_subnotificacoes_das_intoxi.pdf" "p01.pdf"
copy_pdf "CHRISTOFFOLI-pedro-PRESA-rosecleia-AZEREDO-raoni-CHRISTOFFOLI-gustavo.pdf" "p02.pdf"
copy_pdf "CHRISTOFFOLI_pedro_CHRISTOFFOLI_gustavo.pdf" "p03.pdf"
copy_pdf "CREDITO_RURAL_COOPERATIVO_E_DESENVOLVIMENTO_LOCAL_.pdf" "p04.pdf"
copy_pdf "Cavalcanteetal_2019REVIEWComunicataScientiae.pdf" "p05.pdf"
copy_pdf "CultivoSoja1.indd.pdf" "p06.pdf"
copy_pdf "Elementos introdut história cooperação no Brasil.pdf" "p07.pdf"
copy_pdf "Estímulo à cooperação entre benef ref agrária.pdf" "p08.pdf"
copy_pdf "Núcleos de Agroecologia construção coletiva e redes.pdf" "p09.pdf"
copy_pdf "Tese_Soja Gm_PedroIvanChristoffoli.pdf" "p10.pdf"
copy_pdf "análise operacionalização PAA.pdf" "p11.pdf"
copy_pdf "artigolivromstunespeufrj.pdf" "p12.pdf"
copy_pdf "capitulo2SPDHpart.pdf" "p13.pdf"
copy_pdf "christoffolilutapelaterraedesenvolvimentolocal.pdf" "p14.pdf"
copy_pdf "dissertacao-christoffoli.pdf" "p15.pdf"

echo
printf '%s\n' "PDFs copiados para $DEST/."

echo "Verificando arquivos:"
for f in "$DEST"/*.pdf; do
  printf '  %s  %s bytes\n' "$(basename "$f")" "$(stat -c '%s' "$f")"
done

echo
git add "$DEST"/*.pdf
git status --short

git commit -m "Disponibiliza PDFs do catálogo de publicações do NECOOP"
git push origin main

echo
echo "Publicação concluída."
