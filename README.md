# Brawiki Game

**Número da Lista**: X<br>
**Conteúdo da Disciplina**: Grafos 1<br>

## Alunos
|Matrícula | Aluno |
| -- | -- |
| 17/0140571 | Douglas Farias de Castro |
| 17/0034941  | Guilherme Peixoto |

## Sobre 
Brawiki é um jogo de exploração na Wikipedia com o objetivo de encontrar o caminho da "Página Inicial" até a "página Objetivo" no menor número possível de cliques.

## Screenshots
### **O Jogo**
#### **Encontrar Partida**
![Screenshot from 2023-09-26 00-17-45](https://github.com/projeto-de-algoritmos/Grafos1_Brawiki-Game/assets/69691521/5e40f980-6a12-49e4-bfd4-0d4f67813779)


#### **Página Inicial**
![Screenshot from 2023-09-26 00-18-07](https://github.com/projeto-de-algoritmos/Grafos1_Brawiki-Game/assets/69691521/2c1d5fc9-2a35-4eaf-b13f-9d93af024cbb)


#### **Página Objetivo**
![Screenshot from 2023-09-26 00-18-32](https://github.com/projeto-de-algoritmos/Grafos1_Brawiki-Game/assets/69691521/25b844c5-cd12-4319-b62f-203a4543fc89)


#### **Página de Vitória**
![Screenshot from 2023-09-26 00-18-53](https://github.com/projeto-de-algoritmos/Grafos1_Brawiki-Game/assets/69691521/b7900493-23df-4fa2-b011-713a1ecd2b10)

### **Algoritmos**
#### **BFS**
![bfs](https://github.com/projeto-de-algoritmos/Grafos1_Brawiki-Game/assets/69691521/caafaead-9c90-4a6e-9ee1-135e63dc9cfc)

#### **DFS**
![dfs](https://github.com/projeto-de-algoritmos/Grafos1_Brawiki-Game/assets/69691521/0aaa4c24-9a12-4958-854b-092368c21ea3)


## Instalação 
**Linguagem**: Python<br>
**Framework**: Django<br>

Antes de executá-lo, você deve ter instalado o Python, Pip e Django na sua máquina.

1. **Entre no diretório do projeto:**
   
   ```bash
      cd Grafos1_Brawiki-Game
    ```

2. **Ative o ambiente virtual:**
   
    ```bash
      python3 -m venv env 
    ```
   
    ```bash
      source env/bin/activate
    ```
    
3. **Instale todas as dependências:**

    ```bash
      pip install -r requirements.txt
    ```

4. **Inicie do servidor:**

    ```bash
      python3 manage.py runserver
    ```

5. **Acesse [http://127.0.0.1:8000](http://127.0.0.1:8000).**
   

## **Uso**

1. Comece o jogo clicando no botão 'Iniciar'

2. Seu objetivo é encontrar um caminho da Página Inicial até a página Objetivo, seguindo os links que aparecem nas páginas da Wikipédia
   
3. Tente chegar ao seu Objetivo com o menor número de cliques possível

## **Vídeo de Apresentação**
- [Apresentação](./apresentação.mp4)

##  **Referências**
- [Wikispeedia navigation paths](https://snap.stanford.edu/data/wikispeedia.html)




