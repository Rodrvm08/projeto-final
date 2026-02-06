🔧 Instalação e Configuração
1. Clone o repositório
git clone [https://github.com/seu-usuario/nome-do-projeto.git](https://github.com/Rodrvm08/projeto-final.git)
cd projeto-final
2. Crie e ative um ambiente virtual
python -m venv venv
No Linux/Mac:
source venv/bin/activate
No Windows:
venv\Scripts\activate
3. Instale as dependências
pip install -r requirements.txt
4. Execute as migrações
python manage.py migrate
5. Execute o servidor de desenvolvimento
python manage.py runserver
