
from pathlib import Path
import base64

import streamlit as st
import streamlit.components.v1 as components


# ============================================================
# CONFIGURAÇÃO DA PÁGINA
# ============================================================

st.set_page_config(
    page_title="Portal SGA",
    page_icon="🏫",
    layout="wide",
    initial_sidebar_state="collapsed"
)


# ============================================================
# CAMINHO DA PASTA DO PROJETO
# ============================================================

PASTA_PROJETO = Path(__file__).parent


# ============================================================
# ARQUIVOS DE IMAGEM
# ============================================================

FUNDO = PASTA_PROJETO / "fundo.png"
LOGO_SESI = PASTA_PROJETO / "logoSesi.jpg"

IMAGEM_NOTAS = PASTA_PROJETO / "notas.png"
IMAGEM_LAYERS = PASTA_PROJETO / "layers.png"
IMAGEM_BIBLIOTECA = PASTA_PROJETO / "biblioteca.png"
IMAGEM_REPOSITORIO = PASTA_PROJETO / "repositorio.png"


# ============================================================
# LINKS
# ============================================================

LINK_NOTAS = "https://sgenotasalunos.streamlit.app/"
LINK_LAYERS = "https://sesiescolalayers.streamlit.app"

# Futuramente:
# LINK_BIBLIOTECA = "https://..."
# LINK_REPOSITORIO = "https://..."


# ============================================================
# VERIFICAÇÃO DOS ARQUIVOS
# ============================================================

arquivos = {
    "fundo.png": FUNDO,
    "logoSesi.jpg": LOGO_SESI,
    "notas.png": IMAGEM_NOTAS,
    "layers.png": IMAGEM_LAYERS,
    "biblioteca.png": IMAGEM_BIBLIOTECA,
    "repositorio.png": IMAGEM_REPOSITORIO,
}

arquivos_faltando = [
    nome for nome, caminho in arquivos.items()
    if not caminho.exists()
]

if arquivos_faltando:

    st.error(
        "Não foi possível localizar os seguintes arquivos na pasta do projeto:"
    )

    for arquivo in arquivos_faltando:
        st.write(f"- {arquivo}")

    st.info(
        "Verifique se todos os arquivos de imagem estão dentro da mesma "
        "pasta do arquivo portalSGA.py."
    )

    st.stop()


# ============================================================
# FUNÇÃO PARA CONVERTER IMAGEM EM BASE64
# ============================================================

def imagem_base64(caminho):

    return base64.b64encode(
        caminho.read_bytes()
    ).decode("utf-8")


# ============================================================
# CONVERSÃO DAS IMAGENS
# ============================================================

fundo_base64 = imagem_base64(FUNDO)
logo_base64 = imagem_base64(LOGO_SESI)

notas_base64 = imagem_base64(IMAGEM_NOTAS)
layers_base64 = imagem_base64(IMAGEM_LAYERS)
biblioteca_base64 = imagem_base64(IMAGEM_BIBLIOTECA)
repositorio_base64 = imagem_base64(IMAGEM_REPOSITORIO)


# ============================================================
# HTML DO PORTAL
# ============================================================

html_portal = f"""
<!DOCTYPE html>

<html lang="pt-BR">

<head>

<meta charset="UTF-8">

<meta name="viewport" content="width=device-width, initial-scale=1.0">


<style>

/* ==========================================================
   RESET
   ========================================================== */

* {{
    box-sizing: border-box;
}}


html,
body {{
    margin: 0;
    padding: 0;
    width: 100%;
    min-height: 100%;
}}


/* ==========================================================
   BODY
   ========================================================== */

body {{

    font-family:
        Arial,
        Helvetica,
        sans-serif;

    overflow-x: hidden;

    background-image:
        linear-gradient(
            rgba(255, 255, 255, 0.08),
            rgba(255, 255, 255, 0.08)
        ),
        url("data:image/png;base64,{fundo_base64}");

    background-size: cover;

    background-position: center center;

    background-repeat: no-repeat;

    background-attachment: fixed;

}}


/* ==========================================================
   ÁREA PRINCIPAL
   ========================================================== */

.portal {{

    width: 100%;

    min-height: 100vh;

    padding:
        25px
        40px
        50px;

    position: relative;

    background-image:
        linear-gradient(
            rgba(255, 255, 255, 0.08),
            rgba(255, 255, 255, 0.08)
        ),
        url("data:image/png;base64,{fundo_base64}");

    background-size: cover;

    background-position: center center;

    background-repeat: no-repeat;

    background-attachment: fixed;

}}


/* ==========================================================
   LOGO SESI
   ========================================================== */

.logo-sesi {{

    position: absolute;

    top: 25px;

    left: 35px;

    width: 125px;

    height: auto;

    display: block;

    border-radius: 5px;

    box-shadow:
        0 3px 12px rgba(0, 0, 0, 0.18);

}}


/* ==========================================================
   TÍTULO
   ========================================================== */

.titulo {{

    text-align: center;

    padding-top: 25px;

    margin-bottom: 45px;

    font-size: 30px;

    font-weight: 700;

    letter-spacing: 1px;

    color: #1f1f1f;

    text-shadow:
        0 1px 2px rgba(255, 255, 255, 0.7);

}}


/* ==========================================================
   GRID DOS SISTEMAS
   ========================================================== */

.grid-sistemas {{

    width: 100%;

    max-width: 900px;

    margin: 0 auto;

    display: grid;

    grid-template-columns: repeat(2, 1fr);

    column-gap: 70px;

    row-gap: 45px;

    justify-items: center;

}}


/* ==========================================================
   CADA SISTEMA
   ========================================================== */

.sistema {{

    width: 270px;

    text-align: center;

}}


/* ==========================================================
   ÁREA DA IMAGEM COM LINK
   ========================================================== */

.link-imagem {{

    display: block;

    width: 250px;

    height: 250px;

    margin: 0 auto;

    overflow: hidden;

    border-radius: 18px;

    background: white;

    box-shadow:
        0 8px 22px rgba(0, 0, 0, 0.20);

    text-decoration: none;

    transition:
        transform 0.25s ease,
        box-shadow 0.25s ease;

}}


.link-imagem:hover {{

    transform:
        translateY(-6px)
        scale(1.02);

    box-shadow:
        0 14px 30px rgba(0, 0, 0, 0.28);

}}


.link-imagem img {{

    width: 100%;

    height: 100%;

    display: block;

    object-fit: cover;

}}


/* ==========================================================
   IMAGENS SEM LINK
   ========================================================== */

.imagem-inativa {{

    width: 250px;

    height: 250px;

    margin: 0 auto;

    overflow: hidden;

    border-radius: 18px;

    background: white;

    box-shadow:
        0 8px 22px rgba(0, 0, 0, 0.20);

}}


.imagem-inativa img {{

    width: 100%;

    height: 100%;

    display: block;

    object-fit: cover;

}}


/* ==========================================================
   NOME DO SISTEMA
   ========================================================== */

.nome-sistema {{

    margin-top: 15px;

    font-size: 17px;

    font-weight: 700;

    line-height: 1.3;

    color: #202020;

    text-shadow:
        0 1px 2px rgba(255, 255, 255, 0.8);

}}


/* ==========================================================
   SISTEMAS INATIVOS
   ========================================================== */

.indisponivel {{

    margin-top: 5px;

    font-size: 12px;

    color: #555;

    font-weight: 500;

}}


/* ==========================================================
   RODAPÉ
   ========================================================== */

.rodape {{

    text-align: center;

    margin-top: 55px;

    padding-bottom: 10px;

    font-size: 12px;

    line-height: 1.7;

    color: #555;

    text-shadow:
        0 1px 2px rgba(255, 255, 255, 0.8);

}}


/* ==========================================================
   RESPONSIVIDADE
   ========================================================== */

@media (max-width: 700px) {{

    .portal {{

        min-height: 100vh;

        padding:
            20px
            20px
            40px;

    }}


    .logo-sesi {{

        position: relative;

        top: auto;

        left: auto;

        width: 95px;

        margin:
            0 auto
            25px;

    }}


    .titulo {{

        padding-top: 0;

        margin-bottom: 30px;

        font-size: 24px;

    }}


    .grid-sistemas {{

        grid-template-columns: 1fr;

        row-gap: 35px;

        column-gap: 0;

    }}


    .sistema {{

        width: 270px;

    }}


    .link-imagem,
    .imagem-inativa {{

        width: 250px;

        height: 250px;

    }}


    .rodape {{

        margin-top: 40px;

    }}

}}

</style>

</head>


<body>


<div class="portal">


    <!-- =====================================================
         LOGO SESI
         ===================================================== -->

    <img
        class="logo-sesi"
        src="data:image/jpeg;base64,{logo_base64}"
        alt="SESI"
    >


    <!-- =====================================================
         TÍTULO
         ===================================================== -->

    <div class="titulo">
        PORTAL SGA
    </div>


    <!-- =====================================================
         SISTEMAS
         ===================================================== -->

    <div class="grid-sistemas">


        <!-- =================================================
             ANÁLISE DE NOTAS
             ================================================= -->

        <div class="sistema">

            <a
                href="{LINK_NOTAS}"
                target="_blank"
                rel="noopener noreferrer"
                class="link-imagem"
            >

                <img
                    src="data:image/png;base64,{notas_base64}"
                    alt="Análise de Notas SGE"
                >

            </a>

            <div class="nome-sistema">
                Análise de Notas SGE
            </div>

        </div>


        <!-- =================================================
             LAYERS
             ================================================= -->

        <div class="sistema">

            <a
                href="{LINK_LAYERS}"
                target="_blank"
                rel="noopener noreferrer"
                class="link-imagem"
            >

                <img
                    src="data:image/png;base64,{layers_base64}"
                    alt="SESI Escola Layers"
                >

            </a>

            <div class="nome-sistema">
                Análises do Layers/SGA
            </div>

        </div>


        <!-- =================================================
             BIBLIOTECA
             ================================================= -->

        <div class="sistema">

            <div class="imagem-inativa">

                <img
                    src="data:image/png;base64,{biblioteca_base64}"
                    alt="Biblioteca - GED"
                >

            </div>

            <div class="nome-sistema">
                Biblioteca - GED
            </div>

            <div class="indisponivel">
                Em breve
            </div>

        </div>


        <!-- =================================================
             REPOSITÓRIO
             ================================================= -->

        <div class="sistema">

            <div class="imagem-inativa">

                <img
                    src="data:image/png;base64,{repositorio_base64}"
                    alt="Repositório - Projetos"
                >

            </div>

            <div class="nome-sistema">
                Repositório - Projetos
            </div>

            <div class="indisponivel">
                Em breve
            </div>

        </div>


    </div>


    <!-- =====================================================
         RODAPÉ
         ===================================================== -->

    <div class="rodape">
        Portal de Acesso aos Sistemas<br>
        Devs Jéssica Martins - Cientista da Informação
    </div>


</div>


</body>

</html>
"""


# ============================================================
# AJUSTES DO STREAMLIT
# ============================================================

st.markdown(
    """
    <style>

    .block-container {
        padding-top: 0 !important;
        padding-bottom: 0 !important;
        padding-left: 0 !important;
        padding-right: 0 !important;
        max-width: 100% !important;
    }

    header {
        visibility: hidden;
    }

    footer {
        visibility: hidden;
    }

    [data-testid="stHeader"] {
        display: none;
    }

    [data-testid="stToolbar"] {
        display: none;
    }

    iframe {
        border: none !important;
        width: 100% !important;
    }

    </style>
    """,
    unsafe_allow_html=True
)


# ============================================================
# EXIBIÇÃO DO PORTAL
# ============================================================

components.html(
    html_portal,
    height=1050,
    scrolling=False
)
