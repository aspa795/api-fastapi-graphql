## Prueba Tech
Backend Developer


## Acerca del proyecto

Info: El Core de esta prueba es Python, no se permite utilizar otro lenguaje de programacion.

1.- Crear integración con el API Publica (https://jsonplaceholder.typicode.com/) y Guarda la información en una DB Postgres:

Dicha integración debe tener todo lo relacionado a una integración, como validación de datos enviados, validación de datos obtenidos y todas las capas necesarias para esta API.

Debe integrar todos los métodos disponibles:

* GET 	/posts
* GET 	/posts/1
* GET 	/posts/1/comments
* GET 	/comments?postId=1
* POST 	/posts
* PUT 	/posts/1
* PATCH 	/posts/1
* DELETE 	/posts/1

Para esta integración no puede usar Django, tampoco puede usar Flask. Puede usar cualquier otra librería.


2.- Con la data fake que se guardo en la DB, se debe hacer un API que pueda guardar mas data (cualquier otra que no sea de la integracion) y consultar la información. El Api debe ser desarrollada en GraphQL. Librería recomendada: Graphene

###Importante:

El código realizado puede subirlo a un repositorio publico para poder revisarlo. Recuerde que deben tener un README.md para conocer mas información del proyecto, también debe tener una manera fácil de como levantar el proyecto para que pueda ser probado de ser necesario.

- Debe tener en cuenta los estándares al escribir código python.
- Hacer pruebas unitarias es un plus.

### Tecnologías usadas en el proyecto

This section should list any major frameworks/libraries used to bootstrap your project. Leave any add-ons/plugins for the acknowledgements section. Here are a few examples.

* [Graphene Graphql](https://graphene-python.org/)
* [Orator](https://orator-orm.com/)
* [FastApi](https://fastapi.tiangolo.com/)
* [Docker](https://www.docker.com/get-started)
* [Postgre](https://www.postgresql.org/)




<!-- GETTING STARTED -->
## Pasos para correr el proyecto localmente

Como pre-requisito, es importante tener instalado el servicio de [Docker](https://www.docker.com/get-started) en tú PC o LAPTOP.

A continuación, puedes continuar con los siguientes pasos:


* Clonar repositorio
  ```sh
  git clone https://github.com/aspa795/api-fastapi-graphql.git
  ```

* Entrar a la carpeta del proyecto
  ```sh
  cd api-fastapi-graphql
  ```


## Instalación


1. Construir los contenedores:
    ```sh
      docker-compose up
    ```

     El proyecto actualmente ya esta corriendo en la ruta: [https://127.0.0.1:8000/graphql](http://127.0.0.1:8000/graphql), pero vamos a ejecutar un par de comandos más para aplicar las migraciones a nuestra base de datos:


2. Abrir otra terminal y continuar con estos pasos:
   
    ```sh
      docker ps #Visualizar los servicios/contenedores activos
    ```
   Entramos a nuestro container de name:api
   ```sh
      docker exec -it api /bin/sh
   ```
   Ejecutamos el siguiente comando:
   ```sh
      orator migrate -c config/settings.py && python3 data.py
   ```
   Escribimos 'yes' y Listo!


## Uso

Para probar la API podemos ejecutar los siguientes ejemplos:

* Listar todos los posts
    ```graphql
    query {
        listPosts{
            id,
            title,
            body,
            userId
        }
    }
    ```
    Respuesta:
    ```response
        {
          "data": {
            "listPosts": [
              {
                "id": 1,
                "title": "sunt aut facere repellat provident occaecati excepturi optio reprehenderit",
                "body": "quia et suscipit\nsuscipit recusandae consequuntur expedita et cum\nreprehenderit molestiae ut ut quas totam\nnostrum rerum est autem sunt rem eveniet architecto",
                "userId": 1
              },
              {
                "id": 2,
                "title": "qui est esse",
                "body": "est rerum tempore vitae\nsequi sint nihil reprehenderit dolor beatae ea dolores neque\nfugiat blanditiis voluptate porro vel nihil molestiae ut reiciendis\nqui aperiam non debitis possimus qui neque nisi nulla",
                "userId": 1
              },
                ...
        }
    ```

* Crear un post
    ```graphql
    mutation {
          createPost(postDetails: {
            userId: 7,
            title: "This title!!!",
            body: "Body test text!!!"
          })
          {
            code
            message
            body{
              id,
              title,
              body,
              userId
            }
          }
    }
    ```
    Response
    ```response
    {
      "data": {
        "createPost": {
          "code": 201,
          "message": "Post Create Success",
          "body": {
            "id": 101,
            "title": "This title!!!",
            "body": "Body test text!!!",
            "userId": 7
          }
        }
      }
    }
    ```

Aquí te dejaré más querys disponibles:

```querys
#Get all posts

# query {
#    listPosts{
#     id,
#     title,
#     body,
#     userId
#   }
# }

#Get single post

# query {
#   getSinglePost(postId:2) {
#     id,
#     title,
#     body,
#     userId
#   }
# }

#Get comments by post

# query {
#   getCommentsByPost(postId: 2) {
#       postId,
#       id,
#       name,
#       email,
#       body
#     }
# }


#Create post

# mutation {
#   createPost(postDetails: {
#     userId: 7,
#     title: "This title!!!",
#     body: "Body test text!!!"
#   })
#   {
#     code
#     message
#     body{
#       id,
#       title,
#       body,
#       userId
#     }
#   }
# }

#Update post

# mutation {
#   updatePost(postDetails: {
#     id: 1,
#     userId: 3,
#     title: "Yes! Modify!!! ohter!",
#     body: "Modify all body!!"
#   }, postId: 1)
#   {
#     code
#     message
#     body{
#       id,
#       title,
#       body,
#       userId
#     }
#   }
# }

#Patch post

# mutation {
#   patchPost(postDetails: {
#     title: "Title Modified!! 1",
#     body: "Other body"
#   }, postId: 1)
#   {
#     code
#     message
#     body{
#       id,
#       title,
#       body,
#       userId
#     }
#   }
# }

#Delete post

# mutation {
#   deletePost(postId: 1)
#   {
#     code
#     message
#   }
# }



#Create comment

# mutation {
#   createComment(commentDetails: {
#     postId: 5,
#     name: "New comment"
#     email: "test@mail.com"
#     body: "Hello everyone!!!"
#   })
#   {
#   code
#   message
#   body{
#     id,
#     postId
#     name,
#     email,
#     body
#   }
#   }
# }


#Get all comments

# query {
#   listComments {
#     id,
#     postId,
#     name,
#     email,
#     body
#   }
# }

```


## Licencia

Distributed under the MIT License.


## Contacto

Alexis Poveda - [LinkedIn](https://www.linkedin.com/in/alexis-poveda-233a4720b)
* Correo: aspoveda@outlook.com

