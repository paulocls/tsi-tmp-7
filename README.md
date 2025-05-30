Transcrição de Áudio com Whisper e Extração de Pontos-Chave com Ollama

1. Descrição do projeto:
O trabalho de avaliação tem como objetivo um script em python na qual transcreve um audio em mp3 convertento texto e, em consequência, eé feito um resumo do texto através do modelo IA OLLAMA. 

2. Instruções para a instalação e execução do script:
Whisper depende do FFmpeg para converter arquivos de áudio. Para verificar se ele está instalado, abra o Prompt de Comando e digite: ffmpeg -version. Se o comando não for reconhecido, você precisará instalar o FFmpeg.
- Baixe o FFmpeg do site oficial: https://ffmpeg.org/download.html.
- Escolha a versão compatível com o seu sistema.
- Extraia os arquivos e adicione a pasta bin do FFmpeg ao PATH do Windows.
- Pressione Win + R, digite sysdm.cpl e pressione Enter.
- Vá até a aba "Avançado" e clique em "Variáveis de ambiente".
- Na seção "Variáveis do sistema", encontre a variável "Path" e clique em "Editar".
- Clique em "Novo", cole o caminho copiado (C:\ffmpeg\bin) e clique em "OK".

Após a instalação ffmpeg, crie um ambiente virtual no Vscode para importar as bibliotecas na pasta escolhida, então crie um arquivo python. 
Então, faça "pip install -U openai-whisper" e "pip install -U langchain-ollama".
O arquivo de audio deve estar na mesma pasta do script.

*Exemplo:
    -whipser.py
    -O audio: record.mp3



