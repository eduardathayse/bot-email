# Bot-email
# Robô básico para enviar emails, usando o outlook
O robô usa a biblioteca selenium para abrir o browser, nesse caso 
ele usa o chrome (o driver do chrome foi baixado e extraido para o disco local C);

O robô ler o email do rementente a senha e o email do destinatário em um arquivo .txt 
chamado login. Nesse arquivo os dados vão estar separados por ponto e vírgula;

O robô guarda o assunto e a mensagem em variáveis;

Depois que abrir uma janela do chrome ele entra no site de login do outlook e realiza 
o login com o email e a senha que foram pegos do arquivo login.txt;

Quando finalmente o robõ entrar no email, o mesmo abrirá a caixa de email, e 
digitará o assunto da mensagem e a mensagem em si;

Feito tudo isso o robô finaliza o email clicando em enviar, e depois de 
alguns segundos fechará o browser.



# Basic robot to send emails, using outlook
The robot uses the selenium library to open the browser, in this case
it uses chrome (the chrome driver has been downloaded and extracted to local disk C);

The robot reads the email as a password and the recipient's email in a .txt file
called login. In this file the data will be separated by a semicolon;

The robot stores the subject and the message in variables;

After opening a chrome window he enters the outlook login website and performs
login with the email and a password that were tracked in the login.txt file;

When finally or what is allowed to not enter email, or even open an email box, and
enter the subject of the message and the message itself;

Once all this is done, the robot ends the email by clicking on send and after
a few seconds to close the browser.


