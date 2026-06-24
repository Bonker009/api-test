from fastapi import FastAPI
from fastapi.responses import HTMLResponse

from app.v1.app import v1_app
from app.v2.app import v2_app
from app.v3.app import v3_app
from app.cinema.v1.app import cinema_v1
from app.cinema.v2.app import cinema_v2
from app.cinema.v3.app import cinema_v3
from app.store.v1.app import store_v1
from app.store.v2.app import store_v2
from app.store.v3.app import store_v3

app = FastAPI(title="API Developer Portal", docs_url=None, redoc_url=None)

app.mount("/gallery/v1", v1_app)
app.mount("/gallery/v2", v2_app)
app.mount("/gallery/v3", v3_app)
app.mount("/cinema/v1",  cinema_v1)
app.mount("/cinema/v2",  cinema_v2)
app.mount("/cinema/v3",  cinema_v3)
app.mount("/store/v1",   store_v1)
app.mount("/store/v2",   store_v2)
app.mount("/store/v3",   store_v3)

LANDING_HTML = """<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8"/>
  <meta name="viewport" content="width=device-width, initial-scale=1.0"/>
  <title>tideAPI — Developer Portal</title>
  <link rel="preconnect" href="https://fonts.googleapis.com"/>
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin/>
  <link href="https://fonts.googleapis.com/css2?family=Nunito:wght@400;600;700;800;900&family=DM+Sans:wght@400;500;600&family=DM+Mono:wght@400;500&display=swap" rel="stylesheet"/>
  <style>
    :root {
      --page-bg:    #eaf6fb;
      --ocean:      #4a9eb8;
      --ocean-dk:   #2d7a96;
      --reef:       #1a3d4a;
      --foam:       #f4fafd;
      --ocean-lt:   #d6edf7;
      --seagrass:   #3aab7b;
      --coral:      #e06c5a;
      --text:       #1e3d4a;
      --text-mid:   #4a7080;
      --text-muted: #8aacb8;
      --border:     #c4dce8;
      --border-h:   #88c0d8;
      --white:      #ffffff;
      --r:          18px;
      --sh:         0 4px 24px rgba(74,158,184,.10);
      --sh-h:       0 12px 40px rgba(74,158,184,.20);
    }
    *, *::before, *::after { box-sizing: border-box; margin: 0; padding: 0; }
    html { scroll-behavior: smooth; }

    body {
      font-family: 'DM Sans', system-ui, sans-serif;
      background: var(--page-bg);
      color: var(--text);
      min-height: 100vh;
      overflow-x: hidden;
    }

    /* ─── AMBIENT BACKGROUND WAVES ─────────────────────────────── */
    /* Very faint drifting waves permanently in the background      */
    .bg-waves {
      position: fixed; inset: 0; z-index: 0;
      pointer-events: none; overflow: hidden;
      opacity: .18;
    }
    .bg-wave-track {
      position: absolute; bottom: -60px; left: 0;
      display: flex; width: 200%;
    }
    .bg-wave-track svg { width: 50%; flex-shrink: 0; }
    .bg-wave-track.t1 { bottom: 10%;  animation: drift 28s linear infinite; }
    .bg-wave-track.t2 { bottom: 30%;  animation: drift 38s linear infinite reverse; }
    .bg-wave-track.t3 { bottom: 55%;  animation: drift 50s linear infinite; }

    @keyframes drift {
      from { transform: translateX(0); }
      to   { transform: translateX(-50%); }
    }

    /* ─── HERO ──────────────────────────────────────────────────── */
    .hero {
      position: relative;
      min-height: 88vh;
      display: flex; flex-direction: column;
      overflow: hidden;
    }

    /* ocean photo */
    .hero-photo {
      position: absolute; inset: 0; z-index: 0;
      background-image: url('https://images.unsplash.com/photo-1507525428034-b723cf961d3e?auto=format&fit=crop&w=1920&q=80');
      background-size: cover; background-position: center 40%;
    }
    /* gradient overlay: dark on top (for nav), fades to page color at bottom */
    .hero-photo::after {
      content: '';
      position: absolute; inset: 0;
      background: linear-gradient(
        to bottom,
        rgba(10, 28, 45, .55)  0%,
        rgba(10, 28, 45, .28) 45%,
        rgba(10, 28, 45, .08) 68%,
        rgba(234, 246, 251, 1) 100%
      );
    }

    /* ─── NAV (sits inside hero, above photo) ─── */
    nav {
      position: relative; z-index: 10;
      display: flex; align-items: center; justify-content: space-between;
      padding: 22px 40px; max-width: 1160px; margin: 0 auto; width: 100%;
    }
    .nav-logo {
      display: flex; align-items: center; gap: 9px;
      font-family: 'Nunito', sans-serif;
      font-weight: 900; font-size: 1.15rem;
      color: #fff; text-decoration: none; letter-spacing: -.01em;
      text-shadow: 0 1px 8px rgba(0,0,0,.3);
    }
    .logo-icon { font-size: 1.5rem; line-height: 1; }
    .nav-status {
      display: flex; align-items: center; gap: 7px;
      background: rgba(255,255,255,.15);
      backdrop-filter: blur(12px); -webkit-backdrop-filter: blur(12px);
      border: 1px solid rgba(255,255,255,.25);
      border-radius: 999px; padding: 7px 16px;
      font-size: .78rem; font-weight: 600; color: rgba(255,255,255,.9);
    }
    .dot {
      width: 7px; height: 7px; border-radius: 50%;
      background: #5debb8;
      box-shadow: 0 0 0 3px rgba(93,235,184,.25);
      animation: breathe 3s ease-in-out infinite;
    }
    @keyframes breathe {
      0%,100% { box-shadow: 0 0 0 3px rgba(93,235,184,.2); }
      50%      { box-shadow: 0 0 0 7px rgba(93,235,184,.07); }
    }

    /* ─── HERO TEXT ─── */
    .hero-body {
      position: relative; z-index: 5;
      flex: 1; display: flex; flex-direction: column;
      align-items: center; justify-content: center;
      text-align: center;
      padding: 32px 28px 140px;
    }
    .hero-eyebrow {
      font-size: .75rem; font-weight: 700;
      letter-spacing: .14em; text-transform: uppercase;
      color: rgba(180, 230, 255, .85);
      margin-bottom: 14px;
    }
    h1 {
      font-family: 'Nunito', sans-serif;
      font-size: clamp(2.6rem, 6vw, 4.2rem);
      font-weight: 900; line-height: 1.06;
      color: #fff;
      text-shadow: 0 2px 20px rgba(0,0,0,.25);
      margin-bottom: 18px; letter-spacing: -.03em;
      max-width: 720px;
    }
    h1 em { font-style: normal; color: #a8e6f8; }
    .hero-sub {
      font-size: 1.05rem; color: rgba(220,240,255,.85);
      max-width: 460px; line-height: 1.7; font-weight: 400;
      text-shadow: 0 1px 6px rgba(0,0,0,.2);
    }

    /* ─── HERO WAVES (3 layers, seamless loop) ────────────────── */
    .hero-waves {
      position: absolute; bottom: -2px; left: 0; right: 0;
      z-index: 6; overflow: hidden; line-height: 0;
    }
    .wave-track {
      display: flex; width: 200%;
    }
    .wave-track svg { width: 50%; flex-shrink: 0; display: block; }

    /* layer 1 — back, slowest, deeper color */
    .wt1 { animation: drift 14s linear infinite; }
    /* layer 2 — mid */
    .wt2 { animation: drift 9s linear infinite reverse; margin-top: -48px; position: relative; z-index: 1; }
    /* layer 3 — front, fastest, matches page bg exactly */
    .wt3 { animation: drift 6s linear infinite; margin-top: -44px; position: relative; z-index: 2; }

    /* ─── PAGE BODY ──────────────────────────────────────────── */
    .wrap {
      position: relative; z-index: 2;
      max-width: 1140px; margin: 0 auto; padding: 0 28px;
    }

    /* ─── STATS SHELF ─── */
    .stats-shelf {
      background: var(--white);
      border: 1.5px solid var(--border);
      border-radius: 20px;
      display: flex; overflow: hidden;
      margin: 0 0 52px;
      box-shadow: var(--sh);
    }
    .stat {
      flex: 1; padding: 22px 16px; text-align: center;
      border-right: 1.5px solid var(--border);
      transition: background .2s;
    }
    .stat:last-child { border-right: none; }
    .stat:hover { background: var(--ocean-lt); }
    .stat-value {
      font-family: 'Nunito', sans-serif;
      font-size: 2rem; font-weight: 900; color: var(--ocean-dk); line-height: 1;
    }
    .stat-label {
      font-size: .7rem; font-weight: 700; color: var(--text-muted);
      text-transform: uppercase; letter-spacing: .08em; margin-top: 5px;
    }

    /* ─── SECTION HEADER ─── */
    .section-header { margin-bottom: 22px; }
    .section-title {
      font-family: 'Nunito', sans-serif;
      font-size: 1.35rem; font-weight: 900; color: var(--reef); letter-spacing: -.01em;
    }
    .section-sub { font-size: .82rem; color: var(--text-muted); margin-top: 3px; }

    /* ─── PROJECT GRID ─── */
    .projects {
      display: grid;
      grid-template-columns: repeat(auto-fill, minmax(340px, 1fr));
      gap: 22px; margin-bottom: 80px;
    }

    /* ─── CARD ─── */
    .card {
      background: var(--white);
      border: 1.5px solid var(--border);
      border-radius: 20px;
      box-shadow: var(--sh);
      overflow: hidden;
      transition: transform .24s ease, box-shadow .24s ease, border-color .24s;
    }
    .card:hover { transform: translateY(-6px); box-shadow: var(--sh-h); border-color: var(--border-h); }

    /* ─── CARD (new design) ───────────────────────────────────── */
    .card {
      border-radius: 22px; padding: 28px 26px 24px;
      border: 1.5px solid;
      transition: transform .26s ease, box-shadow .26s ease;
    }
    .card.gallery { background: #f3f9fd; border-color: #b8d8ed; }
    .card.cinema  { background: #fdf6f4; border-color: #ecc8b8; }
    .card.store   { background: #f3fdf7; border-color: #acd8c0; }
    .card.gallery:hover { transform: translateY(-7px); box-shadow: 0 20px 52px rgba(60,148,184,.15); }
    .card.cinema:hover  { transform: translateY(-7px); box-shadow: 0 20px 52px rgba(210,100,80,.15); }
    .card.store:hover   { transform: translateY(-7px); box-shadow: 0 20px 52px rgba(50,160,110,.15); }

    /* icon + name row */
    .c-head { display: flex; align-items: center; gap: 12px; margin-bottom: 12px; }
    .c-icon { font-size: 2rem; line-height: 1; flex-shrink: 0; }
    .c-name {
      font-family: 'Nunito', sans-serif;
      font-size: 1.08rem; font-weight: 900; color: var(--reef); line-height: 1.2;
    }
    .c-desc {
      font-size: .82rem; color: var(--text-muted); line-height: 1.65;
      margin-bottom: 16px;
    }

    /* resource paths — inline monospace list */
    .c-paths {
      display: flex; flex-wrap: wrap; gap: 5px;
      margin-bottom: 20px;
    }
    .c-path {
      font-family: 'DM Mono', monospace; font-size: .65rem;
      color: var(--ocean-dk); background: rgba(74,158,184,.08);
      border: 1px solid rgba(74,158,184,.18);
      border-radius: 6px; padding: 3px 8px;
    }

    /* changelog header */
    .cl-head {
      display: flex; align-items: center; gap: 10px; margin-bottom: 14px;
    }
    .cl-title {
      font-size: .62rem; font-weight: 800; letter-spacing: .12em;
      text-transform: uppercase; color: var(--text-muted); white-space: nowrap;
    }
    .cl-rule { flex: 1; height: 1px; background: var(--border); }

    /* timeline */
    .timeline { position: relative; padding-left: 24px; }
    .timeline::before {
      content: ''; position: absolute;
      left: 5px; top: 12px; bottom: 12px; width: 1.5px;
      background: linear-gradient(to bottom, #70bcd8 0%, #60c898 50%, #e08870 100%);
      border-radius: 2px;
    }
    .tl-item {
      position: relative; padding: 9px 0;
    }
    /* connecting dot */
    .tl-item::before {
      content: ''; position: absolute;
      left: -24px; top: 13px;
      width: 12px; height: 12px; border-radius: 50%;
      background: var(--white); border: 2.5px solid; z-index: 1;
    }
    .tl-item.vi1::before { border-color: #4a9eb8; box-shadow: 0 0 0 3px rgba(74,158,184,.12); }
    .tl-item.vi2::before { border-color: #3aab7b; box-shadow: 0 0 0 3px rgba(58,171,123,.12); }
    .tl-item.vi3::before { border-color: #e06c5a; box-shadow: 0 0 0 3px rgba(224,108,90,.12); }

    /* each item: two rows */
    .tl-top {
      display: flex; align-items: center; gap: 6px;
      flex-wrap: wrap; margin-bottom: 6px;
    }
    .tl-ver {
      font-family: 'DM Mono', monospace; font-size: .68rem; font-weight: 600;
      padding: 2px 9px; border-radius: 6px; flex-shrink: 0;
    }
    .tl-item.vi1 .tl-ver { background: #daedf8; color: #286080; border: 1px solid #a4cce0; }
    .tl-item.vi2 .tl-ver { background: #d4f0e6; color: #1e6048; border: 1px solid #84ccac; }
    .tl-item.vi3 .tl-ver { background: #fdeee8; color: #884030; border: 1px solid #eaac9c; }

    .tl-pills { display: flex; gap: 4px; flex-wrap: wrap; }
    .cpill {
      font-size: .59rem; font-weight: 700; padding: 2px 7px; border-radius: 99px;
    }
    .breaking    { background: #fdecea; color: #b83c38; border: 1px solid #edb0a8; }
    .nonbreaking { background: #e0f7ec; color: #287048; border: 1px solid #90d4b0; }

    .tl-btns { display: flex; gap: 5px; padding-left: 2px; }
    a.vbtn {
      font-size: .66rem; font-weight: 600; padding: 4px 11px; border-radius: 7px;
      text-decoration: none; white-space: nowrap;
      transition: transform .12s ease, box-shadow .12s ease;
    }
    a.vbtn:hover { transform: translateY(-1px); }
    a.sw { background: #daedf8; color: #286080; border: 1px solid #a4cce0; }
    a.sw:hover { box-shadow: 0 3px 10px rgba(74,158,184,.22); }
    a.rd { background: #d4f0e6; color: #1e6048; border: 1px solid #84ccac; }
    a.rd:hover { box-shadow: 0 3px 10px rgba(58,171,123,.2); }

    /* ─── FOOTER ─── */
    .footer-wave { line-height: 0; }
    .footer-wave svg { display: block; width: 100%; }
    footer {
      background: var(--ocean-lt);
      border-top: 1.5px solid var(--border);
      padding: 26px;
      text-align: center; color: var(--text-mid); font-size: .8rem;
    }
    footer code {
      font-family: 'DM Mono', monospace;
      background: var(--white); border: 1px solid var(--border);
      padding: 2px 8px; border-radius: 6px; font-size: .77rem; color: var(--ocean-dk);
    }

    /* ─── RESPONSIVE ─── */
    @media (max-width: 700px) {
      nav { padding: 18px 20px; }
      h1  { font-size: 2.4rem; }
      .stats-shelf { flex-direction: column; }
      .stat { border-right: none; border-bottom: 1.5px solid var(--border); }
      .stat:last-child { border-bottom: none; }
      .projects { grid-template-columns: 1fr; }
    }
  </style>
</head>
<body>

  <!-- ── AMBIENT BACKGROUND WAVES ── -->
  <div class="bg-waves" aria-hidden="true">
    <div class="bg-wave-track t1">
      <svg viewBox="0 0 1440 160" preserveAspectRatio="none">
        <path d="M0,80 C180,140 360,20 540,80 C720,140 900,20 1080,80 C1260,140 1440,20 1440,80 L1440,160 L0,160Z" fill="#4a9eb8"/>
      </svg>
      <svg viewBox="0 0 1440 160" preserveAspectRatio="none">
        <path d="M0,80 C180,140 360,20 540,80 C720,140 900,20 1080,80 C1260,140 1440,20 1440,80 L1440,160 L0,160Z" fill="#4a9eb8"/>
      </svg>
    </div>
    <div class="bg-wave-track t2">
      <svg viewBox="0 0 1440 120" preserveAspectRatio="none">
        <path d="M0,60 C200,110 400,10 600,60 C800,110 1000,10 1200,60 C1320,85 1400,40 1440,60 L1440,120 L0,120Z" fill="#2d7a96"/>
      </svg>
      <svg viewBox="0 0 1440 120" preserveAspectRatio="none">
        <path d="M0,60 C200,110 400,10 600,60 C800,110 1000,10 1200,60 C1320,85 1400,40 1440,60 L1440,120 L0,120Z" fill="#2d7a96"/>
      </svg>
    </div>
    <div class="bg-wave-track t3">
      <svg viewBox="0 0 1440 100" preserveAspectRatio="none">
        <path d="M0,50 C160,90 320,10 480,50 C640,90 800,10 960,50 C1120,90 1280,10 1440,50 L1440,100 L0,100Z" fill="#88c8e0"/>
      </svg>
      <svg viewBox="0 0 1440 100" preserveAspectRatio="none">
        <path d="M0,50 C160,90 320,10 480,50 C640,90 800,10 960,50 C1120,90 1280,10 1440,50 L1440,100 L0,100Z" fill="#88c8e0"/>
      </svg>
    </div>
  </div>

  <!-- ── HERO ── -->
  <section class="hero">
    <div class="hero-photo"></div>

    <!-- NAV (floats over photo) -->
    <nav>
      <a class="nav-logo" href="/">
        <span class="logo-icon">🌊</span>
        tideAPI
      </a>
      <div class="nav-status">
        <div class="dot"></div>
        9 versions live
      </div>
    </nav>

    <!-- HEADLINE -->
    <div class="hero-body">
      <div class="hero-eyebrow">API Developer Portal</div>
      <h1>Where great APIs<br><em>meet the shore</em></h1>
      <p class="hero-sub">
        Three versioned REST APIs with live Swagger docs.
        Watch flat strings become rich objects — one version at a time.
      </p>
    </div>

    <!-- 3-LAYER ANIMATED WAVES — transition hero photo into page -->
    <div class="hero-waves" aria-hidden="true">
      <!-- back wave -->
      <div class="wave-track wt1">
        <svg viewBox="0 0 1440 110" preserveAspectRatio="none">
          <path d="M0,55 C200,100 400,10 600,55 C800,100 1000,10 1200,55 C1320,78 1400,35 1440,55 L1440,110 L0,110Z" fill="rgba(180,222,240,.55)"/>
        </svg>
        <svg viewBox="0 0 1440 110" preserveAspectRatio="none">
          <path d="M0,55 C200,100 400,10 600,55 C800,100 1000,10 1200,55 C1320,78 1400,35 1440,55 L1440,110 L0,110Z" fill="rgba(180,222,240,.55)"/>
        </svg>
      </div>
      <!-- mid wave -->
      <div class="wave-track wt2">
        <svg viewBox="0 0 1440 90" preserveAspectRatio="none">
          <path d="M0,45 C180,85 360,5 540,45 C720,85 900,5 1080,45 C1260,85 1380,20 1440,45 L1440,90 L0,90Z" fill="rgba(210,238,250,.75)"/>
        </svg>
        <svg viewBox="0 0 1440 90" preserveAspectRatio="none">
          <path d="M0,45 C180,85 360,5 540,45 C720,85 900,5 1080,45 C1260,85 1380,20 1440,45 L1440,90 L0,90Z" fill="rgba(210,238,250,.75)"/>
        </svg>
      </div>
      <!-- front wave — exact page-bg color, seals the transition -->
      <div class="wave-track wt3">
        <svg viewBox="0 0 1440 70" preserveAspectRatio="none">
          <path d="M0,35 C160,65 320,5 480,35 C640,65 800,5 960,35 C1120,65 1280,5 1440,35 L1440,70 L0,70Z" fill="#eaf6fb"/>
        </svg>
        <svg viewBox="0 0 1440 70" preserveAspectRatio="none">
          <path d="M0,35 C160,65 320,5 480,35 C640,65 800,5 960,35 C1120,65 1280,5 1440,35 L1440,70 L0,70Z" fill="#eaf6fb"/>
        </svg>
      </div>
    </div>
  </section>

  <!-- ── PAGE CONTENT ── -->
  <div class="wrap">

    <!-- STATS -->
    <div class="stats-shelf">
      <div class="stat"><div class="stat-value">3</div><div class="stat-label">Projects</div></div>
      <div class="stat"><div class="stat-value">9</div><div class="stat-label">Versions</div></div>
      <div class="stat"><div class="stat-value">36</div><div class="stat-label">Endpoints</div></div>
      <div class="stat"><div class="stat-value">0</div><div class="stat-label">Databases</div></div>
    </div>

    <!-- APIs -->
    <div class="section-header">
      <div class="section-title">Available APIs</div>
      <div class="section-sub">Open Swagger or ReDoc on any version for interactive docs</div>
    </div>

    <div class="projects">

      <!-- GALLERY MUSEUM -->
      <div class="card gallery">
        <div class="c-head">
          <span class="c-icon">🖼️</span>
          <span class="c-name">Gallery Museum API</span>
        </div>
        <p class="c-desc">Artworks, galleries and exhibitions — flat strings that grow into rich nested objects across each version.</p>
        <div class="c-paths">
          <span class="c-path">/artworks</span>
          <span class="c-path">/galleries</span>
          <span class="c-path">/exhibitions</span>
          <span class="c-path">/artworks/{id}/related</span>
        </div>
        <div class="cl-head"><span class="cl-title">Changelog</span><div class="cl-rule"></div></div>
        <div class="timeline">
          <div class="tl-item vi1">
            <div class="tl-top">
              <span class="tl-ver">v1</span>
              <div class="tl-pills"><span class="cpill nonbreaking">baseline</span></div>
            </div>
            <div class="tl-btns">
              <a class="vbtn sw" href="/gallery/v1/docs">Swagger</a>
              <a class="vbtn rd" href="/gallery/v1/redoc">ReDoc</a>
            </div>
          </div>
          <div class="tl-item vi2">
            <div class="tl-top">
              <span class="tl-ver">v2</span>
              <div class="tl-pills">
                <span class="cpill breaking">artist→artist_name</span>
                <span class="cpill breaking">location→object</span>
                <span class="cpill nonbreaking">+related</span>
              </div>
            </div>
            <div class="tl-btns">
              <a class="vbtn sw" href="/gallery/v2/docs">Swagger</a>
              <a class="vbtn rd" href="/gallery/v2/redoc">ReDoc</a>
            </div>
          </div>
          <div class="tl-item vi3">
            <div class="tl-top">
              <span class="tl-ver">v3</span>
              <div class="tl-pills">
                <span class="cpill breaking">paginated list</span>
                <span class="cpill breaking">year→created_at</span>
                <span class="cpill nonbreaking">+exhibitions</span>
              </div>
            </div>
            <div class="tl-btns">
              <a class="vbtn sw" href="/gallery/v3/docs">Swagger</a>
              <a class="vbtn rd" href="/gallery/v3/redoc">ReDoc</a>
            </div>
          </div>
        </div>
      </div>

      <!-- CINEMA BOOKING -->
      <div class="card cinema">
        <div class="c-head">
          <span class="c-icon">🎬</span>
          <span class="c-name">Cinema Booking API</span>
        </div>
        <p class="c-desc">Movies, showtimes and bookings — genre strings become arrays, directors gain nationality over time.</p>
        <div class="c-paths">
          <span class="c-path">/movies</span>
          <span class="c-path">/showtimes</span>
          <span class="c-path">/bookings</span>
          <span class="c-path">/movies/{id}/showtimes</span>
        </div>
        <div class="cl-head"><span class="cl-title">Changelog</span><div class="cl-rule"></div></div>
        <div class="timeline">
          <div class="tl-item vi1">
            <div class="tl-top">
              <span class="tl-ver">v1</span>
              <div class="tl-pills"><span class="cpill nonbreaking">baseline</span></div>
            </div>
            <div class="tl-btns">
              <a class="vbtn sw" href="/cinema/v1/docs">Swagger</a>
              <a class="vbtn rd" href="/cinema/v1/redoc">ReDoc</a>
            </div>
          </div>
          <div class="tl-item vi2">
            <div class="tl-top">
              <span class="tl-ver">v2</span>
              <div class="tl-pills">
                <span class="cpill breaking">year→release_year</span>
                <span class="cpill breaking">screen→venue object</span>
                <span class="cpill nonbreaking">+movie showtimes</span>
              </div>
            </div>
            <div class="tl-btns">
              <a class="vbtn sw" href="/cinema/v2/docs">Swagger</a>
              <a class="vbtn rd" href="/cinema/v2/redoc">ReDoc</a>
            </div>
          </div>
          <div class="tl-item vi3">
            <div class="tl-top">
              <span class="tl-ver">v3</span>
              <div class="tl-pills">
                <span class="cpill breaking">genre→genres[]</span>
                <span class="cpill breaking">director→object</span>
                <span class="cpill nonbreaking">+bookings</span>
              </div>
            </div>
            <div class="tl-btns">
              <a class="vbtn sw" href="/cinema/v3/docs">Swagger</a>
              <a class="vbtn rd" href="/cinema/v3/redoc">ReDoc</a>
            </div>
          </div>
        </div>
      </div>

      <!-- STORE -->
      <div class="card store">
        <div class="c-head">
          <span class="c-icon">🛍️</span>
          <span class="c-name">Store API</span>
        </div>
        <p class="c-desc">Products, orders and categories — prices evolve from a plain float into a full currency object.</p>
        <div class="c-paths">
          <span class="c-path">/products</span>
          <span class="c-path">/orders</span>
          <span class="c-path">/categories</span>
          <span class="c-path">/products/{id}/related</span>
        </div>
        <div class="cl-head"><span class="cl-title">Changelog</span><div class="cl-rule"></div></div>
        <div class="timeline">
          <div class="tl-item vi1">
            <div class="tl-top">
              <span class="tl-ver">v1</span>
              <div class="tl-pills"><span class="cpill nonbreaking">baseline</span></div>
            </div>
            <div class="tl-btns">
              <a class="vbtn sw" href="/store/v1/docs">Swagger</a>
              <a class="vbtn rd" href="/store/v1/redoc">ReDoc</a>
            </div>
          </div>
          <div class="tl-item vi2">
            <div class="tl-top">
              <span class="tl-ver">v2</span>
              <div class="tl-pills">
                <span class="cpill breaking">category→object</span>
                <span class="cpill breaking">total→total_amount</span>
                <span class="cpill nonbreaking">+related products</span>
              </div>
            </div>
            <div class="tl-btns">
              <a class="vbtn sw" href="/store/v2/docs">Swagger</a>
              <a class="vbtn rd" href="/store/v2/redoc">ReDoc</a>
            </div>
          </div>
          <div class="tl-item vi3">
            <div class="tl-top">
              <span class="tl-ver">v3</span>
              <div class="tl-pills">
                <span class="cpill breaking">price→{amount,cur}</span>
                <span class="cpill breaking">customer→object</span>
                <span class="cpill nonbreaking">+categories</span>
              </div>
            </div>
            <div class="tl-btns">
              <a class="vbtn sw" href="/store/v3/docs">Swagger</a>
              <a class="vbtn rd" href="/store/v3/redoc">ReDoc</a>
            </div>
          </div>
        </div>
      </div>

    </div>
  </div>

  <!-- FOOTER -->
  <div class="footer-wave">
    <svg viewBox="0 0 1440 56" preserveAspectRatio="none" xmlns="http://www.w3.org/2000/svg">
      <path d="M0,28 C180,56 360,0 540,28 C720,56 900,0 1080,28 C1260,56 1380,14 1440,28 L1440,56 L0,56Z" fill="#d6edf7"/>
    </svg>
  </div>
  <footer>
    <span style="opacity:.5">🌊</span>
  </footer>

</body>
</html>"""


@app.get("/", response_class=HTMLResponse, include_in_schema=False)
def landing_page():
    return LANDING_HTML
