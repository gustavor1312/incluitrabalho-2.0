import streamlit as st
from datetime import date
import html as _html
import streamlit.components.v1 as components

st.set_page_config(
    page_title="IncluiTrabalho 2.0",
    page_icon="♿",
    layout="wide",
    initial_sidebar_state="collapsed"
)

DEFAULT_VAGAS = [
    {"id": 1, "titulo": "Desenvolvedor Front-end Jr", "empresa": "TechAcessível",
     "local": "Remoto", "modalidade": "Remoto",
     "descricao": "Desenvolvimento de interfaces digitais acessíveis.",
     "pcd": True, "libras": False, "leitor": True, "legendas": True},
    {"id": 2, "titulo": "Analista de Dados", "empresa": "InclusãoDigital",
     "local": "São Paulo, SP", "modalidade": "Híbrido",
     "descricao": "Análise de dados e elaboração de relatórios.",
     "pcd": False, "libras": True, "leitor": True, "legendas": True},
    {"id": 3, "titulo": "Assistente Administrativo", "empresa": "Empresa Inclusiva",
     "local": "Caieiras, SP", "modalidade": "Presencial",
     "descricao": "Apoio administrativo, organização de documentos e atendimento.",
     "pcd": True, "libras": True, "leitor": True, "legendas": True},
]

if "vagas" not in st.session_state:
    st.session_state.vagas = [dict(v) for v in DEFAULT_VAGAS]
if "perfil" not in st.session_state:
    st.session_state.perfil = {}
if "candidaturas" not in st.session_state:
    st.session_state.candidaturas = []
if "modo_empresa" not in st.session_state:
    st.session_state.modo_empresa = False
if "fonte" not in st.session_state:
    st.session_state.fonte = 16
if "contraste" not in st.session_state:
    st.session_state.contraste = False
if "aviso" not in st.session_state:
    st.session_state.aviso = ""

def esc(v):
    return _html.escape(str(v or ""))

def avisar(msg, tipo="success"):
    st.session_state.aviso = (tipo, msg)

def rolar_para(element_id):
    """Injeta JavaScript para rolar a tela ate o elemento desejado."""
    js = f"""
    <script>
        var el = window.parent.document.getElementById('{element_id}');
        if (el) {{
            el.scrollIntoView({{behavior: 'smooth', block: 'start'}});
        }}
    </script>
    """
    components.html(js, height=0, width=0)

primary = "#00d9ff" if st.session_state.contraste else "#2563eb"
bg = "#05070a" if st.session_state.contraste else "#eef3f8"
surface = "#111820" if st.session_state.contraste else "#ffffff"
text = "#ffffff" if st.session_state.contraste else "#172033"
muted = "#d6dce5" if st.session_state.contraste else "#596579"
border = "#ffffff" if st.session_state.contraste else "#d7e0ea"
fonte_tamanho = f"{st.session_state.fonte}px"

st.markdown(f"""
<style>
/* Ajuste dinâmico do tamanho da fonte global */
html, body, [data-testid="stAppViewContainer"], .stApp, p, span, label, input, textarea, select, button {{
    font-size: {fonte_tamanho} !important;
}}

html, body, [data-testid="stAppViewContainer"], [data-testid="stApp"], .stApp {{
    background: {bg} !important;
}}
[data-testid="stHeader"] {{
    background: {bg} !important;
    box-shadow: none !important;
}}
[data-testid="stToolbar"] {{
    background: transparent !important;
}}
.block-container {{
    max-width: 1100px !important;
    padding-top: 1.2rem !important;
    padding-bottom: 3rem !important;
}}
.stApp p, .stApp label, .stApp h1, .stApp h2, .stApp h3, .stApp h4,
.stApp [data-testid="stMarkdownContainer"] {{
    color: {text};
}}
.hero {{
    background: linear-gradient(135deg, {"#111820,#111820" if st.session_state.contraste else "#e8f1ff,#ffffff"}) !important;
    border: 1px solid {border};
    border-radius: 16px;
    padding: 30px;
    margin: 20px 0;
    box-shadow: 0 5px 20px rgba(15,23,42,.08);
}}
.card {{
    background: {surface} !important;
    color: {text} !important;
    border: 1px solid {border};
    border-radius: 14px;
    padding: 20px;
    margin-bottom: 16px;
    box-shadow: 0 4px 18px rgba(15,23,42,.08);
}}
.card h2, .card h3, .card p, .card strong {{
    color: {text} !important;
}}
.meta {{
    color: {muted} !important;
}}
.badge {{
    display:inline-block;
    border-radius:999px;
    padding:4px 10px;
    background:#e8f1ff;
    color:#1456c4 !important;
    font-size:.82rem !important;
    font-weight:700;
    margin:2px 4px 8px 0;
}}
.badge.green {{
    background:#e8f7ed;
    color:#15803d !important;
}}
.notice {{
    padding:13px 15px;
    border-radius:999px;
    margin:12px 0;
}}
.notice.success {{ background:#eaf7ee; border-left:5px solid #15803d; color:#14532d; }}
.notice.info {{ background:#eaf2ff; border-left:5px solid #2563eb; color:#173b76; }}
.notice.error {{ background:#feecec; border-left:5px solid #dc2626; color:#7f1d1d; }}

div[data-testid="stButton"] > button,
div[data-testid="stFormSubmitButton"] > button {{
    background: #ffffff !important;
    color: #17345f !important;
    border: 1px solid #b9c8da !important;
    border-radius: 10px !important;
    font-weight: 700 !important;
    min-height: 42px !important;
    box-shadow: 0 2px 8px rgba(15,23,42,.06) !important;
}}
div[data-testid="stButton"] > button:hover,
div[data-testid="stFormSubmitButton"] > button:hover {{
    background: #eaf2ff !important;
    color: #0f3f91 !important;
    border-color: {primary} !important;
}}
.stTextInput input, .stTextArea textarea,
.stSelectbox [data-baseweb="select"] > div {{
    background: {surface} !important;
    color: {text} !important;
    border-color: {border} !important;
}}
.stCheckbox label, .stRadio label {{
    color: {text} !important;
}}
[data-testid="stAlert"] {{
    border-radius: 10px;
}}
footer {{ visibility: hidden; }}
</style>
""", unsafe_allow_html=True)

# Cabeçalho
st.markdown(f"""
<div id="sec-inicio" style="
display:flex;align-items:center;justify-content:space-between;
padding:8px 0 14px;border-bottom:4px solid {primary};
margin-bottom:18px;gap:20px;">
<div style="font-weight:800;font-size:1.35rem;color:{text};">♿ IncluiTrabalho 2.0</div>
<div style="font-weight:600;color:{muted};">Plataforma inclusiva de oportunidades de emprego</div>
</div>
""", unsafe_allow_html=True)

# Menu Superior de Navegação
nav = st.columns(5)
with nav[0]: 
    if st.button("Início", use_container_width=True):
        rolar_para("sec-inicio")
with nav[1]: 
    if st.button("Vagas", use_container_width=True):
        rolar_para("sec-vagas")
with nav[2]: 
    if st.button("Meu perfil", use_container_width=True):
        rolar_para("sec-perfil")
with nav[3]: 
    if st.button("Candidaturas", use_container_width=True):
        rolar_para("sec-candidaturas")
with nav[4]: 
    if st.button("Empresa", use_container_width=True):
        st.session_state.modo_empresa = True
        rolar_para("sec-empresa")

# Recursos de acessibilidade
st.markdown('<div class="card"><h3>♿ Recursos de acessibilidade</h3><p>Use os controles visuais ou os controles de voz abaixo.</p></div>',
            unsafe_allow_html=True)

a1, a2, a3 = st.columns(3)
with a1:
    if st.button("A+ Aumentar fonte", use_container_width=True):
        st.session_state.fonte = min(24, st.session_state.fonte + 2)
        st.rerun()
with a2:
    if st.button("A− Diminuir fonte", use_container_width=True):
        st.session_state.fonte = max(14, st.session_state.fonte - 2)
        st.rerun()
with a3:
    if st.button("◐ Alto contraste", use_container_width=True):
        st.session_state.contraste = not st.session_state.contraste
        st.rerun()

# Voz no navegador
voice_html = """
<!doctype html>
<html lang="pt-BR">
<head>
<meta charset="utf-8">
<style>
body { margin:0; font-family:Arial,sans-serif; background:transparent; }
.row { display:flex; flex-wrap:wrap; gap:10px; }
button {
  border:1px solid #9fb4cc; border-radius:10px; padding:12px 15px;
  background:#fff; color:#17345f; font-weight:700; cursor:pointer;
}
button:hover { background:#eaf2ff; }
#status { margin-top:10px; padding:10px 12px; border-radius:9px;
  background:#eaf7ee; color:#14532d; font-size:14px; }
</style>
</head>
<body>
<div class="row">
<button onclick="lerPagina()">🔊 Ler página</button>
<button onclick="pararLeitura()">⏹ Parar leitura</button>
<button onclick="comandoVoz()">🎙 Comando de voz</button>
</div>
<div id="status">Voz pronta. Clique em “Ler página” para ouvir o conteúdo.</div>
<script>
let reconhecimento = null;

function textoPagina() {
  const main = window.parent.document.querySelector('section.main');
  if (!main) return window.parent.document.body.innerText;
  return main.innerText.replace(/\\s+/g, ' ').trim();
}

function lerPagina() {
  pararLeitura();
  const texto = textoPagina();
  if (!('speechSynthesis' in window)) {
    document.getElementById('status').textContent = 'Seu navegador não oferece leitura por voz.';
    return;
  }
  const partes = texto.match(/.{1,450}(?:\\s|$)/g) || [texto];
  let i = 0;
  function falarProxima() {
    if (i >= partes.length) {
      document.getElementById('status').textContent = 'Leitura concluída.';
      return;
    }
    const u = new SpeechSynthesisUtterance(partes[i++]);
    u.lang = 'pt-BR';
    u.rate = 0.95;
    u.onend = falarProxima;
    speechSynthesis.speak(u);
  }
  document.getElementById('status').textContent = '🔊 Lendo a página...';
  falarProxima();
}

function pararLeitura() {
  if ('speechSynthesis' in window) speechSynthesis.cancel();
  document.getElementById('status').textContent = 'Leitura parada.';
}

function comandoVoz() {
  const SR = window.parent.SpeechRecognition || window.parent.webkitSpeechRecognition;
  if (!SR) {
    document.getElementById('status').textContent =
      'Reconhecimento de voz não disponível. Use Chrome ou Edge.';
    return;
  }
  if (reconhecimento) reconhecimento.stop();
  reconhecimento = new SR();
  reconhecimento.lang = 'pt-BR';
  reconhecimento.continuous = false;
  reconhecimento.interimResults = false;
  reconhecimento.onstart = () => {
    document.getElementById('status').textContent = '🎙 Ouvindo... Diga um comando.';
  };
  reconhecimento.onresult = (e) => {
    const comando = e.results[0][0].transcript.toLowerCase();
    document.getElementById('status').textContent = 'Comando reconhecido: ' + comando;
    if (comando.includes('ler') || comando.includes('leia')) lerPagina();
    else if (comando.includes('parar')) pararLeitura();
  };
  reconhecimento.onerror = () => {
    document.getElementById('status').textContent = 'Erro ao reconhecer a voz. Verifique a permissão do microfone.';
  };
  reconhecimento.start();
}
</script>
</body>
</html>
"""
components.html(voice_html, height=115, scrolling=False)

if st.session_state.aviso:
    tipo, msg = st.session_state.aviso
    st.markdown(f'<div class="notice {tipo}">{esc(msg)}</div>', unsafe_allow_html=True)
    st.session_state.aviso = ""

# Hero
st.markdown("""
<div class="hero">
<h1>Oportunidades para todos.</h1>
<p>Encontre vagas, apresente seu talento e informe às empresas quais recursos de acessibilidade você precisa.</p>
<p><strong>IncluiTrabalho 2.0</strong> — protótipo de plataforma inclusiva.</p>
</div>
""", unsafe_allow_html=True)

b1, b2 = st.columns(2)
with b1:
    if st.button("🔎 Encontrar vagas", use_container_width=True):
        rolar_para("sec-vagas")
with b2:
    if st.button("👤 Criar meu perfil", use_container_width=True):
        rolar_para("sec-perfil")

c1, c2 = st.columns(2)
with c1:
    st.markdown('<div class="card"><h2>♿ Acessibilidade</h2><p>Fonte ajustável, alto contraste e organização acessível da interface.</p></div>',
                unsafe_allow_html=True)
with c2:
    st.markdown('<div class="card"><h2>🧏 Recursos para pessoas surdas</h2><p>As vagas podem informar Libras, entrevistas por vídeo, comunicação escrita e legendas.</p></div>',
                unsafe_allow_html=True)

# Seção de Vagas
st.markdown('<div id="sec-vagas"></div>', unsafe_allow_html=True)
st.header("🔎 Buscar oportunidades")

f1, f2, f3, f4 = st.columns([2,1,1,1])
with f1:
    busca = st.text_input("Cargo, empresa ou palavra-chave", key="busca")
with f2:
    locais = ["Todos os locais"] + sorted({v["local"] for v in st.session_state.vagas})
    local = st.selectbox("Local", locais)
with f3:
    acess = st.selectbox("Acessibilidade", ["Acessibilidade", "Libras", "Leitor de tela", "Remoto"])
with f4:
    if st.button("Limpar filtros", use_container_width=True):
        st.session_state.busca = ""
        st.rerun()

arr = []
for v in st.session_state.vagas:
    texto = f'{v["titulo"]} {v["empresa"]} {v["descricao"]}'.lower()
    okq = not busca or busca.lower() in texto
    okl = local == "Todos os locais" or v["local"] == local
    oka = (
        acess == "Acessibilidade" or
        (acess == "Libras" and v["libras"]) or
        (acess == "Leitor de tela" and v["leitor"]) or
        (acess == "Remoto" and v["modalidade"] == "Remoto")
    )
    if okq and okl and oka:
        arr.append(v)

for v in arr:
    badges = ""
    if v["pcd"]: badges += '<span class="badge green">♿ Exclusiva PCD</span>'
    if v["libras"]: badges += '<span class="badge">🧏 Libras</span>'
    if v["leitor"]: badges += '<span class="badge">🔊 Leitor de tela</span>'
    if v["legendas"]: badges += '<span class="badge">CC Legendas</span>'
    st.markdown(f"""
    <div class="card">
      {badges}
      <div style="font-size:1.2rem;font-weight:800;color:{text};">{esc(v["titulo"])}</div>
      <div class="meta">🏢 {esc(v["empresa"])} · 📍 {esc(v["local"])} · {esc(v["modalidade"])}</div>
      <p>{esc(v["descricao"])}</p>
    </div>
    """, unsafe_allow_html=True)
    x, y = st.columns(2)
    with x:
        if st.button("Ver detalhes", key=f"det_{v['id']}", use_container_width=True):
            st.session_state[f"detalhe_{v['id']}"] = not st.session_state.get(f"detalhe_{v['id']}", False)
    with y:
        if st.button("📩 Candidatar-me", key=f"cand_{v['id']}", use_container_width=True):
            p = st.session_state.perfil
            if not p.get("nome"):
                avisar("Preencha e salve seu perfil antes de enviar uma candidatura.", "info")
                rolar_para("sec-perfil")
            elif any(c["vagaId"] == v["id"] for c in st.session_state.candidaturas):
                avisar("Você já se candidatou a esta vaga.", "error")
            else:
                st.session_state.candidaturas.insert(0, {
                    "id": len(st.session_state.candidaturas)+1,
                    "vagaId": v["id"], "nome": p["nome"],
                    "data": date.today().strftime("%d/%m/%Y"), "status": "Enviada"
                })
                avisar("Candidatura enviada com sucesso!", "success")
                rolar_para("sec-candidaturas")
    if st.session_state.get(f"detalhe_{v['id']}", False):
        recursos = [
            ("Atendimento/interação em Libras", v["libras"]),
            ("Compatibilidade com leitor de tela", v["leitor"]),
            ("Vídeos/entrevistas com legendas", v["legendas"]),
        ]
        st.markdown(f"""
        <div class="card">
        <h3>Detalhes — {esc(v["titulo"])}</h3>
        <p><strong>Empresa:</strong> {esc(v["empresa"])}</p>
        <p><strong>Local:</strong> {esc(v["local"])}</p>
        <p><strong>Modalidade:</strong> {esc(v["modalidade"])}</p>
        <h4>Acessibilidade oferecida</h4>
        <ul>{''.join(f"<li>{'✅' if ok else '❌'} {esc(nome)}</li>" for nome, ok in recursos)}</ul>
        </div>
        """, unsafe_allow_html=True)

if not arr:
    st.info("Nenhuma vaga encontrada com esses filtros.")

# Seção de Perfil
st.markdown('<div id="sec-perfil"></div>', unsafe_allow_html=True)
st.header("👤 Meu perfil profissional")
p = st.session_state.perfil
with st.form("perfil_form"):
    c1, c2 = st.columns(2)
    with c1:
        nome = st.text_input("Nome", value=p.get("nome",""))
        email = st.text_input("E-mail", value=p.get("email",""))
        telefone = st.text_input("Telefone", value=p.get("telefone",""))
        cidade = st.text_input("Cidade", value=p.get("cidade",""), placeholder="Ex.: Caieiras - SP")
    with c2:
        objetivo = st.text_area("Objetivo profissional", value=p.get("objetivo",""))
        habilidades = st.text_input("Habilidades", value=p.get("habilidades",""), placeholder="Ex.: informática, atendimento...")
        curriculo = st.text_input("Link do currículo (opcional)", value=p.get("curriculo",""))
    st.subheader("Recursos de acessibilidade necessários")
    q1, q2, q3 = st.columns(3)
    with q1:
        visual = st.checkbox("Apoio para deficiência visual / leitor de tela", value=p.get("visual",False))
        surda = st.checkbox("Comunicação acessível para pessoa surda", value=p.get("surda",False))
    with q2:
        libras = st.checkbox("Intérprete / atendimento em Libras", value=p.get("libras",False))
        legendas = st.checkbox("Vídeos e entrevistas com legendas", value=p.get("legendas",False))
    with q3:
        outros = st.checkbox("Outro recurso", value=p.get("outros",False))
    salvar = st.form_submit_button("💾 Salvar perfil")

if salvar:
    if not nome.strip() or not email.strip():
        avisar("Nome e e-mail são obrigatórios.", "error")
    else:
        st.session_state.perfil = {
            "nome": nome.strip(), "email": email.strip(), "telefone": telefone.strip(),
            "cidade": cidade.strip(), "objetivo": objetivo.strip(),
            "habilidades": habilidades.strip(), "curriculo": curriculo.strip(),
            "visual": visual, "surda": surda, "libras": libras,
            "legendas": legendas, "outros": outros
        }
        avisar("Perfil salvo nesta sessão.", "success")

# Seção de Candidaturas
st.markdown('<div id="sec-candidaturas"></div>', unsafe_allow_html=True)
st.header("📩 Minhas candidaturas")
if not st.session_state.candidaturas:
    st.info("Você ainda não enviou nenhuma candidatura.")
else:
    for c in st.session_state.candidaturas:
        v = next((x for x in st.session_state.vagas if x["id"] == c["vagaId"]), None)
        if v:
            st.markdown(f"""
            <div class="card">
              <div style="font-size:1.2rem;font-weight:800;color:{text};">{esc(v["titulo"])}</div>
              <div class="meta">{esc(v["empresa"])} · Candidatura em {esc(c["data"])}</div>
              <p>Status: <strong>{esc(c["status"])}</strong></p>
            </div>
            """, unsafe_allow_html=True)

# Seção Empresa
if st.session_state.modo_empresa:
    st.markdown('<div id="sec-empresa"></div>', unsafe_allow_html=True)
    st.header("🏢 Área da empresa")
    st.info("Cadastre uma oportunidade e informe claramente os recursos de acessibilidade oferecidos.")
    with st.form("vaga_form"):
        t, e = st.columns(2)
        with t:
            vtitulo = st.text_input("Título da vaga *", placeholder="Ex.: Assistente Administrativo")
            vempresa = st.text_input("Empresa *", placeholder="Nome da empresa")
            vlocal = st.text_input("Local *", placeholder="Remoto / São Paulo, SP")
        with e:
            vtipo = st.selectbox("Modalidade", ["Presencial", "Híbrido", "Remoto"])
            vdesc = st.text_area("Descrição", placeholder="Atividades, requisitos e informações importantes.")
        st.subheader("Recursos oferecidos")
        a,b,c,d = st.columns(4)
        with a: vlibras = st.checkbox("Atendimento/interação em Libras")
        with b: vleitor = st.checkbox("Ambiente compatível com leitor de tela")
        with c: vlegendas = st.checkbox("Entrevista/vídeo com legendas")
        with d: vpcd = st.checkbox("Vaga exclusiva para PCD")
        publicar = st.form_submit_button("📢 Publicar vaga")

    if publicar:
        if not vtitulo.strip() or not vempresa.strip() or not vlocal.strip():
            avisar("Preencha título, empresa e local.", "error")
        else:
            novo_id = max([v["id"] for v in st.session_state.vagas] + [0]) + 1
            st.session_state.vagas.insert(0, {
                "id": novo_id, "titulo": vtitulo.strip(), "empresa": vempresa.strip(),
                "local": vlocal.strip(), "modalidade": vtipo,
                "descricao": vdesc.strip() or "Sem descrição",
                "libras": vlibras, "leitor": vleitor, "legendas": vlegendas, "pcd": vpcd
            })
            avisar("Vaga publicada com sucesso!", "success")
            st.rerun()

    st.subheader("📋 Vagas cadastradas")
    for v in st.session_state.vagas:
        st.markdown(f"""
        <div class="card">
          <strong>{esc(v["titulo"])}</strong>
          <p class="meta">{esc(v["empresa"])} · {esc(v["local"])}</p>
        </div>
        """, unsafe_allow_html=True)
        if st.button("🗑️ Excluir", key=f"del_{v['id']}"):
            st.session_state.vagas = [x for x in st.session_state.vagas if x["id"] != v["id"]]
            st.session_state.candidaturas = [c for c in st.session_state.candidaturas if c["vagaId"] != v["id"]]
            st.rerun()

st.markdown(f"<hr><div style='text-align:center;color:{muted};padding:20px;'>IncluiTrabalho 2.0 — protótipo de plataforma de inclusão profissional.</div>",
            unsafe_allow_html=True)