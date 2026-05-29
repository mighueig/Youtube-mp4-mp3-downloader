# 🔴 Lopes' Panel

> Baixador de vídeos e áudios do YouTube com interface hacker no terminal.

```
 ██╗      ██████╗ ██████╗ ███████╗███████╗      ██████╗  █████╗ ███╗   ██╗███████╗██╗
 ██║     ██╔═══██╗██╔══██╗██╔════╝██╔════╝      ██╔══██╗██╔══██╗████╗  ██║██╔════╝██║
 ██║     ██║   ██║██████╔╝█████╗  ███████╗      ██████╔╝███████║██╔██╗ ██║█████╗  ██║
 ██║     ██║   ██║██╔═══╝ ██╔══╝  ╚════██║      ██╔═══╝ ██╔══██║██║╚██╗██║██╔══╝  ██║
 ███████╗╚██████╔╝██║     ███████╗███████║      ██║     ██║  ██║██║ ╚████║███████╗███████╗
 ╚══════╝ ╚═════╝ ╚═╝     ╚══════╝╚══════╝      ╚═╝     ╚═╝  ╚═╝╚═╝  ╚═══╝╚══════╝╚══════╝
                                                                                        's
```

---

## ✅ Funcionalidades

| Opção | Função |
|-------|--------|
| `[01]` | Baixar vídeo em **MP4** |
| `[02]` | Baixar áudio em **M4A/WebM** (sem ffmpeg) |
| `[03]` | Configurar pastas de destino |
| `[04]` | Sair |

- Interface colorida estilo terminal hacker
- Barra de progresso animada com velocidade e ETA
- Abre CMD automaticamente ao dar duplo clique
- Configurações salvas em `lopes_config.json`
- Instala `yt-dlp` automaticamente se não estiver presente

---

## ⚙️ Requisitos

- **Python 3.8+** → [python.org/downloads](https://www.python.org/downloads/)
  - Durante a instalação, marque ✅ **"Add Python to PATH"**
- **yt-dlp** (instalado automaticamente pelo script ou pelo `install.bat`)

> **Áudio em MP3 de verdade?** Instale o [ffmpeg](https://ffmpeg.org/download.html) e adicione ao PATH. O script detecta e usa automaticamente.

---

## 🚀 Como usar

### Opção 1 — Instalação rápida (recomendado)

```
1. Baixe ou clone este repositório
2. Dê duplo clique em  install.bat  (instala as dependências)
3. Dê duplo clique em  run.bat      (abre o painel)
```

### Opção 2 — Via terminal

```bash
# Instalar dependências
pip install -r requirements.txt

# Rodar
python lopes_painel.py
```

### Opção 3 — Clonar via Git

```bash
git clone https://github.com/SEU_USUARIO/lopes-panel.git
cd lopes-panel
pip install -r requirements.txt
python lopes_painel.py
```

---

## 📁 Estrutura do projeto

```
lopes-panel/
├── lopes_painel.py      # Script principal
├── run.bat              # Inicializador Windows (duplo clique)
├── install.bat          # Instalador de dependências Windows
├── requirements.txt     # Dependências Python
├── .gitignore           # Arquivos ignorados pelo Git
└── README.md            # Este arquivo
```

> O arquivo `lopes_config.json` é gerado automaticamente na primeira configuração e está no `.gitignore`.

---

## 📦 Pastas de download padrão

```
C:\Users\SEU_USUARIO\Downloads\LopesPanel\
├── MP4\    ← vídeos
└── MP3\    ← áudios
```

Você pode alterar pelo menu `[03]` dentro do painel.

---

## 🛠️ Tecnologias

- [Python 3](https://www.python.org/)
- [yt-dlp](https://github.com/yt-dlp/yt-dlp)
- ANSI Escape Codes para cores no terminal

---

## 📄 Licença

MIT License — use à vontade.
