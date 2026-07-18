-- ============================================================
-- Game Guides — Seed Definitivo
-- ============================================================

BEGIN;

-- =============================================================================
-- DATOS INICIALES - Languages
-- =============================================================================

INSERT INTO pf_languages (name, img_url, is_enabled) VALUES
('C#', 'https://res.cloudinary.com/dsvkbe0mc/image/upload/v1775410722/language/nr8vdnjridkymdt61kgh.webp', TRUE),
('CSS3', 'https://res.cloudinary.com/dsvkbe0mc/image/upload/v1775410869/language/efa0g6dd8rvb3qhzp49z.webp', TRUE),
('HTML5', 'https://res.cloudinary.com/dsvkbe0mc/image/upload/v1775410885/language/vihxjjp82otesd36lfai.webp', TRUE),
('Java', 'https://res.cloudinary.com/dsvkbe0mc/image/upload/v1775410898/language/qct8fbtc4ntqck0gdulx.webp', TRUE),
('JavaScript', 'https://res.cloudinary.com/dsvkbe0mc/image/upload/v1775410950/language/laovezt7xoxgzafc1krc.webp', TRUE),
('TypeScript', 'https://res.cloudinary.com/dsvkbe0mc/image/upload/v1775410965/language/ojrfirqqlvp225yunbyg.webp', TRUE),
('Visual Basic', 'https://res.cloudinary.com/dsvkbe0mc/image/upload/v1775410979/language/inygef09q4de372nbng0.webp', TRUE),
('Python', 'https://res.cloudinary.com/dsvkbe0mc/image/upload/v1781718673/language/c3ayzfn5ad6pvpnshn9h.webp', TRUE)
ON CONFLICT (name) DO NOTHING;

-- =============================================================================
-- DATOS INICIALES - Technologies
-- =============================================================================

INSERT INTO pf_technologies (name, img_url, is_enabled) VALUES
('Angular', 'https://res.cloudinary.com/dsvkbe0mc/image/upload/v1775411010/technology/gzwq8wesqa6briy6xtbm.webp', TRUE),
('Bootstrap', 'https://res.cloudinary.com/dsvkbe0mc/image/upload/v1775411025/technology/skj0ta8jkt886nt0np8q.webp', TRUE),
('.NET', 'https://res.cloudinary.com/dsvkbe0mc/image/upload/v1775411053/technology/wyngbcme2adf5ghd2nra.webp', TRUE),
('Git', 'https://res.cloudinary.com/dsvkbe0mc/image/upload/v1775411068/technology/rxuzuqcodtx78liajzpu.webp', TRUE),
('GitHub', 'https://res.cloudinary.com/dsvkbe0mc/image/upload/v1775411082/technology/ryy6f1jdrriqwloczvde.webp', TRUE),
('SQL Server', 'https://res.cloudinary.com/dsvkbe0mc/image/upload/v1775411104/technology/pcqc6q9xctncxywqagza.webp', TRUE),
('MySQL', 'https://res.cloudinary.com/dsvkbe0mc/image/upload/v1775411118/technology/f6sushzc9qskjjlacbbd.webp', TRUE),
('NextJS', 'https://res.cloudinary.com/dsvkbe0mc/image/upload/v1775411135/technology/pxwdu3fwegqs7l7fkxcq.webp', TRUE),
('NodeJS', 'https://res.cloudinary.com/dsvkbe0mc/image/upload/v1775411153/technology/lvf9s5pd1ifsfr0dw23i.webp', TRUE),
('PostgreSQL', 'https://res.cloudinary.com/dsvkbe0mc/image/upload/v1775411175/technology/duroyqtlr35vdop7whpp.webp', TRUE),
('React', 'https://res.cloudinary.com/dsvkbe0mc/image/upload/v1775411227/technology/hbqnbm1gywh1l53givwa.webp', TRUE),
('TailwindCSS', 'https://res.cloudinary.com/dsvkbe0mc/image/upload/v1775411250/technology/htebevsyvtvjgdt2wfg5.webp', TRUE),
('Unity', 'https://res.cloudinary.com/dsvkbe0mc/image/upload/v1775411265/technology/axo4xgc18eaga08b7qmw.webp', TRUE),
('Visual Studio', 'https://res.cloudinary.com/dsvkbe0mc/image/upload/v1775411279/technology/qxgrwvzrxhiufepgppl6.webp', TRUE),
('VSCode', 'https://res.cloudinary.com/dsvkbe0mc/image/upload/v1775411293/technology/wgaf48s5ie2hbvhlxphd.webp', TRUE),
('VueJS', 'https://res.cloudinary.com/dsvkbe0mc/image/upload/v1775411311/technology/g80skjveoixlkcmmuovr.webp', TRUE),
('AstroJS', 'https://res.cloudinary.com/dsvkbe0mc/image/upload/v1775411324/technology/yqgbpo0vs7abn0dbdscg.webp', TRUE),
('FastAPI', 'https://res.cloudinary.com/dsvkbe0mc/image/upload/v1781718926/technology/cveysioo7pe6hjpl7kkw.webp', TRUE),
('DaisyUI', 'https://res.cloudinary.com/dsvkbe0mc/image/upload/v1781719264/technology/rc22nnoa0s2ktj1nd5ld.webp', TRUE)
ON CONFLICT (name) DO NOTHING;

-- =============================================================================
-- DATOS INICIALES - Projects
-- =============================================================================

INSERT INTO pf_projects (name, description, img_url, repo_url, app_url, is_enabled) VALUES
('Transbank POS Integration', NULL, 'https://res.cloudinary.com/dsvkbe0mc/image/upload/v1781630970/project/ii9arpgiiyck0zzgdblj.webp', 'https://github.com/TheNefelin/Transbank_POS_v1', NULL, TRUE),
('Arduino DHT Temperature Monitoring by Network', NULL, 'https://res.cloudinary.com/dsvkbe0mc/image/upload/v1781632839/project/yvhyxoa2p53m6x8apnev.webp', 'https://github.com/TheNefelin/DHT', NULL, TRUE),
('El Cubo v2.0 (Unity)', NULL, 'https://res.cloudinary.com/dsvkbe0mc/image/upload/v1781630654/project/qflqe0ms4gzyaqycmvup.webp', NULL, NULL, TRUE),
('Bier Heart Page (VueJS)', NULL, 'https://res.cloudinary.com/dsvkbe0mc/image/upload/v1781630362/project/jdnmojtuztwovegux8r2.webp', 'https://github.com/TheNefelin/BierHeart_Vue', 'https://www.bierheart.cl', TRUE),
('WebP Converter (.NET)', NULL, 'https://res.cloudinary.com/dsvkbe0mc/image/upload/v1781633241/project/daczw3xvvplxqzjptq1v.webp', 'https://github.com/TheNefelin/WebPConverter_.NETCore', NULL, TRUE),
('Trueke (Android Maui)', NULL, 'https://res.cloudinary.com/dsvkbe0mc/image/upload/v1781632070/project/xsrvdublh4z9nxviths6.webp', 'https://github.com/TheNefelin/Kambio_.NetCore', NULL, TRUE),
('Password Manager (Android Maui)', NULL, 'https://res.cloudinary.com/dsvkbe0mc/image/upload/v1781631621/project/k5skudxso73kh4mg3g1h.webp', 'https://github.com/TheNefelin/PasswordManager_.NET10', NULL, TRUE),
('Guides for Games (NextJS)', NULL, 'https://res.cloudinary.com/dsvkbe0mc/image/upload/v1781630298/project/wvffkwuvmi9xbqg0eqjh.webp', 'https://github.com/TheNefelin/game-guides-nextjs', 'https://game-guides-nextjs.vercel.app', TRUE),
('Portafolio v3.0 (Astro)', NULL, 'https://res.cloudinary.com/dsvkbe0mc/image/upload/v1781629778/project/e05ymaji6ekbvfglxqfd.webp', 'https://github.com/TheNefelin/portfolio-astro', 'https://www.francisco-dev.cl', TRUE),
('WebApi for Projects (.NET)', NULL, 'https://res.cloudinary.com/dsvkbe0mc/image/upload/v1781629813/project/ayfcf27njzaqlsrqk4ng.webp', 'https://github.com/TheNefelin/Projects_.NETCore', 'https://dragonra.bsite.net/index.html', TRUE),
('Navaja Suiza (Android Maui)', NULL, 'https://res.cloudinary.com/dsvkbe0mc/image/upload/v1781632294/project/xowohirc0dm9kiuzsw0h.webp', 'https://github.com/TheNefelin/NavajaSuiza_.NET10', NULL, TRUE),
('CéspedPro Chile (Astro)', NULL, 'https://res.cloudinary.com/dsvkbe0mc/image/upload/v1781630113/project/tdjqz0pbld4ykqqv7htp.webp', 'https://github.com/TheNefelin/cespedprochile-astro', 'https://www.cespedprochile.cl', TRUE),
('Biblioteca Wallmapu (Angular)', NULL, 'https://res.cloudinary.com/dsvkbe0mc/image/upload/v1781630179/project/xbkdbizilylywe5ehn40.webp', 'https://github.com/TheNefelin/biblioteca-wallmapu-angular', 'https://biblioteca-wallmapu-angular.vercel.app', TRUE),
('Biblioteca Wallmapu (Python)', NULL, 'https://res.cloudinary.com/dsvkbe0mc/image/upload/v1781635261/project/cdcjtuhieswghcqmbfv9.webp', 'https://github.com/TheNefelin/biblioteca-wallmapu-python', 'https://admin-api-python.vercel.app/docs', TRUE)
ON CONFLICT (name) DO NOTHING;

-- Project ↔ Language (M:N)
INSERT INTO pf_pro_lang (id_project, id_language)
SELECT p.id_project, l.id_language
FROM pf_projects p
CROSS JOIN pf_languages l
WHERE (p.name, l.name) IN (
  ('Transbank POS Integration', 'Visual Basic'),
  ('Arduino DHT Temperature Monitoring by Network', 'Visual Basic'),
  ('El Cubo v2.0 (Unity)', 'C#'),
  ('Bier Heart Page (VueJS)', 'JavaScript'),
  ('Bier Heart Page (VueJS)', 'CSS3'),
  ('Bier Heart Page (VueJS)', 'HTML5'),
  ('WebP Converter (.NET)', 'C#'),
  ('Trueke (Android Maui)', 'C#'),
  ('Password Manager (Android Maui)', 'C#'),
  ('Guides for Games (NextJS)', 'HTML5'),
  ('Guides for Games (NextJS)', 'TypeScript'),
  ('Guides for Games (NextJS)', 'CSS3'),
  ('Portafolio v3.0 (Astro)', 'TypeScript'),
  ('Portafolio v3.0 (Astro)', 'CSS3'),
  ('Portafolio v3.0 (Astro)', 'HTML5'),
  ('WebApi for Projects (.NET)', 'C#'),
  ('Navaja Suiza (Android Maui)', 'C#'),
  ('CéspedPro Chile (Astro)', 'TypeScript'),
  ('CéspedPro Chile (Astro)', 'HTML5'),
  ('CéspedPro Chile (Astro)', 'CSS3'),
  ('Biblioteca Wallmapu (Angular)', 'CSS3'),
  ('Biblioteca Wallmapu (Angular)', 'TypeScript'),
  ('Biblioteca Wallmapu (Angular)', 'HTML5'),
  ('Biblioteca Wallmapu (Python)', 'Python')
)
ON CONFLICT (id_project, id_language) DO NOTHING;

-- Project ↔ Technology (M:N)
INSERT INTO pf_pro_tech (id_project, id_technology)
SELECT p.id_project, t.id_technology
FROM pf_projects p
CROSS JOIN pf_technologies t
WHERE (p.name, t.name) IN (
  ('Transbank POS Integration', 'Visual Studio'),
  ('Transbank POS Integration', '.NET'),
  ('Arduino DHT Temperature Monitoring by Network', 'Visual Studio'),
  ('Arduino DHT Temperature Monitoring by Network', '.NET'),
  ('El Cubo v2.0 (Unity)', 'Unity'),
  ('El Cubo v2.0 (Unity)', 'Visual Studio'),
  ('Bier Heart Page (VueJS)', 'VueJS'),
  ('Bier Heart Page (VueJS)', 'TailwindCSS'),
  ('Bier Heart Page (VueJS)', 'DaisyUI'),
  ('WebP Converter (.NET)', 'Visual Studio'),
  ('WebP Converter (.NET)', '.NET'),
  ('WebP Converter (.NET)', 'Bootstrap'),
  ('Trueke (Android Maui)', '.NET'),
  ('Trueke (Android Maui)', 'SQL Server'),
  ('Trueke (Android Maui)', 'Visual Studio'),
  ('Password Manager (Android Maui)', '.NET'),
  ('Password Manager (Android Maui)', 'Visual Studio'),
  ('Guides for Games (NextJS)', 'NextJS'),
  ('Guides for Games (NextJS)', 'TailwindCSS'),
  ('Guides for Games (NextJS)', 'DaisyUI'),
  ('Portafolio v3.0 (Astro)', 'AstroJS'),
  ('Portafolio v3.0 (Astro)', 'DaisyUI'),
  ('Portafolio v3.0 (Astro)', 'TailwindCSS'),
  ('WebApi for Projects (.NET)', 'SQL Server'),
  ('WebApi for Projects (.NET)', 'Visual Studio'),
  ('WebApi for Projects (.NET)', '.NET'),
  ('Navaja Suiza (Android Maui)', 'Visual Studio'),
  ('Navaja Suiza (Android Maui)', '.NET'),
  ('CéspedPro Chile (Astro)', 'TailwindCSS'),
  ('CéspedPro Chile (Astro)', 'AstroJS'),
  ('CéspedPro Chile (Astro)', 'DaisyUI'),
  ('Biblioteca Wallmapu (Angular)', 'DaisyUI'),
  ('Biblioteca Wallmapu (Angular)', 'TailwindCSS'),
  ('Biblioteca Wallmapu (Angular)', 'Angular'),
  ('Biblioteca Wallmapu (Python)', 'FastAPI'),
  ('Biblioteca Wallmapu (Python)', 'PostgreSQL')
)
ON CONFLICT (id_project, id_technology) DO NOTHING;

-- =============================================================================
-- DATOS INICIALES - URL Groups
-- =============================================================================

INSERT INTO pf_urlgrp (name, is_enabled) VALUES
('Development Platforms', TRUE),
('Frontend', TRUE),
('Backend', TRUE),
('AI / LLM Tools', TRUE),
('Learning & Documentation', TRUE),
('Infrastructure / Hosting', TRUE),
('Design & Assets', TRUE),
('Productivity & Collaboration', TRUE),
('Personal Links', TRUE),
('VPNs', TRUE)
ON CONFLICT (name) DO NOTHING;

-- =============================================================================
-- DATOS INICIALES - URLs
-- =============================================================================

INSERT INTO pf_url (name, link, is_enabled, id_urlgrp) VALUES
('GitHub', 'https://github.com/TheNefelin', TRUE, (SELECT id_urlgrp FROM pf_urlgrp WHERE name = 'Development Platforms')),
('.NET', 'https://dotnet.microsoft.com', TRUE, (SELECT id_urlgrp FROM pf_urlgrp WHERE name = 'Development Platforms')),
('Visual Studio Community', 'https://visualstudio.microsoft.com/downloads/', TRUE, (SELECT id_urlgrp FROM pf_urlgrp WHERE name = 'Development Platforms')),
('NextAuth', 'https://next-auth.js.org', TRUE, (SELECT id_urlgrp FROM pf_urlgrp WHERE name = 'Development Platforms')),
('PlayCode', 'https://playcode.io', TRUE, (SELECT id_urlgrp FROM pf_urlgrp WHERE name = 'Development Platforms')),
('CodePen', 'https://codepen.io', TRUE, (SELECT id_urlgrp FROM pf_urlgrp WHERE name = 'Development Platforms')),
('DbDiagram', 'https://dbdiagram.io/home', TRUE, (SELECT id_urlgrp FROM pf_urlgrp WHERE name = 'Development Platforms')), 
('Draw.io', 'https://app.diagrams.net', TRUE, (SELECT id_urlgrp FROM pf_urlgrp WHERE name = 'Development Platforms')),
('Excalidraw', 'https://excalidraw.com', TRUE, (SELECT id_urlgrp FROM pf_urlgrp WHERE name = 'Development Platforms')),
('MapBox', 'https://www.mapbox.com', TRUE, (SELECT id_urlgrp FROM pf_urlgrp WHERE name = 'Development Platforms')),
('PublicAPI', 'https://publicapi.dev', TRUE, (SELECT id_urlgrp FROM pf_urlgrp WHERE name = 'Development Platforms')),
('Songsterr', 'https://www.songsterr.com', TRUE, (SELECT id_urlgrp FROM pf_urlgrp WHERE name = 'Personal Links')),

('VueJS', 'https://vuejs.org', TRUE, (SELECT id_urlgrp FROM pf_urlgrp WHERE name = 'Frontend')),
('VueUse', 'https://vueuse.org', TRUE, (SELECT id_urlgrp FROM pf_urlgrp WHERE name = 'Frontend')),
('NextJS', 'https://nextjs.org', TRUE, (SELECT id_urlgrp FROM pf_urlgrp WHERE name = 'Frontend')),
('Tailwind CSS', 'https://tailwindcss.com', TRUE, (SELECT id_urlgrp FROM pf_urlgrp WHERE name = 'Frontend')),
('DaisyUI', 'https://daisyui.com', TRUE, (SELECT id_urlgrp FROM pf_urlgrp WHERE name = 'Frontend')),
('Flowbite', 'https://flowbite.com', TRUE, (SELECT id_urlgrp FROM pf_urlgrp WHERE name = 'Frontend')),
('MUI', 'https://mui.com', TRUE, (SELECT id_urlgrp FROM pf_urlgrp WHERE name = 'Frontend')),
('NextUI', 'https://nextui.org', TRUE, (SELECT id_urlgrp FROM pf_urlgrp WHERE name = 'Frontend')),
('Heroicons', 'https://heroicons.com', TRUE, (SELECT id_urlgrp FROM pf_urlgrp WHERE name = 'Frontend')),
('Tremor', 'https://www.tremor.so', TRUE, (SELECT id_urlgrp FROM pf_urlgrp WHERE name = 'Frontend')),
('ApexCharts', 'https://apexcharts.com', TRUE, (SELECT id_urlgrp FROM pf_urlgrp WHERE name = 'Frontend')),
('SwiperJS', 'https://swiperjs.com', TRUE, (SELECT id_urlgrp FROM pf_urlgrp WHERE name = 'Frontend')),

('FastAPI', 'https://fastapi.tiangolo.com', TRUE, (SELECT id_urlgrp FROM pf_urlgrp WHERE name = 'Backend')),
('Strapi', 'https://strapi.io', TRUE, (SELECT id_urlgrp FROM pf_urlgrp WHERE name = 'Backend')),
('Java JDK', 'https://www.oracle.com/cl/java/technologies/downloads', TRUE, (SELECT id_urlgrp FROM pf_urlgrp WHERE name = 'Backend')),

('ChatGPT', 'https://chat.openai.com', TRUE, (SELECT id_urlgrp FROM pf_urlgrp WHERE name = 'AI / LLM Tools')),
('Claude', 'https://claude.ai', TRUE, (SELECT id_urlgrp FROM pf_urlgrp WHERE name = 'AI / LLM Tools')),
('Google Gemini', 'https://gemini.google.com', TRUE, (SELECT id_urlgrp FROM pf_urlgrp WHERE name = 'AI / LLM Tools')),
('Leonardo AI', 'https://leonardo.ai', TRUE, (SELECT id_urlgrp FROM pf_urlgrp WHERE name = 'AI / LLM Tools')),
('ElevenLabs', 'https://elevenlabs.io', TRUE, (SELECT id_urlgrp FROM pf_urlgrp WHERE name = 'AI / LLM Tools')),
('Adobe Podcast', 'https://podcast.adobe.com/enhance', TRUE, (SELECT id_urlgrp FROM pf_urlgrp WHERE name = 'AI / LLM Tools')),
('BlackBox AI', 'https://www.useblackbox.io', TRUE, (SELECT id_urlgrp FROM pf_urlgrp WHERE name = 'AI / LLM Tools')),
('AgentGPT', 'https://agentgpt.reworkd.ai', TRUE, (SELECT id_urlgrp FROM pf_urlgrp WHERE name = 'AI / LLM Tools')),
('Manus', 'https://manus.im/', TRUE, (SELECT id_urlgrp FROM pf_urlgrp WHERE name = 'AI / LLM Tools')),
('Stitch', 'https://stitch.withgoogle.com', TRUE, (SELECT id_urlgrp FROM pf_urlgrp WHERE name = 'AI / LLM Tools')),
('AI Studio', 'https://aistudio.google.com', TRUE, (SELECT id_urlgrp FROM pf_urlgrp WHERE name = 'AI / LLM Tools')),
('OpenRouter', 'https://openrouter.ai/', TRUE, (SELECT id_urlgrp FROM pf_urlgrp WHERE name = 'AI / LLM Tools')),

('DevDocs', 'https://devdocs.io', TRUE, (SELECT id_urlgrp FROM pf_urlgrp WHERE name = 'Learning & Documentation')),
('Web.dev', 'https://web.dev', TRUE, (SELECT id_urlgrp FROM pf_urlgrp WHERE name = 'Learning & Documentation')),
('W3Schools', 'https://www.w3schools.com', TRUE, (SELECT id_urlgrp FROM pf_urlgrp WHERE name = 'Learning & Documentation')),
('Scrimba', 'https://scrimba.com', TRUE, (SELECT id_urlgrp FROM pf_urlgrp WHERE name = 'Learning & Documentation')),
('CodeDex', 'https://www.codedex.io', TRUE, (SELECT id_urlgrp FROM pf_urlgrp WHERE name = 'Learning & Documentation')),
('CodelyTV', 'https://www.youtube.com/@CodelyTV', TRUE, (SELECT id_urlgrp FROM pf_urlgrp WHERE name = 'Learning & Documentation')),
('VS Dev Essentials', 'https://visualstudio.microsoft.com/dev-essentials/', TRUE, (SELECT id_urlgrp FROM pf_urlgrp WHERE name = 'Learning & Documentation')),
('Uiverse', 'https://uiverse.io/all', TRUE, (SELECT id_urlgrp FROM pf_urlgrp WHERE name = 'Frontend')),
('Animate.css', 'https://animate.style', TRUE, (SELECT id_urlgrp FROM pf_urlgrp WHERE name = 'Frontend')),

('Vercel', 'https://vercel.com', TRUE, (SELECT id_urlgrp FROM pf_urlgrp WHERE name = 'Infrastructure / Hosting')),
('Netlify', 'https://www.netlify.com', TRUE, (SELECT id_urlgrp FROM pf_urlgrp WHERE name = 'Infrastructure / Hosting')),
('Cloudflare', 'https://www.cloudflare.com', TRUE, (SELECT id_urlgrp FROM pf_urlgrp WHERE name = 'Infrastructure / Hosting')),
('DigitalOcean', 'https://www.digitalocean.com', TRUE, (SELECT id_urlgrp FROM pf_urlgrp WHERE name = 'Infrastructure / Hosting')),
('Railway', 'https://railway.app', TRUE, (SELECT id_urlgrp FROM pf_urlgrp WHERE name = 'Infrastructure / Hosting')),
('Fly.io', 'https://fly.io', TRUE, (SELECT id_urlgrp FROM pf_urlgrp WHERE name = 'Infrastructure / Hosting')),
('Free ASP hosting', 'https://freeasphosting.net', TRUE, (SELECT id_urlgrp FROM pf_urlgrp WHERE name = 'Infrastructure / Hosting')),

('Figma', 'https://www.figma.com', TRUE, (SELECT id_urlgrp FROM pf_urlgrp WHERE name = 'Design & Assets')),
('Canva', 'https://www.canva.com', TRUE, (SELECT id_urlgrp FROM pf_urlgrp WHERE name = 'Design & Assets')),
('Unsplash', 'https://unsplash.com', TRUE, (SELECT id_urlgrp FROM pf_urlgrp WHERE name = 'Design & Assets')),
('Freepik', 'https://www.freepik.com', TRUE, (SELECT id_urlgrp FROM pf_urlgrp WHERE name = 'Design & Assets')),
('Pixabay', 'https://pixabay.com', TRUE, (SELECT id_urlgrp FROM pf_urlgrp WHERE name = 'Design & Assets')),
('Iconify', 'https://iconify.design', TRUE, (SELECT id_urlgrp FROM pf_urlgrp WHERE name = 'Design & Assets')),
('SVGRepo', 'https://www.svgrepo.com', TRUE, (SELECT id_urlgrp FROM pf_urlgrp WHERE name = 'Design & Assets')),

('Notion', 'https://www.notion.so', TRUE, (SELECT id_urlgrp FROM pf_urlgrp WHERE name = 'Productivity & Collaboration')),
('Trello', 'https://trello.com', TRUE, (SELECT id_urlgrp FROM pf_urlgrp WHERE name = 'Productivity & Collaboration')),
('Jira', 'https://www.atlassian.com/software/jira', TRUE, (SELECT id_urlgrp FROM pf_urlgrp WHERE name = 'Productivity & Collaboration')),
('ClickUp', 'https://clickup.com', TRUE, (SELECT id_urlgrp FROM pf_urlgrp WHERE name = 'Productivity & Collaboration')),
('Asana', 'https://asana.com', TRUE, (SELECT id_urlgrp FROM pf_urlgrp WHERE name = 'Productivity & Collaboration')),

('AnimeFLV', 'https://www3.animeflv.net', TRUE, (SELECT id_urlgrp FROM pf_urlgrp WHERE name = 'Personal Links')),
('Elden Ring Map', 'https://mapgenie.io/elden-ring/maps/the-lands-between', TRUE, (SELECT id_urlgrp FROM pf_urlgrp WHERE name = 'Personal Links')),
('GetOnbrd', 'https://www.getonbrd.com/misempleos', TRUE, (SELECT id_urlgrp FROM pf_urlgrp WHERE name = 'Personal Links')),
('ChileBT', 'https://chilebt.com', TRUE, (SELECT id_urlgrp FROM pf_urlgrp WHERE name = 'Personal Links')),
('Futbol Libre', 'https://futbollibre.mx', TRUE, (SELECT id_urlgrp FROM pf_urlgrp WHERE name = 'Personal Links'))
ON CONFLICT DO NOTHING;

INSERT INTO pf_url (name, link, is_enabled, id_urlgrp) VALUES
('Proton VPN', 'https://protonvpn.com', TRUE, (SELECT id_urlgrp FROM pf_urlgrp WHERE name = 'VPNs')),
('Mullvad VPN', 'https://mullvad.net/es', TRUE, (SELECT id_urlgrp FROM pf_urlgrp WHERE name = 'VPNs'))
ON CONFLICT DO NOTHING;

-- =============================================================================
-- SECUENCIAS (asegurar que nextval funcione correctamente)
-- =============================================================================

-- Sincronizar secuencias: si el último ID es 14, el próximo INSERT generará 15.
-- No es necesario tras DROP+CREATE desde cero, pero previene errores si se
-- ejecuta un INSERT manual después del seed (ej: prueba local).
SELECT setval('pf_projects_id_project_seq', (SELECT MAX(id_project) FROM pf_projects));
SELECT setval('pf_languages_id_language_seq', (SELECT MAX(id_language) FROM pf_languages));
SELECT setval('pf_technologies_id_technology_seq', (SELECT MAX(id_technology) FROM pf_technologies));
SELECT setval('pf_urlgrp_id_urlgrp_seq', (SELECT MAX(id_urlgrp) FROM pf_urlgrp));
SELECT setval('pf_url_id_url_seq', (SELECT MAX(id_url) FROM pf_url));

COMMIT;
