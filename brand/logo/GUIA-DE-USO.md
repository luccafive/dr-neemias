# Nemias Martins Advocacia — Guia de uso da marca

## 1. A marca

**Ideia:** N e M dividem a mesma coluna central e repousam sobre um alicerce dourado. As três colunas lembram a
fachada de um edifício (Direito Imobiliário e Condominial), e a coluna compartilhada é o advogado como ponto de apoio
do cliente. O alicerce traduz os mais de 20 anos de atuação.

| Versão | Quando usar | Arquivo |
|---|---|---|
| **Horizontal** (principal) | Site, papel timbrado, assinatura de e-mail, placas largas | `final/nm-horizontal-*.svg` |
| **Empilhada** | Espaços quadrados ou verticais: capa de documentos, fachada estreita, crachás | `final/nm-stacked-*.svg` |
| **Símbolo** | Avatar de redes sociais, favicon, carimbo, selo em documentos | `final/nm-symbol-*.svg` |
| **Somente nome** | Quando o símbolo já aparece por perto (ex.: rodapé de uma página com o símbolo no topo) | `final/nm-wordmark-*.svg` |
| **Ícone** | Ícone de app/atalho, foto de perfil sobre fundo verde | `final/nm-icon-tile.svg`, `final/web/` |

Cada versão existe em quatro cores:
- `color`: verde e dourado, sobre fundo claro
- `reverse`: branco e dourado, sobre o Verde Ardósia
- `black`: uma cor, para fax, carimbo e gravação
- `white`: uma cor, sobre fotos e fundos escuros

Use **SVG** em telas e gráfica. Os **PNG** em `final/png/` servem para Word, PowerPoint e redes sociais.

## 2. Área de proteção

Mantenha livre ao redor da marca um espaço igual a **1 coluna**, ou seja, a largura de uma das hastes do NM. Esse
espaço cresce e diminui junto com a marca. Nada de texto, foto ou borda dentro dessa área.

## 3. Tamanho mínimo

| Versão | Tela | Impressão |
|---|---|---|
| Horizontal | 140 px de largura | 35 mm de largura |
| Empilhada | 90 px de largura | 22 mm de largura |
| Símbolo | 16 px (use `final/web/favicon.svg`) | 6 mm |

Abaixo desses tamanhos, use só o símbolo.

## 4. Cores

| Nome | HEX | RGB | CMYK (aprox.) | Pantone (aprox.) | Uso |
|---|---|---|---|---|---|
| **Verde Ardósia** | `#1D3B36` | 29 · 59 · 54 | 78 · 42 · 60 · 58 | 5535 C | Cor principal: letras do símbolo, nome, fundos |
| **Dourado Antigo** | `#A9874E` | 169 · 135 · 78 | 25 · 38 · 75 · 15 | 7562 C / 872 C (metálico) | Somente o alicerce e "ADVOCACIA". Nunca em textos longos |
| **Pergaminho** | `#F5F1E8` | 245 · 241 · 232 | 3 · 4 · 9 · 0 | — | Fundo claro alternativo ao branco |
| Branco | `#FFFFFF` | 255 · 255 · 255 | 0 · 0 · 0 · 0 | — | Fundo padrão |

Os valores CMYK e Pantone são aproximados. Peça uma prova de cor à gráfica antes da primeira tiragem. Para cartões de
visita sofisticados, o alicerce pode ser feito em hot stamping dourado.

**Contraste:** verde sobre branco 12,1:1 (excelente). O dourado sobre branco (3,4:1) funciona na marca, mas **não
deve ser usado em textos corridos**.

**Combinações aprovadas:** colorida sobre branco ou Pergaminho · `reverse` sobre Verde Ardósia · preta sobre branco ·
branca sobre fotos escuras ou fundos escuros.

## 5. Tipografia

- **Nome da marca:** Caladea Regular, já convertida em curvas nos arquivos. Não é preciso instalar a fonte para usar
  o logo.
- **"ADVOCACIA":** Inter Medium, espaçamento amplo, já convertida em curvas.
- **Para documentos e site:**
  - Títulos em serifa: Caladea, ou Georgia/Cambria como alternativas de sistema.
  - Textos em Inter, ou Arial/Helvetica.
- **Licenças:** Caladea (Apache 2.0) e Inter (SIL Open Font License) são gratuitas, inclusive para uso comercial e em
  logotipos.

## 6. Não faça

- Não estique, não achate e não gire a marca.
- Não troque as cores fora da paleta. Em especial, não pinte o NM de dourado nem o alicerce de verde.
- Não adicione sombras, contornos, brilhos, gradientes ou efeitos 3D.
- Não separe o alicerce do NM nem mude a proporção entre símbolo e nome.
- Não reescreva o nome digitando-o em outra fonte. Use sempre os arquivos.
- Não aplique a versão colorida sobre fotos ou fundos médios. Use a branca ou a preta.
- Não combine a marca com balança, martelo ou coluna grega.

## 7. Publicidade (OAB)

O Código de Ética e o Provimento 205/2021 da OAB pedem publicidade **sóbria e informativa**. A marca foi pensada para
isso. Nas peças, prefira informações objetivas (nome, OAB/SP nº, áreas de atuação, contato) e evite promessas de
resultado, preços e apelos de captação de clientes.

## 8. Arquivos

```
brand/logo/
├── final/            masters SVG (símbolo, horizontal, empilhada, nome, ícone) em 4 cores
│   ├── png/          PNGs em alta resolução, com fundo transparente
│   └── web/          favicon.ico/svg, ícones 16–512 px, apple-touch-icon, site.webmanifest, head-snippet.html
├── presentation/     apresentação (HTML) + slides em PNG com aplicações
├── concepts/         conceitos iniciais (histórico)
└── src/build.py      script que gera os masters (geometria documentada)
```

Para instalar os ícones no site, copie a pasta `final/web/` para a raiz pública do site e cole o conteúdo de
`head-snippet.html` dentro do `<head>`.

## 9. Pendências

- Fazer uma **pesquisa de anterioridade no INPI** (classe 45, serviços jurídicos) antes de registrar a marca. Este
  trabalho não substitui essa busca.
- Incluir o número de inscrição na OAB/SP nos cartões e no timbrado.
- Formatos para gráfica (PDF/EPS em CMYK) podem ser exportados dos SVGs no Illustrator, Inkscape ou Affinity.
