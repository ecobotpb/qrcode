
# Usando Python para gerar QRCODE

Este projeto é um gerador de payload e QR Code para pagamentos PIX, utilizando a estrutura do BRCode. O código Python cria um payload de pagamento no formato exigido pelo sistema Pix e gera um QR Code correspondente, que pode ser escaneado para realizar transações.

O BR Code é o nome do padrão de QR Code, para fins de iniciação de pagamentos, adotado no Brasil, nos termos da Circular nº 3.682, de 4 de novembro de 2013.

O Pix se consolidou como o meio de pagamento mais popular do Brasil em 2023 com quase 42 bilhões de transações.



## Referência

 - [Manual BRCode](https://www.bcb.gov.br/content/estabilidadefinanceira/spb_docs/ManualBRCode.pdf)
 - [Códigos QR EMV](https://www.emvco.com/emv-technologies/qr-codes/)
 - [Pix EMV QRCode Tester](https://openpix.com.br/qrcode/scanner/)


 


## Funcionalidades

- Geração de Payload Pix: cria um payload no formato QRCP-S, conforme especificações do sistema Pix.
- Geração de QR Code: cria um QR Code a partir do payload gerado e salva a imagem em um diretório especificado.
- Geração do Pix Copia e Cola: cria a linha digitável a partir do payload gerado, o codigo do Pix Copia e Cola é mostrado no saida.
