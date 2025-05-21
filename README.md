
# 🚀 Portifolio-Django

![License](https://img.shields.io/badge/license-MIT-green) ![Python](https://img.shields.io/badge/python-3.8%2B-blue) ![Django](https://img.shields.io/badge/django-4.x-green)

---

## ✨ Sobre

Portifolio-Django é um projeto **open source** feito em Django, criado para você que quer construir um portfólio pessoal moderno e integrado a um blog de forma rápida e fácil. 

Feito para ser **flexível** e **reutilizável**, ele permite que qualquer desenvolvedor personalize o conteúdo e o design sem dor de cabeça — ideal para mostrar seus projetos, compartilhar artigos e se destacar no mercado.

---

## ⚙️ Funcionalidades

- 📂 Exibição dinâmica de projetos do portfólio com imagens e descrições.
- 📝 Blog integrado para você publicar artigos, novidades e aprendizados.
- 🛠️ Gerenciamento simples via painel administrativo do Django (não precisa mexer no código para mudar conteúdo).
- 🎨 Design responsivo e elegante com Tailwind CSS.
- 🔄 Estrutura modular que facilita a reutilização e customização por outros devs.

---

## 🛠️ Tecnologias Utilizadas

| Tecnologia      | Versão          | Descrição                         |
| --------------- | --------------- | -------------------------------- |
| Python          | 3.8+            | Linguagem de programação          |
| Django          | 4.x             | Framework web                     |
| Tailwind CSS    | Última          | Framework CSS utilitário          |
| SQLite          | Nativo          | Banco de dados padrão, leve e rápido |

---

## 🚀 Como começar

Siga os passos abaixo para rodar o projeto localmente e começar a customizar seu portfólio:

### 1. Clone o repositório

```bash
git clone https://github.com/JaimeMartinsOliveira/Portifolio-Django.git
cd Portifolio-Django
```

### 2. Crie e ative um ambiente virtual (recomendado)

```bash
python -m venv venv
source venv/bin/activate  # Linux / macOS
venv\Scripts\activate   # Windows
```

### 3. Instale as dependências

```bash
pip install -r requirements.txt
```

### 4. Configure o banco de dados e execute as migrações

```bash
python manage.py migrate
```

### 5. Crie um superusuário para acessar o painel administrativo

```bash
python manage.py createsuperuser
```

### 6. Inicie o servidor de desenvolvimento

```bash
python manage.py runserver
```

### 7. Acesse

- 🌐 Site: [http://127.0.0.1:8000](http://127.0.0.1:8000)
- 🔧 Admin: [http://127.0.0.1:8000/admin](http://127.0.0.1:8000/admin)

---

## 🎨 Personalize seu Portfólio

Quer deixar seu portfólio com a sua cara? Aqui vão algumas dicas:

- 📝 Edite ou adicione projetos e posts direto pelo painel admin do Django.
- 🎨 Modifique os templates em `templates/` para alterar o layout e o conteúdo estático.
- 🎨 Ajuste as cores, fontes e estilos no arquivo `tailwind.config.js` para um visual único.
- 📸 Suba imagens e arquivos para deixar seu portfólio mais atraente.

---

## 🤝 Como contribuir

Contribuições são super bem-vindas! Quer ajudar a melhorar este projeto? Siga esses passos:

1. Faça um fork do repositório
2. Crie uma branch para sua feature:  
   `git checkout -b minha-feature`
3. Faça commit das suas alterações:  
   `git commit -m "Minha nova feature"`
4. Envie para o seu fork:  
   `git push origin minha-feature`
5. Abra um Pull Request aqui no repositório original

Vamos crescer juntos! 🚀

---

## 📄 Licença

Este projeto está licenciado sob a licença **MIT** — ou seja, é open source e pode ser usado e modificado livremente. Veja o arquivo [LICENSE](LICENSE) para detalhes.

---

Feito com ❤️ por Jaime Martins Oliveira — código aberto para a comunidade.

---

### 💬 Dúvidas ou sugestões?

Abra uma issue no GitHub ou entre em contato comigo!

---
