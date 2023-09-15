#Grafico para el direccionamiento de carpetas
```mermaid




    flowchart TD
        A[proyecto-datos-y-algoritmos]
        A-->B(images)
        A-->C(src)
        A-->D(proyecto_env)

        B-->E(logo.png)
        C-->F(modules)

        A-->G(test)
        G-->interfaz.py
        G-->interfaz2.py
        G-->interfaz1.py
        G-->main
        G-->prueba_de_interfaz
       
       F-->base_de_datos.py
       F-->enviarCorreos.py
       F-->enviarCorreo.py
       F-->persona.py
       F-->prueba.py
       F-->registro_perosna.py
       F-->whatsapp.py
       
    
```
