<div align="center" display="flex" style="justify-content:flex-start;">
      <img align="center" alt="js" height="40" width="40" src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/python/python-original.svg" />
</div>

<p align="center">
 <a href="#desc">Descrição</a> •
 <a href="#features">Testes</a> •
 <a href="#tecnologias">Tecnologias</a> • 
 <a href="#executando">Executar o projeto</a> • 
 <a href="#autor">Autor</a>
</p>

<div id="desc"/>

## 📝 Descrição
Testes de API utilizando as técnicas de testes de caixa preta, a partir de requisições HTTP. <br>
O padrão de projeto Facade, ou fachada, foi implementado na arquitetura dos testes para abstrair algumas funcinoalidades da API. <br>
A API utilizada nos testes pode ser acessada [aqui](https://api-course-test-automatized.herokuapp.com)

<div id="projeto" />

## ✔️ Testes
Os testes realizados foram feitos no módulo usuário:
- [ ] POST /auth/login Login com sucesso
- [ ] POST /auth/login Login com falha - senha inválida
- [ ] POST /auth/login Login com falha - usuário não cadastrado no sistema
- [ ] POST /auth/login  Login com falha - email inválido
- [ ] POST /auth/login Login com falha - campo email em branco
- [ ] POST /auth/login Login com falha - campo senha em branco
- [ ] GET api/users/ - recuperar todos os usuários
- [ ] GET api/users/details - recuperar dados do usuário logado
- [ ] POST api/users/ - cruar usuário com sucesso
- [ ] PUT api/users/ - atualizar dados do usuário


<div id="tecnologias"/>

## ✨ Tecnologias

-   [ ] [Python](https://www.python.org/)
-   [ ] [Pytest](https://docs.pytest.org/en/6.2.x/contents.html)
-   [ ] [Requests](https://docs.python-requests.org/en/latest/)
-   [ ] [Código API](https://github.com/MarcosLudgerio/api-automation-test)
  
<div id="executando" />

## ▶️ Executando o projeto

Execute no terminal os comandos abaixo

```sh
$ git clone https://github.com/MarcosLudgerio/test-api-python.git
$ cd test-api-python
$ pip install
$ pytest
```

<div id="autor" />

## 👩‍💻 Autor 

<table>
   <tr>
     <td align="center">
        <a href="https://github.com/MarcosLudgerio">
         <img style="border-radius: 50%;" src="https://avatars0.githubusercontent.com/u/43012976?s=460&u=1163c04d9f35b577063b3f6550ae520c4dd2f866&v=4" width="100px;" alt=""/>
        </a>
        <br/><sub><b>Marcos Ludgério</b></sub>
     </td>
   </tr>
</table>
