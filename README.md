# Conversor-de-Audio
Este script converte arquivos MP4 para MP3 rapidamente.

Como funciona:
-  O script acessa o diretório ./MP4, lê todos os arquivos que tenham a extensão .mp4 e converte todos eles em .mp3, salvando no diretório ./MP3. Ele é muito útil para converter uma massa de arquivos.

Dependências:
- O script utiliza as bibliotecas Pydub e Os para fazer a leitura e conversão dos arquivos.
- O software FFMPEG é utilizado pel Pydub para realizar as conversões. Caso a execução apresente algum problema relacionado ao FFMPEG ou FFPROBE, basta seguir este tutorial de como instalar e adicionar ao path do seu sistema operacional: https://phoenixnap.com/kb/ffmpeg-windows

Passo a passo:
- Certifique-se de que os diretórios /MP4 e /MP3 estejam criados no mesmo nível do script.
- Execute o script.
- Siga as instruções exibidas no terminal.
- Aguarde a mensagem de êxito no final do script.
- Pronto! Seus áudios estarão salvos no diretório /MP3

Detalhes técnicos:
- Linguagem: Python
- Bibliotecas: OS e Pydub
- Apps adicionais: FFMPEG

O script foi escrito com a necessidade de converter diversas músicas para o formato mp3 e decidi compartilhá-lo com todos que tenham a mesma demanda. Este script é livre para uso e edição e sua comercialização é proibida.
