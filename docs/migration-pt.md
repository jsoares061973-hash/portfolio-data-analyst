# Migração segura para a estrutura organizada

## Método recomendado: GitHub Desktop

1. Baixe e extraia este pacote.
2. No GitHub Desktop, clone `jsoares061973-hash/portfolio-data-analyst`.
3. Abra a pasta clonada no Explorador de Arquivos.
4. Copie **o conteúdo** deste pacote para a pasta clonada, substituindo `index.html`, `styles.css` e `README.md`.
5. Apague da pasta clonada os antigos arquivos soltos da raiz que começam por `bottleneck-`, `p2-`, `p4-`, `p5-`, `p7-`, `p8-`, `p9-`, `p10-`, `p11-` ou `p12-`.
6. Apague também as duplicatas `README (1).md`, `bottleneck-notebook (1).ipynb`, `P9_Lapage_Analyse_Ventes_Clients.ipynb`, `P9_Lapage_Presentation.pdf` e `requirements.txt` da raiz.
7. Não apague a pasta oculta `.git` criada pelo GitHub Desktop.
8. Faça o commit `Reorganize portfolio files by project` e clique em **Push origin**.
9. Aguarde a publicação do GitHub Pages e teste a página.

O GitHub Desktop deverá mostrar automaticamente os arquivos antigos como removidos e os novos como adicionados ou renomeados.

## Alternativa pelo site do GitHub

1. Use **Add file > Upload files**.
2. Arraste as pastas `assets`, `docs` e `projects`, além de `index.html`, `styles.css`, `README.md` e `.gitignore`.
3. Faça o commit e valide a página publicada.
4. Só depois elimine os antigos arquivos soltos da raiz.

Essa alternativa exige várias exclusões manuais; por isso, o GitHub Desktop é mais seguro para esta reorganização.
