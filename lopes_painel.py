import os
import sys
import json
import subprocess
import time

# ─────────────────────────────────────────────
#  Abre um CMD novo se não estiver rodando nele
# ─────────────────────────────────────────────
def relaunchar_em_cmd():
    """
    No Windows: se o script foi iniciado por duplo-clique (sem janela de
    terminal dedicada) ou via pythonw, reabre a si mesmo num CMD configurado
    com fundo preto e título personalizado.
    """
    if sys.platform != "win32":
        return  # Linux/Mac já têm terminal

    # Se já estemos dentro de um CMD/PowerShell com console real, não faz nada
    try:
        import ctypes
        if ctypes.windll.kernel32.GetConsoleWindow() != 0:
            # Já tem janela de console — só configura título e cores
            ctypes.windll.kernel32.SetConsoleTitleW("Lopes' Panel")
            # Ativa ANSI
            kernel32 = ctypes.windll.kernel32
            kernel32.SetConsoleMode(kernel32.GetStdHandle(-11), 7)
            return
    except Exception:
        pass

    # Sem janela de console: relança num CMD dedicado
    script = os.path.abspath(__file__)
    cmd = (
        f'start "Lopes\' Panel" cmd /k '
        f'"color 04 && title Lopes\' Panel && python \"{script}\""'
    )
    os.system(cmd)
    sys.exit(0)


relaunchar_em_cmd()

# ─────────────────────────────────────────────
#  Tenta importar yt-dlp; instala se não tiver
# ─────────────────────────────────────────────
try:
    import yt_dlp
except ImportError:
    print("\n[!] yt-dlp nao encontrado. Instalando...")
    subprocess.check_call([sys.executable, "-m", "pip", "install", "yt-dlp"])
    import yt_dlp

# ─────────────────────────────────────────────
#  Arquivo de configuração
# ─────────────────────────────────────────────
CONFIG_FILE = os.path.join(os.path.dirname(os.path.abspath(__file__)), "lopes_config.json")

DEFAULT_CONFIG = {
    "pasta_mp4": os.path.join(os.path.expanduser("~"), "Downloads", "LopesPanel", "MP4"),
    "pasta_mp3": os.path.join(os.path.expanduser("~"), "Downloads", "LopesPanel", "MP3"),
}

def carregar_config():
    if os.path.exists(CONFIG_FILE):
        with open(CONFIG_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    return DEFAULT_CONFIG.copy()

def salvar_config(cfg):
    with open(CONFIG_FILE, "w", encoding="utf-8") as f:
        json.dump(cfg, f, indent=4, ensure_ascii=False)

# ─────────────────────────────────────────────
#  Cores ANSI
# ─────────────────────────────────────────────
class C:
    RESET   = "\033[0m"
    BOLD    = "\033[1m"
    RED     = "\033[38;5;196m"   # vermelho vivo
    RED2    = "\033[38;5;160m"   # vermelho escuro (contraste)
    CYAN    = "\033[38;5;51m"
    GREEN   = "\033[38;5;82m"
    YELLOW  = "\033[38;5;220m"
    BLUE    = "\033[38;5;33m"
    GRAY    = "\033[38;5;244m"
    WHITE   = "\033[38;5;255m"
    MAGENTA = "\033[38;5;201m"
    ORANGE  = "\033[38;5;208m"

def enable_ansi():
    if sys.platform == "win32":
        try:
            import ctypes
            kernel32 = ctypes.windll.kernel32
            kernel32.SetConsoleMode(kernel32.GetStdHandle(-11), 7)
        except Exception:
            pass

# ─────────────────────────────────────────────
#  Banner  LOPES' PANEL  — todo em vermelho
# ─────────────────────────────────────────────
BANNER = r"""
 ██╗      ██████╗ ██████╗ ███████╗███████╗      ██████╗  █████╗ ███╗   ██╗███████╗██╗
 ██║     ██╔═══██╗██╔══██╗██╔════╝██╔════╝      ██╔══██╗██╔══██╗████╗  ██║██╔════╝██║
 ██║     ██║   ██║██████╔╝█████╗  ███████╗      ██████╔╝███████║██╔██╗ ██║█████╗  ██║
 ██║     ██║   ██║██╔═══╝ ██╔══╝  ╚════██║      ██╔═══╝ ██╔══██║██║╚██╗██║██╔══╝  ██║
 ███████╗╚██████╔╝██║     ███████╗███████║      ██║     ██║  ██║██║ ╚████║███████╗███████╗
 ╚══════╝ ╚═════╝ ╚═╝     ╚══════╝╚══════╝      ╚═╝     ╚═╝  ╚═╝╚═╝  ╚═══╝╚══════╝╚══════╝
"""

APOSTROFE = "                                                           's"

# ─────────────────────────────────────────────
#  UI helpers
# ─────────────────────────────────────────────
def limpar():
    os.system("cls" if sys.platform == "win32" else "clear")

def separador(char="═", largura=72, cor=C.RED):
    print(f"{cor}{char * largura}{C.RESET}")

def digitar(texto, cor=C.RED, delay=0.022):
    for ch in texto:
        print(f"{cor}{ch}{C.RESET}", end="", flush=True)
        time.sleep(delay)
    print()

def cabecalho():
    limpar()
    separador("▓", 72, C.RED2)
    for linha in BANNER.split("\n"):
        print(f"{C.RED}{linha}{C.RESET}")
    print(f"{C.RED2}{APOSTROFE}{C.RESET}")
    print()
    separador("▓", 72, C.RED2)
    print()

def menu_principal():
    cabecalho()
    cfg = carregar_config()
    print(f"  {C.GRAY}Pasta MP4 : {C.CYAN}{cfg['pasta_mp4']}{C.RESET}")
    print(f"  {C.GRAY}Pasta MP3 : {C.CYAN}{cfg['pasta_mp3']}{C.RESET}")
    print()
    separador("─", 52, C.RED2)
    print(f"        {C.RED}[01]{C.RESET}{C.GRAY}-->{C.RESET} {C.WHITE}Baixar Video  {C.GRAY}(MP4){C.RESET}")
    print(f"        {C.RED}[02]{C.RESET}{C.GRAY}-->{C.RESET} {C.WHITE}Baixar Audio  {C.GRAY}(MP3){C.RESET}")
    print(f"        {C.RED}[03]{C.RESET}{C.GRAY}-->{C.RESET} {C.WHITE}Configurar Pastas de Destino{C.RESET}")
    print(f"        {C.RED2}[04]{C.RESET}{C.GRAY}-->{C.RESET} {C.WHITE}Sair{C.RESET}")
    separador("─", 52, C.RED2)
    print()

# ─────────────────────────────────────────────
#  Barra de progresso
# ─────────────────────────────────────────────
def hook_progresso(d):
    if d["status"] == "downloading":
        pct   = d.get("_percent_str", "??%").strip()
        speed = d.get("_speed_str",   "??/s").strip()
        eta   = d.get("_eta_str",     "??s").strip()
        barra = progresso_bar(pct)
        print(f"\r  {C.RED}{barra}{C.RESET}  {C.GREEN}{pct:>6}{C.RESET}  "
              f"{C.YELLOW}x {speed}{C.RESET}  {C.GRAY}ETA {eta}{C.RESET}   ",
              end="", flush=True)
    elif d["status"] == "finished":
        print(f"\n  {C.GREEN}[OK] Download concluido! Processando...{C.RESET}")

def progresso_bar(pct_str, largura=28):
    try:
        valor = float(pct_str.replace("%", "").strip())
    except ValueError:
        valor = 0
    preenchido = int(largura * valor / 100)
    barra = "#" * preenchido + "." * (largura - preenchido)
    return f"[{barra}]"

# ─────────────────────────────────────────────
#  Baixar MP4
# ─────────────────────────────────────────────
def baixar_mp4():
    cabecalho()
    cfg = carregar_config()
    separador("─", 52, C.RED)
    print(f"  {C.RED}>>> MODO: DOWNLOAD MP4 (Video){C.RESET}")
    separador("─", 52, C.RED)
    print()
    print(f"  {C.GRAY}Destino: {C.CYAN}{cfg['pasta_mp4']}{C.RESET}")
    print()

    url = input(f"  {C.YELLOW}>> Cole a URL do YouTube: {C.WHITE}").strip()
    if not url:
        print(f"\n  {C.RED}[!] URL vazia. Cancelado.{C.RESET}")
        time.sleep(2)
        return

    print()
    print(f"  {C.CYAN}[*] Iniciando download MP4...{C.RESET}")
    print()

    os.makedirs(cfg["pasta_mp4"], exist_ok=True)

    opcoes = {
        # Prioriza formato que já tem vídeo+áudio no mesmo arquivo (sem merge)
        "format": "best[ext=mp4]/best[vcodec!=none][acodec!=none]/best",
        "outtmpl": os.path.join(cfg["pasta_mp4"], "%(title)s.%(ext)s"),
        "progress_hooks": [hook_progresso],
        "quiet": True,
        "no_warnings": True,
    }

    try:
        with yt_dlp.YoutubeDL(opcoes) as ydl:
            info = ydl.extract_info(url, download=True)
            titulo = info.get("title", "Desconhecido")
        print()
        separador("─", 52, C.GREEN)
        print(f"  {C.GREEN}[OK] Salvo em:{C.RESET}")
        print(f"       {C.WHITE}{titulo}{C.RESET}")
        print(f"       {C.CYAN}{cfg['pasta_mp4']}{C.RESET}")
        separador("─", 52, C.GREEN)
    except Exception as e:
        print(f"\n  {C.RED}[ERRO] {e}{C.RESET}")

    print()
    input(f"  {C.GRAY}Pressione ENTER para voltar...{C.RESET}")

# ─────────────────────────────────────────────
#  Baixar MP3
# ─────────────────────────────────────────────
def baixar_mp3():
    cabecalho()
    cfg = carregar_config()
    separador("─", 52, C.RED)
    print(f"  {C.RED}>>> MODO: DOWNLOAD MP3 (Audio){C.RESET}")
    separador("─", 52, C.RED)
    print()
    print(f"  {C.GRAY}Destino: {C.CYAN}{cfg['pasta_mp3']}{C.RESET}")
    print()

    url = input(f"  {C.YELLOW}>> Cole a URL do YouTube: {C.WHITE}").strip()
    if not url:
        print(f"\n  {C.RED}[!] URL vazia. Cancelado.{C.RESET}")
        time.sleep(2)
        return

    print()
    print(f"  {C.CYAN}[*] Baixando melhor audio disponivel (m4a/webm)...{C.RESET}")
    print()

    os.makedirs(cfg["pasta_mp3"], exist_ok=True)

    opcoes = {
        # Baixa o melhor áudio disponível sem precisar do ffmpeg
        "format": "bestaudio[ext=m4a]/bestaudio[ext=webm]/bestaudio/best[vcodec=none]/best",
        "outtmpl": os.path.join(cfg["pasta_mp3"], "%(title)s.%(ext)s"),
        "progress_hooks": [hook_progresso],
        "quiet": True,
        "no_warnings": True,
    }

    try:
        with yt_dlp.YoutubeDL(opcoes) as ydl:
            info = ydl.extract_info(url, download=True)
            titulo = info.get("title", "Desconhecido")
        print()
        separador("─", 52, C.GREEN)
        print(f"  {C.GREEN}[OK] Salvo em:{C.RESET}")
        print(f"       {C.WHITE}{titulo}{C.RESET}")
        print(f"       {C.CYAN}{cfg['pasta_mp3']}{C.RESET}")
        separador("─", 52, C.GREEN)
    except Exception as e:
        print(f"\n  {C.RED}[ERRO] {e}{C.RESET}")

    print()
    input(f"  {C.GRAY}Pressione ENTER para voltar...{C.RESET}")

# ─────────────────────────────────────────────
#  Configurar Pastas
# ─────────────────────────────────────────────
def configurar_pastas():
    cabecalho()
    cfg = carregar_config()
    separador("─", 52, C.ORANGE)
    print(f"  {C.ORANGE}>>> CONFIGURAR PASTAS DE DESTINO{C.RESET}")
    separador("─", 52, C.ORANGE)
    print()
    print(f"  {C.GRAY}(Deixe em branco para manter o valor atual){C.RESET}")
    print()

    print(f"  {C.RED}>> Pasta MP4 atual:{C.RESET}")
    print(f"     {C.CYAN}{cfg['pasta_mp4']}{C.RESET}")
    nova_mp4 = input(f"  {C.YELLOW}   Nova pasta MP4: {C.WHITE}").strip()
    if nova_mp4:
        cfg["pasta_mp4"] = nova_mp4

    print()
    print(f"  {C.RED}>> Pasta MP3 atual:{C.RESET}")
    print(f"     {C.CYAN}{cfg['pasta_mp3']}{C.RESET}")
    nova_mp3 = input(f"  {C.YELLOW}   Nova pasta MP3: {C.WHITE}").strip()
    if nova_mp3:
        cfg["pasta_mp3"] = nova_mp3

    salvar_config(cfg)
    print()
    separador("─", 52, C.GREEN)
    print(f"  {C.GREEN}[OK] Configuracoes salvas!{C.RESET}")
    print(f"       {C.GRAY}MP4 -> {C.CYAN}{cfg['pasta_mp4']}{C.RESET}")
    print(f"       {C.GRAY}MP3 -> {C.CYAN}{cfg['pasta_mp3']}{C.RESET}")
    separador("─", 52, C.GREEN)
    print()
    input(f"  {C.GRAY}Pressione ENTER para voltar...{C.RESET}")

# ─────────────────────────────────────────────
#  Loop principal
# ─────────────────────────────────────────────
def main():
    enable_ansi()

    # Define título e cor do CMD (Windows)
    if sys.platform == "win32":
        os.system("title Lopes' Panel")
        os.system("color 04")   # fundo preto (0) + texto vermelho (4)

    while True:
        menu_principal()
        escolha = input(f"  {C.RED}Oque desejas, mortal? {C.WHITE}").strip()
        print(C.RESET, end="")

        if escolha in ("1", "01"):
            baixar_mp4()
        elif escolha in ("2", "02"):
            baixar_mp3()
        elif escolha in ("3", "03"):
            configurar_pastas()
        elif escolha in ("4", "04"):
            cabecalho()
            digitar("  Ate logo, mortal...", C.RED, 0.04)
            print()
            time.sleep(1)
            sys.exit(0)
        else:
            print(f"\n  {C.RED}[!] Opcao invalida. Tente novamente.{C.RESET}")
            time.sleep(1.5)

if __name__ == "__main__":
    main()
