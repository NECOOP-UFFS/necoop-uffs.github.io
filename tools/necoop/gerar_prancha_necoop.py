#!/usr/bin/env python3

"""
Gerador de pranchas visuais para o acervo fotográfico do NECOOP.

Princípios:
- nunca altera os arquivos originais;
- processa somente a pasta explicitamente indicada;
- ignora arquivos temporários, ocultos e pranchas já produzidas;
- mantém a proporção original das imagens;
- numera as imagens de forma inequívoca;
- gera uma prancha visual e um inventário CSV.
"""

from __future__ import annotations

import argparse
import csv
from pathlib import Path

from PIL import Image, ImageOps, ImageDraw, ImageFont


EXTENSOES = {".jpg", ".jpeg", ".png", ".webp", ".tif", ".tiff"}
IGNORAR_PREFIXOS = (".",)
IGNORAR_TERMOS = (
    ".tmp",
    "prancha",
    "board",
    "backup",
)


def listar_imagens(pasta: Path) -> list[Path]:
    imagens = []

    for caminho in sorted(pasta.iterdir(), key=lambda p: p.name.lower()):
        if not caminho.is_file():
            continue

        nome = caminho.name.lower()

        if caminho.name.startswith(IGNORAR_PREFIXOS):
            continue

        if any(termo in nome for termo in IGNORAR_TERMOS):
            continue

        if caminho.suffix.lower() not in EXTENSOES:
            continue

        imagens.append(caminho)

    return imagens


def carregar_fonte(tamanho: int):
    candidatos = [
        "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf",
        "/usr/share/fonts/truetype/liberation2/LiberationSans-Regular.ttf",
    ]

    for caminho in candidatos:
        fonte = Path(caminho)
        if fonte.exists():
            return ImageFont.truetype(str(fonte), tamanho)

    return ImageFont.load_default()


def gerar_prancha(imagens: list[Path], saida: Path, colunas: int, largura_celula: int):
    margem = 30
    espaco = 20
    altura_imagem = int(largura_celula * 0.68)
    altura_texto = 90
    linhas = (len(imagens) + colunas - 1) // colunas

    largura = margem * 2 + colunas * largura_celula + (colunas - 1) * espaco
    altura = margem * 2 + linhas * (altura_imagem + altura_texto) + (linhas - 1) * espaco

    prancha = Image.new("RGB", (largura, altura), "white")
    draw = ImageDraw.Draw(prancha)

    fonte_numero = carregar_fonte(28)
    fonte_nome = carregar_fonte(18)
    fonte_info = carregar_fonte(15)

    for indice, caminho in enumerate(imagens, start=1):
        linha = (indice - 1) // colunas
        coluna = (indice - 1) % colunas

        x = margem + coluna * (largura_celula + espaco)
        y = margem + linha * (altura_imagem + altura_texto + espaco)

        try:
            with Image.open(caminho) as original:
                imagem = ImageOps.exif_transpose(original).convert("RGB")
                largura_original, altura_original = imagem.size
                miniatura = ImageOps.contain(
                    imagem,
                    (largura_celula, altura_imagem),
                )

            moldura = Image.new(
                "RGB",
                (largura_celula, altura_imagem),
                "#eeeeee",
            )

            px = (largura_celula - miniatura.width) // 2
            py = (altura_imagem - miniatura.height) // 2
            moldura.paste(miniatura, (px, py))

            prancha.paste(moldura, (x, y))

            draw.text(
                (x, y + altura_imagem + 5),
                f"{indice:02d} — {caminho.name}",
                fill="black",
                font=fonte_nome,
            )

            orientacao = (
                "horizontal"
                if largura_original > altura_original
                else "vertical"
                if altura_original > largura_original
                else "quadrada"
            )

            draw.text(
                (x, y + altura_imagem + 31),
                f"{largura_original} × {altura_original} px — {orientacao}",
                fill="#555555",
                font=fonte_info,
            )

        except Exception as exc:
            draw.text(
                (x, y + 10),
                f"{indice:02d} — ERRO: {caminho.name}",
                fill="black",
                font=fonte_numero,
            )
            draw.text(
                (x, y + 45),
                str(exc)[:80],
                fill="#555555",
                font=fonte_info,
            )

    saida.parent.mkdir(parents=True, exist_ok=True)
    prancha.save(saida, quality=95)


def gerar_inventario(imagens: list[Path], saida: Path):
    saida.parent.mkdir(parents=True, exist_ok=True)

    with saida.open("w", newline="", encoding="utf-8") as arquivo:
        escritor = csv.writer(arquivo)
        escritor.writerow(
            [
                "numero",
                "arquivo",
                "extensao",
                "largura_px",
                "altura_px",
                "orientacao",
            ]
        )

        for indice, caminho in enumerate(imagens, start=1):
            try:
                with Image.open(caminho) as imagem:
                    imagem = ImageOps.exif_transpose(imagem)
                    largura, altura = imagem.size

                orientacao = (
                    "horizontal"
                    if largura > altura
                    else "vertical"
                    if altura > largura
                    else "quadrada"
                )

                escritor.writerow(
                    [
                        indice,
                        caminho.name,
                        caminho.suffix.lower(),
                        largura,
                        altura,
                        orientacao,
                    ]
                )

            except Exception:
                escritor.writerow(
                    [
                        indice,
                        caminho.name,
                        caminho.suffix.lower(),
                        "",
                        "",
                        "ERRO",
                    ]
                )


def main():
    parser = argparse.ArgumentParser(
        description="Gera prancha visual e inventário de imagens do NECOOP."
    )

    parser.add_argument(
        "candidatos",
        type=Path,
        help="Pasta contendo EXCLUSIVAMENTE as imagens candidatas.",
    )

    parser.add_argument(
        "--saida-prancha",
        type=Path,
        default=None,
        help="Arquivo JPG da prancha.",
    )

    parser.add_argument(
        "--saida-csv",
        type=Path,
        default=None,
        help="Arquivo CSV do inventário.",
    )

    parser.add_argument(
        "--colunas",
        type=int,
        default=3,
        help="Número de colunas da prancha.",
    )

    args = parser.parse_args()

    pasta = args.candidatos.expanduser().resolve()

    if not pasta.exists():
        raise SystemExit(f"ERRO: pasta não encontrada: {pasta}")

    if not pasta.is_dir():
        raise SystemExit(f"ERRO: não é uma pasta: {pasta}")

    imagens = listar_imagens(pasta)

    if not imagens:
        raise SystemExit(
            "ERRO: nenhuma imagem candidata encontrada na pasta indicada."
        )

    saida_prancha = args.saida_prancha or (
        pasta.parent / "pranchas" / f"{pasta.name}.jpg"
    )

    saida_csv = args.saida_csv or (
        pasta.parent / "inventarios" / f"{pasta.name}.csv"
    )

    gerar_prancha(
        imagens,
        saida_prancha,
        max(1, args.colunas),
        500,
    )

    gerar_inventario(imagens, saida_csv)

    print(f"Imagens processadas: {len(imagens)}")
    print(f"Prancha: {saida_prancha}")
    print(f"Inventário: {saida_csv}")


if __name__ == "__main__":
    main()
