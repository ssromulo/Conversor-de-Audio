Audio Converter
- This script quickly converts MP4 files to MP3.

How it works:
- The script accesses the ./MP4 directory, reads all files with the .mp4 extension, and converts them to .mp3, saving them in the ./MP3 directory. It is very useful for converting a batch of .mp4 files to .mp3.

Dependencies:
- The script uses the Pydub and Os libraries to read and convert the files.
- The FFMPEG software is used by Pydub to perform the conversions. If you encounter any issues related to FFMPEG or FFPROBE during execution, follow this tutorial to install and add it to your operating system's path: https://phoenixnap.com/kb/ffmpeg-windows.

Step-by-step:
- Ensure the /MP4 and /MP3 directories are created at the same level as the script.
- Run the script.
- Follow the instructions displayed in the terminal.
- Wait for the success message at the end of the script.
- Done! Your audio files will be saved in the /MP3 directory.
- 
Technical details:
- Language: Python
- Libraries: OS and Pydub
- Additional Apps: FFMPEG
- 
This script was created to meet the need of converting multiple music files to the MP3 format, and I decided to share it with everyone who has the same demand. This script is free to use and edit, but its commercialization is prohibited.

#####################################################################################################################################################################################################################
Versão em Português

# Conversor-de-Audio
Este script converte arquivos MP4 para MP3 rapidamente.

Como funciona:
-  O script acessa o diretório ./MP4, lê todos os arquivos que tenham a extensão .mp4 e converte todos eles em .mp3, salvando no diretório ./MP3. Ele é muito útil para converter uma massa de arquivos que tenham a extensão .mp4 para .mp3.

Dependências:
- O script utiliza as bibliotecas Pydub e Os para fazer a leitura e conversão dos arquivos.
- O software FFMPEG é utilizado pelo Pydub para realizar as conversões. Caso a execução apresente algum problema relacionado ao FFMPEG ou FFPROBE, basta seguir este tutorial de como instalar e adicionar ao path do seu sistema operacional: https://phoenixnap.com/kb/ffmpeg-windows

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
