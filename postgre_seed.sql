-- ============================================================
-- Seed regenerado desde BDPorfolio.xlsx
-- ============================================================

BEGIN;

-- Languages
INSERT INTO pf_languages (id_language, name, img_url, is_enabled) VALUES
  (17, 'C#', 'https://res.cloudinary.com/dsvkbe0mc/image/upload/v1775410722/language/nr8vdnjridkymdt61kgh.webp', TRUE),
  (18, 'CSS3', 'https://res.cloudinary.com/dsvkbe0mc/image/upload/v1775410869/language/efa0g6dd8rvb3qhzp49z.webp', TRUE),
  (19, 'HTML5', 'https://res.cloudinary.com/dsvkbe0mc/image/upload/v1775410885/language/vihxjjp82otesd36lfai.webp', TRUE),
  (20, 'Java', 'https://res.cloudinary.com/dsvkbe0mc/image/upload/v1775410898/language/qct8fbtc4ntqck0gdulx.webp', TRUE),
  (21, 'JavaScript', 'https://res.cloudinary.com/dsvkbe0mc/image/upload/v1775410950/language/laovezt7xoxgzafc1krc.webp', TRUE),
  (22, 'TypeScript', 'https://res.cloudinary.com/dsvkbe0mc/image/upload/v1775410965/language/ojrfirqqlvp225yunbyg.webp', TRUE),
  (23, 'Visual Basic', 'https://res.cloudinary.com/dsvkbe0mc/image/upload/v1775410979/language/inygef09q4de372nbng0.webp', TRUE),
  (24, 'Python', 'https://res.cloudinary.com/dsvkbe0mc/image/upload/v1781718673/language/c3ayzfn5ad6pvpnshn9h.webp', TRUE)
ON CONFLICT (name) DO NOTHING;

-- Technologies
INSERT INTO pf_technologies (id_technology, name, img_url, is_enabled) VALUES
  (1, 'Angular', 'https://res.cloudinary.com/dsvkbe0mc/image/upload/v1775411010/technology/gzwq8wesqa6briy6xtbm.webp', TRUE),
  (2, 'Bootstrap', 'https://res.cloudinary.com/dsvkbe0mc/image/upload/v1775411025/technology/skj0ta8jkt886nt0np8q.webp', TRUE),
  (3, '.NET', 'https://res.cloudinary.com/dsvkbe0mc/image/upload/v1775411053/technology/wyngbcme2adf5ghd2nra.webp', TRUE),
  (4, 'Git', 'https://res.cloudinary.com/dsvkbe0mc/image/upload/v1775411068/technology/rxuzuqcodtx78liajzpu.webp', TRUE),
  (5, 'GitHub', 'https://res.cloudinary.com/dsvkbe0mc/image/upload/v1775411082/technology/ryy6f1jdrriqwloczvde.webp', TRUE),
  (6, 'SQL Server', 'https://res.cloudinary.com/dsvkbe0mc/image/upload/v1775411104/technology/pcqc6q9xctncxywqagza.webp', TRUE),
  (7, 'MySQL', 'https://res.cloudinary.com/dsvkbe0mc/image/upload/v1775411118/technology/f6sushzc9qskjjlacbbd.webp', TRUE),
  (8, 'NextJS', 'https://res.cloudinary.com/dsvkbe0mc/image/upload/v1775411135/technology/pxwdu3fwegqs7l7fkxcq.webp', TRUE),
  (9, 'NodeJS', 'https://res.cloudinary.com/dsvkbe0mc/image/upload/v1775411153/technology/lvf9s5pd1ifsfr0dw23i.webp', TRUE),
  (10, 'PostgreSQL', 'https://res.cloudinary.com/dsvkbe0mc/image/upload/v1775411175/technology/duroyqtlr35vdop7whpp.webp', TRUE),
  (11, 'React', 'https://res.cloudinary.com/dsvkbe0mc/image/upload/v1775411227/technology/hbqnbm1gywh1l53givwa.webp', TRUE),
  (12, 'TailwindCSS', 'https://res.cloudinary.com/dsvkbe0mc/image/upload/v1775411250/technology/htebevsyvtvjgdt2wfg5.webp', TRUE),
  (13, 'Unity', 'https://res.cloudinary.com/dsvkbe0mc/image/upload/v1775411265/technology/axo4xgc18eaga08b7qmw.webp', TRUE),
  (14, 'Visual Studio', 'https://res.cloudinary.com/dsvkbe0mc/image/upload/v1775411279/technology/qxgrwvzrxhiufepgppl6.webp', TRUE),
  (15, 'VSCode', 'https://res.cloudinary.com/dsvkbe0mc/image/upload/v1775411293/technology/wgaf48s5ie2hbvhlxphd.webp', TRUE),
  (16, 'VueJS', 'https://res.cloudinary.com/dsvkbe0mc/image/upload/v1775411311/technology/g80skjveoixlkcmmuovr.webp', TRUE),
  (17, 'AstroJS', 'https://res.cloudinary.com/dsvkbe0mc/image/upload/v1775411324/technology/yqgbpo0vs7abn0dbdscg.webp', TRUE),
  (18, 'FastAPI', 'https://res.cloudinary.com/dsvkbe0mc/image/upload/v1781718926/technology/cveysioo7pe6hjpl7kkw.webp', TRUE),
  (19, 'DaisyUI', 'https://res.cloudinary.com/dsvkbe0mc/image/upload/v1781719264/technology/rc22nnoa0s2ktj1nd5ld.webp', TRUE)
ON CONFLICT (name) DO NOTHING;

-- Projects
INSERT INTO pf_projects (id_project, name, description, img_url, repo_url, app_url, is_enabled) VALUES
  (1, 'Transbank POS Integration', NULL, 'https://res.cloudinary.com/dsvkbe0mc/image/upload/v1781630970/project/ii9arpgiiyck0zzgdblj.webp', 'https://github.com/TheNefelin/Transbank_POS_v1', NULL, TRUE),
  (2, 'Arduino DHT Temperature Monitoring by Network', NULL, 'https://res.cloudinary.com/dsvkbe0mc/image/upload/v1781632839/project/yvhyxoa2p53m6x8apnev.webp', 'https://github.com/TheNefelin/DHT', NULL, TRUE),
  (3, 'El Cubo v2.0 (Unity)', NULL, 'https://res.cloudinary.com/dsvkbe0mc/image/upload/v1781630654/project/qflqe0ms4gzyaqycmvup.webp', NULL, NULL, TRUE),
  (4, 'Bier Heart Page (VueJS)', NULL, 'https://res.cloudinary.com/dsvkbe0mc/image/upload/v1781630362/project/jdnmojtuztwovegux8r2.webp', 'https://github.com/TheNefelin/BierHeart_Vue', 'https://www.bierheart.cl', TRUE),
  (5, 'WebP Converter (.NET)', NULL, 'https://res.cloudinary.com/dsvkbe0mc/image/upload/v1781633241/project/daczw3xvvplxqzjptq1v.webp', 'https://github.com/TheNefelin/WebPConverter_.NETCore', NULL, TRUE),
  (6, 'Trueke (Android Maui)', NULL, 'https://res.cloudinary.com/dsvkbe0mc/image/upload/v1781632070/project/xsrvdublh4z9nxviths6.webp', 'https://github.com/TheNefelin/Kambio_.NetCore', NULL, TRUE),
  (7, 'Password Manager (Android Maui)', NULL, 'https://res.cloudinary.com/dsvkbe0mc/image/upload/v1781631621/project/k5skudxso73kh4mg3g1h.webp', 'https://github.com/TheNefelin/PasswordManager_.NET10', NULL, TRUE),
  (8, 'Guides for Games (NextJS)', NULL, 'https://res.cloudinary.com/dsvkbe0mc/image/upload/v1781630298/project/wvffkwuvmi9xbqg0eqjh.webp', 'https://github.com/TheNefelin/game-guides-nextjs', NULL, TRUE),
  (9, 'Portafolio v3.0 (Astro)', NULL, 'https://res.cloudinary.com/dsvkbe0mc/image/upload/v1781629778/project/e05ymaji6ekbvfglxqfd.webp', 'https://github.com/TheNefelin/portfolio-astro', 'https://www.francisco-dev.cl', TRUE),
  (10, 'WebApi for Projects (.NET)', NULL, 'https://res.cloudinary.com/dsvkbe0mc/image/upload/v1781629813/project/ayfcf27njzaqlsrqk4ng.webp', 'https://github.com/TheNefelin/Projects_.NETCore', 'https://dragonra.bsite.net/index.html', TRUE),
  (11, 'Navaja Suiza (Android Maui)', NULL, 'https://res.cloudinary.com/dsvkbe0mc/image/upload/v1781632294/project/xowohirc0dm9kiuzsw0h.webp', 'https://github.com/TheNefelin/NavajaSuiza_.NET10', NULL, TRUE),
  (12, 'CéspedPro Chile (Astro)', NULL, 'https://res.cloudinary.com/dsvkbe0mc/image/upload/v1781630113/project/tdjqz0pbld4ykqqv7htp.webp', 'https://github.com/TheNefelin/cespedprochile-astro', 'https://www.cespedprochile.cl', TRUE),
  (13, 'Biblioteca Wallmapu (Angular)', NULL, 'https://res.cloudinary.com/dsvkbe0mc/image/upload/v1781630179/project/xbkdbizilylywe5ehn40.webp', 'https://github.com/TheNefelin/biblioteca-wallmapu-angular', 'https://biblioteca-wallmapu-angular.vercel.app', TRUE),
  (14, 'Biblioteca Wallmapu (Python)', NULL, 'https://res.cloudinary.com/dsvkbe0mc/image/upload/v1781635261/project/cdcjtuhieswghcqmbfv9.webp', 'https://github.com/TheNefelin/biblioteca-wallmapu-python', 'https://biblioteca-wallmapu-python.vercel.app/docs', TRUE),
  (17, 'Game Guides v2 (Astro)', NULL, 'https://res.cloudinary.com/dsvkbe0mc/image/upload/v1786989000/project/v05wxyqlpdrov1mnyxxk.webp', 'https://github.com/TheNefelin/game_guides_astro', 'https://game-guides-astro.vercel.app', TRUE),
  (18, 'Game Guides v2 (python)', NULL, 'https://res.cloudinary.com/dsvkbe0mc/image/upload/v1786989857/project/n4awikkjbkwdsdy59dcq.webp', 'https://github.com/TheNefelin/game_guides_python', 'https://game-guides-python.vercel.app/docs', TRUE),
  (20, 'Transportes Drakkar (Angular)', NULL, 'https://res.cloudinary.com/dsvkbe0mc/image/upload/v1794419767/project/mniomv7ajhtzqnzvfmzr.webp', 'https://github.com/TheNefelin/drakkar-angular', 'https://transportesdrakkar.cl', TRUE)
ON CONFLICT (name) DO NOTHING;

-- Project - Language
INSERT INTO pf_pro_lang (id_project, id_language)
SELECT p.id_project, l.id_language
FROM pf_projects p CROSS JOIN pf_languages l
WHERE (p.name, l.name) IN (
  ('El Cubo v2.0 (Unity)', 'C#'),
  ('WebP Converter (.NET)', 'C#'),
  ('Trueke (Android Maui)', 'C#'),
  ('Password Manager (Android Maui)', 'C#'),
  ('WebApi for Projects (.NET)', 'C#'),
  ('Navaja Suiza (Android Maui)', 'C#'),
  ('Bier Heart Page (VueJS)', 'CSS3'),
  ('Guides for Games (NextJS)', 'CSS3'),
  ('Portafolio v3.0 (Astro)', 'CSS3'),
  ('CéspedPro Chile (Astro)', 'CSS3'),
  ('Biblioteca Wallmapu (Angular)', 'CSS3'),
  ('Bier Heart Page (VueJS)', 'HTML5'),
  ('Guides for Games (NextJS)', 'HTML5'),
  ('Portafolio v3.0 (Astro)', 'HTML5'),
  ('CéspedPro Chile (Astro)', 'HTML5'),
  ('Biblioteca Wallmapu (Angular)', 'HTML5'),
  ('Bier Heart Page (VueJS)', 'JavaScript'),
  ('Guides for Games (NextJS)', 'TypeScript'),
  ('Portafolio v3.0 (Astro)', 'TypeScript'),
  ('CéspedPro Chile (Astro)', 'TypeScript'),
  ('Biblioteca Wallmapu (Angular)', 'TypeScript'),
  ('Transbank POS Integration', 'Visual Basic'),
  ('Arduino DHT Temperature Monitoring by Network', 'Visual Basic'),
  ('Biblioteca Wallmapu (Python)', 'Python'),
  ('Game Guides v2 (Astro)', 'TypeScript'),
  ('Game Guides v2 (Astro)', 'HTML5'),
  ('Game Guides v2 (Astro)', 'CSS3'),
  ('Game Guides v2 (python)', 'Python'),
  ('Transportes Drakkar (Angular)', 'CSS3'),
  ('Transportes Drakkar (Angular)', 'HTML5'),
  ('Transportes Drakkar (Angular)', 'TypeScript')
)
ON CONFLICT (id_project, id_language) DO NOTHING;

-- Project - Technology
INSERT INTO pf_pro_tech (id_project, id_technology)
SELECT p.id_project, t.id_technology
FROM pf_projects p CROSS JOIN pf_technologies t
WHERE (p.name, t.name) IN (
  ('Biblioteca Wallmapu (Angular)', 'Angular'),
  ('WebP Converter (.NET)', 'Bootstrap'),
  ('Transbank POS Integration', '.NET'),
  ('Arduino DHT Temperature Monitoring by Network', '.NET'),
  ('WebP Converter (.NET)', '.NET'),
  ('Trueke (Android Maui)', '.NET'),
  ('Password Manager (Android Maui)', '.NET'),
  ('WebApi for Projects (.NET)', '.NET'),
  ('Navaja Suiza (Android Maui)', '.NET'),
  ('Trueke (Android Maui)', 'SQL Server'),
  ('WebApi for Projects (.NET)', 'SQL Server'),
  ('Guides for Games (NextJS)', 'NextJS'),
  ('Biblioteca Wallmapu (Python)', 'PostgreSQL'),
  ('Bier Heart Page (VueJS)', 'TailwindCSS'),
  ('Guides for Games (NextJS)', 'TailwindCSS'),
  ('Portafolio v3.0 (Astro)', 'TailwindCSS'),
  ('CéspedPro Chile (Astro)', 'TailwindCSS'),
  ('Biblioteca Wallmapu (Angular)', 'TailwindCSS'),
  ('El Cubo v2.0 (Unity)', 'Unity'),
  ('Transbank POS Integration', 'Visual Studio'),
  ('Arduino DHT Temperature Monitoring by Network', 'Visual Studio'),
  ('El Cubo v2.0 (Unity)', 'Visual Studio'),
  ('WebP Converter (.NET)', 'Visual Studio'),
  ('Trueke (Android Maui)', 'Visual Studio'),
  ('Password Manager (Android Maui)', 'Visual Studio'),
  ('WebApi for Projects (.NET)', 'Visual Studio'),
  ('Navaja Suiza (Android Maui)', 'Visual Studio'),
  ('Bier Heart Page (VueJS)', 'VueJS'),
  ('Portafolio v3.0 (Astro)', 'AstroJS'),
  ('CéspedPro Chile (Astro)', 'AstroJS'),
  ('Biblioteca Wallmapu (Python)', 'FastAPI'),
  ('Bier Heart Page (VueJS)', 'DaisyUI'),
  ('Guides for Games (NextJS)', 'DaisyUI'),
  ('Portafolio v3.0 (Astro)', 'DaisyUI'),
  ('CéspedPro Chile (Astro)', 'DaisyUI'),
  ('Biblioteca Wallmapu (Angular)', 'DaisyUI'),
  ('Game Guides v2 (Astro)', 'TailwindCSS'),
  ('Game Guides v2 (Astro)', 'AstroJS'),
  ('Game Guides v2 (Astro)', 'DaisyUI'),
  ('Game Guides v2 (python)', 'PostgreSQL'),
  ('Game Guides v2 (python)', 'FastAPI'),
  ('Transportes Drakkar (Angular)', 'Angular'),
  ('Transportes Drakkar (Angular)', 'TailwindCSS'),
  ('Transportes Drakkar (Angular)', 'DaisyUI')
)
ON CONFLICT (id_project, id_technology) DO NOTHING;

-- URL groups
INSERT INTO pf_urlgrp (id_urlgrp, name, is_enabled) VALUES
  (1, 'Development Platforms', TRUE),
  (2, 'Frontend', TRUE),
  (3, 'Backend', TRUE),
  (4, 'AI / LLM Tools', TRUE),
  (5, 'Learning & Documentation', TRUE),
  (6, 'Infrastructure / Hosting', TRUE),
  (7, 'Design & Assets', TRUE),
  (8, 'Productivity & Collaboration', TRUE),
  (9, 'Personal Links', TRUE),
  (10, 'VPNs', TRUE)
ON CONFLICT (name) DO NOTHING;

-- URLs
INSERT INTO pf_url (id_url, name, link, is_enabled, id_urlgrp) VALUES
  (1, 'GitHub', 'https://github.com/TheNefelin', TRUE, (SELECT id_urlgrp FROM pf_urlgrp WHERE name = 'Development Platforms')),
  (2, '.NET', 'https://dotnet.microsoft.com', TRUE, (SELECT id_urlgrp FROM pf_urlgrp WHERE name = 'Development Platforms')),
  (3, 'Visual Studio Community', 'https://visualstudio.microsoft.com/downloads/', TRUE, (SELECT id_urlgrp FROM pf_urlgrp WHERE name = 'Development Platforms')),
  (4, 'NextAuth', 'https://next-auth.js.org', TRUE, (SELECT id_urlgrp FROM pf_urlgrp WHERE name = 'Development Platforms')),
  (5, 'PlayCode', 'https://playcode.io', TRUE, (SELECT id_urlgrp FROM pf_urlgrp WHERE name = 'Development Platforms')),
  (6, 'CodePen', 'https://codepen.io', TRUE, (SELECT id_urlgrp FROM pf_urlgrp WHERE name = 'Development Platforms')),
  (7, 'DbDiagram', 'https://dbdiagram.io/home', TRUE, (SELECT id_urlgrp FROM pf_urlgrp WHERE name = 'Development Platforms')),
  (8, 'Draw.io', 'https://app.diagrams.net', TRUE, (SELECT id_urlgrp FROM pf_urlgrp WHERE name = 'Development Platforms')),
  (9, 'Excalidraw', 'https://excalidraw.com', TRUE, (SELECT id_urlgrp FROM pf_urlgrp WHERE name = 'Development Platforms')),
  (10, 'MapBox', 'https://www.mapbox.com', TRUE, (SELECT id_urlgrp FROM pf_urlgrp WHERE name = 'Development Platforms')),
  (11, 'PublicAPI', 'https://publicapi.dev', TRUE, (SELECT id_urlgrp FROM pf_urlgrp WHERE name = 'Development Platforms')),
  (12, 'Songsterr', 'https://www.songsterr.com', TRUE, (SELECT id_urlgrp FROM pf_urlgrp WHERE name = 'Personal Links')),
  (13, 'VueJS', 'https://vuejs.org', TRUE, (SELECT id_urlgrp FROM pf_urlgrp WHERE name = 'Frontend')),
  (14, 'VueUse', 'https://vueuse.org', TRUE, (SELECT id_urlgrp FROM pf_urlgrp WHERE name = 'Frontend')),
  (15, 'NextJS', 'https://nextjs.org', TRUE, (SELECT id_urlgrp FROM pf_urlgrp WHERE name = 'Frontend')),
  (16, 'Tailwind CSS', 'https://tailwindcss.com', TRUE, (SELECT id_urlgrp FROM pf_urlgrp WHERE name = 'Frontend')),
  (17, 'DaisyUI', 'https://daisyui.com', TRUE, (SELECT id_urlgrp FROM pf_urlgrp WHERE name = 'Frontend')),
  (18, 'Flowbite', 'https://flowbite.com', TRUE, (SELECT id_urlgrp FROM pf_urlgrp WHERE name = 'Frontend')),
  (19, 'MUI', 'https://mui.com', TRUE, (SELECT id_urlgrp FROM pf_urlgrp WHERE name = 'Frontend')),
  (20, 'NextUI', 'https://nextui.org', TRUE, (SELECT id_urlgrp FROM pf_urlgrp WHERE name = 'Frontend')),
  (21, 'Heroicons', 'https://heroicons.com', TRUE, (SELECT id_urlgrp FROM pf_urlgrp WHERE name = 'Frontend')),
  (22, 'Tremor', 'https://www.tremor.so', TRUE, (SELECT id_urlgrp FROM pf_urlgrp WHERE name = 'Frontend')),
  (23, 'ApexCharts', 'https://apexcharts.com', TRUE, (SELECT id_urlgrp FROM pf_urlgrp WHERE name = 'Frontend')),
  (24, 'SwiperJS', 'https://swiperjs.com', TRUE, (SELECT id_urlgrp FROM pf_urlgrp WHERE name = 'Frontend')),
  (25, 'FastAPI', 'https://fastapi.tiangolo.com', TRUE, (SELECT id_urlgrp FROM pf_urlgrp WHERE name = 'Backend')),
  (26, 'Strapi', 'https://strapi.io', TRUE, (SELECT id_urlgrp FROM pf_urlgrp WHERE name = 'Backend')),
  (27, 'Java JDK', 'https://www.oracle.com/cl/java/technologies/downloads', TRUE, (SELECT id_urlgrp FROM pf_urlgrp WHERE name = 'Backend')),
  (28, 'ChatGPT', 'https://chat.openai.com', TRUE, (SELECT id_urlgrp FROM pf_urlgrp WHERE name = 'AI / LLM Tools')),
  (29, 'Claude', 'https://claude.ai', TRUE, (SELECT id_urlgrp FROM pf_urlgrp WHERE name = 'AI / LLM Tools')),
  (30, 'Google Gemini', 'https://gemini.google.com', TRUE, (SELECT id_urlgrp FROM pf_urlgrp WHERE name = 'AI / LLM Tools')),
  (31, 'Leonardo AI', 'https://leonardo.ai', TRUE, (SELECT id_urlgrp FROM pf_urlgrp WHERE name = 'AI / LLM Tools')),
  (32, 'ElevenLabs', 'https://elevenlabs.io', TRUE, (SELECT id_urlgrp FROM pf_urlgrp WHERE name = 'AI / LLM Tools')),
  (33, 'Adobe Podcast', 'https://podcast.adobe.com/enhance', TRUE, (SELECT id_urlgrp FROM pf_urlgrp WHERE name = 'AI / LLM Tools')),
  (34, 'BlackBox AI', 'https://www.blackbox.ai', TRUE, (SELECT id_urlgrp FROM pf_urlgrp WHERE name = 'AI / LLM Tools')),
  (35, 'AgentGPT', 'https://agentgpt.reworkd.ai', TRUE, (SELECT id_urlgrp FROM pf_urlgrp WHERE name = 'AI / LLM Tools')),
  (36, 'Manus', 'https://manus.im/', TRUE, (SELECT id_urlgrp FROM pf_urlgrp WHERE name = 'AI / LLM Tools')),
  (37, 'Stitch', 'https://stitch.withgoogle.com', TRUE, (SELECT id_urlgrp FROM pf_urlgrp WHERE name = 'AI / LLM Tools')),
  (38, 'AI Studio', 'https://aistudio.google.com', TRUE, (SELECT id_urlgrp FROM pf_urlgrp WHERE name = 'AI / LLM Tools')),
  (39, 'OpenRouter', 'https://openrouter.ai/', TRUE, (SELECT id_urlgrp FROM pf_urlgrp WHERE name = 'AI / LLM Tools')),
  (40, 'DevDocs', 'https://devdocs.io', TRUE, (SELECT id_urlgrp FROM pf_urlgrp WHERE name = 'Learning & Documentation')),
  (41, 'Web.dev', 'https://web.dev', TRUE, (SELECT id_urlgrp FROM pf_urlgrp WHERE name = 'Learning & Documentation')),
  (42, 'W3Schools', 'https://www.w3schools.com', TRUE, (SELECT id_urlgrp FROM pf_urlgrp WHERE name = 'Learning & Documentation')),
  (43, 'Scrimba', 'https://scrimba.com', TRUE, (SELECT id_urlgrp FROM pf_urlgrp WHERE name = 'Learning & Documentation')),
  (44, 'CodeDex', 'https://www.codedex.io', TRUE, (SELECT id_urlgrp FROM pf_urlgrp WHERE name = 'Learning & Documentation')),
  (45, 'CodelyTV', 'https://www.youtube.com/@CodelyTV', TRUE, (SELECT id_urlgrp FROM pf_urlgrp WHERE name = 'Learning & Documentation')),
  (46, 'VS Dev Essentials', 'https://visualstudio.microsoft.com/dev-essentials/', TRUE, (SELECT id_urlgrp FROM pf_urlgrp WHERE name = 'Learning & Documentation')),
  (47, 'Uiverse', 'https://uiverse.io/all', TRUE, (SELECT id_urlgrp FROM pf_urlgrp WHERE name = 'Frontend')),
  (48, 'Animate.css', 'https://animate.style', TRUE, (SELECT id_urlgrp FROM pf_urlgrp WHERE name = 'Frontend')),
  (49, 'Vercel', 'https://vercel.com', TRUE, (SELECT id_urlgrp FROM pf_urlgrp WHERE name = 'Infrastructure / Hosting')),
  (50, 'Netlify', 'https://www.netlify.com', TRUE, (SELECT id_urlgrp FROM pf_urlgrp WHERE name = 'Infrastructure / Hosting')),
  (51, 'Cloudflare', 'https://www.cloudflare.com', TRUE, (SELECT id_urlgrp FROM pf_urlgrp WHERE name = 'Infrastructure / Hosting')),
  (52, 'DigitalOcean', 'https://www.digitalocean.com', TRUE, (SELECT id_urlgrp FROM pf_urlgrp WHERE name = 'Infrastructure / Hosting')),
  (53, 'Railway', 'https://railway.app', TRUE, (SELECT id_urlgrp FROM pf_urlgrp WHERE name = 'Infrastructure / Hosting')),
  (54, 'Fly.io', 'https://fly.io', TRUE, (SELECT id_urlgrp FROM pf_urlgrp WHERE name = 'Infrastructure / Hosting')),
  (55, 'Free ASP hosting', 'https://freeasphosting.net', TRUE, (SELECT id_urlgrp FROM pf_urlgrp WHERE name = 'Infrastructure / Hosting')),
  (56, 'Figma', 'https://www.figma.com', TRUE, (SELECT id_urlgrp FROM pf_urlgrp WHERE name = 'Design & Assets')),
  (57, 'Canva', 'https://www.canva.com', TRUE, (SELECT id_urlgrp FROM pf_urlgrp WHERE name = 'Design & Assets')),
  (58, 'Unsplash', 'https://unsplash.com', TRUE, (SELECT id_urlgrp FROM pf_urlgrp WHERE name = 'Design & Assets')),
  (59, 'Freepik', 'https://www.freepik.com', TRUE, (SELECT id_urlgrp FROM pf_urlgrp WHERE name = 'Design & Assets')),
  (60, 'Pixabay', 'https://pixabay.com', TRUE, (SELECT id_urlgrp FROM pf_urlgrp WHERE name = 'Design & Assets')),
  (61, 'Iconify', 'https://iconify.design', TRUE, (SELECT id_urlgrp FROM pf_urlgrp WHERE name = 'Design & Assets')),
  (62, 'SVGRepo', 'https://www.svgrepo.com', TRUE, (SELECT id_urlgrp FROM pf_urlgrp WHERE name = 'Design & Assets')),
  (63, 'Notion', 'https://www.notion.so', TRUE, (SELECT id_urlgrp FROM pf_urlgrp WHERE name = 'Productivity & Collaboration')),
  (64, 'Trello', 'https://trello.com', TRUE, (SELECT id_urlgrp FROM pf_urlgrp WHERE name = 'Productivity & Collaboration')),
  (65, 'Jira', 'https://www.atlassian.com/software/jira', TRUE, (SELECT id_urlgrp FROM pf_urlgrp WHERE name = 'Productivity & Collaboration')),
  (66, 'ClickUp', 'https://clickup.com', TRUE, (SELECT id_urlgrp FROM pf_urlgrp WHERE name = 'Productivity & Collaboration')),
  (67, 'Asana', 'https://asana.com', TRUE, (SELECT id_urlgrp FROM pf_urlgrp WHERE name = 'Productivity & Collaboration')),
  (68, 'AnimeFLV', 'https://www3.animeflv.net', TRUE, (SELECT id_urlgrp FROM pf_urlgrp WHERE name = 'Personal Links')),
  (69, 'YarrList', 'https://yarrlist.net', TRUE, (SELECT id_urlgrp FROM pf_urlgrp WHERE name = 'Personal Links')),
  (70, 'GetOnbrd', 'https://www.getonbrd.com/misempleos', TRUE, (SELECT id_urlgrp FROM pf_urlgrp WHERE name = 'Personal Links')),
  (71, 'ChileBT', 'https://chilebt.com', TRUE, (SELECT id_urlgrp FROM pf_urlgrp WHERE name = 'Personal Links')),
  (72, 'Futbol Libre', 'https://futbollibre.mx', TRUE, (SELECT id_urlgrp FROM pf_urlgrp WHERE name = 'Personal Links')),
  (73, 'Proton VPN', 'https://protonvpn.com', TRUE, (SELECT id_urlgrp FROM pf_urlgrp WHERE name = 'VPNs')),
  (74, 'Mullvad VPN', 'https://mullvad.net/es', TRUE, (SELECT id_urlgrp FROM pf_urlgrp WHERE name = 'VPNs')),
  (75, 'Mixboard', 'https://mixboard.google.com/projects', TRUE, (SELECT id_urlgrp FROM pf_urlgrp WHERE name = 'AI / LLM Tools')),
  (76, 'Pixilart', 'https://www.pixilart.com', TRUE, (SELECT id_urlgrp FROM pf_urlgrp WHERE name = 'Design & Assets')),
  (77, 'Softicons', 'https://www.softicons.com', TRUE, (SELECT id_urlgrp FROM pf_urlgrp WHERE name = 'Design & Assets')),
  (78, 'Tailwind Animations', 'https://tailwind-animations.com', TRUE, (SELECT id_urlgrp FROM pf_urlgrp WHERE name = 'Frontend')),
  (79, 'Linode', 'https://www.linode.com/', TRUE, (SELECT id_urlgrp FROM pf_urlgrp WHERE name = 'Infrastructure / Hosting')),
  (80, 'Azure DevOps', 'https://azure.microsoft.com/en-us/products/devops', TRUE, (SELECT id_urlgrp FROM pf_urlgrp WHERE name = 'Infrastructure / Hosting')),
  (81, 'Oracle Cloud', 'https://www.oracle.com/cloud/free', TRUE, (SELECT id_urlgrp FROM pf_urlgrp WHERE name = 'Infrastructure / Hosting')),
  (82, 'AWS', 'https://www.awsacademy.com/vforcesite/LMS_Login', TRUE, (SELECT id_urlgrp FROM pf_urlgrp WHERE name = 'Infrastructure / Hosting')),
  (83, 'UpWork', 'https://www.upwork.com/', TRUE, (SELECT id_urlgrp FROM pf_urlgrp WHERE name = 'Personal Links')),
  (84, 'Pixler', 'https://pixler.dev', TRUE, (SELECT id_urlgrp FROM pf_urlgrp WHERE name = 'AI / LLM Tools')),
  (85, 'Cloudinary', 'https://cloudinary.com/', TRUE, (SELECT id_urlgrp FROM pf_urlgrp WHERE name = 'Infrastructure / Hosting')),
  (86, 'WeLib', 'https://welib.org/', TRUE, (SELECT id_urlgrp FROM pf_urlgrp WHERE name = 'Personal Links')),
  (87, 'Free For Students', 'https://freeforstudents.org/row', TRUE, (SELECT id_urlgrp FROM pf_urlgrp WHERE name = 'Learning & Documentation')),
  (88, 'Zoho Mail', 'https://www.zoho.com', TRUE, (SELECT id_urlgrp FROM pf_urlgrp WHERE name = 'Infrastructure / Hosting')),
  (89, 'Brevo', 'https://www.brevo.com', TRUE, (SELECT id_urlgrp FROM pf_urlgrp WHERE name = 'Backend'))
ON CONFLICT (name) DO NOTHING;

-- Sequences
SELECT setval('pf_projects_id_project_seq', (SELECT COALESCE(MAX(id_project), 0) FROM pf_projects));
SELECT setval('pf_languages_id_language_seq', (SELECT COALESCE(MAX(id_language), 0) FROM pf_languages));
SELECT setval('pf_technologies_id_technology_seq', (SELECT COALESCE(MAX(id_technology), 0) FROM pf_technologies));
SELECT setval('pf_urlgrp_id_urlgrp_seq', (SELECT COALESCE(MAX(id_urlgrp), 0) FROM pf_urlgrp));
SELECT setval('pf_url_id_url_seq', (SELECT COALESCE(MAX(id_url), 0) FROM pf_url));

COMMIT;
