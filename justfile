#!/usr/bin/env just --justfile

zipapp-build:
    -mkdir ./tmp
    python3 -m zipapp ./src --output ./tmp/signpic-generator.pyz
    echo '#!/usr/bin/env python3' | cat - ./tmp/signpic-generator.pyz > ./tmp/signpic-generator
    chmod +x ./tmp/signpic-generator
