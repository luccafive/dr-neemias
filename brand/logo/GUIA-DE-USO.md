# Nemias Martins Advocacia — Guia de uso da marca

## 1. A marca — conceito "A Divisa"

**Ideia:** o N e o M dividem a mesma haste, a linha que define limites e une as partes. A divisa é o tema central do
Direito Imobiliário e Condominial (lotes, unidades, convivência). A haste compartilhada, em terracota, representa o
advogado como quem une as partes e resolve o conflito.

| Versão | Quando usar | Arquivo |
|---|---|---|
| **Horizontal** (principal) | Site, papel timbrado, assinatura de e-mail, placas largas | `final/nm-horizontal-*.svg` |
| **Empilhada** | Espaços quadrados ou verticais: capa de documentos, placa da sala, crachás | `final/nm-stacked-*.svg` |
| **Símbolo** | Selo em documentos, carimbo, marca d'água | `final/nm-symbol-*.svg` |
| **Somente nome** | Quando o símbolo já aparece por perto | `final/nm-wordmark-*.svg` |
| **Ícone / avatar** | Foto de perfil (Instagram, LinkedIn, WhatsApp), ícone de app | `final/nm-avatar.svg`, `final/nm-icon-tile.svg`, `final/web/` |

As versões horizontal, empilhada, símbolo e somente nome existem em quatro cores:
- `color`: verde com terracota, sobre fundo claro
- `reverse`: areia com terracota clara, sobre o Verde Divisa
- `black`: uma cor, para carimbo, gravação e fax
- `white`: uma cor, sobre fotos e fundos escuros

Use **SVG** em telas e gráfica. Os **PNG** em `final/png/` servem para Word, PowerPoint e redes sociais. Para a foto
de perfil, use `nm-avatar-1080.png`.

## 2. Área de proteção

Mantenha livre ao redor da marca um espaço igual à **altura do "M"** dividida por 4, aproximadamente a largura de uma
haste. Esse espaço cresce e diminui junto com a marca. Nada de texto, foto ou borda dentro dessa área.

## 3. Tamanho mínimo

| Versão | Tela | Impressão |
|---|---|---|
| Horizontal | 160 px de largura | 40 mm de largura |
| Empilhada | 100 px de largura | 25 mm de largura |
| Símbolo | 16 px (use `final/web/favicon.svg`) | 6 mm |

Abaixo desses tamanhos, use só o símbolo. Em tamanhos muito pequenos, a haste terracota pode se misturar ao verde.
Isso é esperado: o NM continua legível.

## 4. Cores

| Nome | HEX | RGB | CMYK (aprox.) | Uso |
|---|---|---|---|---|
| **Verde Divisa** | `#1F3D36` | 31 · 61 · 54 | 78 · 42 · 60 · 56 | Principal: letras, fundos, botões |
| **Terracota** | `#9E5536` | 158 · 85 · 54 | 20 · 70 · 85 · 20 | Destaque: a divisa, "ADVOCACIA", detalhes |
| **Terracota claro** | `#D9A486` | 217 · 164 · 134 | 12 · 38 · 48 · 0 | Somente sobre o Verde Divisa |
| **Areia** | `#F4EFE6` | 244 · 239 · 230 | 3 · 5 · 9 · 0 | Fundo padrão |
| **Pedra** | `#D9CFBF` | 217 · 207 · 191 | 14 · 15 · 25 · 0 | Apoio: linhas, divisórias, fundos secundários |
| **Grafite** | `#1C1C1A` | 28 · 28 · 26 | 70 · 65 · 65 · 80 | Texto corrido |

Os valores CMYK são aproximados. Peça uma prova de cor à gráfica antes da primeira tiragem e, se for o caso, a
referência Pantone mais próxima.

**Contraste (WCAG):**

| Combinação | Contraste | Resultado |
|---|---|---|
| Verde sobre areia | 10,3:1 | Excelente |
| Grafite sobre areia | 14,9:1 | Excelente |
| Terracota sobre areia | 4,8:1 | Aprovado para texto |
| Terracota sobre branco | 5,5:1 | Aprovado para texto |
| Terracota claro sobre verde | 5,4:1 | Aprovado para texto |

**Combinações aprovadas:**
- colorida sobre areia ou branco
- `reverse` sobre Verde Divisa
- preta sobre fundo claro
- branca sobre fotos escuras

## 5. Tipografia

- **Cormorant Garamond SemiBold**: nome da marca, títulos e frases de destaque.
- **Manrope Regular e SemiBold**: textos, rótulos, botões e "ADVOCACIA", que é escrita em caixa alta e bem espaçada.
- **No logo:** as duas fontes já estão convertidas em curvas nos arquivos. Não é preciso instalá-las para usar o logo.
- **Para documentos e site:** instale as duas fontes pelo Google Fonts (gratuitas). Os arquivos usados estão em
  `src/fonts/`.
- **Alternativas de sistema:**
  - no lugar da Cormorant Garamond: Garamond ou Georgia
  - no lugar da Manrope: Segoe UI, Helvetica ou Arial
- **Licença:** SIL Open Font License, que permite uso comercial, inclusive em logotipo.

## 6. Não faça

- Não estique, não achate e não gire a marca.
- Não troque a cor da divisa. Ela é sempre terracota, ou terracota claro sobre o verde, e o restante do NM é sempre
  de uma única cor.
- Não use a versão colorida sobre fotos ou fundos médios. Use a branca ou a preta.
- Não adicione sombras, contornos, brilhos, gradientes ou efeitos 3D.
- Não mude a proporção entre símbolo e nome, nem reescreva o nome digitando em outra fonte.
- Não combine a marca com balança, martelo ou coluna grega.

## 7. Publicidade (OAB)

A comunicação deve ser **sóbria e informativa**, conforme o Código de Ética da OAB e o Provimento 205/2021. Nas peças,
use informações objetivas (nome, OAB/SP nº, áreas de atuação, contato) e evite promessas de resultado, preços e
apelos de captação de clientes.

## 8. Arquivos

```
brand/logo/
├── final/            masters SVG (símbolo, horizontal, empilhada, nome) em 4 cores + ícone e avatar
│   ├── png/          PNGs em alta resolução, com fundo transparente
│   └── web/          favicon.ico/svg, ícones 16–512 px, apple-touch-icon, site.webmanifest, head-snippet.html
├── presentation/     apresentação (HTML) + slides em PNG com aplicações
├── concepts/         conceitos iniciais (histórico)
└── src/              build.py (gera os masters) + fontes OFL usadas
```

Para instalar os ícones no site, copie a pasta `final/web/` para a raiz pública do site e cole o conteúdo de
`head-snippet.html` dentro do `<head>`.

## 9. Pendências

- Fazer uma **pesquisa de anterioridade no INPI** (classe 45, serviços jurídicos) antes de registrar a marca.
- Incluir o número de inscrição na OAB/SP, o telefone e o e-mail reais nos cartões e no timbrado.
- Os formatos para gráfica (PDF/EPS em CMYK) podem ser exportados dos SVGs no Illustrator, Inkscape ou Affinity.
