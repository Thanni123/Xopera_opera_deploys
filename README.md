# xOpera deploy von Thumbnail Generator (Microservice) bzw. ToDo List API (Serverless)

**Notiz**: Dieses Projekt enthält ausführbare TOSCA Deployment Modelle für die jeweiligen im Titel erwähnten Applikationen. Implementiert wurden die Deployment Modelle basierend auf dem TOSCA Standard Version 1.3 (Quelle: https://docs.oasis-open.org/tosca/TOSCA-Simple-Profile-YAML/v1.3/os/TOSCA-Simple-Profile-YAML-v1.3-os.pdf) und unter Zuhilfenahme einer externen Repository (Quelle: https://github.com/radon-h2020/radon-particles/tree/master). Validiert wurden Sie unter der Linux Distribution, Ubuntu 20.04. Des Weiteren beschränkt sich die Umsetzung lediglich auf die Umgebungen der Cloud-Provider Amazon Web Services (kurz: AWS) und Microsoft Azure.

**Voraussetzungen**:
* Die aktuelleste Version von Ansible (während der Entwicklung [Stand: 10/2020] kam 2.10.3 zum Einsatz). Zur Installation einfach der folgenden Link folgen und je nach OS die dazugehöirge Anleitung befolgen (Quelle: https://docs.ansible.com/ansible/latest/installation_guide/intro_installation.html).

* xOpera benötigt für die Ausführung Python3 und eine virtuelle Umgebung. Für die Einrichtung sind folgende Befehle auszuführen:
    ```
    $ sudo apt update
    $ sudo apt install -y python3-venv python3-wheel python-wheel-common
    ```

* Im Anschluss kann opera dann wie folgt installiert werden:
    ```
    $ mkdir ~/opera && cd ~/opera
    $ python3 -m venv .venv && . .venv/bin/activate    
    (.venv) $ pip install opera
    ```
    
* Um die TOSCA Deployment Modelle zu deployen, muss hierzu das Repository kopiert werden:
    ```
    (.venv) $ git clone https://github.com/Thanni123/Xopera_opera_deploys.git
    ```
    
* Die jeweiligen Service Templates besitzen für die Ausführung bereits vordefinierte Property Values. Je nach Bedarf können diese manuell mit einem bel. Editor verändert werden.
    

## Ausführung der TOSCA Deployment Modelle für den Thumbnail Generator
### Cloud-Provider: AWS
Für die Ausführung muss zuvor in das Wurzelverzeichnis navigiert werden: 
    ```
    cd <PATH_TO_Thumbnail_Generation_AWS_w1-wip1>
    ```

Das TOSCA Deployment Modell kann dann im Anschluss durch den folgenden Befehl ausgeführt werden:
    ```
    opera deploy _definitions/aws_deploy.tosca
    ```

### Cloud-Provider: Microsoft Azure
Für die Ausführung muss zuvor in das Wurzelverzeichnis navigiert werden: 
    ```
    cd <PATH_TO_ImageResizeAzure_w1-wip1>
    ```

Das TOSCA Deployment Modell kann dann im Anschluss durch den folgenden Befehl ausgeführt werden:
    ```
    opera deploy _definitions/azure_deploy.tosca
    ```

## Ausführung der TOSCA Deployment Modelle für die ToDo List API
### AWS
Für die Ausführung muss zuvor in das Wurzelverzeichnis navigiert werden: 
    ```
    cd <PATH_TO_ToDoListAPI_w1-wip1>
    ```

Das TOSCA Deployment Modell kann dann im Anschluss durch den folgenden Befehl ausgeführt werden:
    ```
    opera deploy _definitions/ServiceTemplate.tosca
    ```

### Microsoft Azure
**Notiz**: Implementierung hierzu nicht vorhanden.
