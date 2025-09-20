# Calculadora: À Vista vs. Parcelado

### Visão Geral

Este é um aplicativo web interativo, construído com Streamlit, que ajuda a tomar decisões financeiras. Ele compara o custo líquido de comprar um produto:

1.  **À Vista:** Pagando um valor com desconto.
2.  **Parcelado:** Pagando o valor total em parcelas, mas investindo o dinheiro que seria gasto de imediato e lucrando com os rendimentos.

O objetivo é descobrir qual opção é mais vantajosa, considerando a taxa de rendimento do seu dinheiro.

### Como Usar

1.  **Valor do Produto:** Insira o preço total do item.
2.  **Desconto à Vista:** Informe o percentual de desconto oferecido para pagamento único.
3.  **Taxa de Rendimento:** Digite a taxa de rendimento mensal que seu investimento oferece.
4.  **Número de Parcelas:** Selecione a quantidade de parcelas do pagamento.

O aplicativo irá calcular e exibir o custo líquido de cada opção, indicando a escolha mais econômica.

### Tecnologias

* **Python:** Linguagem de programação.
* **Streamlit:** Framework para criação da interface web.

### Instalação e Execução

Para rodar o aplicativo localmente, siga os passos abaixo:

1.  **Clone o repositório:**
    ```bash
    git clone [https://github.com/SEU-USUARIO/calculadora-a-vista-vs-parcelado.git](https://github.com/SEU-USUARIO/calculadora-a-vista-vs-parcelado.git)
    cd calculadora-a-vista-vs-parcelado
    ```

2.  **Instale as dependências:**
    ```bash
    pip install -r requirements.txt
    ```
    *Crie o arquivo `requirements.txt` com o conteúdo `streamlit` e `pandas`.*

3.  **Execute o aplicativo:**
    ```bash
    streamlit run app.py
    ```
